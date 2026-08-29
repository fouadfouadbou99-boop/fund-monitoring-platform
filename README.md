# Fund Monitoring Platform

## Description

Fund Monitoring Platform est une application développée en Python et Streamlit permettant d'automatiser le suivi des fonds de Capital Investissement, OPCI et autres véhicules d'investissement.

La plateforme extrait automatiquement les informations contenues dans les reportings, règlements de gestion, pactes d'actionnaires et autres documents de suivi afin de produire :

- Des fiches synthétiques des fonds
- Des indicateurs de performance
- Des tableaux de bord consolidés
- Des alertes automatiques
- Des contrôles de conformité
- Des rapports de monitoring institutionnels

Cette solution est particulièrement adaptée aux investisseurs institutionnels, caisses de retraite, assurances, fonds souverains et sociétés de gestion.

---

## Fonctionnalités

### Extraction documentaire

Prise en charge :

- PDF
- DOCX

Extraction automatique :

- Informations générales
- Performance
- Portefeuille
- Gouvernance
- Risques
- Alertes

---

### Suivi des fonds de Capital Investissement

Extraction des indicateurs :

- TRI
- TVPI
- DPI
- RVPI
- MOIC
- Valeur liquidative
- Valorisation portefeuille
- Capital appelé
- Capital non appelé

---

### Suivi OPCI

Extraction :

- Valeur expertise
- Valeur des actifs immobiliers
- Taux d'occupation
- LTV
- Endettement
- Loyers facturés
- Loyers recouvrés
- Vacance locative
- Distributions

---

### Gouvernance

Analyse automatique de :

- Conseils d'administration
- Comités
- Assemblées Générales
- Décisions importantes
- Restructurations
- Acquisitions
- Cessions

---

### Contrôle de conformité

Contrôles automatiques :

- Limites d'endettement
- Quotas sectoriels
- Quotas géographiques
- Exposition maximale
- Distribution minimale
- Respect du règlement de gestion
- Respect du pacte d'actionnaires

---

### Contrôle des droits de veto

Détection automatique des décisions stratégiques nécessitant l'approbation du promoteur :

- Cession d'actifs
- Modification du règlement
- Changement de stratégie
- Emprunts
- Fusion
- Liquidation

---

### Alertes

Génération automatique d'alertes :

- Baisse du TRI
- Baisse de valorisation
- Vacance locative excessive
- Dépassement des limites réglementaires
- Non-conformité

---

## Architecture du projet

```text
fund-monitoring-platform/

├── app.py

├── ai/
│   ├── extractor.py
│   ├── prompts.py
│   ├── extract_regulation.py
│   └── regulation_prompt.py

├── extraction/
│   ├── pdf_reader.py
│   └── docx_reader.py

├── monitoring/
│   ├── alert_engine.py
│   ├── rules_engine.py
│   ├── quota_checker.py
│   ├── capital_call_checker.py
│   ├── distribution_checker.py
│   ├── covenant_checker.py
│   ├── veto_checker.py
│   ├── check_regulation.py
│   └── consolidated_checker.py

├── reporting/
│   ├── note_generator.py
│   └── compliance_report.py

├── models/
│   ├── fund_schema.py
│   └── master_fund_schema.py

├── database/
│   └── database.py

├── utils/
│   └── parser.py

├── data/

├── pages/
│   ├── dashboard.py
│   ├── fonds.py
│   └── alertes.py

├── requirements.txt

├── .env

└── README.md
