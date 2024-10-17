from List1 import dna_complement
def sequencer(sequence):
    """
    This function takes a DNA sequence and returns the sequence of genes
    Parameters:
        sequence(str): the DNA sequence
    Returns:
        genes(list): the list of genes
    """
    genes = []
    gene = ""
    for i in sequence:
        if (i == "A" or i == "T" or i == "C" or i == "G") and len(gene) != 3:
            gene += i
            if len(gene) == 3:
                genes.append(gene)
                gene = ""
    return genes
sequence = input("Enter your DNA sequence: ")
gene = ""
stop = False
into_threes = sequencer(sequence)
genes = []
for i in into_threes:
    if i == "ATG" or "ATG" in gene:
        gene += i
    if i == "TAA" or i == "TAG" or i == "TGA":
        if len(gene) % 9 == 0 and len(gene)>=9:
            genes.append(gene)
        gene = ""
for i in genes:
    print("The gene is: " + i)
    print("And it's complement is: " + dna_complement(i))