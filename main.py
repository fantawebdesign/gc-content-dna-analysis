from Bio import SeqIO
import matplotlib.pyplot as plt

# Ganti dengan nama fail fasta sebenar
fasta_file = "dna_sequences.fasta"

# Ambil satu sahaja contig (biasanya NCBI FASTA panjang gila)
record = next(SeqIO.parse(fasta_file, "fasta"))
sequence = record.seq

# Kira GC content
gc_count = sequence.count("G") + sequence.count("C")
gc_content = (gc_count / len(sequence)) * 100

# Papar GC content
print(f"GC content: {gc_content:.2f}%")

# Pie chart
plt.pie(
    [gc_count, len(sequence) - gc_count],
    labels=["G+C", "A+T"],
    colors=["green", "red"],
    autopct="%.1f%%"
)
plt.title("GC Content in Human Sapiens")
plt.show()
