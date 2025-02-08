import tkinter as tk
from tkinter import messagebox

# Hardcoded credentials for demonstration purposes
USERNAME = "admin"
PASSWORD = "password"

def login():
    """Check the entered credentials."""
    username = entry_username.get()
    password = entry_password.get()
    
    if username == USERNAME and password == PASSWORD:
        messagebox.showinfo("Login Successful", "Welcome to the system!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password.")

# Create the main window
root = tk.Tk()
root.title("Login Panel Simulator")

# Create and place the username and password labels and entries
label_username = tk.Label(root, text="Username:")
label_username.pack(pady=5)
entry_username = tk.Entry(root)
entry_username.pack(pady=5)

label_password = tk.Label(root, text="Password:")
label_password.pack(pady=5)
entry_password = tk.Entry(root, show="*")
entry_password.pack(pady=5)

# Create and place the login button
button_login = tk.Button(root, text="Login", command=login)
button_login.pack(pady=20)

# Run the application
root.mainloop()
