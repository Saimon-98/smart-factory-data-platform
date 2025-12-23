## Database Setup

Il database PostgreSQL è avviato tramite Docker Compose.

**Dettagli:**
- Image: postgres:15
- Database: factory_db
- User: factory_user
- Porta: 5433

Il database è utilizzato come sorgente e target per le pipeline ETL.

## Python Environment

Il progetto utilizza un ambiente virtuale Python con le seguenti dipendenze:
- psycopg2-binary per la connessione a PostgreSQL

Le dipendenze sono versionate tramite requirements.txt.