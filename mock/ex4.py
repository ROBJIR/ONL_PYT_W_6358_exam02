from flask import Flask, request


app = Flask(__name__)

@app.route("/add_product")
def my_page():
    return """
<form action="/solution" method="POST">
    <input type="text" name="name" placeholder="name">
    <input type="text" name="description" placeholder="description">
    <input type="text" name="price" placeholder="price">
    <input type="submit">

</form>
"""


@app.route("/solution", methods=["POST"])
def my_page2():
    if len(request.form['name']) > 40:
        return "invalid name"
    
    try:
        num = float(request.form['price'])
    except:
        return "invalid name"
    
    return f"""<h1>
    {request.form['name']}
     {request.form['description']}
      {request.form['price']}
</h1>
"""



app.run()