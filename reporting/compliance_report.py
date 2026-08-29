from datetime import datetime


def generate_compliance_report(
    fund_name,
    results
):

    report = []

    report.append(
        "RAPPORT DE CONFORMITE"
    )

    report.append(
        f"Fonds : {fund_name}"
    )

    report.append(
        f"Date : {datetime.today().date()}"
    )

    report.append("")

    total = len(results)

    nc = sum(

        1

        for r in results

        if r["statut"]
        in [
            "NON CONFORME",
            "VALIDATION REQUISE"
        ]
    )

    report.append(
        f"Contrôles réalisés : {total}"
    )

    report.append(
        f"Points à surveiller : {nc}"
    )

    report.append("")

    for r in results:

        report.append(

            f"[{r['statut']}] "
            f"{r['controle']}"

        )

    return "\n".join(report)
