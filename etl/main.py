import psycopg2
from extract import extract_data
from transform import transform_data
from load import load_data
import logging

# Configurazione logging
logging.basicConfig(
    filename="logs/etl.log",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

def main():
    logging.info("ETL started")
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
        logging.info(f"Extracted {len(rows)} rows")

        # Transform
        transformed, rejected = transform_data(rows)
        logging.info(f"Transformed into {len(transformed)} aggregated rows")
        logging.info(f"Rejected rows: {len(rejected)}")

        # (opzionale) Mostra esempi di scarti (i primi 5 elementi)
        for r, reason in rejected[:5]:
            logging.warning(f"Rejected {r} → {reason}")

        # Load
        load_data(conn, transformed)
        logging.info("Load completed successfully")

    except Exception as e:
        logging.error(f"ETL failed: {e}")
        raise

    finally:
        conn.close()
        logging.info("ETL finished\n")

if __name__ == "__main__":
    main()
