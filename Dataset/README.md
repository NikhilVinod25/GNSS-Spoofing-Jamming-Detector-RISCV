# GNSS Spoofing and Jamming Dataset

This directory contains the dataset used for training and evaluating the
machine-learning model developed for the **GNSS Spoofing and Jamming Detector
using RISC-V** project.

## Dataset Source

The data used in this project was obtained from the **JammerTest 2024** dataset:

- **Dataset:** GNSS Dataset Under Jamming, Spoofing, and Meaconing Conditions (JammerTest 2024)
- **Repository:** Zenodo
- **Dataset Link:** https://zenodo.org/records/15911589
- **DOI:** https://doi.org/10.5281/zenodo.15911589

### Citation

M. I. Sayyaf, M. Ortiz, and V. Renaudin,  
*"GNSS Dataset Under Jamming, Spoofing, and Meaconing Conditions (JammerTest 2024),"*  
Zenodo, Jul. 15, 2025.  
doi: 10.5281/zenodo.15911589.

> **Note:** The original dataset was not created by the authors of this
> project. Credit for the data belongs to the original dataset creators and
> publishers.

## Purpose

The dataset was used to develop and evaluate a machine-learning model capable
of distinguishing between different GNSS operating conditions.

For this project, the classification problem was formulated using three
classes:

- **Normal** – Legitimate GNSS operation without intentional interference.
- **Jamming** – GNSS reception affected by intentional radio-frequency interference.
- **Spoofing** – Manipulated or counterfeit GNSS signals intended to mislead the receiver.

Although the original JammerTest 2024 dataset also contains data associated
with meaconing conditions, this project focuses on the **Normal, Jamming, and
Spoofing** classes required for the implemented detection system.

## Dataset Processing

The original GNSS data was processed using Python before being used for
machine-learning model development.

The preprocessing pipeline included:

1. Loading the required GNSS data.
2. Selecting the relevant samples and features.
3. Cleaning and preprocessing the data.
4. Assigning labels for Normal, Jamming, and Spoofing conditions.
5. Preparing the processed data for machine-learning training and evaluation.
6. Training and evaluating a Support Vector Machine (SVM) classifier.

The Python scripts used for preprocessing and model development are available
in the [`Python`](../Python/) directory.

## Machine Learning Model

A **Support Vector Machine (SVM)** classifier was trained using the processed
GNSS data.

The trained model parameters were subsequently adapted for embedded inference
and deployed on a **RISC-V soft-core processor implemented on an FPGA**.

The objective was to develop a lightweight classification system suitable for
real-time GNSS threat detection on resource-constrained embedded hardware.

## Dataset Files

The files contained in this directory represent the data used during the
machine-learning development stage of this project.

```text
Dataset/
├── <Dataset_Balanced.csv>
└── README.md
```

Replace `<dataset-file-name.csv>` above with the actual filename present in
this directory.

## Related Project Files

- [`../Python/`](../Python/) – Data preprocessing and SVM development scripts
- [`../Firmware/`](../Firmware/) – RISC-V embedded inference firmware
- [`../Vivado/`](../Vivado/) – FPGA implementation files
- [`../Docs/`](../Docs/) – Detailed project documentation

## License and Attribution

This repository does not claim ownership of the original **JammerTest 2024**
dataset.

Users who wish to reuse or redistribute the original data should refer to the
official Zenodo dataset page for the applicable licensing terms and citation
requirements.

When using the dataset in academic or research work, please cite the original
dataset creators and the corresponding Zenodo record.

## Reference

M. I. Sayyaf, M. Ortiz, and V. Renaudin,  
*"GNSS Dataset Under Jamming, Spoofing, and Meaconing Conditions (JammerTest 2024),"*  
Zenodo, 2025.  
doi: 10.5281/zenodo.15911589.
