from flask import Flask, request
from psycopg2 import connect, OperationalError

app = Flask(__name__)

FORM = """
<form action="" method="POST">
    <label for="name">Product name:</label><br>
    <input type="text" name="name" id="name"><br>
    <label for="description">Description:</label><br>
    <input type="text" name="description" id="description"><br>
    <label for="price">Price:</label><br>
    <input type="number" name="price" id="price" step="0.01"><br><br>
    <input type="submit" value="Submit">
</form>
"""


def save_product(cur, name, description, price):
    sql = "INSERT INTO items(name, description, price) VALUES(%s, %s, %s)"
    values = (name, description, price)
    cur.execute(sql, values)


@app.route("/add_product", methods=("GET", "POST"))
def add_product_view():
    if request.method == "GET":
        return FORM
    else:
        name = request.form.get("name")
        description = request.form.get("description")
        price = request.form.get("price")

        if len(name) > 40 or not price or not description:
            return "Invalid data!"

        try:
            connection = connect(database="exam2", user="postgres", password="coderslab", host="127.0.0.1")
            connection.autocommit = True
            cursor = connection.cursor()
            save_product(cursor, name, description, price)
            connection.close()
            return "Product added!"
        except OperationalError as err:
            return err


if __name__ == '__main__':
    app.run()
