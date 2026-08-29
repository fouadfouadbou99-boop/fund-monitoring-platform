class QuotaChecker:

    def __init__(self, rules, reporting):

        self.rules = rules
        self.reporting = reporting

    def check_sector_limits(self):

        results = []

        sector_limit = self.rules.get(
            "sector_limit"
        )

        portfolio = self.reporting.get(
            "sector_breakdown",
            {}
        )

        for sector, weight in portfolio.items():

            results.append({

                "controle":
                f"Quota secteur {sector}",

                "limite":
                sector_limit,

                "constate":
                weight,

                "statut":
                "CONFORME"
                if weight <= sector_limit
                else "NON CONFORME"

            })

        return results

    def check_geographic_limits(self):

        results = []

        geo_limit = self.rules.get(
            "geographic_limit"
        )

        geography = self.reporting.get(
            "geographic_breakdown",
            {}
        )

        for zone, weight in geography.items():

            results.append({

                "controle":
                f"Quota géographique {zone}",

                "limite":
                geo_limit,

                "constate":
                weight,

                "statut":
                "CONFORME"
                if weight <= geo_limit
                else "NON CONFORME"

            })

        return results
