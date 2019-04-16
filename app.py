import os
from flask import Flask, jsonify
  
app = Flask(__name__)


doe_family=[
    {
    "id":1,
    "name":"jhon",
    "last name":"Doe",
    "age":33,
    "luckynumbers":[7,13,22],
    },
    {
    "id":2,
    "name":"jane",
    "last name":"Doe",
    "age":35,
    "luckynumbers":[10, 14, 3],
    },
    {
    "id":3,
    "name":"jimmy",
    "last name":"Doe",
    "age":5,
    "luckynumbers":[1],
    }
]


    






  
@app.route('/')
def hello():
    
    aux=0
    
    for number in doe_family[0]['luckynumbers']:
       aux=aux+number
       
    for number in doe_family[1]['luckynumbers']:
       aux=aux+number
       
    for number in doe_family[2]['luckynumbers']:
       aux=aux+number
       
    names=[]
    
    for name in doe_family:
        names.append(name["name"])
    
    aux_two=[]
    
    for luckynumber in doe_family[0]['luckynumbers']:
        aux_two.append(luckynumber)
    
    for luckynumber in doe_family[1]['luckynumbers']:
        aux_two.append(luckynumber)
        
    for luckynumber in doe_family[2]['luckynumbers']:
        aux_two.append(luckynumber)
   
   
    data={
    
    "members":names,
    "lastname":"Doe",
    "sum_luckynumbers":aux,
    "luckynumbers":aux_two
    
    }
    
    return jsonify(data)
    
@app.route('/members/<int:id>')
def seeya(id):
    for member in doe_family:
        if member["id"] == id:
            
            return jsonify(member)
        
    return jsonify({"message":"member not found"})

  
  
app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))
