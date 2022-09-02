"""Module for getting the RNA complement of a DNA strand."""

RNA_COMPLEMENT = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}

def to_rna(dna_strand: str) -> str:
    """Return the RNA complement of a DNA strand."""
    
    return ''.join(RNA_COMPLEMENT[nucleotide] for nucleotide in dna_strand)
