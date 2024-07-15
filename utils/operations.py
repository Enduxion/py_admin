import msvcrt
from datetime import datetime

def lis():
  return msvcrt.getch().decode().lower()

def log(msg, type="info"):
  with open("log/log.dat", "a") as f:
    f.write(f"{type} - [{datetime.now()}]: {msg}\n")