import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image
import os 

print ("**********************************************************************")
print("           WELCOME TO THE CONVERSION OF IMAGES TO PDF DOCUMENTS")
print("**********************************************************************")

def images_to_pdf(images, pdf_name):
    try: 
        pdf = Image.open(images[0])
        pdf.save(pdf_name, "PDF", resolution=100.0,save_all=True, append_images = images [1:])
        messagebox.showinfo("Success", f"Images have been successfully saved as PDF as name of: {pdf_name}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to convert images to PDF. Error: {str(e)}")

def select_images():
    images = filedialog.askopenfilenames(title="Select Images", filetypes=(("Image Files", "*.jpg,*.jpeg,*.png"),
    ("All files", "*.*")), initialdir= "C:/")
    return images

def select_pdf():
    pdf = filedialog.askopenfilename(title="Save PDF As",
        defaultextension=".pdf", initialdir= "C:/",
        filetypes=(("PDF Files", "*.pdf"),("All Files", "*.*")))
    return pdf

root = tk.Tk()
root.title=("Convert Images to PDF")

select_images_btn = tk.Button(root, text="Select Image", command=select_images)
select_pdf_btn = tk.Button(root, text="Select PDF", command=select_pdf)
convert_btn = tk.Button(root, text="Convert", 
    command= lambda: images_to_pdf(select_images(),select_pdf()))
select_images_btn.pack()
select_pdf_btn.pack()
convert_btn.pack()
root.mainloop()
