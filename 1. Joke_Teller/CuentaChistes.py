import tkinter as tk
from tkinter import messagebox
import requests
import time

# Función para obtener un chiste desde la API JokeAPI en el idioma seleccionado
def obtener_chiste(idioma):
    url = "https://v2.jokeapi.dev/joke/Any"
    params = {
        "lang": idioma,       # Idioma del chiste ("es" o "en")
        "type": "twopart"     # Solicitamos chistes de dos partes: setup y delivery
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()  # Devuelve la respuesta en formato JSON
    else:
        return None             # Si ocurre un error, devolvemos None

# Función para mostrar el chiste en ventanas emergentes (pop-ups)
def mostrar_chiste():
    # Si el idioma seleccionado en el radiobutton es "Español", se usa "es", de lo contrario "en"
    idioma = "es" if var_idioma.get() == "Español" else "en"
    chiste = obtener_chiste(idioma)
    
    if chiste:
        # Mostrar la primera parte del chiste (setup)
        messagebox.showinfo("Chiste", chiste['setup'])
        time.sleep(1)  # Esperar 1 segundo antes de mostrar la segunda parte
        # Mostrar la segunda parte del chiste (delivery)
        messagebox.showinfo("Chiste", chiste['delivery'])
    else:
        # Mostrar un error si no se pudo obtener el chiste
        messagebox.showerror("Error", "Se obtuvo un error al obtener el chiste")

# Crear la ventana principal de la aplicación
ventana = tk.Tk()
ventana.title("Cuenta Chistes :D")

# Variable para almacenar el idioma seleccionado
var_idioma = tk.StringVar(value="Español")

# Botones de selección de idioma
tk.Radiobutton(ventana, text="Español", variable=var_idioma, value="Español").pack()
tk.Radiobutton(ventana, text="Inglés", variable=var_idioma, value="Inglés").pack()

# Botón para contar el chiste
tk.Button(ventana, text="Contar chiste", command=mostrar_chiste).pack()

# Iniciar el bucle principal de la interfaz gráfica
ventana.mainloop()
