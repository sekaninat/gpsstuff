# from Tkinter import Tk     # from tkinter import Tk for Python 3.x
# from tkinter.filedialog import askopenfilename

# Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
# filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
# print(filename)

import tkinter as tk
from tkinter import filedialog
from tkinter import simpledialog
from tkinter import ttk

import gpxpy

# application_window = tk.Tk()

# file_path = filedialog.askopenfilename(parent=application_window, title="Vybat soubor")

# with open(file_path, 'r') as f:
#     gpx = gpxpy.parse(f)

# new_name = simpledialog.askstring("Novy nazev", "Zadejte novy nazev trasy", parent=application_window)
# gpx.name = new_name

# if len(gpx.tracks) == 0:
#     gpx.tracks[0].name = new_name
# else:
#     for i, track in enumerate(gpx.tracks):
#         track.name = "{}_{}".format(new_name, i)

# with filedialog.asksaveasfile(parent=application_window, title="Ulozit jako") as file_out:
#     file_out.write(gpx.to_xml())    

window = tk.Tk()

# Create the user interface
my_label = ttk.Label(window, text="Hello World")
my_label.pack()
def select_file():
    file_path = filedialog.askopenfilename(parent=window, title="Vybat soubor")

open_button = ttk.Button(window, text="Vybrat soubor")
open_button.pack()
open_button['command'] = select_file

new_name = ttk.Entry(window)

path = tk.Message(window, text="Nova cesta")
path.pack()

def update_path():
    path.configure(text=new_name.get())
    print(new_name.get())

new_name.after(10, update_path)
new_name.

new_name.pack()



save_button = ttk.Button(window, text="Ulozit soubor")
save_button['command'] = update_path
save_button.pack()
open_button['command'] = select_file


quit_button = ttk.Button(window, text="Quit")
quit_button.pack()
quit_button['command'] = window.destroy

# Start the GUI event loop
window.mainloop()