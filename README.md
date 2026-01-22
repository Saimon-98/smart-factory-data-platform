# Smart Factory Data Platform

## Scenario

Questo progetto simula una **piattaforma dati per uno stabilimento manifatturiero** (es. settore automotive).
Lo stabilimento produce pneumatici su diverse linee e macchine.

Il database operativo raccoglie dati giornalieri di:
- quantità prodotte
- quantità di scarti
- stabilimento e linea di produzione

Il business richiede una vista analitica per:
- analizzare produzione e scarti nel tempo
- confrontare stabilimenti e linee
- supportare decisioni operative e di qualità

---

## Architettura

### Versione locale (sviluppo)
- PostgreSQL (Docker)
- Python ETL
- Logging su file

### Versione cloud (concettuale)
- Database → Amazon RDS (PostgreSQL)
- ETL → AWS Lambda o EC2
- Logging & Monitoring → Amazon CloudWatch
- Storage storico → Amazon S3

Questa architettura è pensata per essere **scalabile e pronta per produzione**, pur essendo implementata localmente.

---

## Flusso ETL

1. **Extract**
   - Estrazione dei dati dalla tabella `production_raw`
   - Dati operativi non aggregati

2. **Transform**
   - Aggregazione per:
     - data di produzione
     - stabilimento
     - linea
   - Controlli di qualità dati:
     - valori negativi
     - date future
     - scarti maggiori della produzione
   - I record non validi vengono scartati e loggati

3. **Load**
   - Caricamento dei dati aggregati nella tabella `production_fact`
   - Inserimento del timestamp di caricamento

---

## Database

### Tabella sorgente (operativa)
`production_raw`
- dati granulari di produzione

### Tabella target (analitica)
`production_fact`
- dati aggregati per analisi e reporting

Sono stati creati **indici SQL** sulle colonne più utilizzate (data, stabilimento) per migliorare le performance.

---

## 📋 Logging & Monitoring

- Logging implementato in Python
- Tracciate tutte le fasi dell’ETL:
  - avvio
  - righe estratte
  - righe aggregate
  - record scartati
  - errori
- Simulazione del comportamento di **Amazon CloudWatch**

---

## ⚠️ Problemi incontrati

- Gestione di dati sporchi e incoerenti
- Evitare duplicazioni in caso di rilanci dell’ETL
- Rendere l’ETL osservabile senza interrompere il flusso

Questi problemi sono stati affrontati con:
- controlli di qualità
- logging dettagliato
- separazione tra dati raw e dati analitici

---

## 🚀 Miglioramenti futuri

- ETL incrementale basato su timestamp
- Ingestione real-time con **Kafka**
- Elaborazioni distribuite con **Spark**
- Persistenza dei dati storici su **Amazon S3**
- Dashboard BI per analisi avanzate

---

## 🧠 Competenze dimostrate

- SQL e ottimizzazione query
- ETL design
- Data quality checks
- Python scripting
- Logging e monitoring
- Architettura cloud (concettuale)
