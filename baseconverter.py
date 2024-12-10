# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 18:38:21 2024

@author: chaud
"""

import tkinter as tk
from tkinter import messagebox

def decimal_to_binary(decimal):
    return bin(decimal).replace('0b', '')

def decimal_to_octal(decimal):
    return oct(decimal).replace('0o', '')

def decimal_to_hexadecimal(decimal):
    return hex(decimal).replace('0x', '').upper()

def binary_to_decimal(binary):
    return int(binary, 2)

def binary_to_octal(binary):
    decimal = int(binary, 2)
    return oct(decimal).replace('0o', '')

def binary_to_hexadecimal(binary):
    decimal = int(binary, 2)
    return hex(decimal).replace('0x', '').upper()

def octal_to_decimal(octal):
    return int(octal, 8)

def octal_to_binary(octal):
    decimal = int(octal, 8)
    return bin(decimal).replace('0b', '')

def octal_to_hexadecimal(octal):
    decimal = int(octal, 8)
    return hex(decimal).replace('0x', '').upper()

def hexadecimal_to_decimal(hexadecimal):
    return int(hexadecimal, 16)

def hexadecimal_to_binary(hexadecimal):
    decimal = int(hexadecimal, 16)
    return bin(decimal).replace('0b', '')

def hexadecimal_to_octal(hexadecimal):
    decimal = int(hexadecimal, 16)
    return oct(decimal).replace('0o', '')

def convert():
    number = entry_number.get()
    base = entry_base.get()
    
    try:
        if base == '2':
            decimal = binary_to_decimal(number)
            results.set(f"Decimal: {decimal}\nOctal: {binary_to_octal(number)}\nHexadecimal: {binary_to_hexadecimal(number)}")
        elif base == '8':
            decimal = octal_to_decimal(number)
            results.set(f"Decimal: {decimal}\nBinary: {octal_to_binary(number)}\nHexadecimal: {octal_to_hexadecimal(number)}")
        elif base == '10':
            decimal = int(number)
            results.set(f"Binary: {decimal_to_binary(decimal)}\nOctal: {decimal_to_octal(decimal)}\nHexadecimal: {decimal_to_hexadecimal(decimal)}")
        elif base == '16':
            decimal = hexadecimal_to_decimal(number)
            results.set(f"Decimal: {decimal}\nBinary: {hexadecimal_to_binary(number)}\nOctal: {hexadecimal_to_octal(number)}")
        else:
            messagebox.showerror("Invalid Base", "Please enter a valid base: 2, 8, 10, or 16.")
    except ValueError:
        messagebox.showerror("Conversion Error", "Invalid number for the given base.")

# Create GUI
root = tk.Tk()
root.title("Base Converter")

# Input fields
tk.Label(root, text="Enter the number:").grid(row=0, column=0, padx=10, pady=10)
entry_number = tk.Entry(root)
entry_number.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Enter the base (2, 8, 10, 16):").grid(row=1, column=0, padx=10, pady=10)
entry_base = tk.Entry(root)
entry_base.grid(row=1, column=1, padx=10, pady=10)

# Convert button
btn_convert = tk.Button(root, text="Convert", command=convert)
btn_convert.grid(row=2, column=0, columnspan=2, pady=20)

# Results display
results = tk.StringVar()
tk.Label(root, textvariable=results, justify="left").grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Run the application
root.mainloop()
