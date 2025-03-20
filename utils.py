# utils.py (complete updated version)

# Color mappings (existing)
digit_colors_list = ['Black', 'Brown', 'Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Violet', 'Grey', 'White']
multiplier_colors_list = digit_colors_list + ['Gold', 'Silver']
tolerance_colors_list = ['Brown', 'Red', 'Green', 'Blue', 'Violet', 'Gold', 'Silver']
cap_multiplier_colors_list = ['Black', 'Brown', 'Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Violet', 'Grey', 'White']
ind_multiplier_colors_list = digit_colors_list + ['Gold', 'Silver']

digit_colors = {color: i for i, color in enumerate(digit_colors_list)}
multiplier_colors = {'Black': 1, 'Brown': 10, 'Red': 100, 'Orange': 1000, 'Yellow': 10000, 
                    'Green': 100000, 'Blue': 1000000, 'Violet': 10000000, 'Grey': 100000000, 
                    'White': 1000000000, 'Gold': 0.1, 'Silver': 0.01}
tolerance_colors = {'Brown': 1, 'Red': 2, 'Green': 0.5, 'Blue': 0.25, 'Violet': 0.1, 
                    'Gold': 5, 'Silver': 10}
cap_multiplier_colors = {'Black': 1, 'Brown': 10, 'Red': 100, 'Orange': 1000, 'Yellow': 10000, 
                         'Green': 100000, 'Blue': 1000000, 'Violet': 0.1, 'Grey': 0.01, 'White': 1}
ind_multiplier_colors = {'Black': 1, 'Brown': 10, 'Red': 100, 'Orange': 1000, 'Yellow': 10000, 
                         'Green': 100000, 'Blue': 1000000, 'Gold': 0.1, 'Silver': 0.01}

# Capacitor-specific mappings (existing)
cap_tolerance_colors = {
    'Black': 20, 'Brown': 1, 'Red': 2, 'Orange': 3, 'Green': 5, 
    'Blue': 10, 'Violet': 0.5, 'Grey': 0.25, 'White': 10, 'Gold': 5, 'Silver': 10
}
cap_voltage_colors = {
    'Black': 100, 'Brown': 200, 'Red': 300, 'Orange': 400, 'Yellow': 500, 
    'Green': 600, 'Blue': 700, 'Violet': 800, 'Grey': 900, 'White': 1000
}
cap_multiplier_colors_list = ['Black', 'Brown', 'Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Violet', 'Grey']
cap_tolerance_colors_list = ['Black', 'Brown', 'Red', 'Orange', 'Green', 'Blue', 'Violet', 'Grey', 'White', 'Gold', 'Silver']
cap_voltage_colors_list = ['Black', 'Brown', 'Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Violet', 'Grey', 'White']

# Inductor-specific mappings (existing)
ind_tolerance_colors = {
    'Black': 20, 'Brown': 1, 'Red': 2, 'Orange': 3, 'Yellow': 4, 'Gold': 5, 'Silver': 10
}
ind_tolerance_colors_list = ['Black', 'Brown', 'Red', 'Orange', 'Yellow', 'Gold', 'Silver']

# Diode-specific mappings (new)
diode_colors_list = ['Black', 'Brown', 'Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Violet', 'Grey', 'White']
diode_digit_colors = {color: i for i, color in enumerate(diode_colors_list)}
diode_suffix_colors = {
    'Brown': 'A', 'Red': 'B', 'Orange': 'C', 'Yellow': 'D', 'Green': 'E',
    'Blue': 'F', 'Violet': 'G', 'Grey': 'H', 'White': 'J'
}

# Helper function for color display (existing)
def get_color_hex(color):
    color_map = {
        'black': '#000000', 'brown': '#8B4513', 'red': '#FF0000', 'orange': '#FFA500',
        'yellow': '#FFFF00', 'green': '#008000', 'blue': '#0000FF', 'violet': '#EE82EE',
        'grey': '#808080', 'white': '#FFFFFF', 'gold': '#FFD700', 'silver': '#C0C0C0'
    }
    return color_map.get(color.lower(), '#000000')  # Default to black if unknown

# Formatting functions (existing)
def format_resistance(value):
    if value >= 1e6:
        return f"{value / 1e6:.2f} MΩ"
    elif value >= 1e3:
        return f"{value / 1e3:.2f} kΩ"
    else:
        return f"{value:.2f} Ω"

def format_capacitance(value):
    if value >= 1e6:
        return f"{value / 1e6:.2f} µF"
    elif value >= 1e3:
        return f"{value / 1e3:.2f} nF"
    else:
        return f"{value:.2f} pF"

def format_inductance(value):
    if value >= 1e6:
        return f"{value / 1e6:.2f} H"
    elif value >= 1e3:
        return f"{value / 1e3:.2f} mH"
    else:
        return f"{value:.2f} µH"