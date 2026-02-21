def predict(values: list):
    # Retornar valor fictício baseado na média
    if not values:
        return 1.0
    return round(sum(values)/len(values), 2)
