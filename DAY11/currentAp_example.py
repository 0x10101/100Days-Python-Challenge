#Bullshit lmao

from flask import Flask
from main import app
from flask import currect_app

#app = Flask(__name__)

app_ctx = app.app_context()
app_ctx.push()


#if __name__ == "__main__":
#   app.run(debug=True,port=5002)
