# Task 3: Data Visualization on Protein Dataset

## Project Overview

This project focuses on transforming the protein dataset extracted in **Task 1** into meaningful visualizations using Python. The visualizations help identify trends, patterns, distributions, and relationships within the biological data, making it easier to interpret and communicate key findings.

---

## Objectives

- Transform raw biological data into meaningful visualizations.
- Explore protein characteristics through charts and graphs.
- Identify trends, patterns, and anomalies within the dataset.
- Present biological information in a clear and understandable manner.
- Build a professional portfolio of scientific data visualizations.

---

## Technologies Used

- Python
- Pandas
- Matplotlib
- Seaborn
- Jupyter Notebook

---

## Dataset

The visualizations are created using the **Protein_Dataset.csv** generated in **Task 1: Biological Data Extraction Using BioPython**.

The dataset contains:

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

## Visualizations Created

The following visualizations were developed:

- Horizontal Bar Chart of Protein Records by Organism
- Bar Chart of Protein Records by Organism
- Histogram of Protein Sequence Length
- Histogram of Molecular Weight
- Boxplot for Protein Sequence Length
- Scatter Plot: Sequence Length vs Molecular Weight
- Correlation Heatmap
- Pie Chart of Organism Distribution

---

## Project Structure

```
Task3_Data_Visualization/
│
├── Protein_Visualization.ipynb
├── Protein_Dataset.csv
├── requirements.txt
├── README.md
└── figures/
    ├── organism_distribution_bar.png
    ├── organism_distribution_horizontal.png
    ├── sequence_length_histogram.png
    ├── molecular_weight_histogram.png
    ├── boxplot_sequence_length.png
    ├── scatter_sequence_vs_weight.png
    ├── correlation_heatmap.png
    └── pie_chart_organisms.png
```

---

## How to Run

1. Install the required libraries:

```bash
pip install -r requirements.txt
```

2. Open the notebook:

```text
Protein_Visualization.ipynb
```

3. Run all notebook cells to generate the visualizations.

---

## Key Insights

- Protein records are distributed across multiple organisms.
- Protein sequence lengths exhibit measurable variability.
- Molecular weight increases with sequence length.
- Boxplots help identify potential outlier proteins.
- Correlation analysis reveals a strong positive relationship between sequence length and molecular weight.
- Visualizations simplify the interpretation of complex biological datasets.

---

## Applications

This project can be applied to:

- Bioinformatics
- Protein Sequence Analysis
- Biological Data Visualization
- Scientific Reporting
- Exploratory Data Analysis (EDA)
- Machine Learning Data Preparation

---

## Future Scope

The visualizations developed in this project can support:

- Protein Classification
- Clustering Analysis
- Predictive Modeling
- Comparative Protein Studies
- Functional Annotation
- Computational Biology Research

---

## Author

**Dhanyalakshmi**

M.Sc. Bioinformatics

CodeAlpha Data Analytics Internship
