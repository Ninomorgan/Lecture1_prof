"""
questo deve collegare tra loro controlle view e model
già impostato
"""
import flet as ft

from gestionale.controller import Controller
from UI.view import View


def main(page: ft.Page): #dobbiamo crrea un oggetto di tipo controllr e view
    v = View(page) #passa la pagine dove scrivere le cose
    c = Controller(v)
    v.set_controller(c) # contrella controller a view
    v.carica_interfaccia() # metodo della view

    pass

ft.app(target = main)