# col = db["Car"]  
# doc = col.find_one() 
# print ("\nfind_one() result:", doc)
####################################
import pymongo
from flask import Flask,jsonify,render_template,request
from flask_pymongo import PyMongo
from bson import json_util

app = Flask(__name__)
client = pymongo.MongoClient("mongodb://admin:EAAbhq41614@10.100.2.120:27017")
#client = pymongo.MongoClient("mongodb://admin:EAAbhq41614@node9143-advweb-05.app.ruk-com.cloud:11152")
db = client["Ass1"] 


@app.route("/") #เช็คว่า Conect ได้หรือป่าว
def index(): 
    texts = "Hello World"
    return texts
#getAll
@app.route("/Car", methods=['GET'])
def get_allCar():
    char = db.Car
    Customer = db.Customer
    output = []
    outputC = []
    for x in char.find(): 
        output.append({'_id':x['_id'],
                        '_name' : x['_name'],
                        '_model' : x['_model'],
                        '_price' : x['_price']}) 
        for x in Customer.find(): 
            outputC.append({'_id':x['_id'],
                            'namecustomer' : x['namecustomer'],
                            'age' : x['age'],
                            'Tel' : x['Tel']}) 
    return jsonify(output,outputC) 



#GetJ
@app.route("/test", methods=['GET'])
def get_Join():
    Customer = db.Customer
    pipel = Customer.aggregate( [     
            {
                '$lookup':  {
                        'from' : 'Car',
                        'localField': 'carid',
                        'foreignField':'custumerid' ,
                        'as': 'Car'
                }
             }
          #   ,           
                #  {'$unwind':'$Car'},             
                #      {'$project':{
                #                    'namecustomer':1,
                #                    '_name':1,                                                                     
                #                  }           
                #      }  
        ]  
    )  
    
    return json_util.dumps(pipel)

#ดูข้อมูลแบบทีละหัวข้อโดยใช้ชื่อของข้อมูล
@app.route("/Car/<name>", methods=['GET'])
def get_oneCar(name):
    char = db.Car 
    x = char.find_one({'_name' : name}) 
    if x:
        output = ({'_name' : x['_name'],'_model' : x['_model'],
                    '_price' : x['_price']})  #เอาค่าในตารางมาอ่านแล้วใส่ไปใน output เป็นเหมือนค่าอาเร
    else: #หากหาไฟล์ไม่ครบหรือพิมชื่อผิดจะทำการแสดงข้อความ
         output = "No such name"
    return jsonify(output) #หลังจากทำเงื่อนไขเสร็จส่งค่ากลับไปที่ output

#ทำการ insert ข้อมูลตารางเข้าไปใหม่
@app.route('/Car', methods=['POST'])
def add_postcar():
  char = db.Car
  name = request.json['_name'] #ทำการสร้างตัวแปรใหม่เพื่อรับค่าจาก _name
  model = request.json['_model']
  price = request.json['_price']
  
  char_id = char.insert({'_name': name, #ทำการพิมให้ตรงกับชื่อตารางแล้วกด sent จะทำการไปทำการทำงานในบรรทัดที่ 53
                        '_model': model,
                        '_price': price,})
  new_char = char.find_one({'_id': char_id }) #สร้างIP ขึ้นมาใหม่โดยการสุ่ม
  output = {'_name' : new_char['_name'], #หลังจากสร้างเพิ่มแล้วทำการใส่เข้าไปในตัวแปรที่สร้างมาทำการใส่ค่าลง output
                        '_model' : new_char['_model'],
                        '_price' : new_char['_price'],}
  return jsonify(output)  #หลังจากทำเงื่อนไขเสร็จส่งค่ากลับไปที่ output

#ทำการ edit ข้อมูลตารางโดยการอิง name or _name
@app.route('/Car/<name>', methods=['PUT'])
def update_character(name):
    char = db.Car
    x = char.find_one({'_name' : name}) #เอาค่าที่ใส่มาใน name เพื่อเช็คว่าตรงกับตารางไหน
    if x: #ในตัวแปร x มี name ที่เรากรอกลงไปใน /Car/<name>
        myquery = {'_name' : x['_name'], #เรียกข้อมูลมาใส่ใน myquery
                        '_model' : x['_model'],
                        '_price' : x['_price']}

    name = request.json['_name'] #ทำการสร้างตัวแปรใหม่เพื่อรับค่าจาก _name
    model = request.json['_model']
    price = request.json['_price']
    
    newvalues = {"$set" : {'_name' : name,  #ทำการแก้ไขไฟล์แล้วใส่ไปในตัวแปรที่ส้รางรวมกันเป็นอาเร
                        '_model': model,
                        '_price': price,}}
    char_id = char.update_one(myquery, newvalues) #ส่งไปอัพเดท
    output = {'_name' : name,  #นำค่าที่อัพเดทมาทั้งหมดลงตัวแปร output
                        '_model': model,
                        '_price': price,}
    return jsonify(output) #หลังจากทำเงื่อนไขเสร็จส่งค่ากลับไปที่ output

#ทำการ Deleted ข้อมูลตารางโดยการอิง name or _name
@app.route('/Car/<name>', methods=['DELETE'])
def Car_delete(name):
    char = db.Car
    x = char.find_one({'_name' : name}) #ในตัวแปร x มี name ที่เรากรอกลงไปใน /Car/<name>

    char_id = char.delete_one(x) #นำ x มาทำฟังชัั่น delete_one 

    output = "Deleted complete" # หลังจากลบเสร็จแสดงข้อความ

    return jsonify(output) 

#ตัว Run server
if __name__ == "__main__":
    app.run(host='0.0.0.0',port = 80)