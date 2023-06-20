import random
import string
import csv
import tkinter as tk
from tkinter import filedialog, messagebox
from datetime import date
from data.dictionary import dictionary_words

def generate_password(length=10):
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_chars = '!@$*'

    all_chars = lowercase_letters + uppercase_letters + digits + special_chars
    password = ''

    while True:
        password = ''.join(random.sample(all_chars, length))
        if (any(char.islower() for char in password) and
            any(char.isupper() for char in password) and
            any(char.isdigit() for char in password) and
            any(char in special_chars for char in password) and
            not password.lower() in dictionary_words):
            break

    return password

def generate_passwords():
    count = int(entry_count.get())
    today = date.today().strftime("%Y-%m-%d")
    file_path = filedialog.asksaveasfilename(defaultextension=".csv")

    if not file_path:
        return

    passwords = []
    while count > 0:
        password = generate_password()
        passwords.append(password)
        count -= 1

    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Password"])
        writer.writerows([[password] for password in passwords])

    messagebox.showinfo("Success", f"Passwords exported to {file_path}")

# Create GUI window
window = tk.Tk()
window.title("Password Generator")
window.geometry("300x150")

# Label and Entry for password count
label_count = tk.Label(window, text="Number of Passwords:")
label_count.pack()
entry_count = tk.Entry(window)
entry_count.pack()

# Generate Passwords button
btn_generate = tk.Button(window, text="Generate Passwords", command=generate_passwords)
btn_generate.pack()

# Run the GUI event loop
window.mainloop()
