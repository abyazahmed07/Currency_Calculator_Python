# Currency_Calculator_Python
Simple Currency Converter with a GUI 


Currency Converter Application

This Python application provides a simple graphical user interface (GUI) for converting amounts between various currencies using predefined exchange rates. The GUI is built with the tkinter library, and the exchange rates are relative to the US Dollar (USD).

Features

	•	Convert amounts between the following currencies:
	•	US Dollar (USD)
	•	Euro (EUR)
	•	British Pound (GBP)
	•	Indian Rupee (INR)
	•	Japanese Yen (JPY)
	•	Australian Dollar (AUD)
	•	Canadian Dollar (CAD)
	•	Swiss Franc (CHF)
	•	Chinese Yuan (CNY)
	•	New Zealand Dollar (NZD)
	•	User-friendly interface with dropdown menus for currency selection.
	•	Error handling for invalid inputs and unsupported currencies.

Prerequisites

	•	Python 3.x installed on your system.

How to Run

	1.	Clone the Repository:

git clone https://github.com/yourusername/currency-converter.git


	2.	Navigate to the Project Directory:

cd currency-converter


	3.	Run the Application:

python currency_converter.py

Ensure that you have Python 3.x installed and properly configured in your system’s PATH.

Usage

	1.	Enter the amount you wish to convert in the “Amount” field.
	2.	Select the source currency from the “From Currency” dropdown menu.
	3.	Select the target currency from the “To Currency” dropdown menu.
	4.	Click the “Convert” button to perform the conversion.
	5.	The converted amount will be displayed below the button.

Exchange Rates

The application uses the following predefined exchange rates relative to USD:

Currency	Exchange Rate
USD	1.00
EUR	0.85
GBP	0.75
INR	74.00
JPY	110.00
AUD	1.35
CAD	1.25
CHF	0.92
CNY	6.45
NZD	1.40

Note: These rates are hardcoded and may not reflect current market values.

Error Handling

	•	If the “Amount” field is empty or contains non-numeric characters, an error message will prompt you to enter a valid amount.
	•	If either the “From Currency” or “To Currency” is not selected, an error message will prompt you to select both currencies.
	•	If an unsupported currency is selected, an error message will indicate that the currency is not supported.

License

This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgments

This application was developed using Python’s tkinter library for the GUI components.

Feel free to contribute to this project by submitting issues or pull requests.
