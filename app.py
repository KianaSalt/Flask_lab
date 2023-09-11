import urllib.request, json
from flask import Flask, render_template, request             # import flask framework
app = Flask(__name__)             # create an app instance

@app.route("/")                           # use the home url
def home():                               # method called home
    url = "https://xkcd.com/info.0.json"  # We need to add the URL we will be using to fetch information from.
    response = urllib.request.urlopen(url)  # Sometimes this means also sending some data like a key, but not for this one
    data = response.read()                  # Once we have the response we need to extract the data we want.
    dict = json.loads(data)
    return render_template("index.html", datum=dict)  # returns whats inside index.html
 
@app.route("/<name>")              # route with URL variable /<name>
def hello_name(name):              # call method hello_name
    #name = "Kiana"
    return "Hello "+ name          # which returns "hello + name

@app.route("/about")           # About page 
def about():
    name = request.args.get('name') if request.args.get('name') else "Hello World!"      #we are taking 'name' from the request args (approute name) and assigning it to a variable named name
    return render_template("about.html", aboutName=name)     #passing name as a variable called aboutName to the about template.


if __name__ == "__main__":        # when running python app.py
    app.run(debug=True)
    
  