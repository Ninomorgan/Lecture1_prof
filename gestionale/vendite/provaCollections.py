from collections import Counter, deque

from gestionale.core.clienti import Cliente, ClienteRecord
from gestionale.core.prodotti import ProdottoRecord
from gestionale.vendite.ordini import Ordine, RigaOrdine

p1=ProdottoRecord("Laptop", 1200.0)
p2=ProdottoRecord("Mouse", 20.0)
p3=ProdottoRecord("Auricolari", 250.0)

#aggiungiamo in una lista
carrello=[p1,p2,p3, ProdottoRecord("Tablet", 700.0)] #posso crerlo anche dentro al volo

print(f"Prodotti nel carrello:")
for i,p in enumerate(carrello):
    print(f"{i} - {p.name} - {p.prezzo_unitario}")

carrello.append(ProdottoRecord("Monitor", 150.0))

#sortiamo lista
carrello.sort(key=lambda x: x.prezzo_unitario ) #crescente , inceve decrescente ->reverse=true
print(f"Prodotti nel carrello (ordine di prezzo):")
for i,p in enumerate(carrello):
    print(f"{i} - {p.name} - {p.prezzo_unitario}")

#calcoliamo il prezzo totale del carrello
tot= sum(p.prezzo_unitario for p in carrello)
print(f"il totale è: {tot}")

#EXTEND mi aggiunge un'alta lista
#carrello.extend([ProdottoRecord("BBB", 1200.0), ProdottoRecord("AAA", 20.0)])

#INSERT mi aggiunge in un indice un oggetto
#carrello.insert(2, ProdottoRecord("Laptop", 1200.0))

#RIMUOVERE
#carrello.pop() POP -> RIMUOVE ULTIMO ELEMENTO
#carrello.pop(2) RIMUOVE ELEMENTO IN INDICE
#carrello.remove(p1) # REMOVE -> RIMUOVE direttamente un Oggetto (prima occorrenza)
#carrello.clear() #CLEAR -> SVUOTA lista

#Sorting
#carrello.sort()
#carrello.sort(reverse=True)
#carrello.sort(key = funzione)
#carrello_ordinato= sorted(carrello) SORTED -> CREO UNA COPIA
#carrello.reverse() inverte ordine

#copie
#carrello_copia = carrello.copy() #shallow copy -> stessi oggetti di carrello (se modifico carrello modifico anche l'altra
#carrello_copia2= copy.deepcopy(carrello) copio

#TUPLE
sede_principale=(45,8,"torino") #sede di torino
sede_milano=(45,9,"milano") #sede milano
sedi=[sede_principale,sede_milano]

print(f"\nSede principale lat: {sede_principale[0]}, long: {sede_principale[1]}")
for s in sedi:
    print(f"Sede lat: {s[0]}, long: {s[1]}, comune: {s[2]}")

AliquotaIva=(
    ("Standard",0.22),
    ("Ridotta", 0.10),
    ("Alimentari", 0.04),
    ("Esente", 0.0),
    )
for tipo,valore in AliquotaIva:
    print(f"{tipo} - {valore}")

def calcola_stat_carrello(carrello):
    """ Restitutisce prezzo totale, max, minimo"""
    prezzi= [p.prezzo_unitario for p in carrello]
    return (sum(prezzi), sum(prezzi)/len(prezzi), max(prezzi), min(prezzi))

tot,media,max,mini=calcola_stat_carrello(carrello)
print("\nStatistica carrello: ")
print(f"{tot} - {media}- {max}- {mini}")

#set
categoria={"Gold","Silver","Bronze", "Gold"}
print(categoria)
categorie2= {"Platinum", "Elite", "Gold"}
categorie_all=categoria.union(categorie2) #unione
#categorie:all= categorie | categorie2
print(categorie_all)
categorie_comuni = categoria & categorie2
print(categorie_comuni)
categorie_esclusive =  categoria-categorie2 #solo quelli presenti in uno
print(categorie_esclusive)

prodotti_ordine_A={ProdottoRecord("Laptop", 1200.0),
                   ProdottoRecord("Mouse", 20.0),
                   ProdottoRecord("Auricolari", 250.0)
                   }

prodotti_ordine_B={ProdottoRecord("Laptop2", 1200.0),
                   ProdottoRecord("Mouse2", 20.0),
                   ProdottoRecord("Auricolari", 250.0)
                   }

#metodi per il set
#prodotti_ordine_A.add(ProdottoRecord("aaa", 1200.0), ) #   AGGIUNGE ELEMENTO
#prodotti_ordine_A.update(ProdottoRecord("Laptop", 1200.0), ProdottoRecord("Mouse", 20.0)) #AGGIUNGE + ELEMENTI

#remove
#s.remove(elem) rimuove elemento, se non esiste errore
#s.discard(elem) #non da errore
#s.pop() #rimuove e resitutisce un elemento
#s.clear()

#operazioni insieme
#s.difference(s1)
#s.symmetric_difference(s1)

#DIZIONARIO

