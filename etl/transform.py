from collections import defaultdict

def transform_data(rows):
    """
    Aggrega quantità prodotte e scarti per data, plant e line
    """
    result = defaultdict(lambda: {"prod": 0, "scrap": 0})

    for r in rows:
        key = (r[0], r[1], r[2])  # (data, stabilimento, linea)
        result[key]["prod"] += r[3]
        result[key]["scrap"] += r[4]

    return result