import tkinter as tk
from tkinter import *
from tkinter.ttk import *
import tkinter as tk
import tkinter.messagebox
from PIL import Image, ImageTk  #pip

TRUCKS = {
    'CAT': {
        '992': {
            'name': 'CAT 992',
            'image': './static/cat_992k.webp'
        },
        '546': {
            'name': 'CAT 546',
            'image': './static/truck_546.bmp'
        }
    },
    'KOMATSU': {
        '930e': {
            'name': 'Komatsu 930E 5SE',
            'image': './static/komatsu-930e-5se.jpeg'
        }
    }
}

MANUFACTURES = ['CAT', 'KOMATSU']


root = tk.Tk()
root.title("Dual Fuel LNG Mining Truck Tool 1.0")
root.geometry("600x500")

# Create global variables to track selected options
selected_mf = tk.StringVar(root, 'Select a Manufacture')
selected_truck = tk.StringVar(root, 'Select a Truck')

# Initialize widgets - they are rendered based on the the order in which we call .pack(), later on
truck_widget = tk.Label(root)
mf_dropdown = tk.OptionMenu(root, selected_mf, 'Select a Manufacture')
truck_dropdown = tk.OptionMenu(root, selected_truck, 'Select a Truck')
submit_button = tk.Button(root, text="Submit", command=lambda: on_truck_select(selected_truck.get()))

# Configure widget display attributes
mf_dropdown.config(width=20)
truck_dropdown.config(width=20)

def on_mf_select(mf_id):
    selected_mf.set(mf_id)
    truck_dropdown['menu'].delete(0,500)
    mf_trucks = TRUCKS[mf_id]
    for truck_id in mf_trucks.keys():
        truck_dropdown["menu"].add_command(label=mf_trucks[truck_id]['name'], command=lambda id=truck_id: selected_truck.set(id))

def on_truck_select(truck_id):
    mf_id = selected_mf.get()
    trucks = TRUCKS[mf_id]
    img = ImageTk.PhotoImage(Image.open(trucks[truck_id]['image']).resize((300,200)))
    truck_widget.configure(image=img)
    truck_widget.image = img

for mf_id in MANUFACTURES:
    mf_dropdown["menu"].add_command(label=mf_id, command=lambda id=mf_id: on_mf_select(id))


# Render widgets in order
mf_dropdown.pack(pady=10, ipadx=10)
truck_dropdown.pack(pady=10, ipadx=10)
submit_button.pack()
truck_widget.pack()

# start window
root.mainloop()