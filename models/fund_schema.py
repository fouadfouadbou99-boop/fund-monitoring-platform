from pydantic import BaseModel
from typing import List, Optional


class FundSchema(BaseModel):

    # Informations générales

    nom_fonds: Optional[str]
    type_fonds: Optional[str]

    societe_gestion: Optional[str]
    depositaire: Optional[str]

    date_creation: Optional[str]
    date_reporting: Optional[str]

    devise: Optional[str]

    # Taille

    taille_fonds: Optional[float]

    montant_engage: Optional[float]
    capital_appele: Optional[float]
    capital_non_appele: Optional[float]

    # Performance

    tri: Optional[float]

    tvpi: Optional[float]

    dpi: Optional[float]

    rvpi: Optional[float]

    moic: Optional[float]

    # Valorisation

    valeur_liquidative: Optional[float]

    valorisation_portefeuille: Optional[float]

    actif_net: Optional[float]

    # Portefeuille

    nombre_participations: Optional[int]

    investissements: List[str] = []

    desinvestissements: List[str] = []

    principales_positions: List[str] = []

    # Gouvernance

    comites: List[str] = []

    conseils: List[str] = []

    assemblees: List[str] = []

    decisions_importantes: List[str] = []

    # Risques

    risques: List[str] = []

    alertes: List[str] = []

    # OPCI

    valeur_expertise: Optional[float]

    taux_occupation: Optional[float]

    vacance_locative: Optional[float]

    loyers_factures: Optional[float]

    loyers_recouvres: Optional[float]

    duree_residuelle_baux: Optional[float]

    endettement: Optional[float]

    distribution: Optional[float]
