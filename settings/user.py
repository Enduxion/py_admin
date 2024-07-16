from states.state import State
from utils.gui import displayer
class UserSettings(State):
  def __init__(self, user):
    super().__init__(user)
    self._menu_items = [
      {
        "name": "Back",
        "key": "",
        "func": None
      },
    ]

  def run(self):
    while True:
      pass