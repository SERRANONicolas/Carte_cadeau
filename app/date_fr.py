WEEKDAYS = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]
MONTHS = [
    "Janvier", "Février", "Mars", "Avril", "Mai", "Juin",
    "Juillet", "Août", "Septembre", "Octobre", "Novembre", "Décembre",
]


def date_fr_parts(d):
    if d is None:
        return None
    return {
        "weekday": WEEKDAYS[d.weekday()],
        "day": d.day,
        "month": MONTHS[d.month - 1],
        "year": d.year,
    }


def date_fr_full(d):
    if d is None:
        return None
    p = date_fr_parts(d)
    return f"{p['weekday']} {p['day']:02d} {p['month']} {p['year']}"
