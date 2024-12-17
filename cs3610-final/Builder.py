from abc import ABC, abstractmethod

class Builder(ABC):
    @abstractmethod
    def createUI(self):
        pass

    @abstractmethod
    def createTheme(self, theme: str):
        pass

    @abstractmethod
    def createDatabase(self, engine: str):
        pass

    @abstractmethod
    def createButton(self, location: float):
        pass

    @abstractmethod
    def getResult(self):
        pass