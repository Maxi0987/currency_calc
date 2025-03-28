import tkinter as tk
from tkinter import ttk  # Import ttk for Combobox

# Define currency values and conversion rates (EUR as the base)
values = ["eur", "dollar", "yen", "GBP", "CHF", "MXN", "CNY"]
conversion_rates = {
    "eur": 1,      
    "dollar": 1.18, 
    "yen": 129.53,   
    "GBP": 0.85,
    "CHF": 1.61,
    "MXN": 19.94,
    "CNY": 9.43
}

translations = {
    "num": {"en": "Number", "de": "Wert"},
    "from_currency": {"en": "From Currency:", "de": "Start Währung"},
    "to_currency": {"en": "To Currency:", "de": "Zu  Wärhung"},
    "convert": {"en": "Convert", "de": "umrechnen"},
    "output": {"en": "Converted Number", "de": "umgerechneter Wert"},
    "invalid_input": {"en": "Invalid input. Enter a valid number.", "de": "Nicht gültiger Wert"},
    "select_currencies": {"en": "Please select valid currencies!", "de": "richtige Währungen wechseln"}
}

background = "#4f4f4f"
foreground = "white"
background_btn = "#616060"

class Currency:
    def __init__(self, root):
        self.root = root
        self.root.title("Currency Converter")
        self.root.geometry('350x320')
        self.root.configure(bg='#4f4f4f')

        self.language = "en"  # Default language is English

        self.entry_label = tk.Label(root, text=translations["num"][self.language], bg=background, fg=foreground)
        self.entry_label.pack(pady=5)

        self.entry = tk.Entry(root, bg=background_btn, fg=foreground)
        self.entry.pack(pady=5)

        self.from_currency_label = tk.Label(root, text=translations["from_currency"][self.language], bg=background, fg=foreground)
        self.from_currency_label.pack()

        combostyle = ttk.Style()
        combostyle.theme_create('combostyle', parent='alt',
                         settings = {'TCombobox':
                                     {'configure':
                                      {'selectbackground': background_btn,
                                       'fieldbackground': background_btn,
                                       'background': background_btn,
                                       'foreground' : foreground
                                       }}}
                         )
        combostyle.theme_use('combostyle') 


        self.from_currency_combobox = ttk.Combobox(root, values=values, state="readonly", width=15)
        self.from_currency_combobox.set("eur")  # Default to EUR
        self.from_currency_combobox.pack(pady=5)

        self.to_currency_label = tk.Label(root, text=translations["to_currency"][self.language], bg=background, fg=foreground)
        self.to_currency_label.pack()

        self.to_currency_combobox = ttk.Combobox(root, values=values, state="readonly", width=15)
        self.to_currency_combobox.set("dollar")  # Default to USD
        self.to_currency_combobox.pack(pady=5)

        self.convert_button = tk.Button(root, text=translations["convert"][self.language], command=self.convert_currency, bg=background_btn, fg=foreground)
        self.convert_button.pack(pady=10)

        self.output_label = tk.Label(root, text=translations["output"][self.language], bg=background, fg=foreground)
        self.output_label.pack(pady=10)

        self.language_button = tk.Button(root, text="Change Language", command=self.change_language, bg=background, fg=foreground)
        self.language_button.pack(pady=10)

    def convert_currency(self):
        try:
            num = float(self.entry.get())  # Convert input to float
            from_currency = self.from_currency_combobox.get()
            to_currency = self.to_currency_combobox.get()

            if from_currency not in values or to_currency not in values:
                self.output_label.config(text=translations["select_currencies"][self.language])
                return

            # Convert to EUR first (if not already in EUR), then to target currency
            amount_in_eur = num / conversion_rates[from_currency]
            converted_amount = amount_in_eur * conversion_rates[to_currency]

            self.output_label.config(text=f"{num} {from_currency} = {converted_amount:.2f} {to_currency}")

        except ValueError:
            self.output_label.config(text=translations["invalid_input"][self.language])

    def change_language(self):
        self.language = "de" if self.language == "en" else "en"  # Toggle
        self.update_language()

    def update_language(self):
        self.entry_label.config(text=translations["num"][self.language])
        self.from_currency_label.config(text=translations["from_currency"][self.language])
        self.to_currency_label.config(text=translations["to_currency"][self.language])
        self.convert_button.config(text=translations["convert"][self.language])
        self.output_label.config(text=translations["output"][self.language])
        self.language_button.config(text="Change Language")

if __name__ == "__main__":
    root = tk.Tk()
    Currency(root)
    root.mainloop()
