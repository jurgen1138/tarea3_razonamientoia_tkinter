# home.py - Pantalla principal (Home)
import tkinter as tk

from estilos import limpiar, boton, AZUL_OSCURO, BLANCO, FONDO, GRIS_BORDE, GRIS_TEXTO


def mostrar_home(ventana, usuario):
    limpiar(ventana)

    # Banda azul con las iniciales y el saludo
    cabecera = tk.Frame(ventana, bg=AZUL_OSCURO)
    cabecera.pack(fill="x")

    iniciales = usuario["nombre"][0].upper() + usuario["apellido"][0].upper()
    tk.Label(cabecera, text=iniciales, bg=BLANCO, fg=AZUL_OSCURO, width=3,
             font=("Arial", 16, "bold")).pack(side="left", padx=(25, 15), pady=25, ipady=8)

    nombre_completo = usuario["nombre"] + " " + usuario["apellido"]
    tk.Label(cabecera, text="Bienvenido, " + nombre_completo, bg=AZUL_OSCURO, fg=BLANCO,
             font=("Arial", 13, "bold"), wraplength=210, justify="left",
             anchor="w").pack(side="left", fill="x")

    cuerpo = tk.Frame(ventana, bg=FONDO)
    cuerpo.pack(fill="both", expand=True, padx=25, pady=30)

    # Contenido libre: un mensaje dentro de una tarjeta
    tarjeta = tk.Frame(cuerpo, bg=BLANCO, highlightthickness=1, highlightbackground=GRIS_BORDE)
    tarjeta.pack(fill="x", pady=(0, 20))
    tk.Label(tarjeta, text="Has iniciado sesión correctamente. Tus datos están guardados en el sistema.",
             bg=BLANCO, fg=GRIS_TEXTO, font=("Arial", 9), wraplength=270,
             justify="left").pack(padx=15, pady=15)

    def cerrar_sesion():
        from login import mostrar_login
        mostrar_login(ventana)

    boton(cuerpo, "Cerrar sesión", cerrar_sesion, relleno=False).pack(fill="x", ipady=6)
