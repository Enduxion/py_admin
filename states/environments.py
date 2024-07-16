from states.state import State
from utils.gui import launcher
from utils.operations import lis
from settings.user import UserSettings

class Environments(State):
  def __init__(self, user):
    super().__init__(user)
    self._menu_list = [
      {
        "name": "User Env",
        "key": "U",
        "instance": UserSettings
      },
      {
        "name": "Theme Env",
        "key": "T",
        "instance": None
      },
      {
        "name": "Application Env",
        "key": "A",
        "instance": None
      },
      {
        "name": "Back up Env",
        "key": "C",
        "instance": None
      },
      {
        "name": "Back",
        "key": "B",
        "instance": None
      }
    ]

  def run(self):
    launcher(self._menu_list, "b", self._user)