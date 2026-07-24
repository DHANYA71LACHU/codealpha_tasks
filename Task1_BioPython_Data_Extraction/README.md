# Task 1: Biological Data Extraction Using BioPython

## Project Overview

This project demonstrates how to extract biological protein data from the NCBI Protein database using the BioPython library. The retrieved records are processed into a structured dataset for downstream bioinformatics and data analysis.

---

## Objectives

- Access the NCBI Protein database using BioPython.
- Retrieve protein information programmatically.
- Create a structured biological dataset.
- Export the dataset as a CSV file.
- Prepare the dataset for Exploratory Data Analysis (EDA).

---

## Technologies Used

- Python
- BioPython
- Pandas
- NCBI Entrez API

---

## Dataset Features

The generated dataset contains the following information:

- Accession ID
- Protein Description
- Organism
- Sequence Length
- Amino Acid Count
- Molecular Weight (Approx.)
- Collection Date (if available)
- Country (if available)
- Protein Sequence

---

## Project Structure

```
Task1_BioPython_Data_Extraction/
│
├── extract_protein_data.py
├── Protein_Dataset.csv
├── requirements.txt
└── README.md
```

---

## How to Run

1. Install the required libraries:

```bash
pip install -r requirements.txt
```

2. Run the Python script:

```bash
python extract_protein_data.py
```

---

## Output

The script generates:

- `Protein_Dataset.csv`


---

## Applications

The generated dataset can be used for:

- Protein sequence analysis
- Exploratory Data Analysis (EDA)
- Bioinformatics research
- Machine Learning applications
- Protein classification studies

---

## Author

**V Dhanyalakshmi**

M.Sc. Bioinformatics

CodeAlpha Data Analytics Internship
