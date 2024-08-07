from states.state import State
from states.application import Application
from states.environments import Environments
from utils.gui import launcher

class MainMenu(State):
  def __init__(self, user):
    super().__init__(user)
    self._menu_list = [
      {
        "name": "Application",
        "key": "a",
        "instance": Application
      },
      {
        "name": "Environments",
        "key": "e",
        "instance": Environments
      },
      {
        "name": "Shut down",
        "key": "s",
        "instance": None
      }
    ]

  def run(self):
    launcher(self._menu_list, "s", self._user)