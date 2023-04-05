from pymongo import MongoClient
from os import environ
client = MongoClient(environ['url'])
db = client['main']['tokens']
def get_top_3():
  classement = sorted(db.find({}), key=lambda x: x["tokens"])
  classement.reverse()
  return [classement[0], classement[1], classement[2]]

def get_classement(id):
  classement = sorted(db.find({}), key=lambda x: x["tokens"])
  classement.reverse()
  for i in range(len(classement)):
    if classement[i]['_id'] == id:
      return i + 1
  return None

def add(id, amount):
  try:
    new = db.find_one({"_id": id})['tokens']
  except:
    db.insert_one({'_id': id, 'tokens': amount})
    return
  new += amount
  db.update_one({'_id': id}, {'$set': {"_id": id, 'tokens': new}})
  return None

def remove(id, amount) -> bool:
  try:
    new = db.find_one({"_id": id})['tokens']
  except:
    return False
  new -= amount
  db.update_one({'_id': id}, {'$set': {"_id": id, 'tokens': new}})
  return True

def get_coin(id):
  try:
    return db.find_one({"_id": id})['tokens']
  except:
    return 0
