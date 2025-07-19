import string
import tkinter as tk
from tkinter import messagebox

def analyze_password(password):
    score = 0
    feedback = []

    length = len(password)
    if length >= 8:
        score += 20
    else:
        feedback.append("Password should be at least 8 characters long.")

    if any(c.islower() for c in password):
        score += 20
    else:
        feedback.append("Add lowercase letters.")

    if any(c.isupper() for c in password):
        score += 20
    else:
        feedback.append("Add uppercase letters.")

    if any(c.isdigit() for c in password):
        score += 20
    else:
        feedback.append("Add digits.")

    if any(c in string.punctuation for c in password):
        score += 20
    else:
        feedback.append("Add special characters (e.g. @, #, $).")

    return score, feedback

def on_check():
    pwd = entry.get()
    if not pwd:
        messagebox.showwarning("Warning", "Please enter a password.")
        return

    score, feedback = analyze_password(pwd)

    if score < 50:
        status = "Weak"
        color = "red"
    elif score < 80:
        status = "Moderate"
        color = "orange"
    else:
        status = "Strong"
        color = "green"

    result_label.config(text=f"Strength: {status} ({score}%)", fg=color)
    feedback_text.delete(1.0, tk.END)
    if feedback:
        feedback_text.insert(tk.END, "\n".join(feedback))
    else:
        feedback_text.insert(tk.END, "Your password is strong!")

# GUI Design
root = tk.Tk()
root.title("Password Analyzer Tool")

tk.Label(root, text="Enter your password:").pack(pady=5)
entry = tk.Entry(root, width=40, show='*')
entry.pack(pady=5)

tk.Button(root, text="Analyze", command=on_check).pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack(pady=5)

feedback_text = tk.Text(root, height=5, width=50)
feedback_text.pack(pady=10)

root.mainloop()
