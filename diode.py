import tkinter as tk
from tkinter import ttk
from utils import (diode_digit_colors, diode_suffix_colors, diode_colors_list, get_color_hex)

class DiodeTab:
    def __init__(self, notebook, result_text):
        self.result_text = result_text
        self.frame = ttk.Frame(notebook)
        notebook.add(self.frame, text="Diode")

        # Band selection
        self.band_var = tk.StringVar(value="4")
        ttk.Radiobutton(self.frame, text="3-Band", variable=self.band_var, value="3", command=self.update_ui).grid(row=0, column=0, padx=5, pady=5)
        ttk.Radiobutton(self.frame, text="4-Band", variable=self.band_var, value="4", command=self.update_ui).grid(row=0, column=1, padx=5, pady=5)
        ttk.Radiobutton(self.frame, text="5-Band", variable=self.band_var, value="5", command=self.update_ui).grid(row=0, column=2, padx=5, pady=5)

        # Color Band Frame
        self.band_frame = ttk.Frame(self.frame)
        self.band_frame.grid(row=1, column=0, columnspan=3, pady=5)

        self.band1_label = ttk.Label(self.band_frame, text="First Digit")
        self.band1_label.grid(row=0, column=0, padx=5, pady=5)
        self.band1_combo = ttk.Combobox(self.band_frame, values=diode_colors_list, state="readonly")
        self.band1_combo.grid(row=0, column=1, padx=5, pady=5)
        self.band1_combo.set("Black")
        self.band1_color = ttk.Label(self.band_frame, width=2)
        self.band1_color.grid(row=0, column=2, padx=5)
        self.band1_combo.bind("<<ComboboxSelected>>", lambda e: self.update_color(self.band1_combo, self.band1_color))
        self.add_tooltip(self.band1_label, "First digit after '1N' in part number")

        self.band2_label = ttk.Label(self.band_frame, text="Second Digit")
        self.band2_label.grid(row=1, column=0, padx=5, pady=5)
        self.band2_combo = ttk.Combobox(self.band_frame, values=diode_colors_list, state="readonly")
        self.band2_combo.grid(row=1, column=1, padx=5, pady=5)
        self.band2_combo.set("Black")
        self.band2_color = ttk.Label(self.band_frame, width=2)
        self.band2_color.grid(row=1, column=2, padx=5)
        self.band2_combo.bind("<<ComboboxSelected>>", lambda e: self.update_color(self.band2_combo, self.band2_color))
        self.add_tooltip(self.band2_label, "Second digit of part number")

        self.band3_label = ttk.Label(self.band_frame, text="Third Digit")
        self.band3_label.grid(row=2, column=0, padx=5, pady=5)
        self.band3_combo = ttk.Combobox(self.band_frame, values=diode_colors_list, state="readonly")
        self.band3_combo.grid(row=2, column=1, padx=5, pady=5)
        self.band3_combo.set("Black")
        self.band3_color = ttk.Label(self.band_frame, width=2)
        self.band3_color.grid(row=2, column=2, padx=5)
        self.band3_combo.bind("<<ComboboxSelected>>", lambda e: self.update_color(self.band3_combo, self.band3_color))
        self.add_tooltip(self.band3_label, "Third digit of part number")

        self.band4_label = ttk.Label(self.band_frame, text="Fourth Digit")
        self.band4_label.grid(row=3, column=0, padx=5, pady=5)
        self.band4_combo = ttk.Combobox(self.band_frame, values=diode_colors_list, state="readonly")
        self.band4_combo.grid(row=3, column=1, padx=5, pady=5)
        self.band4_combo.set("Black")
        self.band4_color = ttk.Label(self.band_frame, width=2)
        self.band4_color.grid(row=3, column=2, padx=5)
        self.band4_combo.bind("<<ComboboxSelected>>", lambda e: self.update_color(self.band4_combo, self.band4_color))
        self.add_tooltip(self.band4_label, "Fourth digit or suffix letter")

        self.band5_label = ttk.Label(self.band_frame, text="Suffix")
        self.band5_label.grid(row=4, column=0, padx=5, pady=5)
        self.band5_combo = ttk.Combobox(self.band_frame, values=list(diode_suffix_colors.keys()), state="readonly")
        self.band5_combo.grid(row=4, column=1, padx=5, pady=5)
        self.band5_combo.set("Brown")
        self.band5_color = ttk.Label(self.band_frame, width=2)
        self.band5_color.grid(row=4, column=2, padx=5)
        self.band5_combo.bind("<<ComboboxSelected>>", lambda e: self.update_color(self.band5_combo, self.band5_color))
        self.add_tooltip(self.band5_label, "Suffix letter (e.g., A-J) if present")

        ttk.Button(self.frame, text="Calculate", command=self.calculate).grid(row=2, column=0, columnspan=3, pady=10)

        self.update_ui()
        self.update_all_colors()

    def update_color(self, combo, color_label):
        color = combo.get()
        color_label.config(background=get_color_hex(color))

    def update_all_colors(self):
        self.update_color(self.band1_combo, self.band1_color)
        self.update_color(self.band2_combo, self.band2_color)
        self.update_color(self.band3_combo, self.band3_color)
        self.update_color(self.band4_combo, self.band4_color)
        self.update_color(self.band5_combo, self.band5_color)

    def add_tooltip(self, widget, text):
        tooltip = tk.Toplevel(widget)
        tooltip.wm_overrideredirect(True)
        tooltip.wm_geometry("+0+0")
        label = tk.Label(tooltip, text=text, background="yellow", relief="solid", borderwidth=1)
        label.pack()
        tooltip.withdraw()
        def show(e): tooltip.wm_geometry(f"+{e.x_root+10}+{e.y_root+10}"); tooltip.deiconify()
        def hide(e): tooltip.withdraw()
        widget.bind("<Enter>", show)
        widget.bind("<Leave>", hide)

    def calculate(self):
        band_count = self.band_var.get()
        try:
            digits = []
            suffix = ""
            if band_count == "3":
                digits = [
                    diode_digit_colors[self.band1_combo.get()],
                    diode_digit_colors[self.band2_combo.get()],
                    diode_digit_colors[self.band3_combo.get()]
                ]
            elif band_count == "4":
                digits = [
                    diode_digit_colors[self.band1_combo.get()],
                    diode_digit_colors[self.band2_combo.get()],
                    diode_digit_colors[self.band3_combo.get()],
                    diode_digit_colors[self.band4_combo.get()]
                ]
            elif band_count == "5":
                digits = [
                    diode_digit_colors[self.band1_combo.get()],
                    diode_digit_colors[self.band2_combo.get()],
                    diode_digit_colors[self.band3_combo.get()],
                    diode_digit_colors[self.band4_combo.get()]
                ]
                suffix = diode_suffix_colors.get(self.band5_combo.get(), "")
            
            part_number = "1N" + "".join(map(str, digits)) + suffix
            self.result_text.set(f"Diode Part Number: {part_number}")
        except KeyError as e:
            self.result_text.set(f"Error: Invalid color '{e.args[0]}'")

    def update_ui(self):
        band_count = self.band_var.get()
        if band_count == "3":
            self.band1_label.grid(row=0, column=0, padx=5, pady=5)
            self.band1_combo.grid(row=0, column=1, padx=5, pady=5)
            self.band1_color.grid(row=0, column=2, padx=5)
            self.band2_label.grid(row=1, column=0, padx=5, pady=5)
            self.band2_combo.grid(row=1, column=1, padx=5, pady=5)
            self.band2_color.grid(row=1, column=2, padx=5)
            self.band3_label.grid(row=2, column=0, padx=5, pady=5)
            self.band3_combo.grid(row=2, column=1, padx=5, pady=5)
            self.band3_color.grid(row=2, column=2, padx=5)
            self.band4_label.grid_remove()
            self.band4_combo.grid_remove()
            self.band4_color.grid_remove()
            self.band5_label.grid_remove()
            self.band5_combo.grid_remove()
            self.band5_color.grid_remove()
        elif band_count == "4":
            self.band1_label.grid(row=0, column=0, padx=5, pady=5)
            self.band1_combo.grid(row=0, column=1, padx=5, pady=5)
            self.band1_color.grid(row=0, column=2, padx=5)
            self.band2_label.grid(row=1, column=0, padx=5, pady=5)
            self.band2_combo.grid(row=1, column=1, padx=5, pady=5)
            self.band2_color.grid(row=1, column=2, padx=5)
            self.band3_label.grid(row=2, column=0, padx=5, pady=5)
            self.band3_combo.grid(row=2, column=1, padx=5, pady=5)
            self.band3_color.grid(row=2, column=2, padx=5)
            self.band4_label.grid(row=3, column=0, padx=5, pady=5)
            self.band4_combo.grid(row=3, column=1, padx=5, pady=5)
            self.band4_color.grid(row=3, column=2, padx=5)
            self.band5_label.grid_remove()
            self.band5_combo.grid_remove()
            self.band5_color.grid_remove()
        elif band_count == "5":
            self.band1_label.grid(row=0, column=0, padx=5, pady=5)
            self.band1_combo.grid(row=0, column=1, padx=5, pady=5)
            self.band1_color.grid(row=0, column=2, padx=5)
            self.band2_label.grid(row=1, column=0, padx=5, pady=5)
            self.band2_combo.grid(row=1, column=1, padx=5, pady=5)
            self.band2_color.grid(row=1, column=2, padx=5)
            self.band3_label.grid(row=2, column=0, padx=5, pady=5)
            self.band3_combo.grid(row=2, column=1, padx=5, pady=5)
            self.band3_color.grid(row=2, column=2, padx=5)
            self.band4_label.grid(row=3, column=0, padx=5, pady=5)
            self.band4_combo.grid(row=3, column=1, padx=5, pady=5)
            self.band4_color.grid(row=3, column=2, padx=5)
            self.band5_label.grid(row=4, column=0, padx=5, pady=5)
            self.band5_combo.grid(row=4, column=1, padx=5, pady=5)
            self.band5_color.grid(row=4, column=2, padx=5)
        self.update_all_colors()