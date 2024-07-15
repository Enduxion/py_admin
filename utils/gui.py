from subprocess import call as sp_call

from utils.operations import lis

def launcher(menu_dicts: list, quit_key: str, props) -> None:
  while True:
    clear()

    print("-"*20)
    for menu_dict in menu_dicts:
      print(f"{menu_dict['key'].upper()}. {menu_dict['name']}")
    print("-"*20)

    dec = lis()

    if dec == quit_key.lower():
      return

    name_of_app = ""
    
    try:
      for menu_dict in menu_dicts:
        if menu_dict['key'].lower() == dec:
          name_of_app = menu_dict['name']
          menu_dict['instance'](props).run()
    except AttributeError:
      print(f"Faulty App: {name_of_app}\nNo run method")
      exit(-1)
    except Exception as err:
      print(f"Faulty App: {name_of_app}\n{err}")
      exit(-1)

def displayer(menu_dicts: list) -> None:
  clear()

  print("-"*20)
  for menu_dict in menu_dicts:
    print(f"{menu_dict['key'].upper()}. {menu_dict['name']}")
  print("-"*20)

def clear():
  _ = sp_call('cls', shell=True)