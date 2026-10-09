import tkinter as tk
from login import mostrar_login


ventana = tk.Tk()
ventana.title("Tarea 3 - Sistema de Usuarios")
ventana.geometry("350x400")
mostrar_login(ventana)
ventana.mainloop()

