import tkinter as tk
from tkinter import ttk
from resistor import ResistorTab
from capacitor import CapacitorTab
from inductor import InductorTab
from diode import DiodeTab  

def main():
    root = tk.Tk()
    root.title("Component Calculator")
    root.geometry("450x650")

    notebook = ttk.Notebook(root)
    notebook.pack(fill=tk.BOTH, expand=1)

    # Shared result display
    result_text = tk.StringVar()
    result_label = ttk.Label(root, textvariable=result_text, font=("Arial", 12))
    result_label.pack(pady=10)

    # Add tabs
    ResistorTab(notebook, result_text)
    CapacitorTab(notebook, result_text)
    InductorTab(notebook, result_text)
    DiodeTab(notebook, result_text) 

    root.mainloop()

if __name__ == "__main__":
    main()