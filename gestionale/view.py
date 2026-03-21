"""

"""
import flet as ft
from mysql.opentelemetry.importlib_metadata import pass_none


class View:
    
    def __init__(self, page):
        self._controller = None
        self._page = page

        #sempre uguali
        self._page.title= "Titolo della finestra"
        self._page.horizontal_alignment= "CENTER" #allineamo la pagina al centro
        self._page.theme_mode= ft.ThemeMode.LIGHT
        self._page.update()

    
    
    def carica_interfaccia(self):
        #tre caampi di testo

        #prodotti
        self._txtInNomeP= ft.TextField( label= "Nome Prodotto", width=200) #label crea il riquadro
        self._txtInPrezzo = ft.TextField( label= "Prezzo",width=200)
        self._txtInQuantita = ft.TextField( label= "Quantità", width=200)
        #mettiamo tutti in una riga
        row1= ft.Row(controls= [self._txtInNomeP,self._txtInPrezzo,self._txtInQuantita],
                     alignment= ft.MainAxisAlignment.CENTER,)


        #cliente (nome, email, categoria)
        self._txtInNomeCiente = ft.TextField(label="Nome Cliente", width=200)  # label crea il riquadro
        self._txtInEmail = ft.TextField(label="email", width=200)
        self._txtInCategoria = ft.TextField(label="Categoria", width=200)
        # mettiamo tutti in una riga
        row2 = ft.Row(controls=[self._txtInNomeCiente, self._txtInEmail, self._txtInCategoria],
                      alignment=ft.MainAxisAlignment.CENTER, )


        #PULSANTI
        #1) agigunge ordine
        #2) processa ordine
        #3) processa tutti
        #4) stampa ordini
        # elevatetbutton --> text, on_click (nome della funzione in controller)
        self._btnAdd = ft.ElevatedButton( text="Aggiungi ordine",
                                          on_click = self._controller.aggiungi_ordine,
                                          width=200
                                          )
        self._btnGestisciOrdine = ft.ElevatedButton( text="Gestisci prossimo ordine",
                                          on_click = self._controller.gestisci_ordine,
                                          width=200
                                          )
        self._btnGestisciAllOrdini = ft.ElevatedButton( text="Gestisci tutti gli ordini",
                                          on_click = self._controller.gestisci_all_ordini,
                                          width=200
                                          )
        self._btnStampaInfo = ft.ElevatedButton( text="Stampa sommario",
                                          on_click = self._controller.stampa_sommario,
                                          width=200
                                          )

        row3 = ft.Row(controls= [self._btnAdd ,
                                 self._btnGestisciOrdine,
                                 self._btnGestisciAllOrdini,
                                 self._btnStampaInfo],
                      alignment=ft.MainAxisAlignment.CENTER)



        #blocco di testo
        self._lvOut = ft.ListView( expand= True)
        self._page.add(row1,row2, row3, self._lvOut)

    def set_controller(self,c):
        self._controller = c


    def update_page(self):
        self._page.update()