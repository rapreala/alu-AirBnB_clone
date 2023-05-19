#!/usr/bin/python3
"""
    Defining HBNB Console.
"""
import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
  """
      Define HBNBCommand interpreter
      Attributes:
          prompt (str): command prompt
  """
  prompt = "(hbnb)"
  __classes = {
    "BaseModel",
    
  }
  
if __name__ == '__main__':
    HBNBCommand().cmdloop()
