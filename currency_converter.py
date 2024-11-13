import tkinter as tk
from tkinter import ttk, messagebox

# Predefined exchange rates relative to USD
exchange_rates = {
    'USD': 1.0,
    'EUR': 0.85,
    'GBP': 0.75,
    'INR': 74.0,
    'JPY': 110.0,
    'AUD': 1.35,
    'CAD': 1.25,
    'CHF': 0.92,
    'CNY': 6.45,
    'NZD': 1.4
}

def convert_currency():
    try:
        amount = float(amount_entry.get())
        from_currency = from_currency_combo.get()
        to_currency = to_currency_combo.get()

        if from_currency == "" or to_currency == "":
            messagebox.showerror("Input Error", "Please select both currencies.")
            return

        # Convert amount to USD
        amount_in_usd = amount / exchange_rates[from_currency]
        # Convert USD to target currency
        converted_amount = amount_in_usd * exchange_rates[to_currency]

        result_label.config(text=f"Converted Amount: {converted_amount:.2f} {to_currency}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid amount.")
    except KeyError:
        messagebox.showerror("Conversion Error", "Currency not supported.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Create the main window
root = tk.Tk()
root.title("Currency Converter")
root.geometry("400x300")
root.resizable(False, False)

# Create and place the widgets
amount_label = tk.Label(root, text="Amount:")
amount_label.pack(pady=5)
amount_entry = tk.Entry(root)
amount_entry.pack(pady=5)

from_currency_label = tk.Label(root, text="From Currency:")
from_currency_label.pack(pady=5)
from_currency_combo = ttk.Combobox(root, values=list(exchange_rates.keys()), state='readonly')
from_currency_combo.pack(pady=5)

to_currency_label = tk.Label(root, text="To Currency:")
to_currency_label.pack(pady=5)
to_currency_combo = ttk.Combobox(root, values=list(exchange_rates.keys()), state='readonly')
to_currency_combo.pack(pady=5)

convert_button = tk.Button(root, text="Convert", command=convert_currency)
convert_button.pack(pady=20)

result_label = tk.Label(root, text="")
result_label.pack(pady=5)

# Start the GUI event loop
root.mainloop()