catalogo= {
    "LAP01": ProdottoRecord("Laptop", 1200.0),
    "LAP02": ProdottoRecord("Laptop2", 2300.0),
    "AUR01": ProdottoRecord("Auricolari", 250.0),
    "MAU01": ProdottoRecord("MAU02", 2300.0),
}

codice= "LAP02"
prodotto = catalogo[codice] #prendo il prodotto associato al codice
print(f"il prodotto di codie: {codice} è :{prodotto}") #creiamo un def__str__ per il toString

prodotto2 = catalogo.get("non esiste")  #IMPORTANTE
if prodotto2 is None:
    print("prodotto non esiste\n")

#VALORI DI CHIAVI
keys= list(catalogo.keys()) #rest un set
values = list(catalogo.values())
for k in keys:
    print(k)
print(values)

print(f"\n i dati salvati sono:\n")
for k1, v2 in catalogo.items():
    print(f" code:{k1} - prod: {v2}")

#rimuovere valori
rimosso = catalogo.pop("LAP01")
print(rimosso)

#dict comprhension
prezzi= {codice:prod.prezzo_unitario for codice, prod in catalogo.items()}
print(prezzi)

#RICORDA
# - valore = d[key] -> legge
# -  d[key] = valore -> associa un valore alla chaive
# - valore = d.get(key, default) -> legge e imposta un valore
# - d.pop(key)
# - d.keys()
# - d.values()
# - d.items()
# if key in d -> vrifica s la chaive è già registrata nel dizionario

"""ESERCIZIO LIVE 
per ciascuno di seguenti casi decidere quale strttura usare:

1) Memorizzare una lista di ordini che devono essere processati in ordine di arrivo
2) Memorizzare i codici fiscali dei clienti che siano univoci
3) Creare un database di prodotti che posso cercare con un codice univoco
4) Memorizzare le coordinate delle sede di roma ;
5) Tenere traccia delle categorie di clienti che hanno fatto un ordine in un certo range di tempo
"""
#1)
o1= Ordine(
    [RigaOrdine(ProdottoRecord("LAP01", 1200.0), 3)],
    ClienteRecord("nino", "nino@gmail", "Gold")
)
o2= Ordine(
    [RigaOrdine(ProdottoRecord("LAP01", 1200.0), 3)],
    ClienteRecord("pippo", "@gmail", "Gold")
)
o3= Ordine(
    [RigaOrdine(ProdottoRecord("LAP01", 1200.0), 3)],
    ClienteRecord("topolino", "@gmail", "Gold")
)

lista_ordini = []
lista_ordini.append((o1,2))
lista_ordini.append((o2,10))
lista_ordini.append((o3,4))
print(lista_ordini)

#2
salvataggio_CF= {"MRGNNN04C16H33","MRGNNN04C16" ,"MRGNC16H33" }
print(salvataggio_CF)

#3
listino_prodotti={
    "LAP01": ProdottoRecord("LAP01", 1200.0),
    "LAP02": ProdottoRecord("LAP02", 2300.0)}

#4
sede_roma= (45,6,"Roma")
sedi.append(sede_roma)
print(sedi)

#5
categorie_periodo=set()
categorie_periodo.add("Gold")
categorie_periodo.add("Bronze")

print("#######################################")

lista_clienti=[
    ClienteRecord("nino", "nino@gmail", "Gold"),
    ClienteRecord("pippo", "pippo@gmail", "Bronze"),
    ClienteRecord("topolino", "topolino@gmail", "Gold"),
    ClienteRecord("ciccio", "LAP01@gmail", "Gold"),
    ClienteRecord("topogiggo", "topolino@gmail", "Bronze")

]

categorie = [c.categoria for c in lista_clienti]
categorie_countr= Counter(categorie)

print("distribuzione clienti")
print(categorie_countr)

print("catregoria piu frequente")
print(categorie_countr.most_common(1))

print("totale:")
print(categorie_countr.total())

vendite_gennaio = Counter(
    {"lap":13 , "tab": 3}
)
vendite_febbr = Counter(
    {"lap":3 , "tab": 2}
)


vendite_bimestre= vendite_febbr+vendite_gennaio

print(f"vednite gennaio: {vendite_gennaio}")
print(f"vednite febbr: {vendite_febbr}")
print(f"vednite bimestre: {vendite_bimestre}")

#COUNTE
#c.most_common(n)c -> restituisce n elementi piu frequenti
#c.total() -> somma dei conteggi

#DEQUE
coda_ordini= deque()

for i in range(1,10):
    cliente=ClienteRecord(f"Cliente {i}", f"cliente{i}@gmail", "Gold")
    prodotto= ProdottoRecord(f"prodotto{i}", 100.0*i)
    ordine= Ordine([RigaOrdine(prodotto,1)], cliente)
    coda_ordini.append(ordine)

print("====================================================")
print("DEQUE")

print(f"coda ordini numero {len(coda_ordini)}")

#se è la coda è vuota si stoppa
while coda_ordini:
    ordine_corrente=coda_ordini.popleft() #elemento aggiunto per primo
    print(f"ordine corrente: {ordine_corrente}")
print ("ho processato tutti gi ordini")
    

