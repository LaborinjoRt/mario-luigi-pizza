from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Create an empty list to store orders
orders = []

@app.route('/')
def order_form():
    return render_template('order.html')

@app.route('/submit_order', methods=['POST'])
def submit_order():
    name = request.form['name']
    order = request.form['order']

    # Store the order in the list
    orders.append({'name': name, 'order': order})

    return redirect(url_for('order_form'))

@app.route('/orders')
def view_orders():
    return render_template('orders.html', orders=orders)

if __name__ == '__main__':
    app.run(debug=True)