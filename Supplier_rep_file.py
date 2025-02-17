import os
from Supplier_rep_File_Strategy import SupplierRepFileStrategy

class SupplierRepFile:

    def __init__(self, strategy: SupplierRepFileStrategy):
        self.strategy = strategy

    def get_all(self):
        """Получить все элементы"""
        return self.strategy.read()

    def get_by_id(self, supplier_id):
        data = self.strategy.read()
        for entry in data:
            if entry['supplier_id'] == supplier_id:
                return entry
        return None

    def get_k_n_short_list(self, k, n):
        data = self.strategy.read()
        start = (n - 1) * k
        end = start + k
        return data[start:end]

    def sort_by_field(self, field):
        data = self.strategy.read()
        if field in ["name", "address", "phone", "ogrn"]:
            data.sort(key=lambda x: x.get(field))
        return data

    def add_entity(self, name, address, phone, ogrn):
        data = self.strategy.read()
        new_id = (max((entry['supplier_id'] for entry in data), default=0) + 1)
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
        self.strategy.write(data)

    def replace_by_id(self, supplier_id, name=None, address=None, phone=None, ogrn=None):
        data = self.strategy.read()
        entity = self.get_by_id(supplier_id)
        if not entity:
            raise ValueError(f"Элемент с ID {supplier_id} не найден.")
        if ogrn and ogrn != entity['ogrn'] and any(entry['ogrn'] == ogrn and entry['supplier_id'] != supplier_id for entry in data):
            raise ValueError("ОГРН должен быть уникальным!")
        updated_entity = {
            'supplier_id': supplier_id,
            'name': name if name else entity['name'],
            'address': address if address else entity['address'],
            'phone': phone if phone else entity['phone'],
            'ogrn': ogrn if ogrn else entity['ogrn']
        }
        for i, entry in enumerate(data):
            if entry['supplier_id'] == supplier_id:
                data[i] = updated_entity
                break
        self.strategy.write(data)


    def delete_by_id(self, supplier_id):
            data = self.strategy.read()
            entity = self.get_by_id(supplier_id)
            if not entity:
                raise ValueError(f"Элемент с ID {supplier_id} не найден.")
            data.remove(entity)
            self.strategy.write(data)

    def get_count(self):
            data = self.strategy.read()
            return len(data)
    

from Supplier_rep_json import SupplierRepJson
from Supplier_rep_file import SupplierRepFile

if __name__ == "__main__":
    filename = "test_suppliers.json"
    strategy = SupplierRepJson(filename)
    repo = SupplierRepFile(strategy)

    # Очистим файл перед тестами
    #strategy.write([])

    #print("\n Добавляем поставщиков")
    #repo.add_entity("Supplier C", "Street C", "123459999", "11161")
    #repo.add_entity("Supplier D", "Street D", "987654888", "22282")
    #print("Все поставщики:", repo.get_all())

    #print("\n Получаем поставщика с ID 1")
    #print(repo.get_by_id(1))

    #print("\n Обновляем данные поставщика с ID 1")
    #repo.replace_by_id(3, name="Updated Supplier A", address="New Address")
    #print(repo.get_by_id(3))

    #print("\n🗑 Удаляем поставщика с ID 3")
    #repo.delete_by_id(3)
    #print("Все поставщики после удаления:", repo.get_all())

    ##print("\n Общее количество поставщиков:", repo.get_count())

    #print("\n Проверяем добавление дублирующего ОГРН")
    #try:
        #repo.add_entity("Supplier C", "Street C", "555555555", "11111")  # Дублирующий ОГРН
    #except ValueError as e:
        #print("Ошибка:", e)

    #print("\n Проверяем сортировку по имени")
    #repo.add_entity("Supplier D", "Street D", "777777777", "44444")
    #repo.add_entity("Supplier E", "Street E", "888888888", "55555")
    #sorted_list = repo.sort_by_field("name")
    #print("Отсортированные поставщики:", sorted_list)

    #print("\n Получаем 2 элемента начиная с 1-го")
    #print(repo.get_k_n_short_list(2, 1))









1