import tkinter as tk
from tkinter import messagebox
import re
import nltk
from nltk.corpus import words

# This line is only needed once to download the word list:
# nltk.download('words')

english_words = set(words.words())

def check_password_strength(password):
    strength = 0
    suggestions = []

    if len(password) >= 8:
        strength += 1
    else:
        suggestions.append("Use at least 8 characters.")

    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        suggestions.append("Add at least one uppercase letter.")

    if re.search(r"[a-z]", password):
        strength += 1
    else:
        suggestions.append("Add at least one lowercase letter.")

    if re.search(r"[0-9]", password):
        strength += 1
    else:
        suggestions.append("Include at least one number.")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    else:
        suggestions.append("Include a special character.")

    if password.lower() in english_words:
        suggestions.append("Avoid using common dictionary words.")

    return strength, suggestions

def evaluate():
    pwd = password_entry.get()
    score, suggestions = check_password_strength(pwd)

    if score == 5:
        result_label.config(text="Strong Password ✅", fg="green")
    elif score >= 3:
        result_label.config(text="Moderate Password ⚠️", fg="orange")
    else:
        result_label.config(text="Weak Password ❌", fg="red")

    if suggestions:
        messagebox.showinfo("Suggestions", "\n".join(suggestions))

# GUI Setup
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x300")

label = tk.Label(root, text="Enter your password:", font=("Arial", 12))
label.pack(pady=10)

password_entry = tk.Entry(root, width=30, show="*")
password_entry.pack(pady=5)

check_button = tk.Button(root, text="Check Strength", command=evaluate)
check_button.pack(pady=20)

result_label = tk.Label(root, text="", font=("Arial", 10), fg="blue")
result_label.pack(pady=10)

root.mainloop()
