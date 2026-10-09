# registro.py - Pantalla de Registro de Usuario
import tkinter as tk
from tkinter import messagebox

from datos import cargar_usuarios, guardar_usuarios, buscar_usuario


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
    # Limpiar la pantalla anterior
    for widget in ventana.winfo_children():
        widget.destroy()

    tk.Label(ventana, text="Registro de Usuario", font=("Arial", 14, "bold")).pack(pady=15)

    #Nombre
    tk.Label(ventana, text="Nombre:").pack()
    entrada_nombre = tk.Entry(ventana, width=30)
    entrada_nombre.pack(pady=3)

    #Apellido
    tk.Label(ventana, text="Apellido:").pack()
    entrada_apellido = tk.Entry(ventana, width=30)
    entrada_apellido.pack(pady=3)

    # Correo
    tk.Label(ventana, text="Correo:").pack()
    entrada_correo = tk.Entry(ventana, width=30)
    entrada_correo.pack(pady=3)

    # Contraseña
    tk.Label(ventana, text="Contraseña:").pack()
    entrada_contrasena = tk.Entry(ventana, width=30, show="*")
    entrada_contrasena.pack(pady=3)


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

    tk.Button(ventana, text="Registrarse", command=registrar).pack(pady=10)

    enlace = tk.Label(ventana, text="¿Ya tienes cuenta? Inicia sesión", fg="blue", cursor="hand2")
    enlace.pack(pady=5)
    enlace.bind("<Button-1>", lambda evento: ir_a_login(ventana))

def ir_a_login(ventana):
    from login import mostrar_login
    mostrar_login(ventana)

