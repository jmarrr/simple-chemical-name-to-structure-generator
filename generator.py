# coding: utf-8
import Tkinter as tk
import tkMessageBox
from rdkit import Chem
from rdkit.Chem import Draw
from PIL import Image, ImageTk
from library import SmilesFromName


def generate_image():
    #Retrieving the value of user's input and convert it to SMILES
    origmolName = textbox.get()
    nameToSmiles = SmilesFromName(textbox.get())
    
    # Draw molecule and save the image
    try:
        m = Chem.MolFromSmiles(nameToSmiles)
        fig = Draw.MolToFile(m,'images/' + origmolName + '.png')
    except TypeError:
        raise tkMessageBox.showinfo("Invalid Input", "The molecule that you are searching is not yet available in the library")
  
    
    
    
# Display the result
    result_title = tk.Label(root, text="Result",font=("Helvetica", 16))
    result_title.grid(row=1, sticky="n", pady=45)
    load = Image.open("images/" + origmolName + ".png")
    render = ImageTk.PhotoImage(load)

    img = tk.Label(root, image=render)
    img.image = render
    img.place(x=150,y=170)

    molName = tk.Label(root,text=origmolName)
    molName.grid(pady=15)

    
    

root = tk.Tk()
root.title('Molecule Generator')
root.geometry('{}x{}'.format(600, 520))
root.resizable(False, False)
# Creates the frames
title_frame = tk.Frame(root, width=450, height=50, pady=3)
center = tk.Frame(root, width=450, height=45, pady=3)

# Layout the frame containers
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)

title_frame.grid(row=0, sticky="ew")
center.grid(row=1, sticky="nsew")

# Create the center widgets
center.grid_rowconfigure(0, weight=1)
center.grid_columnconfigure(1, weight=1)

ctr_mid = tk.Frame(center, width=250, height=190, padx=3, pady=3)
ctr_mid.grid(row=0, column=1, sticky="nsew")

# Creates the widget for title frame
title = tk.Label(title_frame, text="CHEMICAL STRUCTURE GENERATOR", font=("Courier", 24))
textbox = tk.Entry(ctr_mid)
button1 = tk.Button(ctr_mid, text="Generate", command=generate_image)

# Layout the widget to the frame
title.grid(row=0, pady=20, padx=20)
textbox.grid(row=1, column=0, ipady=3, ipadx=190, padx=10)
button1.grid(row=1, column=1)




root.mainloop()