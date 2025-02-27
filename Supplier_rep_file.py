import os
from Supplier_rep_File_Strategy import SupplierRepFileStrategy

class SupplierRepFile:

    def __init__(self, strategy: SupplierRepFileStrategy):
        self._data = []
        self._strategy = strategy

    def write_data_to_file(self):
        self._strategy.write(self._data)

    def read_data_from_file(self):
        self._data = self._strategy.read()

    def get_by_id(self, supplier_id):
        for entry in self._data:
            if entry['supplier_id'] == supplier_id:
                return entry
        return None

    def get_k_n_short_list(self, k, n):
        start = (n - 1) * k
        end = start + k
        return self._data[start:end]

    def sort_by_field(self, field):
        if field in ["name", "address", "phone", "ogrn"]:
            self._data.sort(key=lambda x: x.get(field))
        return self._data

    def add_entity(self, name, address, phone, ogrn):

        new_id = max([entry['id'] for entry in self._data], default=0) + 1
        new_entity = {
            'supplier_id': new_id,
            'name': name,
            'address': address,
            'phone': phone,
            'ogrn': ogrn
        }
        if any(entry['ogrn'] == ogrn for entry in self._data):
            raise ValueError('огрн должен быть уникальным!')
        self._data.append(new_entity)

    def replace_by_id(self, supplier_id, name=None, address=None, phone=None, ogrn=None):
        entity = self.get_by_id(supplier_id)
        if not entity:
            raise ValueError(f"Элемент с ID {supplier_id} не найден.")
        if ogrn and ogrn != entity['ogrn'] and any(entry['ogrn'] == ogrn and entry['supplier_id'] != supplier_id for entry in self._data):
            raise ValueError("ОГРН должен быть уникальным!")
        if supplier_id:
            entity['supplier_id']=supplier_id
        if name:
            entity['name']=name
        if address:
            entity['address']=address
        if phone:
            entity['phone']=phone
        if ogrn:
            entity['ogrn']=ogrn   

    def delete_by_id(self, supplier_id):
            entity = self.get_by_id(supplier_id)
            if not entity:
                raise ValueError(f"Элемент с ID {supplier_id} не найден.")
            self._data.remove(entity)

    def get_count(self):
            return len(self._data)
    