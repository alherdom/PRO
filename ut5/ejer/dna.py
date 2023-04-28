from __future__ import annotations

class DNA:
    ADENINE = "A"
    CYTOSINE = "C"
    GUANINE = "G"
    THYMINE = "T"
    BASES = (ADENINE,CYTOSINE,GUANINE,THYMINE)

    def __init__(self, sequence: str):  
        self.sequence = sequence

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

    def __str__(self) -> str:
        return self.sequence

    def __len__(self) -> int:
        return len(self.sequence)

    def __add__(self, other) -> DNA:
        new_sequence = ""
        for char1, char2 in zip(self.sequence, other.sequence):
            new_sequence += max(char1, char2)
        new_sequence += self.sequence[len(other):] if len(self) > len(other) else other.sequence[len(self):]
        return DNA(new_sequence)

    def __mul__(self, other) -> DNA:
        new_sequence = ""
        for char1, char2 in zip(self.sequence, other.sequence):
            new_sequence += char1 if char1 == char2 else ""
        return DNA(new_sequence)

    def __getitem__(self, index: int) -> str:
        return self.sequence[index]

    def __setitem__(self, index: int, char: str):
        new_char = char if char in DNA.BASES else DNA.ADENINE
        self.sequence = self.sequence[:index] + new_char + self.sequence[index + 1:]

    @staticmethod
    def calc_percent(qty_base: int, dna_size: int) -> float:
        return (qty_base / dna_size) * 100

    def stats(self) -> dict:
        dna_size = len(self)
        pct_adenine = DNA.calc_percent(self.adenines, dna_size)
        pct_cytosine = DNA.calc_percent(self.cytosines, dna_size)
        pct_guanine = DNA.calc_percent(self.guanines, dna_size)
        pct_thymine = DNA.calc_percent(self.thymines, dna_size)
        return {DNA.ADENINE:pct_adenine,DNA.CYTOSINE:pct_cytosine,DNA.GUANINE:pct_guanine,DNA.THYMINE:pct_thymine}    

    @classmethod
    def build_from_file(cls, path: str) -> DNA:
        return DNA(open(path).read())

    def dump_to_file(self, path: str):    
        with open(path, "w") as f:
            f.write(self.sequence)