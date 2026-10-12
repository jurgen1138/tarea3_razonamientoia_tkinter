# login.py - Pantalla de Inicio de Sesión
import tkinter as tk
from tkinter import messagebox

from datos import buscar_usuario
from estilos import limpiar, cabecera, campo, boton, enlace, FONDO
from registro import mostrar_registro


def mostrar_login(ventana):
    limpiar(ventana)
    cabecera(ventana, "Inicio de Sesión", "Ingresa tus datos")

    cuerpo = tk.Frame(ventana, bg=FONDO)
    cuerpo.pack(fill="both", expand=True, padx=25, pady=20)

    entrada_correo = campo(cuerpo, "Correo:")
    entrada_correo.contenedor.pack(fill="x", pady=(0, 10))
    entrada_contrasena = campo(cuerpo, "Contraseña:", oculto=True)
    entrada_contrasena.contenedor.pack(fill="x", pady=(0, 15))

    def iniciar_sesion():
        correo = entrada_correo.get().strip().lower()
        contrasena = entrada_contrasena.get()

        if correo == "" or contrasena == "":
            messagebox.showerror("Error", "Debe completar todos los campos.")
            return

        usuario = buscar_usuario(correo)
        if usuario is None:
            messagebox.showerror("Error", "El usuario no está registrado")
            return
        if usuario["contrasena"] != contrasena:
            messagebox.showerror("Error", "Correo o contraseña incorrectos")
            return

        # Import aquí adentro para evitar el import circular (home importa login)
        from home import mostrar_home
        mostrar_home(ventana, usuario)

    boton(cuerpo, "Iniciar sesión", iniciar_sesion).pack(fill="x", ipady=6)
    # Con Enter también se inicia sesión
    ventana.bind("<Return>", lambda evento: iniciar_sesion())

    enlace(cuerpo, "¿No tienes cuenta?", "Regístrate",
           lambda: mostrar_registro(ventana)).pack(pady=15)

    entrada_correo.focus()
