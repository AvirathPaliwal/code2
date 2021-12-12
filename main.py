from flask import Flask , jsonify , request

app = Flask(__name__)
tasks = [
    {
        'id': 1,
        'name': "raju",
        'contact': "9987644456",
        'done': False
    },
    {
        'id': 2,
        'name': "rahul",
        'contact':'9876543222', 
        'done': False

    }
]
@app.route("/")
def hello():
    return "wlecome to my page"

@app.route("/add-data",methods = ["POST"] )
def add_task():
    if not request.json:
        return jsonify( {
            "status":"error",
            "message":"pls provide data"
        }, 400 )
    task = {
        "id":tasks[-1]["id"]+1,
        'name': request.json['name'],
        'contact': request.json.get('nontact', ""),
        "done":False
    }
    tasks.append(task)
    return jsonify( {
        "status":"success",
        "message":"task added successfully"
    } )

@app.route("/get-data")
def get_task():
    return jsonify( {
        "data":tasks
    } )

if (__name__ == "__main__"):
    app.run( debug = True )
