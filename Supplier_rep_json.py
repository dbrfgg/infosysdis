import json
import os
from Supplier_rep_File_Strategy import SupplierRepFileStrategy
class SupplierRepJson(SupplierRepFileStrategy):
    def __init__(self, filename):
        self.filename = filename
    
    #читаем из файла
    def read(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                data = json.load(f)
                return data
        return []
    
    #записываем в файл
    def write(self, data):
        with open(self.filename, 'w') as f:
            json.dump(data, f, indent=4)
    
    

    
