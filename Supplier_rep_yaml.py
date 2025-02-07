import yaml
import os

class SupplierRepYaml:

    def __init__(self, filename):
        self.filename = filename
    
    def read(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                data = yaml.safe_load(f)
                return data
        return []
    
    def write(self, data):
        with open(self.filename, 'w') as f:
            yaml.dump(data, f, default_flow_style=False)

    def get_by_id(self, supplier_id):
        data = self.read()
        for entry in data:
            if entry['supplier_id'] == supplier_id:
                return entry
        return None

    def get_k_n_short_list(self, k, n):
        data = self.read()
        start = (n - 1) * k
        end = start + k
        return data[start:end]
    
    def sort_by_field(self, field):
        data = self.read()
        if field in ["name", "address", "phone", "ogrn"]:
            data.sort(key=lambda x: x.get(field))
        return data
          
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
            raise ValueError('огрн должен быть уникальным!')
        data.append(new_entity)
        self.write(data)

    def replace_by_id(self, supplier_id, name, address, phone, ogrn):
        data = self.read()
        entity = self.get_by_id(supplier_id)
        if not entity:
            raise ValueError(f"Элемент с ID {supplier_id} не найден.")
        if ogrn and ogrn != entity['ogrn'] and any(entry['ogrn'] == ogrn for entry in data):
            raise ValueError('огрн должен быть уникальным!')
        if name:
            entity['name'] = name
        if address:
            entity['address'] = address
        if ogrn is not None:
            entity['ogrn'] = ogrn
        if phone:
            entity['phone'] = phone
            # Записываем обновленные данные в файл
            self.strategy.write(data)
    
    def delete_by_id(self, supplier_id):
            data = self.read()
            entity = self.get_by_id(supplier_id)
            if not entity:
                raise ValueError(f"Элемент с ID {supplier_id} не найден.")
            data.remove(entity)
            self.write(data)
    
    def get_count(self):
            data = self.read()
            return len(data)