import tkinter as tk
from tkinter import ttk
from utils import (digit_colors, ind_multiplier_colors, ind_tolerance_colors, 
                  digit_colors_list, ind_multiplier_colors_list, ind_tolerance_colors_list, 
                  format_inductance, get_color_hex)

class InductorTab:
    def __init__(self, notebook, result_text):
        self.result_text = result_text
        self.frame = ttk.Frame(notebook)
        notebook.add(self.frame, text="Inductor")

        self.type_var = tk.StringVar(value="Color Band")
        ttk.Radiobutton(self.frame, text="Color Band", variable=self.type_var, value="Color Band", command=self.update_ui).grid(row=0, column=0, padx=5, pady=5)
        ttk.Radiobutton(self.frame, text="SMD", variable=self.type_var, value="SMD", command=self.update_ui).grid(row=0, column=1, padx=5, pady=5)

        # Color Band Frame
        self.band_frame = ttk.Frame(self.frame)
        self.band_var = tk.StringVar(value="4")
        ttk.Radiobutton(self.band_frame, text="4-Band", variable=self.band_var, value="4", command=self.update_ui).grid(row=0, column=0, padx=5, pady=5)
        ttk.Radiobutton(self.band_frame, text="5-Band (Mil-Spec)", variable=self.band_var, value="5", command=self.update_ui).grid(row=0, column=1, padx=5, pady=5)

        self.band1_label = ttk.Label(self.band_frame, text="Mil-Spec")
        self.band1_label.grid(row=1, column=0, padx=5, pady=5)
        self.band1_combo = ttk.Combobox(self.band_frame, values=['Silver'], state="disabled")
        self.band1_combo.grid(row=1, column=1, padx=5, pady=5)
        self.band1_combo.set("Silver")
        self.band1_color = ttk.Label(self.band_frame, width=2)
        self.band1_color.grid(row=1, column=2, padx=5)
        self.add_tooltip(self.band1_label, "Military Specification (5-band only)")

        self.band2_label = ttk.Label(self.band_frame, text="First Digit")
        self.band2_label.grid(row=2, column=0, padx=5, pady=5)
        self.band2_combo = ttk.Combobox(self.band_frame, values=digit_colors_list, state="readonly")
        self.band2_combo.grid(row=2, column=1, padx=5, pady=5)
        self.band2_combo.set("Black")
        self.band2_color = ttk.Label(self.band_frame, width=2)
        self.band2_color.grid(row=2, column=2, padx=5)
        self.band2_combo.bind("<<ComboboxSelected>>", lambda e: self.update_color(self.band2_combo, self.band2_color))
        self.add_tooltip(self.band2_label, "First significant digit of inductance")

        self.band3_label = ttk.Label(self.band_frame, text="Second Digit")
        self.band3_label.grid(row=3, column=0, padx=5, pady=5)
        self.band3_combo = ttk.Combobox(self.band_frame, values=digit_colors_list, state="readonly")
        self.band3_combo.grid(row=3, column=1, padx=5, pady=5)
        self.band3_combo.set("Black")
        self.band3_color = ttk.Label(self.band_frame, width=2)
        self.band3_color.grid(row=3, column=2, padx=5)
        self.band3_combo.bind("<<ComboboxSelected>>", lambda e: self.update_color(self.band3_combo, self.band3_color))
        self.add_tooltip(self.band3_label, "Second significant digit of inductance")

        self.band4_label = ttk.Label(self.band_frame, text="Multiplier")
        self.band4_label.grid(row=4, column=0, padx=5, pady=5)
        self.band4_combo = ttk.Combobox(self.band_frame, values=ind_multiplier_colors_list, state="readonly")
        self.band4_combo.grid(row=4, column=1, padx=5, pady=5)
        self.band4_combo.set("Black")
        self.band4_color = ttk.Label(self.band_frame, width=2)
        self.band4_color.grid(row=4, column=2, padx=5)
        self.band4_combo.bind("<<ComboboxSelected>>", lambda e: self.update_color(self.band4_combo, self.band4_color))
        self.add_tooltip(self.band4_label, "Multiplier: µH scale factor")

        self.band5_label = ttk.Label(self.band_frame, text="Tolerance")
        self.band5_combo = ttk.Combobox(self.band_frame, values=ind_tolerance_colors_list, state="readonly")
        self.band5_combo.grid(row=5, column=1, padx=5, pady=5)
        self.band5_combo.set("Gold")
        self.band5_color = ttk.Label(self.band_frame, width=2)
        self.band5_combo.bind("<<ComboboxSelected>>", lambda e: self.update_color(self.band5_combo, self.band5_color))
        self.add_tooltip(self.band5_label, "Tolerance: ±% variation")

        # SMD
        self.smd_label = ttk.Label(self.frame, text="Enter SMD Code (e.g., 2R2, 101):")
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
                digit1 = digit_colors[self.band2_combo.get()]
                digit2 = digit_colors[self.band3_combo.get()]
                multiplier = ind_multiplier_colors[self.band4_combo.get()]
                tolerance = ind_tolerance_colors[self.band5_combo.get()]
                inductance = (digit1 * 10 + digit2) * multiplier
                if band_count == "4":
                    self.result_text.set(f"Inductance: {format_inductance(inductance)} ± {tolerance}%")
                elif band_count == "5":
                    self.result_text.set(f"Inductance: {format_inductance(inductance)} ± {tolerance}% (Mil-Spec)")
            elif type_mode == "SMD":
                code = self.smd_entry.get().strip()
                if not (('R' in code and code.replace('R', '').replace('.', '').isdigit()) or 
                        (len(code) == 3 and code.isdigit())):
                    self.result_text.set("Error: Invalid SMD code (e.g., 101, 2R2)")
                    return
                if 'R' in code:
                    inductance = float(code.replace('R', '.'))  # e.g., 2R2 = 2.2 µH
                elif len(code) == 3:
                    inductance = (int(code[:2]) * (10 ** int(code[2]))) / 1000  # e.g., 101 = 100 nH = 0.1 µH
                self.result_text.set(f"Inductance: {format_inductance(inductance)}")
        except KeyError as e:
            self.result_text.set(f"Error: Invalid color '{e.args[0]}'")
        except ValueError:
            self.result_text.set("Error: Invalid input format")

    def reverse_lookup(self):
        if self.type_var.get() != "SMD":
            self.result_text.set("Error: Reverse lookup only available in SMD mode")
            return
        try:
            target = float(self.smd_entry.get())
            if target <= 0:
                self.result_text.set("Error: Enter a positive inductance value")
                return
            for d1 in range(10):
                for d2 in range(10):
                    for mult_color, mult in ind_multiplier_colors.items():
                        value = (d1 * 10 + d2) * mult
                        if abs(value - target) / target < 0.01:  # 1% tolerance
                            self.result_text.set(f"Possible 4-Band: {digit_colors_list[d1]}-{digit_colors_list[d2]}-{mult_color}-Gold")
                            return
            self.result_text.set("No exact match found within 1%")
        except ValueError:
            self.result_text.set("Error: Enter a valid inductance value (e.g., 5600)")

    def update_ui(self):
        type_mode = self.type_var.get()
        band_count = self.band_var.get()
        if type_mode == "Color Band":
            self.smd_label.grid_remove()
            self.smd_entry.grid_remove()
            self.band_frame.grid(row=1, column=0, columnspan=2, pady=5)
            if band_count == "4":
                self.band1_label.grid_remove()
                self.band1_combo.grid_remove()
                self.band1_color.grid_remove()
                self.band2_label.config(text="First Digit")
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
            elif band_count == "5":
                self.band1_label.grid(row=1, column=0, padx=5, pady=5)
                self.band1_combo.grid(row=1, column=1, padx=5, pady=5)
                self.band1_color.grid(row=1, column=2, padx=5)
                self.band2_label.config(text="First Digit")
                self.band2_label.grid(row=2, column=0, padx=5, pady=5)
                self.band2_combo.grid(row=2, column=1, padx=5, pady=5)
                self.band2_color.grid(row=2, column=2, padx=5)
                self.band3_label.grid(row=3, column=0, padx=5, pady=5)
                self.band3_combo.grid(row=3, column=1, padx=5, pady=5)
                self.band3_color.grid(row=3, column=2, padx=5)
                self.band4_label.grid(row=4, column=0, padx=5, pady=5)
                self.band4_combo.grid(row=4, column=1, padx=5, pady=5)
                self.band4_color.grid(row=4, column=2, padx=5)
                self.band5_label.grid(row=5, column=0, padx=5, pady=5)
                self.band5_combo.grid(row=5, column=1, padx=5, pady=5)
                self.band5_color.grid(row=5, column=2, padx=5)
        elif type_mode == "SMD":
            self.band_frame.grid_remove()
            self.smd_label.grid(row=1, column=0, padx=5, pady=5)
            self.smd_entry.grid(row=1, column=1, padx=5, pady=5)
        self.update_all_colors()