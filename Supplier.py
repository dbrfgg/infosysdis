import re
import json

class Supplier:

    def __init__(self, supplier_id, name, address, phone, ogrn):
        self.set_supplier_id(supplier_id)
        self.set_name(name)
        self.set_address(address)
        self.set_phone(phone)
        self.set_ogrn(ogrn)

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

    # Setters с вызовом методов валидации
    def set_supplier_id(self, supplier_id):
        if not self.validate_id(supplier_id):
            raise ValueError("Supplier ID должен быть положительным целым числом.")
        self.__supplier_id = supplier_id

    def set_name(self, name):
        if not self.validate_name(name):
            raise ValueError("Название должно быть непустой строкой.")
        self.__name = name

    def set_address(self, address):
        if not self.validate_address(address):
            raise ValueError("Адрес должен быть строкой длиной не менее 5 символов.")
        self.__address = address

    def set_phone(self, phone):
        if not self.validate_phone(phone):
            raise ValueError("Неверный формат телефона.")
        self.__phone = phone

    def set_ogrn(self, ogrn):
        if not self.validate_ogrn(ogrn):
            raise ValueError("OGRN должен содержать ровно 13 цифр.")
        self.__ogrn = ogrn

    # Статические методы для валидации полей
    @staticmethod
    def validate_id(supplier_id):
        return isinstance(supplier_id, int) and supplier_id > 0
    
    @staticmethod
    def validate_name(name):
        return isinstance(name, str) and bool(name.strip())
    
    @staticmethod
    def validate_address(address):
        return isinstance(address, str) and len(address.strip()) >= 5
    
    @staticmethod
    def validate_phone(phone):
        pattern = r'^\+?\d{7,15}$'  # Номер телефона: от 7 до 15 цифр с возможным "+" в начале
        return isinstance(phone, str) and re.fullmatch(pattern, phone)
    
    @staticmethod
    def validate_ogrn(ogrn):
        return isinstance(ogrn, str) and len(ogrn) == 13 and ogrn.isdigit()
    
    # Полная версия объекта
    @property
    def full_version(self):
        return (f"Supplier(supplier_id={self.get_supplier_id()}, name={self.get_name()}, "
                f"address={self.get_address()}, phone={self.get_phone()}, ogrn={self.get_ogrn()})")
    
    # Краткая версия объекта
    @property
    def short_version(self):
        return f"Supplier({self.get_name()} {self.get_ogrn()})"
    
    # Сравнение объектов на равенство
    def __eq__(self, other):
        if isinstance(other, Supplier):
            return (self.get_supplier_id() == other.get_supplier_id() and
                    self.get_name() == other.get_name() and
                    self.get_address() == other.get_address() and
                    self.get_phone() == other.get_phone() and 
                    self.get_ogrn() == other.get_ogrn())
        return False



