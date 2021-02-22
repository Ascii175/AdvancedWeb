import pymongo  
client = pymongo.MongoClient("mongodb://admin:EAAbhq41614@node9143-advweb-05.app.ruk-com.cloud:11152") 
db = client["Ass1"]  
col = db["Car"]  
doc = col.find_one() 
print ("\nfind_one() result:", doc)
