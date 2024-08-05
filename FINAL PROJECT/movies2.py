import tkinter as tk
from tkinter import *
import sqlite3
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk  # Install Pillow library: pip install Pillow
from cinemadatabase import *
connection = sqlite3.connect('database.db')


def on_next_clicked():
    selected_movie = movie_combobox.get()
    ticket_count = int(tickets_entry.get())
    cur = connection.cursor()

    if is_tickets_available(selected_movie, ticket_count):
        print(f"Proceeding to the next page with {ticket_count} tickets for {selected_movie}")
        root.destroy()
        import tickethall

    else:
        cur.execute('SELECT tickets_available FROM movies WHERE name = ?',(selected_movie,))
        a = cur.fetchone()
        if a is not None:
            available_tickets = a[0]
            messagebox.showerror(":( Sorry", f"Onli {available_tickets} are available")

def is_tickets_available(selected_movie, ticket_count):
    movies = view_all_movies(connection)
    for movie in movies:
        if movie[1] == selected_movie:
            available_tickets = movie[5]
            return available_tickets >= ticket_count
    return False

# Create Tkinter window
root = tk.Tk()
root.title("Movies")
root.geometry("996x560+70+50")
root.resizable(False, False)

bgimage = ImageTk.PhotoImage(file='bg2.jpg')
bglabel = tk.Label(root, image=bgimage)
bglabel.place(x=0, y=0)
header = Label(root, text='Select Movie')
# Fetch movie data
movies = view_all_movies(connection)
movie_names = [movie[1] for movie in movies if movie[5] > 0]

# Movie Selection
label = tk.Label(root, text=("Select a Movie:"), bg='white', font=("Arial", 20))
label.pack(pady=30)

movie_combobox = ttk.Combobox(root, values=movie_names,font=("Arial", 15))
movie_combobox.pack(pady=18)

# Tickets Entry
label_tickets = tk.Label(root, text="Enter the count of tickets:", bg='white',font=("Arial", 16))
label_tickets.pack()

tickets_entry = tk.Entry(root,font=("Arial", 12))
tickets_entry.pack(pady=18)

# Next Button
next_button = tk.Button(root, text="Next", command=on_next_clicked,font=("Arial", 14))
next_button.pack(pady=18)

# Run Tkinter main loop
root.mainloop()
