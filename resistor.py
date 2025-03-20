import tkinter as tk
from tkinter import ttk
from utils import (digit_colors, multiplier_colors, tolerance_colors, digit_colors_list, 
                  multiplier_colors_list, tolerance_colors_list, format_resistance, get_color_hex)

class ResistorTab:
    def __init__(self, notebook, result_text):
        self.result_text = result_text
        self.frame = ttk.Frame(notebook)
        notebook.add(self.frame, text="Resistor")

        self.type_var = tk.StringVar(value="Color Band")
        ttk.Radiobutton(self.frame, text="Color Band", variable=self.type_var, value="Color Band", command=self.update_ui).grid(row=0, column=0, padx=5, pady=5)
        ttk.Radiobutton(self.frame, text="SMD", variable=self.type_var, value="SMD", command=self.update_ui).grid(row=0, column=1, padx=5, pady=5)

        # Color Band Frame
        self.band_frame = ttk.Frame(self.frame)
        self.band_var = tk.StringVar(value="4")
        ttk.Radiobutton(self.band_frame, text="4-Band", variable=self.band_var, value="4", command=self.update_ui).grid(row=0, column=0, padx=5, pady=5)
        ttk.Radiobutton(self.band_frame, text="5-Band", variable=self.band_var, value="5", command=self.update_ui).grid(row=0, column=1, padx=5, pady=5)
        ttk.Radiobutton(self.band_frame, text="6-Band", variable=self.band_var, value="6", command=self.update_ui).grid(row=0, column=2, padx=5, pady=5)

        self.band1_label = ttk.Label(self.band_frame, text="First Digit")
        self.band1_label.grid(row=1, column=0, padx=5, pady=5)
        self.band1_combo = ttk.Combobox(self.band_frame, values=digit_colors_list, state="readonly")
        self.band1_combo.grid(row=1, column=1, padx=5, pady=5)
        self.band1_combo.set("Black")
        self.band1_color = ttk.Label(self.band_frame, width=2)
        self.band1_color.grid(row=1, column=2, padx=5)
        self.band1_combo.bind("<<ComboboxSelected>>", lambda e: self.update_color(self.band1_combo, self.band1_color))
        self.add_tooltip(self.band1_label, "First significant digit of resistance")

        self.band2_label = ttk.Label(self.band_frame, text="Second Digit")
        self.band2_label.grid(row=2, column=0, padx=5, pady=5)
        self.band2_combo = ttk.Combobox(self.band_frame, values=digit_colors_list, state="readonly")
        self.band2_combo.grid(row=2, column=1, padx=5, pady=5)
        self.band2_combo.set("Black")
        self.band2_color = ttk.Label(self.band_frame, width=2)
        self.band2_color.grid(row=2, column=2, padx=5)
        self.band2_combo.bind("<<ComboboxSelected>>", lambda e: self.update_color(self.band2_combo, self.band2_color))
        self.add_tooltip(self.band2_label, "Second significant digit of resistance")

        self.band3_label = ttk.Label(self.band_frame, text="Third Digit")
        self.band3_label.grid(row=3, column=0, padx=5, pady=5)
        self.band3_combo = ttk.Combobox(self.band_frame, values=digit_colors_list, state="readonly")
        self.band3_combo.grid(row=3, column=1, padx=5, pady=5)
        self.band3_combo.set("Black")
        self.band3_color = ttk.Label(self.band_frame, width=2)
        self.band3_color.grid(row=3, column=2, padx=5)
        self.band3_combo.bind("<<ComboboxSelected>>", lambda e: self.update_color(self.band3_combo, self.band3_color))
        self.add_tooltip(self.band3_label, "Third significant digit (5/6-band only)")

        self.band4_label = ttk.Label(self.band_frame, text="Multiplier")
        self.band4_label.grid(row=4, column=0, padx=5, pady=5)
        self.band4_combo = ttk.Combobox(self.band_frame, values=multiplier_colors_list, state="readonly")
        self.band4_combo.grid(row=4, column=1, padx=5, pady=5)
        self.band4_combo.set("Black")
        self.band4_color = ttk.Label(self.band_frame, width=2)
        self.band4_color.grid(row=4, column=2, padx=5)
        self.band4_combo.bind("<<ComboboxSelected>>", lambda e: self.update_color(self.band4_combo, self.band4_color))
        self.add_tooltip(self.band4_label, "Multiplier: 10^n ohms")

        self.band5_label = ttk.Label(self.band_frame, text="Tolerance")
        self.band5_label.grid(row=5, column=0, padx=5, pady=5)
        self.band5_combo = ttk.Combobox(self.band_frame, values=tolerance_colors_list, state="readonly")
        self.band5_combo.grid(row=5, column=1, padx=5, pady=5)
        self.band5_combo.set("Brown")
        self.band5_color = ttk.Label(self.band_frame, width=2)
        self.band5_color.grid(row=5, column=2, padx=5)
        self.band5_combo.bind("<<ComboboxSelected>>", lambda e: self.update_color(self.band5_combo, self.band5_color))
        self.add_tooltip(self.band5_label, "Tolerance: ±% variation")

        self.band6_label = ttk.Label(self.band_frame, text="Temp. Coefficient")
        self.band6_combo = ttk.Combobox(self.band_frame, values=['Brown', 'Red', 'Orange', 'Yellow', 'Blue', 'Violet'], state="readonly")
        self.band6_combo.set("Brown")
        self.band6_color = ttk.Label(self.band_frame, width=2)
        self.band6_combo.bind("<<ComboboxSelected>>", lambda e: self.update_color(self.band6_combo, self.band6_color))
        self.add_tooltip(self.band6_label, "Temperature Coefficient: ppm/°C")

        # SMD
        self.smd_label = ttk.Label(self.frame, text="Enter SMD Code (e.g., 103, 4R7):")
        self.smd_entry = ttk.Entry(self.frame)

        ttk.Button(self.frame, text="Calculate", command=self.calculate).grid(row=2, column=0, pady=10)
        ttk.Button(self.frame, text="Reverse Lookup", command=self.reverse_lookup).grid(row=2, column=1, pady=10)

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
        self.update_color(self.band6_combo, self.band6_color)

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
        type_mode = self.type_var.get()
        band_count = self.band_var.get() if type_mode == "Color Band" else None
        try:
            if type_mode == "Color Band":
                if band_count == "4":
                    digit1 = digit_colors[self.band1_combo.get()]
                    digit2 = digit_colors[self.band2_combo.get()]
                    multiplier = multiplier_colors[self.band4_combo.get()]
                    tolerance = tolerance_colors[self.band5_combo.get()]
                    resistance = (digit1 * 10 + digit2) * multiplier
                    self.result_text.set(f"Resistance: {format_resistance(resistance)} ± {tolerance}%")
                elif band_count == "5":
                    digit1 = digit_colors[self.band1_combo.get()]
                    digit2 = digit_colors[self.band2_combo.get()]
                    digit3 = digit_colors[self.band3_combo.get()]
                    multiplier = multiplier_colors[self.band4_combo.get()]
                    tolerance = tolerance_colors[self.band5_combo.get()]
                    resistance = (digit1 * 100 + digit2 * 10 + digit3) * multiplier
                    self.result_text.set(f"Resistance: {format_resistance(resistance)} ± {tolerance}%")
                elif band_count == "6":
                    digit1 = digit_colors[self.band1_combo.get()]
                    digit2 = digit_colors[self.band2_combo.get()]
                    digit3 = digit_colors[self.band3_combo.get()]
                    multiplier = multiplier_colors[self.band4_combo.get()]
                    tolerance = tolerance_colors[self.band5_combo.get()]
                    temp_coeff = {'Brown': 100, 'Red': 50, 'Orange': 15, 'Yellow': 25, 'Blue': 10, 'Violet': 5}[self.band6_combo.get()]
                    resistance = (digit1 * 100 + digit2 * 10 + digit3) * multiplier
                    self.result_text.set(f"Resistance: {format_resistance(resistance)} ± {tolerance}%, Temp. Coeff: {temp_coeff} ppm/°C")
            elif type_mode == "SMD":
                code = self.smd_entry.get().strip()
                if not (('R' in code and code.replace('R', '').replace('.', '').isdigit()) or 
                        (len(code) in (3, 4) and code.isdigit())):
                    self.result_text.set("Error: Invalid SMD code (e.g., 103, 4R7)")
                    return
                if 'R' in code:
                    resistance = float(code.replace('R', '.'))
                elif len(code) == 3:
                    resistance = int(code[:2]) * (10 ** int(code[2]))
                elif len(code) == 4:
                    resistance = int(code[:3]) * (10 ** int(code[3]))
                self.result_text.set(f"Resistance: {format_resistance(resistance)}")
        except KeyError as e:
            self.result_text.set(f"Error: Invalid color '{e.args[0]}'")
        except ValueError:
            self.result_text.set("Error: Invalid input format")

    def reverse_lookup(self):
        type_mode = self.type_var.get()
        if type_mode != "SMD":
            self.result_text.set("Error: Reverse lookup only available in SMD mode")
            return
        try:
            target = float(self.smd_entry.get())
            if target <= 0:
                self.result_text.set("Error: Enter a positive resistance value")
                return
            for d1 in range(10):
                for d2 in range(10):
                    for mult_color, mult in multiplier_colors.items():
                        value = (d1 * 10 + d2) * mult
                        if abs(value - target) / target < 0.01:  # 1% tolerance
                            self.result_text.set(f"Possible 4-Band: {digit_colors_list[d1]}-{digit_colors_list[d2]}-{mult_color}-Gold")
                            return
            self.result_text.set("No exact match found within 1%")
        except ValueError:
            self.result_text.set("Error: Enter a valid resistance value (e.g., 470)")

    def update_ui(self):
        type_mode = self.type_var.get()
        band_count = self.band_var.get()
        if type_mode == "Color Band":
            self.smd_label.grid_remove()
            self.smd_entry.grid_remove()
            self.band_frame.grid(row=1, column=0, columnspan=2, pady=5)
            if band_count == "4":
                self.band3_label.grid_remove()
                self.band3_combo.grid_remove()
                self.band3_color.grid_remove()
                self.band4_label.config(text="Multiplier")
                self.band5_label.config(text="Tolerance")
                self.band6_label.grid_remove()
                self.band6_combo.grid_remove()
                self.band6_color.grid_remove()
                self.band4_combo['values'] = multiplier_colors_list
                self.band5_combo['values'] = tolerance_colors_list
            elif band_count == "5":
                self.band3_label.grid(row=3, column=0, padx=5, pady=5)
                self.band3_combo.grid(row=3, column=1, padx=5, pady=5)
                self.band3_color.grid(row=3, column=2, padx=5)
                self.band4_label.config(text="Multiplier")
                self.band5_label.config(text="Tolerance")
                self.band6_label.grid_remove()
                self.band6_combo.grid_remove()
                self.band6_color.grid_remove()
                self.band3_combo['values'] = digit_colors_list
                self.band4_combo['values'] = multiplier_colors_list
                self.band5_combo['values'] = tolerance_colors_list
            elif band_count == "6":
                self.band3_label.grid(row=3, column=0, padx=5, pady=5)
                self.band3_combo.grid(row=3, column=1, padx=5, pady=5)
                self.band3_color.grid(row=3, column=2, padx=5)
                self.band4_label.config(text="Multiplier")
                self.band5_label.config(text="Tolerance")
                self.band6_label.grid(row=6, column=0, padx=5, pady=5)
                self.band6_combo.grid(row=6, column=1, padx=5, pady=5)
                self.band6_color.grid(row=6, column=2, padx=5)
                self.band3_combo['values'] = digit_colors_list
                self.band4_combo['values'] = multiplier_colors_list
                self.band5_combo['values'] = tolerance_colors_list
        elif type_mode == "SMD":
            self.band_frame.grid_remove()
            self.smd_label.grid(row=1, column=0, padx=5, pady=5)
            self.smd_entry.grid(row=1, column=1, padx=5, pady=5)
        self.update_all_colors()