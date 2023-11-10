import string
import random
import tkinter as tk
from tkinter import messagebox

def generate_password():
    if not plen_entry.get(): 
        messagebox.showerror("Error", "Please enter a password length.")
        return

    s1 = string.ascii_lowercase
    s2 = string.ascii_uppercase
    s3 = string.digits
    s4 = string.punctuation
    plen = int(plen_entry.get()) 
    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))

    password = "".join(random.sample(s, plen))
    
    password_label.config(text=f"Your Password: {password}")

def close_window():
    window.destroy()

window = tk.Tk()
window.title("Password Generator")
window.geometry("500x350") 
window.configure(bg='#3498db')  

plen_label = tk.Label(window, text="Enter password length:", font=('Helvetica', 14), bg='#3498db', fg='white')
plen_label.grid(row=0, column=0, padx=10, pady=(50, 10))

plen_entry = tk.Entry(window, font=('Helvetica', 14), relief=tk.FLAT, bd=2)
plen_entry.grid(row=0, column=1, padx=10, pady=(50, 10))

button_frame = tk.Frame(window, bg='#3498db')
button_frame.grid(row=1, column=0, columnspan=2, pady=20, sticky='n')

generate_button = tk.Button(button_frame, text="Generate Password", command=generate_password, font=('Helvetica', 12, 'bold'), bg='#2ecc71', fg='white', relief=tk.GROOVE)
generate_button.grid(row=0, column=0, padx=10)

ok_button = tk.Button(button_frame, text="OK", command=close_window, font=('Helvetica', 12, 'bold'), bg='#e74c3c', fg='white', relief=tk.GROOVE)
ok_button.grid(row=0, column=1, padx=10)

password_label = tk.Label(window, text="", font=('Helvetica', 16, 'bold'), bg='#3498db', fg='white')
password_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

window.mainloop()
