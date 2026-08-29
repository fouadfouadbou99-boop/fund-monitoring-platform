class DistributionChecker:

    def __init__(self, rules, reporting):

        self.rules = rules
        self.reporting = reporting

    def run(self):

        results = []

        minimum = self.rules.get(
            "minimum_distribution"
        )

        actual = self.reporting.get(
            "distribution"
        )

        if minimum is None or actual is None:
            return results

        results.append({

            "controle":
            "Distribution minimale",

            "attendu":
            minimum,

            "constate":
            actual,

            "statut":
            "CONFORME"
            if actual >= minimum
            else "NON CONFORME"

        })

        return results
