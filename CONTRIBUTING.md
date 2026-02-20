# Contributing to Medical-Imaging-Data-Hub

First of all, thank you for your interest in contributing to **Medical-Imaging-Data-Hub**.

This repository aims to provide a structured, research-friendly, and industry-relevant index of publicly available medical imaging datasets. Contributions that improve accuracy, organization, metadata quality, and usability are highly appreciated.

---

## 🎯 Project Goal

The goal of this repository is to:

- Provide a structured index of medical imaging datasets
- Standardize metadata for research and engineering use
- Improve discoverability of publicly available medical datasets
- Maintain high-quality formatting and consistency
- Support both academic research and industry prototyping

---

## 🛠 How You Can Contribute

You can contribute in several ways:

- Add a new dataset
- Improve metadata of an existing dataset
- Fix broken links
- Improve formatting consistency
- Add missing license or citation information
- Improve documentation clarity
- Suggest better categorization

---

## 📂 Adding a New Dataset

### Step 1: Fork the Repository

Click the **Fork** button on GitHub.

### Step 2: Follow the Folder Structure

Add the dataset inside:
```datasets/<body_region>/<dataset_name>.md```

Example:
```datasets/brain/new_dataset.md```

If the body region folder does not exist, create it.

---

### Step 3: Follow the Standard Dataset Template

Every dataset file must follow this structure:


# Dataset Name

**Dataset Name:**  
**Body Region:**  
**Modality:**  
**Primary Task:**  
**Format:**  
**Approx Size/Images:**  
**License:**  
**Access Type:**  

---

## Description

Brief description of the dataset.

---

## Research Tasks

- Task 1
- Task 2

---

## Source

Official dataset URL

---

## Citation

Academic reference if available

### Step 4: Update Metadata Files

You must update:
```
metadata/dataset_index.csv
metadata/dataset_index.json
```

Ensure consistency between:
- CSV entry
- JSON entry
- Markdown dataset file

All metadata fields must match.


## 📊 Metadata Standards

Please follow these formatting rules:

- Use consistent naming for modalities (MRI, CT, X-ray, Ultrasound, PET)
- Use | to separate multiple modalities
- Use | to separate multiple tasks
- Avoid abbreviations unless widely recognized
- Do not use promotional language
- Provide official source links only

## 🔍 Dataset Requirements

Only include datasets that:

- Are publicly available
- Have official access links
- Are legitimate academic or institutional releases
- Provide clear licensing information

Do NOT include:

- Private datasets
- Unverified Google Drive links
- Pirated data
- Commercial datasets without permission

### 🧪 Quality Control

Before submitting a Pull Request:
- Check that all links work
- Ensure metadata is complete
- Verify license information
- Ensure formatting matches existing entries
- Run a CSV formatting check (no broken columns)