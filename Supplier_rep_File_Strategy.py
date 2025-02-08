import os
from abc import ABC, abstractmethod

class SupplierRepFileStrategy(ABC):
  
    @abstractmethod
    def read(self):
        pass
      
    @abstractmethod
    def write(self, data):
        pass