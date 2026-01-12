# it-tools
import tkinter as tk
from tkinter import messagebox

def add():
      result_label.delete(0,10)
        n1 = int(entry1.get())
        n2 = int(entry2.get())
        addition=n1+n2
        result_label.insert(0,addition)

# Main window
w = tk.Tk()
w.title("Simple Calculator")
w.geometry("300x250")

# Labels & Entries
tk.Label(w, text="Enter Number 1").grid(row=0, column=0, pady=5)
entry1 = tk.Entry(w, bd=4)
entry1.grid(row=0, column=1, pady=5)

tk.Label(w, text="Enter Number 2").grid(row=1, column=0, pady=5)
entry2 = tk.Entry(w, bd=4)
entry2.grid(row=1, column=1, pady=5)

# Result
result_label = tk.Label(w, text="Result:", font=("Arial", 14), fg="blue")
result_label.grid(row=2, column=0, columnspan=2, pady=10)

# Buttons
tk.Button(w, text="ADD", width=10, command=add).grid(row=3, column=0, pady=3)
tk.Button(w, text="SUB", width=10, command=sub).grid(row=3, column=1, pady=3)
tk.Button(w, text="MULTIPLY", width=10, command=mul).grid(row=4, column=0, pady=3)
tk.Button(w, text="DIVIDE", width=10, command=div).grid( )

w.mainloop()
