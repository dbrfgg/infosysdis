import re

class BaseSupplier:

    def __init__(self, name, phone, ogrn, supplier_id=None):
        self.set_name(name)
        self.set_phone(phone)
        self.set_ogrn(ogrn)
        self.set_supplier_id(supplier_id)

    # Геттеры
    def get_supplier_id(self):
        return self.__supplier_id
    
    def get_name(self):
        return self.__name
    
    def get_phone(self):
        return self.__phone
    
    def get_ogrn(self):
        return self.__ogrn
    
    # Сеттеры 
    def set_name(self, name):
        if not self.validate_name(name):
            raise ValueError("Имя должно быть непустой строкой.")
        self.__name = name.strip()
        
    def set_phone(self, phone):
        if not self.validate_phone(phone):
            raise ValueError("Неверный формат контактного телефона.")
        self.__phone = phone.strip()

    def set_ogrn(self, ogrn):
        if not self.validate_ogrn(ogrn):
            raise ValueError("OGRN должен содержать ровно 13 цифр.")
        self.__ogrn = ogrn

    def set_supplier_id(self, supplier_id):
        if supplier_id is not None and not self.validate_id(supplier_id):
            raise ValueError("Supplier ID должен быть положительным числом.")
        self.__supplier_id = supplier_id if supplier_id else None

    # Статические методы для валидации
    @staticmethod
    def validate_name(name):
        return isinstance(name, str) and bool(name.strip())
    
    @staticmethod
    def validate_phone(phone):
        pattern = r'^\+?\d{7,15}$'  # Номер телефона: от 7 до 15 цифр с возможным "+" в начале
        return isinstance(phone, str) and re.fullmatch(pattern, phone)
    
    @staticmethod
    def validate_ogrn(ogrn):
        return isinstance(ogrn, str) and len(ogrn) == 13 and ogrn.isdigit()
    
    @staticmethod
    def validate_id(supplier_id):
        return isinstance(supplier_id, int) and supplier_id > 0
    
    # Сравнение объектов на равенство
    def __eq__(self, other):
        if isinstance(other, BaseSupplier):
            return (self.get_supplier_id() == other.get_supplier_id() and
                    self.get_name() == other.get_name() and
                    self.get_phone() == other.get_phone() and 
                    self.get_ogrn() == other.get_ogrn())
        return False
    
    # Строковое представление объекта
    def __str__(self):
        initials = f"{self.__name[0].upper()}." if self.__name else "Unknown"
        return f"BaseSupplier: (Contact: {self.__phone})"


