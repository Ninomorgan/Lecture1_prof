from gestionale.core.prodotti import ProdottoRecord

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
