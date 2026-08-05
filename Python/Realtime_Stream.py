from pynq import Overlay, MMIO
import numpy as np
import pandas as pd
import time

# --- Configuration ---
BITSTREAM_PATH = "system.bit" # Ensure this is your latest bitstream!
FIRMWARE_PATH  = "firmware.bin"
DATASET_PATH   = "dataset_balanced.csv"
BRAM_BASE      = 0x42000000 
GPIO_RESET_BASE = 0x41200000

# NEW: The ARM address for the 7-Segment GPIO block
SEV_SEG_BASE   = 0x41220000  

SCALE_FACTOR   = 8192

# Adjusted slightly so the 7-segment doesn't flicker too fast for human eyes
STREAM_DELAY   = 0.05  

# --- SCALING VALUES ---
SCALER_MEAN  = np.array([4057.8926634313448, 15.199330201857835, 134.9586032446246, 12.147823765812163, -0.010634125276620039, -0.0001930981153297173, -0.0017126380536682845, 36.35678013282843, 0.4320764373739651, 0.06407865441735654, 0.010309407346560091, 783168.1907226901, 34179610.117281474])
SCALER_SCALE = np.array([2149.1019177110984, 9.354677767217579, 52.158371818110055, 2.373038659776659, 0.1357900990867289, 0.03629609883123221, 0.013159932160053548, 62.165559858709365, 0.18551853048633132, 0.016416749376823563, 0.000563101851462426, 1177599.3822929808, 43108223.284344725])

# 1. Setup Hardware
ol = Overlay(BITSTREAM_PATH)
bram = MMIO(BRAM_BASE, 0x10000)
reset_gpio = MMIO(GPIO_RESET_BASE, 0x1000)
sev_gpio = MMIO(SEV_SEG_BASE, 0x1000) # NEW: Map the 7-segment hardware

# NEW: Force GPIOs to be outputs to prevent floating bugs
reset_gpio.write(0x4, 0x0)
sev_gpio.write(0x4, 0x0) 

# 2. Flash Firmware (PicoRV32 in Reset)
reset_gpio.write(0x0, 0) 
with open(FIRMWARE_PATH, "rb") as f:
    words = np.frombuffer(f.read(), dtype=np.uint32)
    for i, word in enumerate(words):
        bram.write(i * 4, int(word))

# 3. Start PicoRV32
reset_gpio.write(0x0, 1)
print("PicoRV32 is running. Starting Live Stream...")

# 4. Load Dataset for Streaming
df = pd.read_csv(DATASET_PATH)

# NEW: Shuffle the dataset so you instantly see attacks!
df = df.sample(frac=1).reset_index(drop=True) 

X_stream = df.drop('label', axis=1).values
y_stream = df['label'].values
class_names = {0: "NORMAL", 1: "JAMMING", 2: "SPOOFING"}

# 5. Continuous Streaming Loop
try:
    print(f"Streaming started at {STREAM_DELAY}s per sample. Press Kernel -> Interrupt to stop.")
    while True: 
        for i in range(len(X_stream)):
            # Normalize and Convert to Fixed Point
            raw_row = X_stream[i]
            scaled = (raw_row - SCALER_MEAN) / SCALER_SCALE
            fixed = (scaled * SCALE_FACTOR).astype(np.int32)
            
            # Inject Data into BRAM (Offset 0x1000)
            for j, val in enumerate(fixed):
                bram.write(0x1000 + (j * 4), int(val))
            
            # Delay for visual assessment 
            time.sleep(STREAM_DELAY) 
            
            # Read Prediction from BRAM (Offset 0x2000)
            prediction = bram.read(0x2000)

            # Python writes the prediction directly to your Verilog Decoder!
            sev_gpio.write(0x0, int(prediction))	
            
            # Visual Feedback in Console
            print(f"Streaming Row {i:04d} | Predicted: {class_names.get(prediction, 'UNKNOWN')} | True: {class_names[y_stream[i]]}      ", end="\r")
            
except KeyboardInterrupt:
    print("\nStreaming stopped by user.")
