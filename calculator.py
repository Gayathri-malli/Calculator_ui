import tkinter as tk
from tkinter import messagebox

# Function to perform operations
def calculate(operation):
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        if operation == "Add":
            result.set(num1 + num2)
        elif operation == "Subtract":
            result.set(num1 - num2)
        elif operation == "Multiply":
            result.set(num1 * num2)
        elif operation == "Divide":
            if num2 == 0:
                messagebox.showerror("Error", "Division by zero is not allowed")
                return
            result.set(num1 / num2)
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers")

# Create main window
root = tk.Tk()
root.title("Python UI Calculator")
root.geometry("300x250")

# Input fields
tk.Label(root, text="Number 1:").pack(pady=5)
entry_num1 = tk.Entry(root)
entry_num1.pack()

tk.Label(root, text="Number 2:").pack(pady=5)
entry_num2 = tk.Entry(root)
entry_num2.pack()

# Result display
result = tk.StringVar()
tk.Label(root, text="Result:").pack(pady=5)
tk.Label(root, textvariable=result, font=("Arial", 14)).pack()

# Buttons for operations
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

tk.Button(button_frame, text="Add", width=10, command=lambda: calculate("Add")).grid(row=0, column=0, padx=5, pady=5)
tk.Button(button_frame, text="Subtract", width=10, command=lambda: calculate("Subtract")).grid(row=0, column=1, padx=5, pady=5)
tk.Button(button_frame, text="Multiply", width=10, command=lambda: calculate("Multiply")).grid(row=1, column=0, padx=5, pady=5)
tk.Button(button_frame, text="Divide", width=10, command=lambda: calculate("Divide")).grid(row=1, column=1, padx=5, pady=5)

# Run the application
root.mainloop()
