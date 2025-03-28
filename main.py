import tkinter as tk

# Define currency values and conversion rates (EUR as the base)
values = ["eur", "dollar", "yen", "GBP", "CHF", "MXN", "CNY"]
conversion_rates = {
    "eur": 1,       # Base currency (1 EUR)
    "dollar": 1.18, # 1 EUR = 1.18 USD
    "yen": 129.53,   # 1 EUR = 129.53 JPY
    "GBP": 0.85,
    "CHF": 1.61,
    "MXN": 19.94,
    "CNY": 9.43
}

class Currency:
    def __init__(self, root):
        self.root = root
        self.root.title("Currency Converter")
        self.root.geometry('400x600')

        tk.Label(root, text="num").pack(pady=5)
        
        self.entry = tk.Entry(root)
        self.entry.pack(pady=5)

        self.from_currency = tk.StringVar(value="eur")  # Default: EUR
        tk.Label(root, text="From Currency:").pack()
        self.create_checkbuttons(self.from_currency)

        self.to_currency = tk.StringVar(value="dollar")  # Default: USD
        tk.Label(root, text="To Currency:").pack()
        self.create_checkbuttons(self.to_currency)

        tk.Button(root, text="Convert", command=self.convert_currency).pack(pady=10)

        self.output_label = tk.Label(root, text="converted num ")
        self.output_label.pack(pady=10)

    def create_checkbuttons(self, variable):
        frame = tk.Frame(self.root)
        frame.pack()
        for value in values:
            chk = tk.Checkbutton(frame, text=value, variable=variable, onvalue=value, offvalue="")
            chk.pack(anchor="w", padx=10)

    def convert_currency(self):
        try:
            num = float(self.entry.get())  # Convert input to float
            from_currency = self.from_currency.get()
            to_currency = self.to_currency.get()

            if from_currency not in values or to_currency not in values:
                self.output_label.config(text="Please select valid currencies!")
                return

            # Convert to EUR first (if not already in EUR), then to target currency
            amount_in_eur = num / conversion_rates[from_currency]
            converted_amount = amount_in_eur * conversion_rates[to_currency]

            self.output_label.config(text=f"{num} {from_currency} = {converted_amount:.2f} {to_currency}")

        except ValueError:
            self.output_label.config(text="Invalid input. Enter a valid number.")

if __name__ == "__main__":
    root = tk.Tk()
    Currency(root)
    root.mainloop()
