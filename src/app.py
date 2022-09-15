from flask import Flask

#create an object
app = Flask(__name__)

#create route
@app.route("/")
def index():
 return "Hello, world"

if __name__ == "__main__":
 app.run
