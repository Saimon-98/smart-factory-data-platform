-- Tabella sorgente: dati operativi di produzione
CREATE TABLE production_raw (
    id SERIAL PRIMARY KEY,
    plant VARCHAR(50),
    line VARCHAR(50),
    machine_id VARCHAR(50),
    production_date DATE,
    produced_qty INT,
    scrap_qty INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabella analitica: dati aggregati per analisi KPI
CREATE TABLE production_fact (
    production_date DATE,
    plant VARCHAR(50),
    line VARCHAR(50),
    total_produced INT,
    total_scrap INT,
    load_timestamp TIMESTAMP
);
