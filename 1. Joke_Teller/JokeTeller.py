import tkinter as tk
from tkinter import messagebox
import requests
import time

# Function to fetch a joke from JokeAPI in the selected language
def get_joke(language):
    url = "https://v2.jokeapi.dev/joke/Any"
    params = {
        "lang": language,
        "type": "twopart"  # We request jokes that have a setup and a delivery
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Function to display the joke in a popup window
def show_joke():
    # If the selected radio button is Spanish, use "es", otherwise use "en"
    language = "es" if language_var.get() == "Spanish" else "en"
    joke = get_joke(language)
    
    if joke:
        # Show the setup part of the joke
        messagebox.showinfo("Joke", joke['setup'])
        time.sleep(1)  # Wait 1 second before showing the punchline
        # Show the delivery (punchline) part of the joke
        messagebox.showinfo("Joke", joke['delivery'])
    else:
        messagebox.showerror("Error", "An error occurred while fetching the joke")

# Main window
window = tk.Tk()
window.title("Joke Teller :D")

# Variable to store the selected language
language_var = tk.StringVar(value="Spanish")

# Radio buttons for language selection
tk.Radiobutton(window, text="Spanish", variable=language_var, value="Spanish").pack()
tk.Radiobutton(window, text="English", variable=language_var, value="English").pack()

# Button to fetch and display the joke
tk.Button(window, text="Tell me a joke", command=show_joke).pack()

# Start the GUI event loop
window.mainloop()
