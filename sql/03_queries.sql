-- Indici per migliorare le query di lettura
CREATE INDEX IF NOT EXISTS idx_raw_date
ON production_raw(production_date);

CREATE INDEX IF NOT EXISTS idx_raw_plant
ON production_raw(plant);