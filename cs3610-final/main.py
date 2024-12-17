from abc import ABC, abstractmethod
from blogBuilder import *
from NewsBuilder import *
from Director import *


director = Director()
builder = BlogBuilder()
director.makeBlogBuilder(builder)
website = builder.getResult()
print(website)


builder = NewsBuilder()
director.makeNewsSite(builder)
website2 = builder.getResult()
print(website2)
