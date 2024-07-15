import pymongo
import os
from dotenv import load_dotenv

load_dotenv()

def _msg(status: int, msg: str) -> dict:
  return {"status": status, "data": msg}

_db = None

try:
  _client = pymongo.MongoClient(os.getenv("MONGODB_URI"))
  _db = _client[os.getenv("MONGODB_DB")]
except Exception as err:
  print(err)
  exit(-1)

def find_one(collection: str, query: dict) -> dict:
  try:
    results = _db[collection].find_one(query)
    if results is None:
      return _msg(400, "Invalid username or password!")
    results.pop("password")
    return _msg(200, results)
  except Exception as err:
    return _msg(500, str(err))