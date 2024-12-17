from abc import ABC, abstractmethod
from News import *
from Builder import *


class NewsBuilder(Builder):
  def __init__(self):
    pass
    
  def createUI(self):
    return "Basic UI generated for News type"

    
  def createTheme(self, theme: str):
    return f"Creating theme with type {theme}"

    
  def createDatabase(self, engine: str):
    return f"Database created with {engine}"

    
  def createButton(self, location: float):
    return f"Button created at {location}"

  def getResult(self) -> News:
      return self.news