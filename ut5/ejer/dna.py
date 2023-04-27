from __future__ import annotations

class DNA:
    ADENINE = "A"
    CYTOSINE = "C"
    GUANINE = "G"
    THYMINE = "T"
    
    def __init__(self, sequence: str):  
        self.sequence = sequence
    
    def __str__(self) -> str:
        return self.sequence
    
    @property
    def adenines(self) -> int:
        return self.sequence.count(self.ADENINE)

    @property
    def cytosines(self) -> int:
        return self.sequence.count(self.CYTOSINE)

    @property       
    def guanines(self) -> int:
        return self.sequence.count(self.GUANINE)

    @property
    def thymines(self) -> int:
        return self.sequence.count(self.THYMINE)
   
    def __len__(self) -> int:
        return len(self.sequence)

    def __add__(self, other) -> DNA:
        new_sequence = ""
        for char1, char2 in zip(self.sequence, other.sequence):
            new_sequence += max(char1, char2)
        if len(self) > len(other):
            new_sequence += self.sequence[len(other):]
        elif len(self) < len(other):
            new_sequence += other.sequence[len(self):]
        return DNA(new_sequence)

    def __mul__(self, other) -> DNA:
        new_sequence = ""
        for char1, char2 in zip(self.sequence, other.sequence):
            new_sequence += char1 if char1 == char2 else ""
        return DNA(new_sequence)
    
    @staticmethod
    def percent_calc(qty_base: int, dna_size: int) -> float:
        return (qty_base / dna_size) * 100

    def stats(self) -> dict:
        dna_size = len(self)
        pct_adenine = DNA.percent_calc(self.adenines, dna_size )
        pct_cytosine = DNA.percent_calc(self.cytosines, dna_size)
        pct_guanine = DNA.percent_calc(self.guanines, dna_size)
        pct_thymine = DNA.percent_calc(self.thymines, dna_size)
        return {self.ADENINE:pct_adenine,self.CYTOSINE:pct_cytosine,self.GUANINE:pct_guanine,self.THYMINE:pct_thymine}    

    @classmethod
    def build_from_file(cls, path: str):
        return DNA(open(path).read())
    
    def dump_to_file(self, path):       
        with open(path, "w") as f:
            f.write(self.sequence)
            
# sequence1 = DNA("CAATGCATGCATGCAC")
# sequence2 = DNA("CAGTACTAGCTAAC")
# sequence3 = sequence1 + sequence2
# sequence4 = sequence1 * sequence2
# print(sequence1)
# print(sequence2)
# print(sequence3)
# print(sequence4)
# print(sequence1.stats())
# print(sequence2.stats())
# print(sequence3.stats())
# print(sequence4.stats())