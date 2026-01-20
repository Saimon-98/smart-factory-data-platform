from collections import defaultdict
from datetime import date

def transform_data(rows):
    """
    Aggrega i dati e applica controlli di qualità
    """
    result = defaultdict(lambda: {"prod": 0, "scrap": 0})

    for r in rows:
        production_date, plant, line, produced_qty, scrap_qty = r

        # Controlli qualità
        if produced_qty < 0 or scrap_qty < 0:
            continue

        if production_date > date.today():
            continue

        if scrap_qty > produced_qty:
            continue

        key = (production_date, plant, line)
        result[key]["prod"] += produced_qty
        result[key]["scrap"] += scrap_qty

    return result