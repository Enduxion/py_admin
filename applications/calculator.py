from states.state import State
from utils.gui import displayer, clear
from utils.operations import lis
from sympy import sympify

from math import factorial

class Calculator(State):
  def __init__(self, user):
    super().__init__(user)
    self._menu_list = [
      {
        "name": "Add",
        "key": "A",
        "func": self.add
      },
      {
        "name": "Substract",
        "key": "S",
        "func": self.sub
      },
      {
        "name": "Multiply",
        "key": "M",
        "func": self.mul
      },
      {
        "name": "Divide",
        "key": "D",
        "func": self.div
      },
      {
        "name": "Other",
        "key": "O",
        "func": self.other

      },
      {
        "name": "Back",
        "key": "B",
        "func": None
      }
    ]
  
  def run(self):
    while True:
      displayer(self._menu_list)
      dec = lis()
      
      if dec == "b":
        break

      if dec == "o":
        self.other()
        continue
      
      for menu_item in self._menu_list:
        if menu_item["key"].lower() == dec:
          menu_item["func"]()
          print("Press any key to continue (alphanumeric)...")
          lis()
          break

      
  def ask_num(self) -> tuple[float, float]:
    clear()
    try:
      num1 = float(input("First number: "))
      num2 = float(input("Second number: "))
      return num1, num2
    except ValueError:
      print("Not a number")
      return None, None
  
  def add(self):
    num1, num2 = self.ask_num()
    if num1 is None or num2 is None:
      return
    print(f"Sum: {num1 + num2}")
  
  def sub(self):
    num1, num2 = self.ask_num()
    if num1 is None or num2 is None:
      return
    print(f"Difference: {num1 - num2}")

  def mul(self):
    num1, num2 = self.ask_num()
    if num1 is None or num2 is None:
      return
    print(f"Product: {num1 * num2}")

  def div(self):
    num1, num2 = self.ask_num()
    if num1 is None or num2 is None:
      return
    try:
      print(f"Quotient: {num1 / num2}")
    except ZeroDivisionError:
      print("Cannot divide by zero")

  def other(self):
    def literal_calc():
      try:
        literal = input("Literal: ")
        converted_literal = sympify(literal)
        print(f"Answer: {converted_literal.evalf()}")
      except (ValueError, SyntaxError):
        print("Invalid mathematical expression")
    def other_factorial():
      try:
        num1 = int(input("Integer: "))
        print(f"Factorial: {factorial(num1)}")
      except ValueError:
        print("Not a number")
        return

    def power():
      num1, num2 = self.ask_num()
      print(f"Power: {num1 ** num2}")
    def root():
      num1, num2 = self.ask_num()
      print(f"Root: {num1 ** (1/num2)}")

    other_menu_items = [
      {
        "name": "Calculate from literal",
        "key": "L",
        "func": literal_calc
      },
      {
        "name": "Factorial",
        "key": "F",
        "func": other_factorial
      },
      {
        "name": "Power",
        "key": "P",
        "func": power
      },
      {
        "name": "Root",
        "key": "R",
        "func": root
      },
      {
        "name": "Back",
        "key": "B",
        "func": None
      }
    ]

    while True:
      displayer(other_menu_items)

      dec = lis()
      if dec == "b":
        break

      for menu_item in other_menu_items:
        if menu_item["key"].lower() == dec:
          clear()
          menu_item["func"]()
          print("Press any key to continue (alphanumeric)...")
          lis()
          break

