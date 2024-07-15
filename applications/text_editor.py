from states.state import State
from applications.all_ import Explorer
from utils.operations import lis
from utils.gui import clear
import msvcrt, os

class TextEditor(State):
  """
  Text Editor for adding new files and editing texts
  """

  def __init__(self, user):
    super().__init__(user)
    self.id = user["_id"]
    self._main_dir_path = f"usr/{self.id}"
    self.currentDirPath = f"usr/{self.id}"
  
  def edit_file(self, contents: str = "", path: str = ""):
    """
    Make new files or edit that already exist
    
    params:
      contents (str) -> Initial content to be edited (Signifies that the file already exists)
      path (str) -> path of the "file" that already exists

    works:
      We use the kbhit function to detect key press and use getch to get the key code.
      If the key is esc, we go to prompt save
      If the key is backspace, we remove the last letter in our content and display the content all over again by clearing the screen.
      If the path was given, the file is saved automatically with "write"
      If the file is a new file, then the user is prompted to select a folder and give it a new name using "Rover" functions.
    """
    # The text editor interface
    initial_content = contents
    clear()
    print(initial_content, end="", flush=True)
    while True:
      if msvcrt.kbhit():
        chr = msvcrt.getch()
        if chr in (b'\x00', b'\xe0'): #Special Char
          _ = msvcrt.getch() # Dealing with the second value
          continue
        elif chr == b'\x1b': # Esc
          break
        elif chr == b'\x08': # Backspace
          initial_content = initial_content[:-1]
          os.system("cls")
          print(initial_content, end="", flush=True)
          continue
        elif chr == b'\x0d': # enter
          initial_content = initial_content + "\n"
          print()
          continue
        print(chr.decode(), end="", flush=True)
        initial_content = initial_content + chr.decode()
    # The save code
    try:
      while True:
        clear()
        print("Do you want to save? (Y/N): ")
        dec = lis()
        if dec == 'n':
          print("File not saved!")
          lis()
          break
        elif dec == 'y':
          if path != '': # If path was given
            with open(path, 'w') as f:
              f.write(initial_content)
          else: # If path was not given
            loc = Explorer(self._user)._helper_file_saver()
            if loc is None:
              continue
            name = Explorer(self._user).make_file(loc)
            with open(os.path.join(loc, name), 'w') as f:
              f.write(initial_content)
          print("File saved successfully")
          lis()
          break  
    except IOError:
      print("Couldn't save the file!")
      return
  
  def run(self):
    """
    Code runs from here.
    """

    while True:
      clear()
      print("-"*20, "N. New File\nE. Existing File\nB. Back", "-"*20, sep="\n")
      dec = lis()
      if dec == "n":
        self.edit_file("", "")
      elif dec == "e":
        path = Explorer(self._user)._helper_file_selector()
        if path is None:
          continue
        content = ""
        with open(path, 'r') as f:
          content = f.read()
        self.edit_file(content, path)
      elif dec == "b":
        break

