from datetime import date


def tage_bis(zieldatum: date) -> int:
    return (zieldatum - date.today()).days


print(tage_bis(date(2027, 12, 31)))
