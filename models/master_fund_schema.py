from pydantic import BaseModel
from typing import Optional, List, Dict


class MasterFundSchema(BaseModel):

    #################################################################
    # IDENTIFICATION
    #################################################################

    nom_fonds: Optional[str] = None

    type_fonds: Optional[str] = None

    strategie: Optional[str] = None

    societe_gestion: Optional[str] = None

    promoteur: Optional[str] = None

    depositaire: Optional[str] = None

    commissaire_aux_comptes: Optional[str] = None

    devise: Optional[str] = None

    date_creation: Optional[str] = None

    date_reporting: Optional[str] = None

    maturite_fonds: Optional[str] = None

    #################################################################
    # LEVEE ET ENGAGEMENTS
    #################################################################

    taille_cible: Optional[float] = None

    taille_fonds: Optional[float] = None

    montant_engage: Optional[float] = None

    capital_appele: Optional[float] = None

    capital_non_appele: Optional[float] = None

    taux_appel: Optional[float] = None

    #################################################################
    # PERFORMANCE PRIVATE EQUITY
    #################################################################

    tri_brut: Optional[float] = None

    tri_net: Optional[float] = None

    tvpi: Optional[float] = None

    dpi: Optional[float] = None

    rvpi: Optional[float] = None

    moic: Optional[float] = None

    cash_return_ratio: Optional[float] = None

    #################################################################
    # VALORISATION
    #################################################################

    valeur_liquidative: Optional[float] = None

    actif_net: Optional[float] = None

    valeur_portefeuille: Optional[float] = None

    plus_values_latentes: Optional[float] = None

    moins_values_latentes: Optional[float] = None

    #################################################################
    # INVESTISSEMENTS
    #################################################################

    nombre_participations: Optional[int] = None

    nombre_investissements: Optional[int] = None

    nombre_desinvestissements: Optional[int] = None

    investissements_realises: List[str] = []

    desinvestissements_realises: List[str] = []

    principales_participations: List[str] = []

    #################################################################
    # CONCENTRATION
    #################################################################

    exposition_plus_grande_position: Optional[float] = None

    exposition_top_5: Optional[float] = None

   
