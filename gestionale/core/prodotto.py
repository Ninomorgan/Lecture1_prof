from dataclasses import dataclass

#per ogni tabella del nostro database creaimo una istanza così
@dataclass
class ProdottoRecord:
    name: str
    prezzo_unitario: float

    #lo dobbaiamo renderlo HASHABLE
    def __hash__(self):
        return hash(self.name) #chiave primaria

    def __str__(self):
        return f"{self.name} -- prezzo unitario {self.prezzo_unitario}"