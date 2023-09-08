from flask import Flask, render_template              # import flask framework
app = Flask(__name__)             # create an app instance

@app.route("/")                   # use the home url
def hello():                      # method called hello
    return "Hello World!"         # returns "hello world"

@app.route("/<name>")              # route with URL variable /<name>
def hello_name(name):              # call method hello_name
    name = "Kiana"
    return "Hello "+ name          # which returns "hello + name

@app.route("/home")                
def home():                    
    return render_template("index.html") 

if __name__ == "__main__":        # when running python app.py
    app.run(debug=True)
    
  