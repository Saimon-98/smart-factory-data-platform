import psycopg2

conn = psycopg2.connect(
    host="localhost",
    port=5433,
    database="factory_db",
    user="factory_user",
    password="factory_pwd"
)

cur = conn.cursor()
cur.execute("SELECT 1;")
print("Database connection OK")

cur.close()
conn.close()
