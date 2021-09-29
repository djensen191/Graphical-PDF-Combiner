#!/usr/bin/env python3

############################################
# Daniel Jensen 28 Aug 2021                #
#                                          #
# A python Front End to Manage PDF Files   #
# Using the PDF toolkit Command Line       #
# Utility                                  #
############################################

import subprocess 
import os
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
import tkinter.font as tkFont
from tkinter.messagebox import showinfo
from tkinter import messagebox
from tkinter.ttk import Label

# create and size the root window
root = tk.Tk()
root.title('PDF Merging Tool')
root.resizable(True, True)
root.geometry('800x600')

Output = Text(root, height=5,
		width = 25,
		bg = "white")
window_label = Label(text = "You Have Selected: ")
# Label the window
Label(root.master,
             text="Choose PDF Files To Merge",
  
             # Changing font-size here
             font=("Arial", 25)
             ).pack()

# Create a list to store filenames 
file_list = []

# Define the command and open a file dialog
def choose_pdf():
	filepath = os.path.basename(fd.askopenfilename(parent=root, title='Choose a PDF'))
	
	# append the filename to the list
	file_list.append(filepath)
	

# Create the button
B = tk.Button(root, text ="Choose PDF", command = choose_pdf)

# Define a function to end the choose loop and print the user selected pdf files.
def done_function():
	
	# Convert file_list to a string
	selected_files = ' '.join(file_list)

	Output.insert(END, selected_files)

# Create the done button allowing execution of the function
donebutton = tk.Button(root, text="Done", command=done_function)

B.pack()
window_label.pack()
Output.pack()
donebutton.pack() 

# Keep doing this until the user is done adding files
root.mainloop()


# Use subprocess to execute the merge command with the files the user has selected
#process = subprocess.Popen(["pdftk",] + file_list + ["cat", "output",] + new_name)





