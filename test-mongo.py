# from pymongo import MongoClient
# con = MongoClient('localhost', 27017)
# db = con.get_database("demo")
# emp = db.employees
# a = db.emp.find({'id':979297479756677120})
# print(a)
# emp.insert({
#    a
# })

# b = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
# print(type(b))
import random
arr =[]
r = random.randint(0,100)
s = ''
if r%2==0:
    s = 'neg'
else:
    s = 'pos'
dict_list = {
    'sentiment' : s
}
arr.append(dict_list)
# print(random.randint(0,100))
print(arr)