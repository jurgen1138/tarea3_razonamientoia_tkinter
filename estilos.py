# estilos.py - colores y widgets que se repiten en las tres pantallas
import tkinter as tk

AZUL_OSCURO = "#0F2A5C"
AZUL = "#1F5FBF"
AZUL_HOVER = "#174A96"
FONDO = "#F5F7FA"
BLANCO = "#FFFFFF"
GRIS_BORDE = "#C5CBD3"
GRIS_TEXTO = "#4A5360"


def limpiar(ventana):
    # Borra lo que haya en la ventana para poder dibujar la siguiente pantalla
    for widget in ventana.winfo_children():
        widget.destroy()
    ventana.configure(bg=FONDO)
    ventana.unbind("<Return>")


def cabecera(ventana, titulo, subtitulo):
    # Banda azul de arriba con el título
    marco = tk.Frame(ventana, bg=AZUL_OSCURO)
    marco.pack(fill="x")
    tk.Label(marco, text=titulo, bg=AZUL_OSCURO, fg=BLANCO,
             font=("Arial", 14, "bold"), anchor="w").pack(fill="x", padx=25, pady=(15, 0))
    tk.Label(marco, text=subtitulo, bg=AZUL_OSCURO, fg="#C9D6EE",
             font=("Arial", 9), anchor="w").pack(fill="x", padx=25, pady=(0, 15))
    return marco


def campo(padre, texto, oculto=False):
    # Label + Entry plano. Devuelve el Entry, y el Frame que lo contiene queda en entrada.contenedor
    contenedor = tk.Frame(padre, bg=FONDO)
    tk.Label(contenedor, text=texto, bg=FONDO, font=("Arial", 9), anchor="w").pack(fill="x")
    entrada = tk.Entry(contenedor, relief="flat", bg=BLANCO, font=("Arial", 10),
                       highlightthickness=1, highlightbackground=GRIS_BORDE,
                       highlightcolor=AZUL, show="*" if oculto else "")
    entrada.pack(fill="x", ipady=4, pady=(2, 0))
    entrada.contenedor = contenedor
    return entrada


def boton(padre, texto, comando, relleno=True):
    # Botón plano; cambia de color cuando el mouse pasa por encima
    if relleno:
        normal, hover, letra = AZUL, AZUL_HOVER, BLANCO
    else:
        normal, hover, letra = BLANCO, "#E8EFFA", AZUL
    b = tk.Button(padre, text=texto, command=comando, relief="flat", bd=0,
                  bg=normal, fg=letra, activebackground=hover, activeforeground=letra,
                  font=("Arial", 10, "bold"), cursor="hand2",
                  highlightthickness=0 if relleno else 1, highlightbackground=AZUL)
    b.bind("<Enter>", lambda e: b.config(bg=hover))
    b.bind("<Leave>", lambda e: b.config(bg=normal))
    return b


def enlace(padre, texto_normal, texto_enlace, comando):
    # Fila tipo "¿No tienes cuenta? Regístrate" con la segunda parte clickeable
    fila = tk.Frame(padre, bg=FONDO)
    tk.Label(fila, text=texto_normal, bg=FONDO, fg=GRIS_TEXTO, font=("Arial", 9)).pack(side="left")
    link = tk.Label(fila, text=texto_enlace, bg=FONDO, fg=AZUL,
                    font=("Arial", 9, "bold"), cursor="hand2")
    link.pack(side="left", padx=(3, 0))
    link.bind("<Button-1>", lambda evento: comando())
    return fila
