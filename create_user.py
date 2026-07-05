import psycopg2

try:
    conn = psycopg2.connect(
        host='localhost',
        user='postgres',
        password='odoo'
    )
    conn.autocommit = True
    cur = conn.cursor()
    cur.execute("CREATE USER odoo WITH PASSWORD 'odoo' CREATEDB;")
    print('? User odoo created successfully!')
    conn.close()
except Exception as e:
    print(f'Error: {e}')
    print('User odoo may already exist')
