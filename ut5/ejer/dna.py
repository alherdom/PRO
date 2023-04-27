from __future__ import annotations

class DNA:
    ADENINE = "A"
    CYTOSINE = "C"
    GUANINE = "G"
    THYMINE = "T"
    
    def __init__(self, sequence: str):  
        self.sequence = sequence
    
    def __str__(self):
        return f'DNA sequence:{self.sequence}'
    
    @property
    def adenine_qty(self) -> int:
        return self.sequence.count(self.ADENINE)

    @property
    def cytosine_qty(self) -> int:
        return self.sequence.count(self.CYTOSINE)

    @property       
    def guanine_qty(self) -> int:
        return self.sequence.count(self.GUANINE)

    @property
    def thymine_qty(self) -> int:
        return self.sequence.count(self.THYMINE)

    @property
    def dna_size(self) -> int:
        return len(self.sequence)

    def __add__(self, other) -> DNA:
        new_sequence = ""
        for char1, char2 in zip(self.sequence, other.sequence):
            new_sequence += max(char1, char2)
        return DNA(new_sequence)

    def __mul__(self, other) -> DNA:
        new_sequence = ""
        for char1, char2 in zip(self.sequence, other.sequence):
            new_sequence += char1 if char1 == char2 else ""
        return DNA(new_sequence)
    
    @staticmethod
    def percent_calc(qty_base: int, dna_size: int) -> float:
        '''Operation to calculate the percent'''
        return round((qty_base / dna_size) * 100, 2)

    def pcts_nitro_bases(self) -> str:
        '''Calculate the percents of each nitrogenous bases'''
        pct_adenine = DNA.percent_calc(self.adenine_qty, self.dna_size)
        pct_cytosine = DNA.percent_calc(self.cytosine_qty, self.dna_size)
        pct_guanine = DNA.percent_calc(self.guanine_qty, self.dna_size)
        pct_thymine = DNA.percent_calc(self.thymine_qty, self.dna_size)
        return f'A:{pct_adenine}% C:{pct_cytosine}% G:{pct_guanine}% T:{pct_thymine}%'


sequence1 = DNA("CAATGCATGCATGC")
sequence2 = DNA("CAGTACTAGCTAAC")
sequence3 = sequence1 + sequence2
sequence4 = sequence1 * sequence2
print(sequence1)
print(sequence2)
print(sequence3)
print(sequence4)
print(sequence1.pcts_nitro_bases())
print(sequence2.pcts_nitro_bases())
print(sequence3.pcts_nitro_bases())
print(sequence4.pcts_nitro_bases())