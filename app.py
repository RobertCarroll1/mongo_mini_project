import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from flask_pymongo import pymongo

app = Flask(__name__)
app.config["MONGO_DBNAME"] = "task_mannager"
app.config["MONGO_URI"] = "mongodb://admin:thefez12@ds147420.mlab.com:47420/task_mannager"

mongo = PyMongo(app)

@app.route("/")
@app.route("/get_tasks")
def get_tasks():
    return render_template("tasks.html", tasks=mongo.db.tasks.find())

# @app.route("/")
# def hello():
#     return "Hello World ...again"

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=True)