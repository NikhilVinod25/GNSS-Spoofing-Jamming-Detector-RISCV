#include <stdint.h>
#include "weights.h"

// --- MEMORY MAP (Using exact PicoRV32 addresses from your image) ---
#define INPUT_ADDR    ((volatile int32_t *)0x1000)
#define OUTPUT_ADDR   ((volatile int32_t *)0x2000)
#define RGB_LED       (*(volatile uint32_t *)0x40000000)
#define SEV_SEG       (*(volatile uint32_t *)0x40010000)

// --- SVM INFERENCE ENGINE ---
int32_t svm_predict_sev(int32_t *features) {
    int32_t best_class = -1;
    // Set baseline to the lowest possible 32-bit signed integer
    int32_t max_score = -2147483648; 

    // 1. Iterate through each of the 3 classes (One-vs-Rest)
    for (int c = 0; c < NUM_CLASSES; c++) {
        // Use 64-bit integer to prevent overflow during multiplication
        int64_t score = 0; 

        // 2. Calculate Dot Product (Weights * Features)
        for (int f = 0; f < NUM_FEATURES; f++) {
            score += (int64_t)SVM_WEIGHTS[c][f] * (int64_t)features[f];
        }

        // 3. Shift the decimal point back and add the Bias
        score = (score / SCALE_FACTOR) + SVM_BIAS[c];

        // 4. Argmax: If this class has the highest score so far, keep it
        if ((int32_t)score > max_score) {
            max_score = (int32_t)score;
            best_class = c;
        }
    }
    
    // Returns 0 (Normal), 1 (Jamming), or 2 (Spoofing)
    return best_class; 
}

int main() {
    int32_t last_result = -1;

    while (1) {
        int32_t result = svm_predict_sev((int32_t *)INPUT_ADDR);
        
        // Write to BRAM for Jupyter Console
        *OUTPUT_ADDR = result;

        if (result != last_result) {
            // 1. Update the RGB LED
            if (result == 0)      { RGB_LED = 0x2; } // Normal (Green)
            else if (result == 1) { RGB_LED = 0x4; } // Jamming (Red)
            else if (result == 2) { RGB_LED = 0x1; } // Spoofing (Blue)
            else                  { RGB_LED = 0x0; }
            
            last_result = result;
        }
        
        // Short delay to prevent AXI bus saturation
        for(volatile int i=0; i<1500; i++);
    }
    return 0;
}      
