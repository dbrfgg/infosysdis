from Supplier_rep_file import SupplierRepFile

class SupplierRepFileAdapter:
    
    def __init__(self, supplier_rep_file: SupplierRepFile):
        supplier_rep_file.read_data_from_file()
        self._supplier_rep_file = supplier_rep_file
    
    def get_k_n_short_list(self, k, n):
        return self._supplier_rep_file.get_k_n_short_list(k, n)
    
    def get_by_id(self, id):
        return self._supplier_rep_file.get_by_id(id)
    
    def delete_by_id(self, id):
        self._supplier_rep_file.delete_by_id(id)
        self._supplier_rep_file.write_data_to_file()
    
    def replace_by_id(self, entity_id, name, address, phone, ogrn):
        self._supplier_rep_file.replace_by_id(entity_id, name, address, phone, ogrn)
        self._supplier_rep_file.write_data_to_file()
    
    def add_entity(self, name, address, phone, ogrn):
        self._supplier_rep_file.add_entity(name, address, phone, ogrn)
        self._supplier_rep_file.write_data_to_file()
    
    def get_count(self):
        return self._supplier_rep_file.get_count()