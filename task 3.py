import tkinter as tk
from tkinter import messagebox


def calculate_series(event):
    try:
        x = float(entry_x.get())
        result = 0
        for k in range(1, 10):
            n = x ** (k + 1)
            d = (k + 1) ** x
            result += n / d
        label_result.config(text=f"Сума ряду: {result:.1f}")
    except ValueError:
        messagebox.showerror("Помилка", "Введіть числове значення для x!")

root = tk.Tk()
root.title("Обчислення суми ряду")
root.geometry("400x200")
root.configure(bg="lightblue")


label_image = tk.Label()
label_image.grid(row=0, column=0, columnspan=2)
photo = tk.PhotoImage(file="photo_2025-05-13_14-59-10.gif")
label_image.configure(image=photo)

label_x = tk.Label(root, text="Введіть значення x:")
label_x.grid(row=1, column=0, padx=10, pady=10)

entry_x = tk.Entry(root)
entry_x.grid(row=1, column=1, padx=10, pady=10)
entry_x.focus()

button_calculate = tk.Button(root, text="Обчислити")
button_calculate.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
button_calculate.bind("<Button-1>", calculate_series)

label_result = tk.Label(root, text="Результат:")
label_result.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()


