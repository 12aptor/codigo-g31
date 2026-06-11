import psycopg2

DATABASE_CONFIG = {
    'dbname': 'flask-postgresql',
    'user': 'postgres',
    'password': 'root',
    'host': 'localhost',
    'port': 5432
}

def get_db_connection():
    conn = psycopg2.connect(**DATABASE_CONFIG)
    return conn

def create_user_table():
    conn = None

    try:
        conn = get_db_connection()

        with conn:
            with conn.cursor() as cursor:
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS users (
                        id SERIAL PRIMARY KEY,
                        name VARCHAR(255) NOT NULL,
                        email VARCHAR(255) NOT NULL UNIQUE,
                        password TEXT NOT NULL,
                        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    )
                ''')
        print('Table created successfully')
    except Exception as e:
        print(f'Error creating table: {e}')
    finally:
        if conn is not None:
            conn.close()