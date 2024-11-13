# aria_dialog_api_base.py

from abc import ABC, abstractmethod

class AriaDialogAPI(ABC):
    """This is the base class to be inherited by implementations of the ARIA dialog API."""

    @abstractmethod
    def OpenConnection(self, auth=None):
        raise NotImplementedError

    @abstractmethod
    def CloseConnection(self):
        raise NotImplementedError

    @abstractmethod
    def GetVersion(self):
        raise NotImplementedError

    @abstractmethod
    def StartSession(self):
        raise NotImplementedError

    @abstractmethod
    def GetResponse(self, text):
        raise NotImplementedError
