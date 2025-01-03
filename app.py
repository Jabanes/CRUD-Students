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
        name = data.get('name')
        names.append({"name" : name, "id" : len(names) +1})

        with open('names.json', 'w') as f:
            json.dump(names, f, indent=4)
        return render_template("names.html")

@app.route("/delete", methods=["GET"])
def delete_page():
    # This method only handles GET requests to display the delete page
    with open('names.json') as f:
        peoples = json.load(f)
    return render_template("delete.html", peoples=peoples)

@app.route("/delete/<int:id>", methods=["DELETE"])
def delete(id):
    # This method handles DELETE requests to delete a specific name by id
    with open('names.json') as f:
        names = json.load(f)

    # Remove the name with the given id
    names = [name for name in names if name["id"] != id]

    with open('names.json', 'w') as f:
        json.dump(names, f, indent=4)

    return '', 204  # No content response after deletion

@app.route("/update", methods=["GET"])
def update_page():
    with open('names.json') as f:
        peoples = json.load(f)
    return render_template("update.html", peoples=peoples)

@app.route("/update/<int:id>", methods=["PUT"])
def update(id):
    # This method handles DELETE requests to delete a specific name by id
    with open('names.json') as f:
        names = json.load(f)

    updatedName = request.get_json().get('name')
    
    for name in names:
        if name['id'] == id:
            name['name'] = updatedName
            break

    with open('names.json', 'w') as f:
        json.dump(names, f, indent=4)

    return '', 204  # No content response after deletion

if __name__ == "__main__":
    app.run(debug=True)