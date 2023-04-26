
class DNA:
    ADENINE = "A"
    CYTOSINE = "c"
    GUANINE = "G"
    THYMINE = "T"
    
    def __init__(self, sequence: str):  
        self.sequence = sequence
    
    def __str__(self):
        return self.sequence
    
    @property
    def qty_of_adenine(self):
        return self.sequence.count(self.ADENINE)

    @property
    def qty_of_cytosine(self):
        return self.sequence.count(self.CYTOSINE)

    @property       
    def qty_of_guanine(self):
        return self.sequence.count(self.GUANINE)

    @property
    def qty_of_thymine(self):
        return self.sequence.count(self.THYMINE)
    
    def __add__(self, other):
        new_sequence = ""
        for char1, char2 in zip(self.sequence, other.sequence):
            new_sequence += max(char1, char2)
        return new_sequence
            
    def percent_of_nitrogenous_base(self):
        pct_of_A = (self.qty_of_adenine / len(self.sequence)) * 100
        pct_of_C = (self.qty_of_cytosine / len(self.sequence)) * 100
        pct_of_G = (self.qty_of_guanine / len(self.sequence)) * 100
        pct_of_T = (self.qty_of_thymine / len(self.sequence)) * 100
        return pct_of_A, pct_of_C, pct_of_G, pct_of_T
        
        
sequence1 = DNA("ATGCATGCATGC")
sequence2 = DNA("CGTACTAGCTAAACCT")
print(sequence2)
print(sequence1 + sequence2)