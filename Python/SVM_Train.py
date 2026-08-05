import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.svm import LinearSVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.preprocessing import StandardScaler

# --- Configuration ---
SCALE_FACTOR = 8192  # 2^13
OUTPUT_FILE = "weights.h"
DATASET_FILE = 'dataset_balanced.csv'

# 1. Load Data
print(f"Loading {DATASET_FILE}...")
df = pd.read_csv(DATASET_FILE)
X = df.drop('label', axis=1)
y = df['label']

# --- PART A: Evaluation (For your Report) ---
print("\n--- Phase 1: Model Evaluation (Train/Test Split) ---")
# Split 80/20 just to calculate accuracy stats
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train on 80%
scaler_eval = StandardScaler()
X_train_scaled = scaler_eval.fit_transform(X_train)
X_test_scaled = scaler_eval.transform(X_test)

clf_eval = LinearSVC(dual=False, C=1.0, max_iter=10000)
clf_eval.fit(X_train_scaled, y_train)

# Evaluate
y_pred = clf_eval.predict(X_test_scaled)
acc = accuracy_score(y_test, y_pred)
cm = confusion_matrix(y_test, y_pred)

# --- TERMINAL OUTPUT FORMATTING ---
print("\n=== CLASSIFICATION REPORT ===")
print(classification_report(y_test, y_pred, digits=2))

print("=== CONFUSION MATRIX ===")
print(cm)

print("\n=== MODEL SHAPES ===")
print(f"Classes        : {clf_eval.classes_.tolist()}")
print(f"Features       : {X_train.shape[1]}")
# Note: LinearSVC does not compute/store individual Support Vectors (SVs) 
# like the standard SVC does. It computes the weights directly, which is 
# why we use it for FPGA deployment!

print("\nModel and scaler parameters evaluated successfully.")

# --- PLOT CONFUSION MATRIX ---
plt.figure(figsize=(6, 5))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues') # Changed to Blues to match your previous style
plt.title(f'Confusion Matrix (Acc: {acc*100:.1f}%)')
plt.ylabel('True Label')
plt.xlabel('Predicted Label')
plt.show()


