class Supplier:
    def __init__(self, supplier_id, name, address, phone, ogrn):
        self.__supplier_id = supplier_id
        self.__name = name
        self.__address = address
        self.__phone = phone
        self.__ogrn = ogrn

# Getters
    def get_supplier_id(self):
        return self.__supplier_id
    def get_name(self):
        return self.__name
    def get_address(self):
        return self.__address
    def get_phone(self):
        return self.__phone
    def get_ogrn(self):
        return self.__ogrn
    
    # Setters
    def set_name(self, name):
        self.__name =name
    def set_address(self, address):
        self.__address = address
    def set_phone(self, phone):
        self.__phone = phone
    def set_ogrn(self, ogrn):
        self.__ogrn = ogrn