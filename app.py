from flask import Flask, render_template, request
import json

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/names")
def names():
    with open('names.json') as f:
        peoples = json.load(f)
    return render_template("names.html", peoples = peoples)


@app.route("/name/<name>")
def name_page(name):
    return render_template("name.html", name=name)

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "GET":
        return render_template("add.html")
    else:
        with open("names.json", "r") as f:
            names = json.load(f)
        
        data = request.get_json()
        names.append(data)

        with open('names.json', 'w') as f:
            json.dump(names, f, indent=4)
        return render_template("names.html")

@app.route("/delete", methods=["GET", "POST"])
def delete():
    if request.method == "GET":
     with open('names.json') as f:
      peoples = json.load(f)
      return render_template("delete.html", peoples = peoples)

    else:
        return render_template("delete.html")


if __name__ == "__main__":
    app.run(debug=True)