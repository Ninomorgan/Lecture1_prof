"""

"""
from gestionale.vendite.gestoreOrdini import GestoreOrdini
from gestionale.vendite.provaCollections import prezzi
import flet as ft

class Controller:

    def __init__(self, v):
        self._view= v
        self._model= GestoreOrdini() # il mio model

    def aggiungi_ordine(self, e):
        #aggiungo value al txt del view
        #devo aggiungere come argomento (self, e) -> e è l'evento scatenante dal pulsante

        nomePstr = self._view._txtInNomeP.value
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
        email= self._view._txtInEmail.value
        categoria= self._view._txtInCategoria.value

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
        pass

    def gestisci_all_ordini(self,e ):
        pass
    def stampa_sommario(self, e):
        pass