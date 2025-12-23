import psycopg2

def extract_data(conn):
    query = """
    SELECT production_date, plant, line,
           produced_qty, scrap_qty
    FROM production_raw;
    """
    cur = conn.cursor()
    cur.execute(query)
    rows = cur.fetchall()
    cur.close()
    return rows
