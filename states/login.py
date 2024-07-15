from states.state import State
from db.db import find_one
from utils.gui import clear
from utils.operations import lis

class Login(State):
  def __init__(self):
    super().__init__(None)

  def run(self):
    while True:
      clear()
      print("!! Enter :q to quit !!")

      username = input("Username: ")
      password = input("Password: ")

      if username.lower() == ":q" or password.lower() == ":q":
        break

      user = find_one("users", {"username": username, "password": password})

      if user["status"] != 200:
        print(user["data"])
        lis()
        continue

      return user["data"]
    
    return None
      

      
