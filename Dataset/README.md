# GNSS Spoofing and Jamming Dataset

This directory contains the dataset used for training and evaluating the
machine-learning model developed for the **GNSS Spoofing and Jamming Detector
using RISC-V** project.

## Dataset Source

The dataset used in this project was obtained from:

**Dataset:** [GNSS Dataset Under Jamming, Spoofing, and Meaconing Conditions (JammerTest 2024)]

**Source:** [Zenodo]

**Dataset Link:** [https://zenodo.org/records/15911589]

**Citation:** [M. I. Sayyaf, . miguel . ortizand V. Renaudin, “GNSS Dataset Under Jamming, Spoofing, and Meaconing Conditions (JammerTest 2024)”. Zenodo, Jul. 15, 2025. doi: 10.5281/zenodo.15911589.]

> The dataset is not originally created by the authors of this project.
> Credit for the original data belongs to the respective dataset creators
> and publishers.

## Purpose

The dataset was used to develop a machine-learning model capable of
distinguishing between different GNSS operating conditions.

The classification problem considered in this project consists of three
classes:

- **Normal** – Represents legitimate GNSS operation without intentional interference.
- **Jamming** – Represents GNSS reception affected by intentional radio-frequency interference.
- **Spoofing** – Represents manipulated or counterfeit GNSS signals intended to mislead the receiver.

## Dataset Processing

Before training the classifier, the original data was processed using Python.

The preprocessing pipeline included:

1. Loading the GNSS dataset.
2. Selecting the features required for classification.
3. Cleaning and preprocessing the data.
4. Assigning class labels for Normal, Jamming and Spoofing conditions.
5. Preparing the data for machine-learning training and evaluation.
6. Training a Support Vector Machine (SVM) classifier.

The Python scripts used for preprocessing and model development are available
in the [`Python`](../Python/) directory.

## Machine Learning Model

A **Support Vector Machine (SVM)** classifier was trained using the processed
GNSS data.

The trained model was subsequently adapted for embedded implementation and
deployed on a **RISC-V soft-core processor implemented on FPGA**.

The objective was to provide a lightweight classifier suitable for real-time
GNSS threat detection on resource-constrained embedded hardware.

## Dataset Files

The dataset files used for this project are stored in this directory.

```text
Dataset/
├── [dataset-file-name.csv]
└── README.md
