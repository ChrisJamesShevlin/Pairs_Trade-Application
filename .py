import tkinter as tk
from tkinter import ttk

def calculate_stake():
    try:
        etf1_price = float(etf1_entry.get())
        etf2_price = float(etf2_entry.get())
        etf2_stake = float(min_stake_entry.get())
        
        # Calculate the required stake per point for ETF1 to balance monetary exposure
        etf1_stake = round(etf2_stake * (etf2_price / etf1_price), 2)
        
        # Display the result
        result_label.config(text=f"To balance:\nETF1 stake per point = £{etf1_stake}\nETF2 stake per point = £{etf2_stake}")
    except ValueError:
        result_label.config(text="Please enter valid numeric values.")

# Set up main window
root = tk.Tk()
root.title("Spread Bet Pairs Trade Calculator")
root.geometry("400x300")

# Set dark theme with bright blue text
root.configure(bg='#1e1e1e')
style = ttk.Style()
style.theme_use('clam')
style.configure("TLabel", foreground="#00bfff", background="#1e1e1e")
style.configure("TButton", foreground="#00bfff", background="#3e3e3e")
style.configure("TEntry", foreground="#00bfff", background="#1e1e1e", fieldbackground="#3e3e3e")

# Input labels and entries
etf1_label = ttk.Label(root, text="ETF1 Price per Share:")
etf1_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")
etf1_entry = ttk.Entry(root)
etf1_entry.grid(row=0, column=1, padx=10, pady=10)

etf2_label = ttk.Label(root, text="ETF2 Price per Share:")
etf2_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")
etf2_entry = ttk.Entry(root)
etf2_entry.grid(row=1, column=1, padx=10, pady=10)

min_stake_label = ttk.Label(root, text="Minimum Stake for ETF2 (£):")
min_stake_label.grid(row=2, column=0, padx=10, pady=10, sticky="e")
min_stake_entry = ttk.Entry(root)
min_stake_entry.insert(0, "1")  # Default value of 1
min_stake_entry.grid(row=2, column=1, padx=10, pady=10)

# Calculate button
calculate_button = ttk.Button(root, text="Calculate", command=calculate_stake)
calculate_button.grid(row=3, column=0, columnspan=2, pady=20)

# Result display
result_label = ttk.Label(root, text="", font=("Arial", 12))
result_label.grid(row=4, column=0, columnspan=2)

# Center the window
root.eval('tk::PlaceWindow . center')

# Run the application
root.mainloop()
