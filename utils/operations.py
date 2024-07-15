import msvcrt
from datetime import datetime

def lis():
  while True:
    char = msvcrt.getch()
    
    if char in (b'\xe0', b'\x00'):
      msvcrt.getch() # Handle the second byte
      continue

    return char.decode().lower()
    

def log(msg, type="info"):
  with open("log/log.dat", "a") as f:
    f.write(f"{type} - [{datetime.now()}]: {msg}\n")