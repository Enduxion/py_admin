from states.state import State
from utils.gui import clear
from utils.operations import lis
import os, re, shutil

class Explorer(State):
  def __init__(self, user):
    super().__init__(user)
    self.id = user["_id"]
    self._main_dir_path = f"usr/{self.id}"
    self.currentDirPath = f"usr/{self.id}"
    if not os.path.isdir("usr"):
      os.mkdir("usr")
    if not os.path.isdir(self._main_dir_path):
      os.mkdir(self._main_dir_path)

  def list_dir(self, dirPath: str):
    print("-"*20)
    try:
      for file in os.listdir(dirPath):
        item_path = os.path.join(dirPath, file)
        if os.path.isdir(item_path):
            print(f"fold: {file}")
        elif os.path.isfile(item_path):
            print(f"file: {file}")
    except Exception:
      print("Something went wrong")
      exit(-1)

    print("-"*20)

  def remove_file(self, dirPath):
    clear()
    name = input("Name: ")

    removePathDir = os.path.join(dirPath, name)

    if (os.path.isfile(removePathDir)):
      os.remove(removePathDir)
    elif (os.path.isdir(removePathDir)):
      shutil.rmtree(removePathDir)
    else:
      print("No file/folder exists with that name")
      lis()

  def make_file(self, dirPath):
    invalid_names = {'CON', 'PRN', 'AUX', 'NUL', 'COM1', 'COM2', 'COM3', 'COM4', 'COM5', 'COM6', 'COM7', 'COM8', 'COM9', 'LPT1', 'LPT2', 'LPT3', 'LPT4', 'LPT5', 'LPT6', 'LPT7', 'LPT8', 'LPT9'}
    while True:
      clear()
      name = input("Name: ")

      if re.search(r'[<>:"/\\|?*\x00-\x1F]', name):
        print('File can not have `<>:"/\\|?*\x00-\x1F` in the name')
        lis()
        continue
      if name.split(".")[0].upper() in invalid_names:
        print('That is a reserved name!')
        lis()
        continue
      
      filePath = os.path.join(dirPath, name)

      if not os.path.isfile(filePath):
        with open(filePath, 'w'):
          return name
      else:
        print('File with filename already exists')
        lis()
        continue

  def _helper_file_saver(self) -> str:
    while True:
      clear()
      print("|| Enter :q to quit ||\n|| Enter :b to go up a dir ||\n|| Enter the name of the folder to view it ||\n|| Enter :s to save the file here ||")
      self.list_dir(self.currentDirPath)
      dec = input()
      if dec == ":q":
        return None
      elif dec == ":b" and self.currentDirPath != self._main_dir_path:
        self.currentDirPath = os.path.dirname(self.currentDirPath)
      elif dec == ":s":
        return self.currentDirPath
      elif dec in os.listdir(self.currentDirPath):
        # if the input is a folder
        if os.path.isdir(os.path.join(self.currentDirPath, dec)):
          self.currentDirPath = os.path.join(self.currentDirPath, dec)

  def _helper_file_selector(self) -> str:
    while True:
      clear()
      print("|| Enter :q to quit ||\n|| Enter :b to go up a dir ||\n|| Enter the name of the folder to view it ||\n|| Enter the name of the file to select it ||")
      self.list_dir(self.currentDirPath)
      dec = input()
      if dec == ":q":
        return None
      elif dec == ":b" and self.currentDirPath != self._main_dir_path:
        self.currentDirPath = os.path.dirname(self.currentDirPath)
      elif dec == ":s":
        return self.currentDirPath
      elif dec in os.listdir(self.currentDirPath):
        # if the input is a file
        if os.path.isfile(os.path.join(self.currentDirPath, dec)):
          self.currentDirPath = os.path.join(self.currentDirPath, dec)
          return self.currentDirPath
        # if the input is a folder
        if os.path.isdir(os.path.join(self.currentDirPath, dec)):
          self.currentDirPath = os.path.join(self.currentDirPath, dec)

  def make_folder(self, dirPath):
    invalid_names = {'CON', 'PRN', 'AUX', 'NUL', 'COM1', 'COM2', 'COM3', 'COM4', 'COM5', 'COM6', 'COM7', 'COM8', 'COM9', 'LPT1', 'LPT2', 'LPT3', 'LPT4', 'LPT5', 'LPT6', 'LPT7', 'LPT8', 'LPT9'}
    while True:
      clear()
      name = input("Name: ")

      if re.search(r'[<>:"/\\|?*\x00-\x1F]', name):
        print('Folder can not have `<>:"/\\|?*\x00-\x1F` in the name')
        lis()
        continue
      if name.split(".")[0].upper() in invalid_names:
        print('That is a reserved name!')
        lis()
        continue
      
      filePath = os.path.join(dirPath, name)
      try:
        os.mkdir(filePath)
        break
      except FileExistsError:
        print("Folder with foldername already exists")
        lis()
        continue

  def run(self):
    while True:
      clear()
      print("|| Enter :q to quit ||\n|| Enter :b to go up a dir ||\n|| Enter :n to create new file ||\n|| Enter :m to make a new dir ||\n|| Enter :r to delete file/folder ||\n|| Enter the name of the file/folder to view it ||")

      self.list_dir(self.currentDirPath)
      dec = input()

      if dec == ":q":
        break
      elif dec == ":b" and self.currentDirPath != self._main_dir_path:
        self.currentDirPath = os.path.dirname(self.currentDirPath)
      elif dec == ":n":
        self.make_file(self.currentDirPath)
      elif dec == ":m":
        self.make_folder(self.currentDirPath)
      elif dec == ":r":
        self.remove_file(self.currentDirPath)

      if dec in os.listdir(self.currentDirPath):
        # if the input is a folder
        if os.path.isdir(os.path.join(self.currentDirPath, dec)):
          self.currentDirPath = os.path.join(self.currentDirPath, dec)
        # if the input is a file
        else:
          pass # TODO: TEXT EDITOR