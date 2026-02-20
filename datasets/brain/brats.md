# BraTS (Brain Tumor Segmentation Challenge)

## 📌 Dataset Overview

**Dataset Name:** Brain Tumor Segmentation (BraTS)  
**Body Region:** Brain  
**Modality:** MRI (T1, T1Gd, T2, FLAIR)  
**Primary Task:** Tumor Segmentation  
**Secondary Tasks:** Survival Prediction, Tumor Sub-region Classification  
**Data Format:** NIfTI (.nii.gz)  
**Annotation Type:** Expert Manual Segmentation  
**Approximate Size:** ~400–2000 cases (varies by year)  
**License:** Research Use Only  
**Access Type:** Registration Required  

---

## 🧠 Description

The Brain Tumor Segmentation (BraTS) dataset is one of the most widely used benchmark datasets in medical image analysis. It provides multi-parametric MRI scans of glioma patients with expert-annotated tumor sub-regions.

The dataset includes:

- Native T1-weighted (T1)
- Post-contrast T1-weighted (T1Gd)
- T2-weighted (T2)
- T2-FLAIR

Each subject includes voxel-level segmentation masks for:

- Enhancing Tumor (ET)
- Tumor Core (TC)
- Whole Tumor (WT)

BraTS has been used extensively in international segmentation challenges and serves as a benchmark for deep learning architectures such as U-Net, 3D CNNs, and transformer-based models.

---

## 🎯 Research Applications

- 3D Medical Image Segmentation
- Multi-modal MRI Fusion
- Tumor Sub-region Delineation
- Survival Prediction Modeling
- Domain Adaptation & Generalization
- Uncertainty Estimation in Medical AI

---

## 📂 Data Structure Example

Typical folder organization after extraction:
```
BraTS/
Patient_001/
T1.nii.gz
T1Gd.nii.gz
T2.nii.gz
FLAIR.nii.gz
seg.nii.gz
```


---

## ⚙ Technical Notes

- Images are skull-stripped and co-registered.
- All scans are resampled to 1mm³ isotropic resolution.
- Segmentation masks use integer labels:
  - 0: Background
  - 1: Necrotic / Non-enhancing Tumor
  - 2: Edema
  - 4: Enhancing Tumor

---

## 📊 Benchmark Importance

BraTS is considered a gold-standard dataset for:

- 3D segmentation benchmarking
- Comparing CNN vs Transformer architectures
- Evaluating medical segmentation robustness
- Multi-center MRI domain shift research

---

## 🔗 Official Source

https://www.med.upenn.edu/cbica/brats/

---

## 📖 Citation

Menze, B.H., Jakab, A., Bauer, S., et al.  
*The Multimodal Brain Tumor Image Segmentation Benchmark (BRATS).*  
IEEE Transactions on Medical Imaging, 2015.

---

## ⚖ License & Usage Notes

- Intended for research and educational purposes.
- Commercial usage may require additional permission.
- Users must register and agree to dataset terms.

---

## 🧩 Related Challenges

- BraTS Annual Segmentation Challenge
- MICCAI BraTS Competition