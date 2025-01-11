import json
l=[1,2,3,4]
with open('data.json','w') as f:
    json.dump(l,f)
with open('data.json','r') as f:
    l=json.load(f)
    print(l)
    print(type(l))


import pickle
class Abc:
    def __init__(self):
        pass
    def display(self):
        print("Hello")

a=Abc()

with open('data.pkl','wb') as f:
    pickle.dump(a,f)
with open('data.pkl','rb') as f:
    l=pickle.load(f)
    l.display()
    print(type(l))
