import psycopg2
import uuid
from DBconnection import DBconnection

class SupplierRepDB:
    
    def __init__(self, db_config):
        self.db = DBconnection(db_config)
    
    def get_by_id(self, supplier_id):
        with self.db.get_cursor() as cursor:
            cursor.execute("SELECT * FROM supplier WHERE id = %s", (supplier_id,))
            result = cursor.fetchone()
        return result
    
    def get_k_n_short_list(self, k, n):
        with self.db.get_cursor() as cursor:
            offset = k * (n - 1)
            cursor.execute("""
                SELECT id, name, phone, ogrn FROM supplier
                ORDER BY id LIMIT %s OFFSET %s
            """, (k, offset))
            result = cursor.fetchall()
        return result
    
    def add(self, name, address, phone, ogrn):
        new_id = str(uuid.uuid4())
        with self.db.get_cursor() as cursor:
            cursor.execute("""
                INSERT INTO supplier (id, name, address, phone, ogrn)
                VALUES (%s, %s, %s, %s, %s)
            """, (new_id, name, address, phone, ogrn))
        return new_id
   
    def update_by_id(self, supplier_id, name=None, address=None, phone=None, ogrn=None):
        fields = []
        values = []
        if name is not None:
            fields.append("name = %s")
            values.append(name)
        if address is not None:
            fields.append("address = %s")
            values.append(address)
        if phone is not None:
            fields.append("phone = %s")
            values.append(phone)
        if ogrn is not None:
            fields.append("ogrn = %s")
            values.append(ogrn)
        values.append(supplier_id)
        with self.db.get_cursor() as cursor:
            cursor.execute(f"""
                UPDATE supplier
                SET {', '.join(fields)}
                WHERE id = %s
            """, tuple(values))
    
    def delete_by_id(self, supplier_id):
        with self.db.get_cursor() as cursor:
            cursor.execute("DELETE FROM supplier WHERE id = %s", (supplier_id,))
    def get_count(self):
        with self.db.get_cursor() as cursor:
            cursor.execute("SELECT COUNT(*) FROM supplier")
            result = cursor.fetchone()
        return result[0]
    

