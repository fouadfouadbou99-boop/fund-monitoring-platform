class CapitalCallChecker:

    def __init__(self, reporting):

        self.reporting = reporting

    def run(self):

        results = []

        engagement = self.reporting.get(
            "montant_engage"
        )

        appele = self.reporting.get(
            "capital_appele"
        )

        if engagement is None or appele is None:
            return results

        ratio = (
            appele /
            engagement
        ) * 100

        results.append({

            "controle":
            "Taux d'appel",

            "ratio":
            round(ratio, 2),

            "statut":
            "NORMAL"
            if ratio < 90
            else "SURVEILLANCE"

        })

        return results
