from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Estos son tus productos de ejemplo
    mis_pasteles = [
        {'nombre': 'Torta de Chocolate', 'precio': '$15.000'},
        {'nombre': 'Red Velvet', 'precio': '$18.000'},
        {'nombre': 'Cheesecake de Fresa', 'precio': '$12.000'}
    ]
    return render_template('index.html', productos=mis_pasteles)

if __name__ == '__main__':
    app.run(debug=True)