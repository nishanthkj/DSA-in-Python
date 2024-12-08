mydic = {"name":"nishanth","age":40,"address":"Indai"}

def traverse(dic):
    for k in dic:
        print(k ,dic[k] )

def search(dic,value):
    for k in dic:
        if value == dic[k]:
            print(f"{k}value {value}")
  

search(mydic,"nishanth")