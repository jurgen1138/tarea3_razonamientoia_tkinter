# registro.py - Pantalla de Registro de Usuario
import tkinter as tk
from tkinter import messagebox

from datos import cargar_usuarios, guardar_usuarios, buscar_usuario
from estilos import limpiar, cabecera, campo, boton, enlace, FONDO


def validar_contrasena(contrasena):
    """Devuelve una lista con los errores encontrados.
    Si la lista está vacía, la contraseña es válida."""
    errores = []

    if len(contrasena) < 6:
        errores.append("Debe tener mínimo 6 caracteres.")

    tiene_mayuscula = False
    tiene_minuscula = False
    tiene_especial = False

    for letra in contrasena:
        if letra.isupper():
            tiene_mayuscula = True
        if letra.islower():
            tiene_minuscula = True
        if not letra.isalnum():
            tiene_especial = True

    if not tiene_mayuscula:
        errores.append("Debe tener al menos una letra mayúscula.")
    if not tiene_minuscula:
        errores.append("Debe tener al menos una letra minúscula.")
    if not tiene_especial:
        errores.append("Debe tener al menos un carácter especial.")

    return errores

def mostrar_registro(ventana):
    limpiar(ventana)
    cabecera(ventana, "Registro de Usuario", "Completa tus datos para crear la cuenta")

    cuerpo = tk.Frame(ventana, bg=FONDO)
    cuerpo.pack(fill="both", expand=True, padx=25, pady=15)

    # Nombre y apellido van lado a lado
    fila = tk.Frame(cuerpo, bg=FONDO)
    fila.pack(fill="x", pady=(0, 8))
    entrada_nombre = campo(fila, "Nombre:")
    entrada_nombre.contenedor.pack(side="left", fill="x", expand=True, padx=(0, 5))
    entrada_apellido = campo(fila, "Apellido:")
    entrada_apellido.contenedor.pack(side="left", fill="x", expand=True, padx=(5, 0))

    entrada_correo = campo(cuerpo, "Correo:")
    entrada_correo.contenedor.pack(fill="x", pady=(0, 8))
    entrada_contrasena = campo(cuerpo, "Contraseña:", oculto=True)
    entrada_contrasena.contenedor.pack(fill="x", pady=(0, 12))

    def registrar():
        #Leer los datos ingresados
        nombre = entrada_nombre.get().strip()
        apellido = entrada_apellido.get().strip()
        correo = entrada_correo.get().strip().lower()
        contrasena = entrada_contrasena.get()
        #Validar que no estén vacíos y que la contraseña cumpla con las reglas
        if nombre == "" or apellido == "" or correo == "" or contrasena == "":
            messagebox.showerror("Error", "Debe completar todos los campos.")
            return
        usuario_existente = buscar_usuario(correo)
        if usuario_existente is not None:
            messagebox.showerror("Error", "El correo ya está registrado.")
            return
        errores = validar_contrasena(contrasena)
        #Une los errores en un solo mensaje y lo muestra en un messagebox
        if errores:
            messagebox.showerror("Error", "\n".join(errores))
            return
        #Cuando todo es válido, guarda el usuario en el archivo y muestra un mensaje de éxito
        usuarios = cargar_usuarios()
        usuarios.append({"nombre": nombre, "apellido": apellido, "correo": correo, "contrasena": contrasena})
        guardar_usuarios(usuarios)
        messagebox.showinfo("Éxito", "Usuario registrado correctamente.")

        # Volver al Login (se importa aquí adentro para evitar el import circular)
        from login import mostrar_login
        mostrar_login(ventana)

    boton(cuerpo, "Registrarse", registrar).pack(fill="x", ipady=6)
    ventana.bind("<Return>", lambda evento: registrar())

    enlace(cuerpo, "¿Ya tienes cuenta?", "Inicia sesión",
           lambda: ir_a_login(ventana)).pack(pady=10)

    entrada_nombre.focus()


def ir_a_login(ventana):
    from login import mostrar_login
    mostrar_login(ventana)
