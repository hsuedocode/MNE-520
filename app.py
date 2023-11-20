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
            'image': './static/cat_992k.webp',
            'lng': 250,
            'diesel': 500
        },
        '546': {
            'name': 'CAT 546',
            'image': './static/truck_546.bmp'
        },
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
root.geometry("800x800")
homepage_image_raw=ImageTk.PhotoImage(Image.open('./static/truck_546.bmp'))

# Create global variables to track selected options
selected_mf = tk.StringVar(root, 'Select a Manufacture')
selected_truck = tk.StringVar(root, 'Select a Truck')
gallon_input =  tk.StringVar(root)

# Initialize widgets - they are rendered based on the the order in which we call .pack(), later on
homepage_title_label = tk.Label(root, text = "Welcome to Dual Fuel LNG Mining Truck Tool 1.0", relief = "flat", width = 45, font = ("arial", 19, "bold"))
homepage_image_label = tk.Label(root, image=homepage_image_raw)
truck_image = tk.Label(root)
mf_dropdown = tk.OptionMenu(root, selected_mf, 'Select a Manufacture')
truck_dropdown = tk.OptionMenu(root, selected_truck, 'Select a Truck')

gallon_panel = tk.Frame(root)
gallon_textbox = tk.Entry(gallon_panel, width=18, background='gray')
gallon_label = tk.Label(gallon_panel, text='Gallon')

greenhousegas_label = tk.Label(root)
submit_button = tk.Button(root, text="Submit", command=lambda: on_submit(selected_truck.get()))


# Configure widget display attributes
mf_dropdown.config(width=20)
truck_dropdown.config(width=20)
gallon_textbox.config()

def on_mf_select(mf_id):
    selected_mf.set(mf_id)
    selected_truck.set('Select a Truck')
    truck_dropdown['menu'].delete(0,500) # resets the menu item when you change Manufacturer
    mf_trucks = TRUCKS[mf_id]
    for truck_id in mf_trucks.keys():
        truck_dropdown["menu"].add_command(label=mf_trucks[truck_id]['name'], command=lambda id=truck_id: selected_truck.set(id))

def calculate_ghg(input: float, truck):
    print(truck)
    # nick does caculation here
    ratio = truck['lng'] / truck['diesel']
    return input * ratio

def on_submit(truck_id):
    try: 
        mf_id = selected_mf.get()
        cur_truck = TRUCKS[mf_id][truck_id]
        img = ImageTk.PhotoImage(Image.open(cur_truck['image']).resize((300,200)))
        truck_image.configure(image=img)
        truck_image.image = img
        truck_image.pack()

        # perform calculation here
        ghg_result = calculate_ghg(float(gallon_textbox.get()), cur_truck)
        greenhousegas_label.config(text = "Green House Gas Conversion: "+str(ghg_result)) 
    except Exception:
        print(Exception)
        truck_image.pack_forget()
        tkinter.messagebox.showinfo("Message", "Enter truck manufacturer, model, and fuel")

for mf_id in MANUFACTURES:
    mf_dropdown["menu"].add_command(label=mf_id, command=lambda id=mf_id: on_mf_select(id))


# Render widgets in order
homepage_title_label.pack()
homepage_image_label.pack()

mf_dropdown.pack(pady=10)
truck_dropdown.pack(pady=10)

gallon_panel.pack()
gallon_textbox.pack(side='left')
gallon_label.pack(side='left')

greenhousegas_label.pack()
submit_button.pack()
truck_image.pack()

# start window
root.mainloop()