"""

"""
from gestionale.vendite.gestoreOrdini import GestoreOrdini
from gestionale.vendite.provaCollections import prezzi, ordine
import flet as ft

class Controller:

    def __init__(self, v):
        self._view= v
        self._model= GestoreOrdini() # il mio model

    def aggiungi_ordine(self, e):
        #aggiungo value al txt del view
        #devo aggiungere come argomento (self, e) -> e è l'evento scatenante dal pulsante

        nomePstr = self._view._txtInNomeP.value
        if nomePstr=="":
            self._view._lvOut.controls.append(
                ft.Text("inserire un nome valido", color="red")
            )
            self._view._update_page()
            return
        try:
            prezzo = float(self._view._txtInPrezzo.value)
        except ValueError:
            self._view._lvOut.controls.append(
                ft.Text("il prezzo deve essere un numero", color= "red")

            )
            self._view.update_page()
            return
        try:
            quantita= int(self._view._txtInQuantita.value)
        except ValueError:
            self._view._lvOut.controls.append(
                ft.Text("la qunatita deve essere un numero", color="red")

            )
            self._view.update_page()
            return

        #Cliente
        nomeC = self._view._txtInNomeCiente.value
        if nomeC == "":
            self._view._lvOut.controls.append(
                ft.Text("inserire un nome valido", color="red")
            )
            self._view._update_page()
            return

        email= self._view._txtInEmail.value
        if email == "":
            self._view._lvOut.controls.append(
                ft.Text("inserire una email valida", color="red")
            )
            self._view._update_page()
            return

        categoria= self._view._txtInCategoria.value
        if categoria == "":
            self._view._lvOut.controls.append(
                ft.Text("inserire una categoria valida", color="red")
            )
            self._view._update_page()
            return

        ordine= self._model.crea_ordine(nomePstr, prezzo, quantita,
                                        nomeC,email,categoria)

        self._model.add_ordine(ordine)

        #puliamo interfaccia dopo averlo utilizzato
        self._view._txtInNomeP.value=""
        self._view._txtInPrezzo.value=""
        self._view._txtInQuantita.value=""
        self._view._txtInNomeCiente.value = ""
        self._view._txtInEmail.value = ""
        self._view._txtInCategoria.value = ""

        self._view._lvOut.controls.append(
            ft.Text("ordine aggiunto correttamente", color= "green")
        )
        self._view._lvOut.controls.append(
            ft.Text("dettagli ordine:")
        )
        self._view._lvOut.controls.append(
            ft.Text(ordine.riepilogo(), color= "blue")
        )
        self._view.update_page()






    def gestisci_ordine(self, e):
        self._view._lvOut.controls.clear()
        res , ordine = self._model.processa_prossimo_ordine() #avrò un output true or false
        if res :
            self._view._lvOut.controls.append(
                ft.Text("ordine processato correttamente", color= "green"))
            self._view._lvOut.controls.append(
                ft.Text(ordine.riepilogo(), color= "blue")
            )
            self._view.update_page()
        else:
            self._view._lvOut.controls.append(
                ft.Text("non ci sono ordini in cosa", color= "blue")
            )
            self._view.update_page()

    def gestisci_all_ordini(self,e ):
        self._view._lvOut.controls.clear()
        ordini = self._model.gestisci_tutti_ordini()
        if not ordini:
            self._view._lvOut.controls.append(
                ft.Text("nessun ordine in coda", color= "blue")
            )
            self._view.update_page()
        else:
            self._view._lvOut.controls.append(ft.Text("\n"))
            self._view._lvOut.controls.append(
                ft.Text(f"ordini processati: {len(ordini)}", color="green")
            )
            for o in ordini:
                self._view._lvOut.controls.append(ft.Text("\n"))
                self._view._lvOut.controls.append(ft.Text(o.riepilogo()))
            self._view.update_page()



    def stampa_sommario(self, e):
        self._view._lvOut.controls.clear()
        self._view._lvOut.controls.append(
            ft.Text("Ecco il riepilogo di tutti gli ordini", color= "orange"))
        self._view._lvOut.controls.append(
            ft.Text(self._model.get_riepilogo()))
        self._view.update_page()

