from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1><a href="/login">Log In</a></h1>'

@app.route('/login/')
def login():
    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)
