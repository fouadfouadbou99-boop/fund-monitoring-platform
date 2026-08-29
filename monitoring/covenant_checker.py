class CovenantChecker:

    def __init__(self, rules, reporting):

        self.rules = rules
        self.reporting = reporting

    def run(self):

        results = []

        max_debt = self.rules.get(
            "max_debt_ratio"
        )

        debt = self.reporting.get(
            "endettement"
        )

        if debt is None:
            return results

        results.append({

            "controle":
            "Endettement OPCI",

            "limite":
            max_debt,

            "constate":
            debt,

            "statut":
            "CONFORME"
            if debt <= max_debt
            else "NON CONFORME"

        })

        return results
