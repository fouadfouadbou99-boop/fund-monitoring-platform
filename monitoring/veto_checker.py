class VetoChecker:

    def __init__(self, reporting):

        self.reporting = reporting

    def run(self):

        alerts = []

        decisions = self.reporting.get(
            "decisions_importantes",
            []
        )

        veto_keywords = [

            "cession",

            "augmentation capital",

            "emprunt",

            "fusion",

            "liquidation",

            "modification règlement",

            "changement stratégie",

            "cession actif"

        ]

        for decision in decisions:

            decision_lower = decision.lower()

            for keyword in veto_keywords:

                if keyword in decision_lower:

                    alerts.append({

                        "decision": decision,

                        "controle":
                        "Veto Promoteur",

                        "statut":
                        "VALIDATION REQUISE"

                    })

        return alerts
