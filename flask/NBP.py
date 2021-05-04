from flask import Flask
from flask import request, redirect, render_template
import requests
import json
currency_bid = {}
currency_type = []
app = Flask(__name__)
response = requests.get("http://api.nbp.pl/api/exchangerates/tables/C?format=json")
data = response.json()
NBP = data[0]
rates = NBP["rates"]
current_date = NBP["effectiveDate"]
for currency in rates:
    currency_bid[currency['code']] = currency['bid']
    currency_type.append(currency['code'])


@app.route("/NBP/", methods=["GET", "POST"])
def currency_bid_sell():
    if request.method == "GET":
        return render_template(
            "NBP.html",
            currency_type=currency_type,
            current_date=current_date
        )
    elif request.method == "POST":
        data_currency = request.form
        currency_pick = data_currency.get("currency")
        currency_quantity = data_currency.get("quantity")
        currency_sell = currency_bid[currency_pick] * int(currency_quantity)
        return f"Kwota do zapłaty za zakup {currency_quantity} {currency_pick} wynosi: {currency_sell} zł"


if __name__ == "__main__":
    app.run(debug=True)