# Currency Converter Documentation

## Overview

This is a simple **Currency Converter** application built using **Tkinter** in Python. It allows you to convert between different currencies with **EUR** as the base currency.

### Supported Currencies:
- Euro (EUR)
- US Dollar (USD)
- Japanese Yen (JPY)

## Features
- Convert between **EUR**, **USD**, and **JPY**.
- Uses **EUR** as the base currency for conversions.
- Input an amount and select the source and target currencies using checkboxes.
- Displays the converted amount after clicking **Convert**.

## How to Use

1. **Enter Amount**: Type the amount you want to convert in the input field.
2. **Select Source Currency**: Choose the currency you are converting from (EUR, USD, or JPY).
3. **Select Target Currency**: Choose the currency you are converting to (EUR, USD, or JPY).
4. **Click Convert**: Press the **Convert** button to perform the conversion.
5. **View Result**: The converted amount will appear below the button.

## Conversion Rates

The current conversion rates (with EUR as the base):
- 1 EUR = 1.18 USD
- 1 EUR = 129.53 JPY

## Example

If you enter `100` in the amount field and select:
- **From Currency**: EUR
- **To Currency**: USD

It will output: `100 EUR = 118.00 USD`.

## Requirements

- Python 3.x
- Tkinter (typically comes pre-installed with Python)

## Running the Application

1. Clone or download the repository.
2. Run the script with Python:  
   ```bash
   python currency_converter.py
