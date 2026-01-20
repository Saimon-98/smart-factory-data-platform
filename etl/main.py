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
        transformed, rejected = transform_data(rows)
        print(f"Transformed into {len(transformed)} aggregated rows")
        print(f"Rejected rows: {len(rejected)}")

        # (opzionale) Mostra esempi di scarti (i primi 5 elementi)
        for r, reason in rejected[:5]:
            print(f"Rejected {r} → {reason}")

        # Load
        load_data(conn, transformed)
        print("Load completed successfully")

    finally:
        conn.close()

if __name__ == "__main__":
    main()
