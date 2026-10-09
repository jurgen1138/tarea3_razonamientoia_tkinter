# datos.py - Persistencia de usuarios en JSON (lo usan registro.py y login.py)
import json
import os

# Ruta del archivo junto a este .py (así funciona sin importar desde dónde se ejecute)
ARCHIVO_USUARIOS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "usuarios.json")


def cargar_usuarios():
    """Devuelve la lista de usuarios guardados. Si el archivo no existe, devuelve []."""
    if not os.path.exists(ARCHIVO_USUARIOS):
        return []
    with open(ARCHIVO_USUARIOS, "r", encoding="utf-8") as f:
        return json.load(f)


def guardar_usuarios(usuarios):
    """Guarda la lista completa de usuarios en el archivo."""
    with open(ARCHIVO_USUARIOS, "w", encoding="utf-8") as f:
        json.dump(usuarios, f, indent=4, ensure_ascii=False)


def buscar_usuario(correo):
    """Devuelve el diccionario del usuario con ese correo, o None si no existe."""
    for usuario in cargar_usuarios():
        if usuario["correo"] == correo:
            return usuario
    return None 



if __name__ == "__main__":
    print("Usuarios al inicio:", cargar_usuarios())
    usuarios = cargar_usuarios()
    usuarios.append({"nombre": "Prueba", "apellido": "Uno",
                     "correo": "prueba@correo.com", "contrasena": "Hola#123"})
    guardar_usuarios(usuarios)
    print("Usuarios después de guardar:", cargar_usuarios())
    print("Buscar prueba@correo.com:", buscar_usuario("prueba@correo.com"))
    print("Buscar nadie@correo.com:", buscar_usuario("nadie@correo.com"))
