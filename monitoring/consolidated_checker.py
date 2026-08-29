from monitoring.quota_checker import QuotaChecker
from monitoring.capital_call_checker import CapitalCallChecker
from monitoring.distribution_checker import DistributionChecker
from monitoring.veto_checker import VetoChecker
from monitoring.covenant_checker import CovenantChecker


class ConsolidatedChecker:

    def __init__(self, rules, reporting):

        self.rules = rules
        self.reporting = reporting

    def run_all_controls(self):

        results = []

        results.extend(

            QuotaChecker(
                self.rules,
                self.reporting
            ).check_sector_limits()
        )

        results.extend(

            QuotaChecker(
                self.rules,
                self.reporting
            ).check_geographic_limits()
        )

        results.extend(

            CapitalCallChecker(
                self.reporting
            ).run()
        )

        results.extend(

            DistributionChecker(
                self.rules,
                self.reporting
            ).run()
        )

        results.extend(

            CovenantChecker(
                self.rules,
                self.reporting
            ).run()
        )

        results.extend(

            VetoChecker(
                self.reporting
            ).run()
        )

        return results
