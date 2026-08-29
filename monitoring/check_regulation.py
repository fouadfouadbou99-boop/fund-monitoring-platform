class RegulationChecker:

    def __init__(self, rules, reporting):

        self.rules = rules
        self.reporting = reporting

        self.results = []

    def check(self):

        self.check_max_exposure()

        self.check_debt_ratio()

        self.check_occupancy_rate()

        self.check_investment_period()

        return self.results

    def add_result(
        self,
        rule_name,
        expected,
        actual,
        status,
        message
    ):

        self.results.append({

            "regle": rule_name,

            "valeur_attendue": expected,

            "valeur_constatee": actual,

            "statut": status,

            "message": message

        })

    def check_max_exposure(self):

        limit = self.rules.get("max_exposure")

        actual = self.reporting.get("max_position_weight")

        if limit is None or actual is None:
            return

        status = "CONFORME"

        if actual > limit:
            status = "NON CONFORME"

        self.add_result(

            "Exposition maximale",

            limit,

            actual,

            status,

            f"Limite {limit}% / constaté {actual}%"

        )

    def check_debt_ratio(self):

        limit = self.rules.get("max_debt_ratio")

        actual = self.reporting.get("debt_ratio")

        if limit is None or actual is None:
            return

        status = "CONFORME"

        if actual > limit:
            status = "NON CONFORME"

        self.add_result(

            "Ratio d'endettement",

            limit,

            actual,

            status,

            f"Limite {limit}% / constaté {actual}%"

        )

    def check_occupancy_rate(self):

        minimum = self.rules.get("min_occupancy")

        actual = self.reporting.get("taux_occupation")

        if minimum is None or actual is None:
            return

        status = "CONFORME"

        if actual < minimum:
            status = "NON CONFORME"

        self.add_result(

            "Taux d'occupation",

            minimum,

            actual,

            status,

            f"Minimum {minimum}% / constaté {actual}%"

        )

    def check_investment_period(self):

        maximum = self.rules.get("max_investment_period")

        actual = self.reporting.get("investment_period")

        if maximum is None or actual is None:
            return

        status = "CONFORME"

        if actual > maximum:
            status = "NON CONFORME"

        self.add_result(

            "Période d'investissement",

            maximum,

            actual,

            status,

            f"Maximum {maximum} ans / constaté {actual} ans"

        )
