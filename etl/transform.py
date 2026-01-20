from collections import defaultdict
from datetime import date

def transform_data(rows):
    """
    Aggrega i dati e applica controlli di qualità
    """
    result = defaultdict(lambda: {"prod": 0, "scrap": 0})
    rejected = []

    for r in rows:
        production_date, plant, line, produced_qty, scrap_qty = r

        # Controlli qualità
        if produced_qty < 0 or scrap_qty < 0:
            rejected.append((r, "NEGATIVE_VALUES"))
            continue

        if production_date > date.today():
            rejected.append((r, "FUTURE_DATE"))
            continue

        if scrap_qty > produced_qty:
            rejected.append((r, "SCRAP_GT_PRODUCTION"))
            continue

        key = (production_date, plant, line)
        result[key]["prod"] += produced_qty
        result[key]["scrap"] += scrap_qty

    return result, rejected