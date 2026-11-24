
import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        operation = operation_var.get()

        if operation == "+":
            result = a + b
        elif operation == "-":
            result = a - b
        elif operation == "×":
            result = a * b
        elif operation == "÷":
            if b == 0:
                messagebox.showerror("Қате", "Нөлге бөлуге болмайды!")
                return
            result = a / b

        result_label.config(text=f"Нәтиже: {result:g}")

    except ValueError:
        messagebox.showerror("Қате", "Сандарды дұрыс енгіз!")

root = tk.Tk()
root.title("Student Calculator")
root.geometry("360x330")

tk.Label(
    root,
    text="STUDENT CALCULATOR",
    font=("Arial", 17, "bold")
).pack(pady=18)

tk.Label(root, text="Бірінші сан:").pack()
entry_a = tk.Entry(root, font=("Arial", 13))
entry_a.pack(pady=5)

operation_var = tk.StringVar(value="+")
tk.OptionMenu(
    root, operation_var, "+", "-", "×", "÷"
).pack(pady=5)

tk.Label(root, text="Екінші сан:").pack()
entry_b = tk.Entry(root, font=("Arial", 13))
entry_b.pack(pady=5)

tk.Button(
    root,
    text="Есептеу",
    command=calculate,
    font=("Arial", 12, "bold")
).pack(pady=15)

result_label = tk.Label(
    root,
    text="Нәтиже:",
    font=("Arial", 14, "bold")
)
result_label.pack()

root.mainloop()
