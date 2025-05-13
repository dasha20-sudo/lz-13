import tkinter as tk
from tkinter import messagebox
import math

def calculate_triangle(event):
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())

        # Проверка существования треугольника на неравенство треугольника
        if a + b > c and a + c > b and b + c > a:
            M_a= (1 / 2) * math.sqrt(2 * a ** 2 + 2 * b ** 2 - c ** 2)
            p = (a + b + c) / 2
            R = ((a * b * c) / (4 * math.sqrt(p * (p - a) * (p - b) * (p - c))))

            entry_median.delete(0, tk.END)
            entry_median.insert(0, str(M_a))
            entry_radius.delete(0, tk.END)
            entry_radius.insert(0, str(R))
        else:
            messagebox.showerror("Помилка", "Такого трикутника не існує")
    except ValueError:
        messagebox.showerror("Помилка", "Введіть сторони трикутника ")

def highlight_active(event):
    event.widget.configure(bg="yellow")

def remove_highlight(event):
    event.widget.configure(bg="white")

root = tk.Tk()
root.title("Медіана трикутника та радіус описаного кола ")
root.geometry("400x300")
root.configure(bg="lightblue")

label_a = tk.Label(root, text="Сторона a:")
label_a.place(x=20, y=20)
entry_a = tk.Entry(root)
entry_a.place(x=120, y=20)
entry_a.focus()

label_b = tk.Label(root, text="Сторона b:")
label_b.place(x=20, y=50)
entry_b = tk.Entry(root)
entry_b.place(x=120, y=50)

label_c = tk.Label(root, text="Сторона c:")
label_c.place(x=20, y=80)
entry_c = tk.Entry(root)
entry_c.place(x=120, y=80)

entry_a.bind("<FocusIn>", highlight_active)
entry_b.bind("<FocusIn>", highlight_active)
entry_c.bind("<FocusIn>", highlight_active)
entry_a.bind("<FocusOut>", remove_highlight)
entry_b.bind("<FocusOut>", remove_highlight)
entry_c.bind("<FocusOut>", remove_highlight)

button_calculate = tk.Button(root, text="Обчислити", bg="#030ffc")
button_calculate.place(x=120, y=120)
button_calculate.bind("<Button-1>", calculate_triangle)

label_median = tk.Label(root, text="Медіана:")
label_median.place(x=20, y=160)
entry_median = tk.Entry(root)
entry_median.place(x=120, y=160)

label_radius = tk.Label(root, text="Площа:")
label_radius.place(x=20, y=190)
entry_radius = tk.Entry(root)
entry_radius.place(x=120, y=190)

root.mainloop()


