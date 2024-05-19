import json
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="dbuser",
  password="Password@123",
  database="mydb"
)
mycursor = mydb.cursor()

with open("data.json" , "r") as f:
    data = json.load(f)

# extract keys from json file.
    # keys = set()
    # for record in data:
    #     for ks in record.keys():      
    #         keys.add(ks)
    # print(keys)


# parsing the key and valuses for sql queries
    for record in data:
       k = []
       v = []
       tresources = record['resources']   # storing recources key temporary 
       del(record['resources'])
       tname = record['name']             # storing name key temporary
       del(record['name'])
       for key, value in record.items():          
         k.append(key)
         v.append(value)
       v = [ json.dumps(x) for x in v]    # Adding double quotes to Vaule string
       for n in tname:

        # Create records for each ransomeware name ; execpt resources key
         sql = "INSERT INTO ransomwaredata ({},{}) VALUES ({},{})".format('name',','.join(k),  json.dumps(n), ','.join(v))
         mycursor.execute(sql)
         for rs in tresources:
            
        # Create records for each resource key 
            sql2 = "INSERT INTO resource (name,resources) VALUES ({},{})".format(json.dumps(n),json.dumps(rs))
            mycursor.execute(sql2)

        #  print(sql)
mydb.commit()


