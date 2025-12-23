import psycopg2
from extract import extract_data
from transform import transform_data
from load import load_data

def main():
    # Connessione DB
    conn = psycopg2.connect(
        host="localhost",
        port=5433,
        database="factory_db",
        user="factory_user",
        password="factory_pwd"
    )

    try:
        # Extract
        rows = extract_data(conn)
        print(f"Extracted {len(rows)} rows")

        # Transform
        transformed = transform_data(rows)
        print(f"Transformed into {len(transformed)} aggregated rows")

        # Load
        load_data(conn, transformed)
        print("Load completed successfully")

    finally:
        conn.close()

if __name__ == "__main__":
    main()
