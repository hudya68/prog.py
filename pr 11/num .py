import tkinter as tk
from tkinter import ttk, messagebox, filedialog

window = tk.Tk()
window.title("Программа с вкладками")

notebook = ttk.Notebook(window)
notebook.pack(fill='both', expand=True)

# Вкладка 1: Калькулятор
calculator_tab = ttk.Frame(notebook)
notebook.add(calculator_tab, text="Калькулятор")

def calculate():
    try:
        number1 = float(num1_entry.get())
        number2 = float(num2_entry.get())
        operation = operation_combobox.get()

        if operation == '+':
            answer = number1 + number2
        elif operation == '-':
            answer = number1 - number2
        elif operation == '*':
            answer = number1 * number2
        elif operation == '/':
            if number2 != 0:
                answer = number1 / number2
            else:
                answer = "На ноль делить нельзя!"
        else:
            answer = "Ошибка операции"

        result_label.config(text=f"Ответ: {answer}")
    except ValueError:
        result_label.config(text="Ошибка: нужно ввести числа!")

num1_entry = tk.Entry(calculator_tab)
num1_entry.grid(row=0, column=0, padx=5, pady=10)

operation_combobox = ttk.Combobox(calculator_tab, values=["+", "-", "*", "/"], width=5)
operation_combobox.current(0)
operation_combobox.grid(row=0, column=1, padx=5, pady=10)

num2_entry = tk.Entry(calculator_tab)
num2_entry.grid(row=0, column=2, padx=5, pady=10)

calc_button = tk.Button(calculator_tab, text="=", command=calculate)
calc_button.grid(row=0, column=3, padx=5, pady=10)

result_label = tk.Label(calculator_tab, text="Ответ: ")
result_label.grid(row=1, column=0, columnspan=4, pady=10)

# Вкладка 2: Выбор
checkbox_tab = ttk.Frame(notebook)
notebook.add(checkbox_tab, text="Выбор")

def show_choice():
    selected_items = []
    if var_check1.get():
        selected_items.append("Пункт 1")
    if var_check2.get():
        selected_items.append("Пункт 2")
    if var_check3.get():
        selected_items.append("Пункт 3")

    if selected_items:
        message = f"Вы выбрали: {', '.join(selected_items)}"
    else:
        message = "Вы ничего не выбрали"
    messagebox.showinfo("Ваш выбор", message)

var_check1 = tk.BooleanVar()
var_check2 = tk.BooleanVar()
var_check3 = tk.BooleanVar()

check1 = tk.Checkbutton(checkbox_tab, text="Пункт 1", variable=var_check1)
check2 = tk.Checkbutton(checkbox_tab, text="Пункт 2", variable=var_check2)
check3 = tk.Checkbutton(checkbox_tab, text="Пункт 3", variable=var_check3)

check1.pack(anchor='w', padx=20, pady=5)
check2.pack(anchor='w', padx=20, pady=5)
check3.pack(anchor='w', padx=20, pady=5)

show_button = tk.Button(checkbox_tab, text="Показать мой выбор", command=show_choice)
show_button.pack(pady=15)

# Вкладка 3: Текст
text_tab = ttk.Frame(notebook)
notebook.add(text_tab, text="Текст")

def load_text_file():
    file_path = filedialog.askopenfilename(filetypes=[("Текстовые файлы", "*.txt")])
    if file_path:
        with open(file_path, 'r', encoding='utf-8') as file:
            file_content = file.read()
            text_area.delete("1.0", tk.END)
            text_area.insert(tk.END, file_content)

load_button = tk.Button(text_tab, text="Загрузить файл (.txt)", command=load_text_file)
load_button.pack(pady=5)

text_area = tk.Text(text_tab, wrap='word')
text_area.pack(expand=True, fill='both', padx=5, pady=5)

window.mainloop()