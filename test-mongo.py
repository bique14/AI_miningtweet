from pymongo import MongoClient
con = MongoClient('localhost', 27017)
db = con.get_database("demo")
emp = db.employees
a = db.emp.find({'id':979297479756677120})
print(a)
# emp.insert({
#    a
# })

# b = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
# print(type(b))