from states.login import Login
from states.main_menu import MainMenu
class App:
  def __init__(self):
    self._user = None 

  def run(self):
    self._user = Login().run()

    if self._user is None:
      print("Unauthorized access!")
      exit(-1)

    MainMenu(self._user).run()