from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Create an empty list to store orders
orders = []

@app.route('/Restaurant.html')
def order_form():
    return render_template('Restaurant.html')

@app.route('/submit_order', methods=['POST'])
def submit_order():
    name = request.form['name']
    order = request.form['order']

    # Store the order in the list
    orders.append({'name': name, 'order': order})

    return redirect(url_for('order_form'))

@app.route('/Menu_customers.html')
def view_orders():
    return render_template('Menu_customers.html')

if __name__ == '__main__':
    app.run(debug=True)