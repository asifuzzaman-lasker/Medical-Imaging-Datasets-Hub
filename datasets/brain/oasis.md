# OASIS (Open Access Series of Imaging Studies)

## 📌 Dataset Overview

**Dataset Name:** OASIS (Open Access Series of Imaging Studies)  
**Body Region:** Brain  
**Modality:** MRI (T1-weighted primarily; some longitudinal releases include additional sequences)  
**Primary Task:** Neurodegenerative Disease Analysis  
**Secondary Tasks:** Alzheimer’s Classification, Brain Aging Analysis, Structural Segmentation  
**Data Format:** NIfTI (.nii.gz)  
**Annotation Type:** Clinical diagnosis labels (varies by release)  
**Approximate Size:** 1,000+ MRI scans (across multiple releases)  
**License:** Open Access (research use)  
**Access Type:** Free Download (registration may be required for some releases)  

---

## 🧠 Description

OASIS (Open Access Series of Imaging Studies) is a publicly available neuroimaging dataset designed to support research in aging, dementia, and neurodegenerative diseases.

The dataset includes cross-sectional and longitudinal MRI scans of:

- Healthy aging adults
- Individuals with mild cognitive impairment (MCI)
- Patients diagnosed with Alzheimer’s disease

OASIS is widely used in medical imaging research for benchmarking classification and structural analysis models in brain MRI.

There are multiple releases:

- **OASIS-1:** Cross-sectional dataset
- **OASIS-2:** Longitudinal MRI dataset
- **OASIS-3:** Multi-modal longitudinal dataset with clinical assessments

---

## 🎯 Research Applications

- Alzheimer’s Disease Classification
- Mild Cognitive Impairment (MCI) Detection
- Brain Aging Modeling
- Structural Brain Segmentation
- Voxel-Based Morphometry (VBM)
- Deep Learning-Based MRI Classification
- Longitudinal Disease Progression Modeling

---

## 📂 Data Structure Example

Typical organization after download:
```
OASIS/
subject_001/
T1.nii.gz
subject_002/
T1.nii.gz
clinical_data.csv```



Some releases also include:

- Demographic data
- Cognitive scores
- Diagnostic labels
- Longitudinal follow-ups

---

## ⚙ Technical Notes

- Images are typically skull-stripped and preprocessed.
- Resolution and acquisition parameters may vary between releases.
- Metadata includes demographic and clinical information.
- Longitudinal data allows disease progression modeling.

---

## 📊 Benchmark Importance

OASIS is considered an important dataset for:

- Alzheimer’s detection benchmarks
- Brain structure analysis
- Age-related brain change studies
- Classical ML vs Deep Learning comparisons
- Transfer learning research in neuroimaging

It is frequently used in:

- CNN-based MRI classification
- 3D volumetric analysis
- Brain region segmentation research

---

## 🔗 Official Source

https://www.oasis-brains.org/

---

## 📖 Citation

Marcus, D.S., Wang, T.H., Parker, J., et al.  
*Open Access Series of Imaging Studies (OASIS): Cross-sectional MRI Data in Young, Middle Aged, Nondemented, and Demented Older Adults.*  
Journal of Cognitive Neuroscience, 2007.

---

## ⚖ License & Usage Notes

- Intended for research and educational purposes.
- Users must comply with data usage agreements.
- Commercial use may require additional permissions.

---

## 🧩 Related Research Directions

- Multi-modal MRI fusion (with PET in other datasets)
- Transformer-based volumetric modeling
- Brain structural connectivity analysis
- Explainable AI in neuroimaging