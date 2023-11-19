# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 17:19:13 2023

@author: Nick
"""
# import necessary libraries
from tkinter import *
from tkinter.ttk import *
import tkinter as tk
import tkinter.messagebox
from PIL import Image, ImageTk  #pip

# ---------------------------------------------------------------------------------------------------------------
# Section for Definited Functions

# Define a function to close the Python Script/Application
def exit_program():
    root.destroy()

def about():
    tkinter.messagebox.showinfo("About Dual Fuel LNG Mining Truck Tool 1.0", "This demo is for MNE 520: Data Analysis and Application Development for Mining Engineers\n\nCreator: Nicholas Yeh\nSemester: Fall 2023")

# Define a function to center the initial application window upon initialization
def center_window(window):
    window.update_idletasks()
    
    # Get the window's width and height
    window_width = window.winfo_width()
    window_height = window.winfo_height()

    # Calculate the x and y coordinates to center the window
    x = (window.winfo_screenwidth() - window_width) // 2
    y = (window.winfo_screenheight() - window_height) // 2

    # Set the window geometry
    window.geometry(f"+{x}+{y}")
    
# Define a function to center pictures/labels withing the Tkinter GUI , and manually adjust with x,y placement
# using pass through variables shift_x and shift_y
def center_image_in_window(image_label, shift_x, shift_y):
    image_label.update_idletasks()
    
    # Get the label's width and height
    label_width = image_label.winfo_width()
    label_height = image_label.winfo_height()
    

    # Calculate the x and y coordinates to center the label
    x = (image_label.winfo_screenwidth() - label_width) // 2
    y = (image_label.winfo_screenheight() - label_height) // 2

    # Set the label geometry
    image_label.place(x=x-shift_x, y=y-shift_y, anchor="center")\
# --------------------------------------------------------------------------------------------------------------

# Initialize Homepage GUI using tkinter, with size, title
root = Tk()
root.geometry("800x800")
center_window(root)
root.title("Dual Fuel LNG Mining Truck Tool 1.0")
# Pull in necessary image files, homepage mining truck upfitted with LNG kit and all other specific mining truck
# options where calculations can then be run in a separate window, PLEASE ADJUST DIRECTORY when you run
# script to put all the images in your own directory to run properly
ImageHomepage = Image.open('./Mining_Truck_w_LNG_Upfit.bmp')
ImageHomepageTk = ImageTk.PhotoImage(ImageHomepage)

# Create a label to display the Homepage image
HomepageLabel = tk.Label(root, image=ImageHomepageTk)
HomepageLabel.pack()

# Center the Homepage label in the window
center_image_in_window(HomepageLabel, 150, 150)
# Create a label to display the Homepage Text Box on top
HomepageTitleLabel = Label(root, text = "Welcome to Dual Fuel LNG Mining Truck Tool 1.0", relief = "flat", width = 45, font = ("arial", 19, "bold"))
center_image_in_window(HomepageTitleLabel, 375, 425)

# ---------------------------------------------------------------------------------------------------------------
# Setup the Menu Bar Creation on the top of the application
menu = Menu(root)
root.config(menu=menu)

submenu1 = Menu(menu)
menu.add_cascade(label="File", menu=submenu1)
submenu1.add_command(label="Exit", command=exit_program)

submenu2 = Menu(menu)
menu.add_cascade(label="Option", menu=submenu2)
submenu2.add_command(label="About", command=about)

# --------------------------------------------------------------------------------------------------------------
# label2 = Label(window, text=”Select Your Mining Truck”, relief = “solid”, width = 20, font = (“arial”, 14, “bold”)
# label2.place(x=150, y = 50)
# Create Buttons for different Manufacturer’s Mining Trucks
# def Run_Caterpillar777():
	
# Button_Caterpillar777 = Button(top or root, text = “Caterpillar 777”, image = ImageCaterpillar777Tk).pack(side = TOP)
root.mainloop() 
