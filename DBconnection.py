import psycopg2
class DBconnection:
    
    _instance = None
    
    def __new__(cls, db_config):
        if cls._instance is None:
            cls._instance = super(DBconnection, cls).__new__(cls)
            cls._instance._initialize(db_config)
        return cls._instance
    
    def _initialize(self, db_config):
        self.connection = psycopg2.connect(
            dbname=db_config['dbname'],
            user=db_config['user'],
            password=db_config['password'],
            host=db_config['host'],
            port=db_config['port']
        )
        self.connection.autocommit = True
        self.ensure_table_exists()
    
    def get_cursor(self):
        return self.connection.cursor()
    
    def table_exists(self, table_name):
        with self.get_cursor() as cursor:
            cursor.execute("""
                SELECT EXISTS (
                    SELECT 1
                    FROM pg_catalog.pg_tables
                    WHERE tablename = %s
                );
            """, (table_name,))
            result = cursor.fetchone()
        return result[0]
    
    def ensure_table_exists(self):
        if not self.table_exists("supplier"):
            with self.get_cursor() as cursor:
                cursor.execute("""
                    CREATE TABLE supplier (
                        id UUID PRIMARY KEY,
                        name VARCHAR(50) NOT NULL,
                        address VARCHAR(50) NOT NULL,
                        phone VARCHAR(15) NOT NULL,
                        ogrn VARCHAR(15) NOT NULL
                    );
                """)
                print("Таблица 'supplier' успешно создана.")
        else:
            print("Таблица 'supplier' уже существует.")
