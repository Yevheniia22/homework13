from flask import Flask, render_template
app = Flask(__name__)
menus = [
    {"pizza": "margarita", "price": 100},
    {"pizza": "paperoni", "price": 78},
    {"pizza": "philadelfia", "price": 65},
    {"pizza": "bawarska", "price": 84},
    {"pizza": "duavola", "price": 99}
]

@app.route('/')
@app.route('/index/')
def index():
    context = {
        'pizzas': menus
    }
    return render_template('index.html', **context)

app.run(debug=True)

########
