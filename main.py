import sqlite3
from flask import Flask, render_template, request, redirect, url_for

ADMIN_USERNAME = "admin"

app = Flask(__name__)

menu = [
    {"pizza": "margarita", "description": "bla bla", "price": 100},
    {"pizza": "paperoni", "description": "bla bla", "price": 78},
    {"pizza": "philadelfia", "description": "bla bla", "price": 65},
    {"pizza": "bawarska", "description": "bla bla", "price": 84},
    {"pizza": "duavola", "description": "bla bla", "price": 99}
]
@app.route('/')
@app.route('/index/')
def index():
    context = {
        'pizzas': menu
    }
    return render_template('index.html', **context)
# Головна сторінка____________________________________________________________________________
# Menu________________________________________________________________________________________

connect = sqlite3.connect("app.db")
cursor = connect.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS menu(pizza TEXT, description TEXT, price TEXT)")

def is_admin(username, password):
    return username == ADMIN_USERNAME

@app.route("/join/", methods=['GET', 'POST'])
def join():
    if request.method == 'POST':
        username = request.form['username']

        if is_admin(username):
            pizza = request.form['pizza']
            description = request.form['description']
            price = request.form['price']

            with sqlite3.connect("app.db") as user:
                cursor = user.cursor()
                cursor.execute("INSERT INTO menu (pizza, description, price) VALUES (?, ?, ?)", (pizza, description, price))
                user.commit()
                return render_template("join.html")
        else:
            return "Unauthorized", 401

    return render_template("join.html")

@app.route('/menu_list/')
def menu():
    connect = sqlite3.connect("app.db")
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM menu")
    data = cursor.fetchall()
    return render_template("menu.html", data=data)


if __name__ == '__main__':
    app.run(debug=True)