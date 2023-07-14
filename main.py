from flask import Flask, render_template,jsonify,request
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://<username>:<password>@atlascluster.ywbchnq.mongodb.net/"
mongo = PyMongo(app)


@app.route("/")
def home():
    chats = mongo.db.chats.find({})
    mychats = [chat for chat in chats]
    print(chats) 
    return render_template("index.html")


@app.route("/api",methods=["GET","POST"])
def qa():
    if request.method == "POST":
        print(request.json)
        request = request.json.get("question")
        data = {"result":f"Answer of {question}"}
        return jsonify(data)
    data = {"result":"You're welcome! I'm glad I could help. If you have any more questions, feel free to ask."}    
    return jsonify(data)   
app.run(debug=True)   
    #return render_template("index.html")
#app.run(debug=True)