#Password Sterngth Checker 
import tkinter as tk
from tkinter import messagebox
import string

def update_realtime_strength(*args):
    name = name_entry.get().strip().lower()
    dob_raw = dob_entry.get().strip()
    dob_cleaned = dob_raw.replace("-", "").replace("/", "")
    pwd = password_text_var.get()

    if not dob_cleaned.isdigit() or len(dob_cleaned) != 8:
        realtime_strength_label.config(text="Enter valid DOB (DD-MM-YYYY)", fg="orange")
        return

    year = dob_cleaned[-4:]

    if len(pwd) < 6:
        realtime_strength_label.config(text="❌Too short (min 6 chars)", fg="red")
        return
    elif len(pwd) > 15:
        realtime_strength_label.config(text="❌Too long (max 15 chars)", fg="red")
        return
    if name and name in pwd.lower():
        realtime_strength_label.config(text="❌Cannot contain your name", fg="red")
        return
    if dob_cleaned and dob_cleaned in pwd:
        realtime_strength_label.config(text="❌Cannot contain DOB", fg="red")
        return
    if year and year in pwd:
        realtime_strength_label.config(text="❌Cannot contain birth year", fg="red")
        return

    has_lower = any(c.islower() for c in pwd)
    has_upper = any(c.isupper() for c in pwd)
    has_digit = any(c.isdigit() for c in pwd)
    has_special = any(c in string.punctuation for c in pwd)

    missing = []
    if not has_lower: missing.append("lowercase")
    if not has_upper: missing.append("uppercase")
    if not has_digit: missing.append("digit")
    if not has_special: missing.append("special")

    if missing:
        realtime_strength_label.config(text="Missing: " + ", ".join(missing), fg="orange")
    else:
        realtime_strength_label.config(text="✅Strong password!", fg="green")

# --- Final Submission Check ---
def submit_full_validation():
    name = name_entry.get().strip().lower()
    dob_raw = dob_entry.get().strip()
    dob_cleaned = dob_raw.replace("-", "").replace("/", "")
    pwd = password_text_var.get()

    if not dob_cleaned.isdigit() or len(dob_cleaned) != 8:
        messagebox.showwarning("Invalid Input", "Enter DOB in DD-MM-YYYY format.")
        return

    year = dob_cleaned[-4:]

    if len(pwd) < 6 or len(pwd) > 15:
        messagebox.showerror("Invalid", "❌ Password must be 6 to 15 characters.")
        return
    if name in pwd.lower() or dob_cleaned in pwd or year in pwd:
        messagebox.showerror("Invalid", "❌ Password cannot contain name, DOB or birth year.")
        return

    has_lower = any(c.islower() for c in pwd)
    has_upper = any(c.isupper() for c in pwd)
    has_digit = any(c.isdigit() for c in pwd)
    has_special = any(c in string.punctuation for c in pwd)

    if not (has_lower and has_upper and has_digit and has_special):
        messagebox.showerror("Invalid", "❌ Must include upper, lower, digit, and special char.")
    else:
        messagebox.showinfo("Success", "Best Password! All rules satisfied.")

# --- GUI Setup ---
root = tk.Tk()
root.title("🔐 Real-time Password Strength Checker")
root.geometry("480x400")
root.configure(bg="#f4f8fb")
root.resizable(False, False)

password_text_var = tk.StringVar()
password_text_var.trace("w", update_realtime_strength)

frame = tk.Frame(root, bg="#f4f8fb", padx=30, pady=25)
frame.pack(expand=True)

tk.Label(frame, text="Real-time Password Validator", font=("Arial", 17, "bold"), bg="#f4f8fb", fg="#333").grid(row=0, column=0, columnspan=2, pady=(0, 20))

tk.Label(frame, text="Name:", bg="#f4f8fb", font=("Arial", 10)).grid(row=1, column=0, sticky="w", pady=5)
name_entry = tk.Entry(frame, width=35, font=("Arial", 10))
name_entry.grid(row=1, column=1, pady=5)

tk.Label(frame, text="DOB (DD-MM-YYYY):", bg="#f4f8fb", font=("Arial", 10)).grid(row=2, column=0, sticky="w", pady=5)
dob_entry = tk.Entry(frame, width=35, font=("Arial", 10))
dob_entry.grid(row=2, column=1, pady=5)

tk.Label(frame, text="Password:", bg="#f4f8fb", font=("Arial", 10)).grid(row=3, column=0, sticky="w", pady=5)
password_entry = tk.Entry(frame, width=35, font=("Arial", 10), show="*", textvariable=password_text_var)
password_entry.grid(row=3, column=1, pady=5)

realtime_strength_label = tk.Label(frame, text="Start typing your password...", font=("Arial", 9, "italic"), bg="#f4f8fb", fg="gray")
realtime_strength_label.grid(row=4, column=0, columnspan=2, pady=(10, 15))

tk.Button(frame, text="Final Password Check", command=submit_full_validation,
          bg="#007acc", fg="white", font=("Arial", 11, "bold"),
          padx=15, pady=8, relief="raised", cursor="hand2").grid(row=5, column=0, columnspan=2, pady=(10, 0))

root.mainloop()