# login.py - TEMPORAL: solo para poder probar registro.py.
# Tu compañero reemplaza este archivo completo con el Login real.
import tkinter as tk


def mostrar_login(ventana):
    for widget in ventana.winfo_children():
        widget.destroy()
    tk.Label(ventana, text="(Login temporal - Beto)").pack(pady=40)
