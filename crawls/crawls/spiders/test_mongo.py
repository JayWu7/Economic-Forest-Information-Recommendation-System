import pymongo

client = pymongo.MongoClient('localhost',27017)
db = client['new_db']

col = db['new_col']

col.insert({'name':'jaywu'})

print(col.find_one())
