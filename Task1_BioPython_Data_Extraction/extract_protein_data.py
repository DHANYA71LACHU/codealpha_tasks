from Bio import Entrez, SeqIO
import pandas as pd

Entrez.email = "dhanu7100@gmail.com"

AVG_AA_WEIGHT = 110

search = Entrez.esearch(
    db="protein",
    term="hemoglobin[Protein]",
    retmax=25
)

record = Entrez.read(search)
protein_ids = record["IdList"]

print(f"Found {len(protein_ids)} protein records.")

data = []

for pid in protein_ids:

    handle = Entrez.efetch(
        db="protein",
        id=pid,
        rettype="gb",
        retmode="text"
    )

    seq_record = SeqIO.read(handle, "genbank")

    sequence = str(seq_record.seq)
    aa_count = len(sequence)
    molecular_weight = aa_count * AVG_AA_WEIGHT

    organism = "Not Available"
    country = "Not Available"
    collection_date = "Not Available"

    
    if "organism" in seq_record.annotations:
        organism = seq_record.annotations["organism"]

        for feature in seq_record.features:
            qualifiers = feature.qualifiers

            if "country" in qualifiers:
                country = qualifiers["country"][0]

            if "collection_date" in qualifiers:
                collection_date = qualifiers["collection_date"][0]

    data.append({
        "Accession": seq_record.id,
        "Description": seq_record.description,
        "Organism": organism,
        "Sequence Length": aa_count,
        "Amino Acid Count": aa_count,
        "Molecular Weight (Da)": molecular_weight,
        "Collection Date": collection_date,
        "Country": country,
        "Protein Sequence": sequence
    })

df = pd.DataFrame(data)

df.to_csv("Protein_Dataset.csv", index=False)

print("\nDataset created successfully!\n")
print(df.head())