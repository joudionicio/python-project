import tkinter as tk
from tkinter import filedialog, messagebox
import img2pdf

def select_images():
    """Open a window to select image files."""
    return filedialog.askopenfilenames(
        title="Select Images",
        filetypes=(("Image Files", "*.jpg;*.jpeg;*.png"), ("All files", "*.*"))
    )

def images_to_pdf(images, pdf_name):
    """Convert selected images to a PDF file."""
    try:
        # Convert images to PDF and save
        with open(pdf_name, "wb") as file:
            file.write(img2pdf.convert(images))
        messagebox.showinfo("Success", f"Successfully created PDF: {pdf_name}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

def main():
    """Main function to run the image-to-PDF conversion."""
    # Initialize Tkinter root window
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    images = select_images()
    if images:
        pdf_name = filedialog.asksaveasfilename(
            defaultextension=".pdf",
            filetypes=[("PDF files", "*.pdf")]
        )
        if pdf_name:
            images_to_pdf(images, pdf_name)
            


print("**********************************************************************")
print("           WELCOME TO THE CONVERSION OF IMAGES TO PDF DOCUMENTS")
print("**********************************************************************")
main()
