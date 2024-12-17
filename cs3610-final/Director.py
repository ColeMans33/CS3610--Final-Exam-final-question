from abc import ABC, abstractmethod
from Builder import Builder
import random




class Director:
  def makeNewsSite(self, builder: Builder):
    builder.createButton(1.1)
    builder.createDatabase("SQL")
    builder.createTheme("lightmode")
    builder.createUI()

  def makeBlogBuilder(self, builder: Builder):
    builder.createButton(10.2)
    builder.createDatabase("SQL")
    builder.createTheme("darkmode")
    builder.createUI()