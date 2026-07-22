from Bio import Entrez, SeqIO
import pandas as pd

# Enter your email (required by NCBI)
Entrez.email = "dhanu7100@gmail.com"

print("Searching NCBI Protein Database...")

# Search for SARS-CoV-2 Spike Proteins
search_handle = Entrez.esearch(
    db="protein",
    term="SARS-CoV-2 spike protein",
    retmax=10
)

search_results = Entrez.read(search_handle)
protein_ids = search_results["IdList"]

print(f"Found {len(protein_ids)} protein records.\n")

data = []

# Fetch each protein record
for pid in protein_ids:

    fetch_handle = Entrez.efetch(
        db="protein",
        id=pid,
        rettype="gb",
        retmode="text"
    )

    record = SeqIO.read(fetch_handle, "genbank")

    data.append({
        "Accession": record.id,
        "Description": record.description,
        "Sequence Length": len(record.seq),
        "Protein Sequence": str(record.seq)
    })

# Create DataFrame
df = pd.DataFrame(data)

# Save files
df.to_csv("Spike_Protein_Dataset.csv", index=False)

print("Dataset saved successfully!\n")
print(df)
