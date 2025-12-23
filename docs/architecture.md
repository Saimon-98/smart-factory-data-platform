# Architettura Cloud – Smart Factory Data Platform

Questo documento descrive la versione cloud prevista del progetto,
simulando un contesto industriale reale.

## Componenti

### Database
- PostgreSQL containerizzato localmente
- In cloud: Amazon RDS (relational database managed service)

### ETL
- Script Python eseguiti su AWS Lambda
- Orchestrazione tramite AWS Step Functions (concettuale)

### Storage Storico
- Amazon S3 come data lake per dati raw, cleansed e curated

### Logging e Monitoring
- CloudWatch per monitorare esecuzione ETL e pipeline
- Alert automatici per errori o degrado performance

## Nota
Tutte le componenti cloud sono descritte concettualmente,
l’implementazione reale avverrà in fase avanzata o in produzione.
