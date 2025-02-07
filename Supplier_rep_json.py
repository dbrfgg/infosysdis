import json
import os
class SupplierRepJson:
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
    
    #получаем поставщика по ID
    def get_by_id(self, supplier_id):
        data = self.read()
        for entry in data:
            if entry['supplier_id'] == supplier_id:
                return entry
        return None  

    #получить список по счету объекта
    def get_k_n_short_list(self, k, n):
        data = self.read()
        start = (n - 1) * k
        end = start + k
        return data[start:end]
    
    #сортировка элементов по выбранному полю
    def sort_by_field(self, field):
        data = self.read()
        if field in ["name", "address", "phone", "ogrn"]:
            data.sort(key=lambda x: x.get(field))
        return data
    
    #добавляем нового поставщика в список с новым ID
    def add_entity(self, name, address, phone, ogrn):
        data = self.read()
        new_id = max([entry['supplier_id'] for entry in data], default=0) + 1
        new_entity = {
            'supplier_id': new_id,
            'name': name,
            'address': address,
            'phone': phone,
            'ogrn': ogrn
        }      
        if any(entry['ogrn'] == ogrn for entry in data):
            raise ValueError('ОГРН должен быть уникальным!')          
        data.append(new_entity)
        self.write(data)

    #заменить данные поставщика по ID
    def replace_by_id(self, supplier_id, name, address, phone, ogrn):
        data = self.read()
        entity = self.get_by_id(supplier_id)
        if not entity:
            raise ValueError(f"Поставщик с ID {supplier_id} не найден.")
        if ogrn and ogrn != entity['ogrn'] and any(entry['ogrn'] == ogrn for entry in data):
            raise ValueError('ОГРН должен быть уникальным!')
        if name:
            entity['name'] = name
        if address:
            entity['address'] = address
        if ogrn is not None:
            entity['ogrn'] = ogrn
        if phone:
            entity['phone'] = phone
        self.write(data)

    #удаляем по ID
    def delete_by_id(self, supplier_id):
        data = self.read()
        entity = self.get_by_id(supplier_id)
        if not entity:
            raise ValueError(f"Поставщик с ID {supplier_id} не найден.")
        data.remove(entity)
        self.write(data)

    #получить количество поставщиков
    def get_count(self):
        data = self.read()
        return len(data)


    
