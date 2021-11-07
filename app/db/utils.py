def row_to_dict(row) -> dict:
    """Костыль, но по-другому не получилось"""
    items = {}

    keys = [k for k in row.keys()]
    values = [v for v in row.values()]

    for i in range(len(keys)):
        items[keys[i]] = values[i]

    return items
