from states.state import State
from utils.gui import launcher

import applications.all_ as Application_

class SysApplication(State):
  def __init__(self, user):
    super().__init__(user)
    self._menu_list = [
      {
        "name": "Calculator",
        "key": "C",
        "instance": Application_.Calculator
      },
      {
        "name": "Back",
        "key": "B",
        "instance": None
      }
    ]

  def run(self):
    launcher(self._menu_list, "B", self._user)


class Application(State):
  def __init__(self, user):
    super().__init__(user)
    self._menu_list = [
      {
        "name": "System Application",
        "key": "S",
        "instance": SysApplication
      },
      {
        "name": "Back",
        "key": "B",
        "instance": None
      }
    ]

  def run(self):
    launcher(self._menu_list, "B", self._user)