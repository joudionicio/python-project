import mysql.connector
import glob  
import pandas as pd
import os
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

conn = mysql.connector.connect(
    host="localhost",
    database="csv_data",
    user="dev",
    password= "Dev2025"
)
cursor = conn.cursor()

# se hace una carpeta vacia para almacenar los archivos y directorios para despues juntarlos en uno 
files_csv = []
directories = []

def merge_CSVs(select_directories, output_file):
    for select_dir in select_directories:
        # se hace un bucle para buscar en todos los directorios ya dados
        file_path = os.path.join(select_dir, "*.csv")
        # se buscan todos los archivos csv en la ruta creada
        for file_csv in glob.glob(file_path):
            # se lee el archivo CSV 
            fc = pd.read_csv(file_csv)
            # se agrega el archivo csv a la lista de archivos csv
            files_csv.append(fc)

    # unir todos en un solo archivo
    if files_csv:  # Verifica si hay archivos para juntar
        one_csv_file = pd.concat(files_csv, ignore_index=True)
        # convertirlo en un csv archivo 
        one_csv_file.to_csv(output_file, index=False)
        messagebox.showinfo("Success", f"Merge files are in: {output_file}")
    else:
        messagebox.showwarning("Warning", "Your directory is empty, there is not CSV files in it.")

def select_output_file():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    output_file = filedialog.asksaveasfilename(defaultextension=".csv", title="Save Merged File", filetypes=[("CSV files", "*.csv"), ("All files", "*.*")])
    return output_file

def select_directories():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    directories = []
    while True:#an infinetely loop where the loop will always work.
        directory = filedialog.askdirectory(mustexist=True)
        if directory:
            directories.append(directory)
        else:
            break  # Sale del ciclo si no desea mas directorios
    return directories

def main():
    directories = select_directories()
    if directories:
        output_file = select_output_file()
        if output_file:
            merge_CSVs(directories, output_file)
            print("CSV files merged successfully!")
        else:
            print("No output file selected.")
    else:
        print("No directories selected.")

main()
