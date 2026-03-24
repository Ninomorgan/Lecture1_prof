"""
creiamo un software che :
1) supporti arrivo e gestione ordini
    quando arriva un ordine lo aggiungo a una coda
2) avere delle  funzionalità per statistiche su ordini (quante volte vendo un prodotto, quanti prodotti acquista un cliente
3) fornire statistiche per cliente
"""
from collections import deque, Counter, defaultdict

from mysql.connector.constants import flag_is_set

from gestionale.core.clienti import ClienteRecord
from gestionale.core.prodotti import ProdottoRecord
from gestionale.vendite.ordini import Ordine, RigaOrdine


class GestoreOrdini:
    def __init__(self):
        self._ordini_da_processare = deque()
        self._ordini_processati= []
        self._statistiche_prodotti= Counter() #importiamo counter per contatore
        self._statistiche_categoria = defaultdict(list)

    #metodo per aggiungere prodotti
    def add_ordine(self, ordine:Ordine):
        self._ordini_da_processare.append(ordine)
        print(f"ricevuto un nuovo ordine da parte di {ordine.cliente}")
        print(f"ordini da evadere ancora : {len(self._ordini_da_processare)}")

    def processa_prossimo_ordine(self):
        """ questo metodo legge il proddimo ordine in coda e lo gestisce"""
        print("\n" + "-" * 60)

        #vediamo se ci sono ordini da prcessare
        if not self._ordini_da_processare:
            print ("non ci sono ordini da processare")
            return False, Ordine([], ClienteRecord("","",""))

        #se esiste lo procssiamo e poi aggiornimao le statisitche
        ordine = self._ordini_da_processare.popleft()

        print (f"sto processando l'ordine di: {ordine.cliente}")
        print(ordine.riepilogo())

        for riga in ordine.righe:
            self._statistiche_prodotti[riga.prodotto.name] += riga.quantita #aggiorno la statistica su prodotti venduti
            #avrò una lista di nome e quatita venduta


            #3) aggiugno un dizionario per categoria e numeor ordini
            self._statistiche_categoria[ordine.cliente.categoria].append(ordine) #asspcia alla categoria un ordine

            #ARCHIVIAMO ORDINE
            self._ordini_processati.append(ordine)

            print(f"Ordine correttamente processato")
            return True, ordine

    def crea_ordine (self , nomeP, prezzoP, quantita, nomeC, mailC, categoriaC):

        return Ordine([RigaOrdine(ProdottoRecord(nomeP, prezzoP), quantita)],
                      ClienteRecord(nomeC, mailC, categoriaC))
    #ci restituisce la o che ci serviva


    def gestisci_tutti_ordini(self):
        """ Processa tutti gli ordini presenti in coda"""
        print("\n" + "=" * 60)
        print(f"processando tutti gli {len(self._ordini_da_processare)} ordini")
        ordini=[]
        while self._ordini_da_processare:
            _, ordine= self.processa_prossimo_ordine()
            ordini.append(ordine)
        print("tutti gli ordini sono stati processati.")
        return ordini

    """ Metodo per stampare caratt. ordine"""

    def get_statistiche_prodotti(self, top_n: int=5):
        """ restituisce info su quanti prodottti ho venduto (unità di un certo prodotto)
        i più venduti """
        valori = []
        for prodotto,quantita in self._statistiche_prodotti.most_common(top_n):
            valori.append((prodotto, quantita))
        return valori




    def get_distribuzione_categoria(self):
        """ questo metodo restituisce info su totale fatturato pr ogni categoria presente"""
        valori = []
        for cat in self._statistiche_categoria.keys():
            ordini= self._statistiche_categoria[cat]
            totale_fatturato= sum(o.totale_lordo(0.22) for o in ordini)
            valori.append((cat, totale_fatturato))
        return valori


    def stampa_riepilogo(self):
        print("\n"+"="*60)
        print("Stato attuale del businees:")
        print(f"Ordini correttamente gestiti: {len(self._ordini_processati)}")
        print(f"Ordini in coda: {len(self._ordini_da_processare)}")
        print("PRODOTTI PIU' VENDUTI")

        for prod, quantita in self.get_statistiche_prodotti():
            print(f"Prodotto: {prod} quantita: {quantita}")

        print(f"fatturato per categorie")
        for cat, fatt in self.get_distribuzione_categoria():
            print(f"Categoria: {cat} fatturato: {fatt}")

    def get_riepilogo(self):
        riepilogo = ""
        riepilogo+=("\n"+"="*60)

        riepilogo+=(f"\nOrdini correttamente gestiti: {len(self._ordini_processati)}")
        riepilogo+=(f"\nOrdini in coda: {len(self._ordini_da_processare)}")
        riepilogo+=("\nPRODOTTI PIU' VENDUTI")

        for prod, quantita in self.get_statistiche_prodotti():
            riepilogo +=(f"\nProdotto: {prod} quantita: {quantita}")

        riepilogo+=(f"\nfatturato per categorie")
        for cat, fatt in self.get_distribuzione_categoria():
            riepilogo+=(f"\nCategoria: {cat} fatturato: {fatt}")
        return riepilogo
def test_modulo():
    sistema= GestoreOrdini()

    ordini= [
        Ordine([RigaOrdine(ProdottoRecord("Laptop",1200.0),1),
                RigaOrdine(ProdottoRecord("Mouse", 10.0), 3)

        ], ClienteRecord("Mario", "mario@gmail", "Gold")),

        Ordine([
            RigaOrdine(ProdottoRecord("Laptop", 1200.0), 1),
            RigaOrdine(ProdottoRecord("Mouse", 10.0), 2),
            RigaOrdine(ProdottoRecord("Ipad", 500.0), 1),
            RigaOrdine(ProdottoRecord("cuffie", 250.0), 3)
        ], ClienteRecord("Peppe", "mario@gmail", "Gold")),

        Ordine([
            RigaOrdine(ProdottoRecord("Laptop", 1200.0), 2),
            RigaOrdine(ProdottoRecord("Mouse", 10.0), 2)
        ], ClienteRecord("gianni", "mario@gmail", "Silver")),

        Ordine([
            RigaOrdine(ProdottoRecord("Ipad", 900.0), 1),
            RigaOrdine(ProdottoRecord("Cuffie", 250.0), 3)
        ], ClienteRecord("ciccio", "mario@gmail", "Gold")),

        Ordine([
            RigaOrdine(ProdottoRecord("Laptop", 1200.0), 1),
            RigaOrdine(ProdottoRecord("Mouse", 10.0), 3)
        ], ClienteRecord("nino", "mario@gmail", "Gold"))
    ]
    for o in ordini:
        sistema.add_ordine(o)

    sistema.gestisci_tutti_ordini()

    sistema.stampa_riepilogo()


if __name__ == "__main__":
    test_modulo()