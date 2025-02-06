import re
import json
from BaseSupplier import BaseSupplier

class Supplier(BaseSupplier):

    def __init__(self, supplier_id, name, address, phone, ogrn):
        super(Supplier, self).__init__(name=name, phone=phone, ogrn=ogrn, supplier_id=supplier_id)
        self.set_address(address)
        

    @classmethod
    def from_json(cls, data_json):
        try:
            data = json.loads(data_json)
            return cls(
                supplier_id=data["supplier_id"],
                name=data["name"],
                address=data["address"],
                phone=data["phone"],
                ogrn=data["ogrn"]
            )
        except (KeyError, json.JSONDecodeError) as e:
            raise ValueError(f"Ошибка при разборе JSON: {e}")

    # Getters
    def get_address(self):
        return self.__address

    # Setters с вызовом методов валидации
    def set_address(self, address):
        if not self.validate_address(address):
            raise ValueError("Адрес должен быть строкой длиной не менее 5 символов.")
        self.__address = address

    # Статические методы для валидации полей
    @staticmethod
    def validate_address(address):
        return isinstance(address, str) and len(address.strip()) >= 5
    
    # Полная версия объекта
    @property
    def full_version(self):
        return (f"Supplier(supplier_id{self.get_supplier_id()}, name={self.get_name()}, "
                f"address={self.get_address()}, phone={self.get_phone()}, ogrn={self.get_ogrn()})")
    
    # Краткая версия объекта
    @property
    def short_version(self):
        return f"Supplier({self.get_name()} {self.get_ogrn()})"
    
    # Сравнение объектов на равенство
    def __eq__(self, other):
        if isinstance(other, Supplier):
            return super(Supplier, self).__eq__(other) and self.get_address() == other.get_address()                    
        return False



