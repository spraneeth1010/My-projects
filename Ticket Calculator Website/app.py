from flask import Flask, render_template, request

app = Flask(__name__)

# Define ticket prices
TICKET_PRICES = {
    'adult': 150,
    'child': 100,
    'senior': 120
}

@app.route('/', methods=['GET', 'POST'])
def index():
    total = None
    if request.method == 'POST':
        category = request.form['category']
        quantity = int(request.form['quantity'])
        price_per_ticket = TICKET_PRICES.get(category, 0)
        total = price_per_ticket * quantity
    return render_template('index.html', total=total)

if __name__ == '__main__':
    app.run(debug=True)
