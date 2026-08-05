
#ifndef WEIGHTS_H
#define WEIGHTS_H

#include <stdint.h>

#define SCALE_FACTOR 8192
#define NUM_FEATURES 13
#define NUM_CLASSES 3

// Standard Scaler Mean and Scale (For Python to use, or reference)
// We DO NOT use these in C anymore. Python does the scaling.

static const int32_t SVM_WEIGHTS[NUM_CLASSES][NUM_FEATURES] = {
    {-15084, 10229, -53160, 17260, 4542, 1295, 221, -27742, -69171, -874, 1124, 716, 11624}, 
    {10397, -10686, 58990, -17462, -5736, -1577, -224, -24652, 70085, 1068, -785, -1233, -11385}, 
    {1226, 222, -1424, 908, 1832, -292, 63, 23861, -1897, -243, 445, -627, -974}
};

static const int32_t SVM_BIAS[NUM_CLASSES] = { -64929, 42227, 1702 };

#endif
