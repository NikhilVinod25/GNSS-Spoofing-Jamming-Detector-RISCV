import pandas as pd

try:
    # 1. Load the two source datasets
    gnss_data = pd.read_csv('merged_gnss_data.csv')
    # Use the new features file with pseudorange standard deviation
    rinex_features = pd.read_csv('advanced_rinex_features.csv')

    print("--- Step 1: Merging Datasets ---")

    # --- Prepare for the time-based merge ---
    gnss_data['real_time_x'] = pd.to_datetime(gnss_data['real_time_x'])
    rinex_features['time'] = pd.to_datetime(rinex_features['time'])
    gnss_data = gnss_data.sort_values('real_time_x')
    rinex_features = rinex_features.sort_values('time')

    # --- Perform the 'asof' merge ---
    final_dataset = pd.merge_asof(
        gnss_data,
        rinex_features,
        left_on='real_time_x',
        right_on='time',
        direction='nearest',
        tolerance=pd.Timedelta('1s')
    )

    # Remove any rows that didn't have a match
    final_dataset.dropna(subset=['avg_snr_L1'], inplace=True)
    print("Merge successful.")
    
    print("\n--- Step 2: Selecting Features ---")

    # 2. Define the list of columns to keep, including the new pseudorange feature
    selected_features = [
        'real_time_x',    # Primary timestamp
        'agcCnt_01',      # Automatic Gain Control
        'jamInd_01',      # Jamming Indicator
        'noisePerMS_01',  # Noise per Millisecond
        'jammingState_01',# Jamming State
        'lat',            # Latitude
        'lon',            # Longitude
        'hMSL',           # Height above Mean Sea Level
        'velN',           # Velocity North
        'velE',           # Velocity East
        'velD',           # Velocity Down
        'hAcc',           # Horizontal Accuracy
        'vAcc',           # Vertical Accuracy
        'sAcc',           # Speed Accuracy
        'pDOP',           # Positional Dilution of Precision
        'numSV',          # Number of Satellites (from PVT)
        'avg_snr_L1',     # Average Signal-to-Noise Ratio
        'pseudorange_std_dev', # New Advanced Feature!
        'num_sats_rinex'  # Number of Satellites (from RINEX)
    ]

    # 3. Create a new dataframe with only the selected features
    features_df = final_dataset[selected_features]
    
    # Rename the time column for clarity
    features_df = features_df.rename(columns={'real_time_x': 'timestamp'})

    # 4. Save the final, cleaned dataframe to a new file
    output_filename = 'features_dataset_advanced.csv'
    features_df.to_csv(output_filename, index=False)

    print(f"Feature selection successful.")
    print(f"\nSuccess! Your final dataset is ready.")
    print(f"Saved as '{output_filename}'")
    print(f"\nThe new dataset has {features_df.shape[0]} rows and {features_df.shape[1]} columns.")
    print("\nHere's a preview:")
    print(features_df.head())

except FileNotFoundError as e:
    print(f"Error: {e}")
except KeyError as e:
    print(f"KeyError: {e}. A specified column was not found.")
