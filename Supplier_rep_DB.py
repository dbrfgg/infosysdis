from DBconnection import DBconnection

class SupplierRepDB:
    
    def __init__(self, db_config):
        self.db = DBconnection(db_config)
    
    def get_by_id(self, supplier_id):
        cursor = self.db.get_cursor()
        cursor.execute("SELECT * FROM supplier WHERE id = %s", (supplier_id,))
        result = cursor.fetchone()
        cursor.close()
        return result
    
    def get_k_n_short_list(self, k, n):
        cursor = self.db.get_cursor()
        offset = (n - 1) * k  
        cursor.execute("""
            SELECT id, name, phone, ogrn FROM supplier
            ORDER BY id LIMIT %s OFFSET %s
        """, (k, offset))  
        result = cursor.fetchall()
        cursor.close()
        return result


    def add(self, name, address, phone, ogrn):
        with self.db.get_cursor() as cursor:
            cursor.execute("""
                INSERT INTO supplier (name, address, phone, ogrn)
                VALUES (%s, %s, %s, %s)
                RETURNING id
            """, (name, address, phone, ogrn))
            
            supplier_id = cursor.fetchone()[0]
        
        return supplier_id

   
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

        if not fields:
            raise ValueError("Нет данных для обновления!")

        values.append(supplier_id)
        cursor = self.db.get_cursor()
        cursor.execute(f"""
            UPDATE supplier
            SET {', '.join(fields)}
            WHERE id = %s
        """, tuple(values))
        cursor.close()
    
    def delete_by_id(self, supplier_id):
        cursor = self.db.get_cursor()
        cursor.execute("DELETE FROM supplier WHERE id = %s", (supplier_id,))
        cursor.close()

    def get_count(self):
        cursor = self.db.get_cursor()
        cursor.execute("SELECT COUNT(*) FROM supplier")
        result = cursor.fetchone()
        cursor.close()
        return result[0]

    

