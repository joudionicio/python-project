import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image

print("**********************************************************************")
print("           WELCOME TO THE CONVERSION OF IMAGES TO PDF DOCUMENTS")
print("**********************************************************************")

def images_to_pdf(images, pdf_name):
    try: 
        pdf = Image.open(images[0])
        pdf.save(pdf_name, "PDF", resolution=100.0, save_all=True, append_images=images[1:])
        images = select_images()
        messagebox.showinfo("Success", f"Images have been successfully saved as PDF with the name: {pdf_name}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to convert images to PDF. Error: {str(e)}")
    images = select_images()
    if not images:
        messagebox.showerror("Error", "No images selected. Please select images to convert.")
    return

def select_images():
    images= filedialog.askopenfilenames(title="Select Images", filetypes=(("Image Files", "*.jpg;*.jpeg;*.png"),
    ("All files", "*.*")), initialdir="C:/")
    return images

def get_pdf_name():
    pdf_name = filedialog.asksaveasfilename(title="Save PDF As",
        defaultextension=".pdf", initialdir="C:/",
        filetypes=(("PDF Files", "*.pdf"), ("All Files", "*.*")))
    return pdf_name



root = tk.Tk()
root.title("Convert Images to PDF")

select_images_btn = tk.Button(root, text="Select Images", command=select_images)
convert_btn = tk.Button(root, text="Convert", 
    command=lambda: (
        (images := select_images()) and 
        (pdf_name := get_pdf_name()) and 
        (images_to_pdf(images, pdf_name) if images and pdf_name else None)
    ))

select_images_btn.pack()
convert_btn.pack()

print("Starting the Tkinter application...")
root.mainloop()
print("Tkinter application has closed.")