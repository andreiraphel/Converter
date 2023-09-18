import tkinter as tk
root = tk.Tk()
root.title("Converter")

# Labels
celsius_label = tk.Label(root, text="Celsius:")
fahrenheit_label = tk.Label(root, text="Fahrenheit:")

# Entry fields
celsius_entry = tk.Entry(root)
fahrenheit_entry = tk.Entry(root)

# Convert button
convert_button = tk.Button(root, text="Convert")

# Result text widget
result_text = tk.Text(root, height=2, width=30)

root.mainloop()