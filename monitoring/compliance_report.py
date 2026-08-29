def generate_compliance_report(results):

    report = []

    report.append("CONTROLE DU REGLEMENT DE GESTION")
    report.append("")

    non_conformes = 0

    for item in results:

        report.append(

            f"{item['regle']} : "
            f"{item['statut']}"

        )

        if item["statut"] == "NON CONFORME":
            non_conformes += 1

    report.append("")
    report.append(
        f"Nombre de non-conformités : {non_conformes}"
    )

    return "\n".join(report)
