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
import re

r = re.compile(r'([A-Z]{1}[a-z]{2})\s([A-Z]{1}[a-z]{2})\s(\d{2})')
s = 'Tue Apr 02'

if(r.match(s)):
    print('1')
else:
    print('2')