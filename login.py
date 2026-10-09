# login.py - TEMPORAL: solo para poder probar registro.py.
# Tu compañero reemplaza este archivo completo con el Login real.
import tkinter as tk
from registro import mostrar_registro

def mostrar_login(ventana):
    for widget in ventana.winfo_children():
        widget.destroy()
    tk.Label(ventana, text="(Login temporal - Beto)").pack(pady=40)
    
    enlace = tk.Label(ventana, text="¿No tienes cuenta? Regístrate", fg="blue", cursor="hand2")
    enlace.pack(pady=10)
    enlace.bind("<Button-1>", lambda evento: mostrar_registro(ventana))
