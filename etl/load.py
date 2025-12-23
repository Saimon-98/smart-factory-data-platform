def load_data(conn, transformed):
    cur = conn.cursor()
    cur.execute("TRUNCATE TABLE production_fact;")
    for key, values in transformed.items():
        cur.execute("""
            INSERT INTO production_fact
            (production_date, plant, line, total_produced, total_scrap, load_timestamp)
            VALUES (%s,%s,%s,%s,%s,NOW())
        """, (*key, values["prod"], values["scrap"]))
    conn.commit()
    cur.close()
