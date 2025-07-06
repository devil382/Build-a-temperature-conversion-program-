import tkinter as tk
from tkinter import ttk
from tkinter import font

def convert_temperature():
    temp = entry_temp.get()
    if temp:
        try:
            temp = float(temp)
            choice = combo_choice.get()

            if choice == "Celsius to Fahrenheit":
                result = (temp * 9/5) + 32
                label_result.config(text=f"{result:.2f} °F")
            elif choice == "Fahrenheit to Celsius":
                result = (temp - 32) * 5/9
                label_result.config(text=f"{result:.2f} °C")
            elif choice == "Celsius to Kelvin":
                result = temp + 273.15
                label_result.config(text=f"{result:.2f} K")
            elif choice == "Kelvin to Celsius":
                result = temp - 273.15
                label_result.config(text=f"{result:.2f} °C")
        except ValueError:
            label_result.config(text="Invalid Input")


root = tk.Tk()
root.title("Temperature Converter")
root.geometry("1350x1250")
root.resizable(False, False)

label_input = ttk.Label(root, text="Enter Temperature:")
label_input.pack(pady=5)

entry_temp = ttk.Entry(root)
entry_temp.pack(pady=5)

combo_choice = ttk.Combobox(root, 
                            values=[
                                "Celsius to Fahrenheit", 
                                "Fahrenheit to Celsius",
                                "Celsius to Kelvin",
                                "Kelvin to Celsius"
                            ],
                            state="readonly")
combo_choice.current(0)
combo_choice.pack(pady=5)

button_convert = ttk.Button(root, text="Convert", command=convert_temperature)
button_convert.pack(pady=10)

# Set font size to 25
large_font = font.Font(family='Helvetica', size=25, weight='bold')

# Apply font to label_result
label_result = ttk.Label(root, text="", font=large_font)
label_result.pack(pady=5)

root.mainloop()
