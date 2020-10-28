# Project rosalind.

A = "A"
C = "C"
G = "G"
T = "T"


RNA_CODON = {
    "UUU": "F",
    "CUU": "L",
    "AUU": "I",
    "GUU": "V",
    "UUC": "F",
    "CUC": "L",
    "AUC": "I",
    "GUC": "V",
    "UUA": "L",
    "CUA": "L",
    "AUA": "I",
    "GUA": "V",
    "UUG": "L",
    "CUG": "L",
    "AUG": "M",
    "GUG": "V",
    "UCU": "S",
    "CCU": "P",
    "ACU": "T",
    "GCU": "A",
    "UCC": "S",
    "CCC": "P",
    "ACC": "T",
    "GCC": "A",
    "UCA": "S",
    "CCA": "P",
    "ACA": "T",
    "GCA": "A",
    "UCG": "S",
    "CCG": "P",
    "ACG": "T",
    "GCG": "A",
    "UAU": "Y",
    "CAU": "H",
    "AAU": "N",
    "GAU": "D",
    "UAC": "Y",
    "CAC": "H",
    "AAC": "N",
    "GAC": "D",
    "UAA": None,
    "CAA": "Q",
    "AAA": "K",
    "GAA": "E",
    "UAG": None,
    "CAG": "Q",
    "AAG": "K",
    "GAG": "E",
    "UGU": "C",
    "CGU": "R",
    "AGU": "S",
    "GGU": "G",
    "UGC": "C",
    "CGC": "R",
    "AGC": "S",
    "GGC": "G",
    "UGA": None,
    "CGA": "R",
    "AGA": "R",
    "GGA": "G",
    "UGG": "W",
    "CGG": "R",
    "AGG": "R",
    "GGG": "G",}


def count_nucleotides(s):
    """Count the occurence of each nucleotide in string s."""
    if len(s) > 1000:
        raise ValueError("String exceeds maximum length of 1000.")
    totals = {A: 0, C: 0, G: 0, T: 0}
    ns = s.upper()
    for c in ns:
        totals[c] += 1
    return "{0} {1} {2} {3}".format(
        totals["A"],
        totals["C"],
        totals["G"],
        totals["T"])


def dna2rna(s):
    """Transcribe string s to rna."""
    if len(s) > 1000:
        raise ValueError("String exceeds maximum length of 1000.")
    return s.replace("t", "u")


def reverse_compliment(s):
    """Produce the reverse compliement of string s."""
    if len(s) > 1000:
        raise ValueError("String exceeds maximum length of 1000.")
    compliments = {A: T, C: G, G: C, T: A}
    comp_s = []
    ns = s.upper()
    for c in ns:
        comp_s.append(compliments[c])
    comp_s.reverse()
    return "".join(comp_s)


def point_mutations(s, t):
    """Count the number of point mutations in strings s and t."""
    ls = len(s)
    lt = len(t)
    if ls > 1000:
        raise ValueError("String exceeds maximum length of 1000.")
    if lt > 1000:
        raise ValueError("String exceeds maximum length of 1000.")
    if ls != lt:
        raise ValueError("Strings must be the same length.")
    diff_count = 0
    for sc, tc in zip(s, t):
        if sc != tc:
            diff_count += 1
    return diff_count


def rna2protein(s):
    """Encode rna string s as a protein string."""
    if len(s) > 10000:
        raise ValueError("String exceeds maximum length of 10000.")
    protein = []
    for i in range(0, len(s), 3):
        c = s[i:i+3]
        p = RNA_CODON[c.upper()]
        if p is None:
            break
        protein.append(p)
    return protein


def motif(s, t):
    """Find all locations of motif t in string s. The first location
    of string s is considered to be 1."""
    ls = len(s)
    lt = len(t)
    if ls > 1000:
        raise ValueError("String exceeds maximum length of 1000.")
    if ls < lt:
        raise ValueError("String t must not exceed length of string s.")
    ns = s.upper()
    nt = t.upper()
    locations = []
    index = 0
    while index != -1:
        index = ns.find(nt, index)
        if index != -1:
            index += 1
            locations.append(index)
    return locations


def _restriction_sites(s, l):
    """ Find all restriction sites of length l in s."""
    locations = []
    for i in range(len(s)):
        r = s[i:i+l]
        if len(r) < l:
            break
        comp_r = reverse_compliment(r)
        if r == comp_r:
            locations.append(i+1)
    return locations


def restriction_sites(s):
    """Find all restriction sites in s between 4 and 12 nucletoides
    in length."""
    if len(s) > 1000:
        raise ValueError("String exceeds maximum length of 1000.")
    ns = s.upper()
    results = {}
    for l in range(4,12):
        locations = _restriction_sites(ns, l)
        if len(locations) > 0:
            results[l] = locations
    output = ""
    for k, v in results.items():
        for j in v:
            output += f"{j}, {k}\n"
    return output

