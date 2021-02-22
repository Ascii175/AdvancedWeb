# col = db["Car"]  
# doc = col.find_one() 
# print ("\nfind_one() result:", doc)
####################################
import pymongo
from flask import Flask,jsonify,render_template,request
from flask_pymongo import PyMongo

app = Flask(__name__)
client = pymongo.MongoClient("mongodb://admin:EAAbhq41614@node9143-advweb-05.app.ruk-com.cloud:11152") 
db = client["Ass1"]  


@app.route("/")
def index():
    texts = "Hello World"
    return texts

@app.route("/Car", methods=['GET'])
def get_allCar():
    char = db.Car
    output = []
    for x in char.find():
        output.append({'_name' : x['_name'],'_model' : x['_model'],
                        '_price' : x['_price']})
    return jsonify(output)

@app.route("/Car/<name>", methods=['GET'])
def get_oneCar(name):
    char = db.Car
    x = char.find_one({'_name' : name})
    if x:
        output = ({'_name' : x['_name'],'_model' : x['_model'],
                    '_price' : x['_price']})
    else:
         output = "No such name"
    return jsonify(output)

@app.route('/Car', methods=['POST'])
def add_postcar():
  char = db.Car
  name = request.json['_name']
  model = request.json['_model']
  price = request.json['_price']
  
  char_id = char.insert({'_name': name, 
                        '_model': model,
                        '_price': price,})
  new_char = char.find_one({'_id': char_id })
  output = {'_name' : new_char['_name'], 
                        '_model' : new_char['_model'],
                        '_price' : new_char['_price'],}
  return jsonify(output)


@app.route('/Car/<name>', methods=['PUT'])
def update_character(name):
    char = db.Car
    x = char.find_one({'_name' : name})
    if x:
        myquery = {'_name' : x['_name'],
                        '_model' : x['_model'],
                        '_price' : x['_price']}

    name = request.json['_name']
    model = request.json['_model']
    price = request.json['_price']
    
    newvalues = {"$set" : {'_name' : name, 
                        '_model': model,
                        '_price': price,}}

    char_id = char.update_one(myquery, newvalues)

    output = {'_name' : name, 
                        '_model': model,
                        '_price': price,}

    return jsonify(output)

@app.route('/Car/<name>', methods=['DELETE'])
def Car_delete(name):
    char = db.Car
    x = char.find_one({'_name' : name})

    char_id = char.delete_one(x)

    output = "Deleted complete"

    return jsonify(output)

if __name__ == "__main__":
    app.run(host='0.0.0.0',port = 5000)