def generate_alerts(data):

    alerts = []

    tri = data.get("tri")
    occupation = data.get("taux_occupation")
    vacance = data.get("vacance_locative")
    tvpi = data.get("tvpi")

    if tri is not None and tri < 5:
        alerts.append("TRI inférieur à 5%")

    if tvpi is not None and tvpi < 1:
        alerts.append("TVPI inférieur à 1")

    if occupation is not None and occupation < 90:
        alerts.append("Taux d'occupation inférieur à 90%")

    if vacance is not None and vacance > 10:
        alerts.append("Vacance locative supérieure à 10%")

    return alerts
