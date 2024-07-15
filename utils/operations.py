import msvcrt
from datetime import datetime

def lis():
  while True:
    char = msvcrt.getch()
    
    # Check for special keys (like arrow keys)
    if char in (b'\xe0', b'\x00'):
      continue  # Ignore special keys

    char = char.decode().lower()
    if char.isalnum():  # Check if the character is alphanumeric
      return char

def log(msg, type="info"):
  with open("log/log.dat", "a") as f:
    f.write(f"{type} - [{datetime.now()}]: {msg}\n")