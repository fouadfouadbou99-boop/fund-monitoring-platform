def generate_note(data):

    note = f"""

FONDS : {data.get('nom_fonds')}

Date du reporting :
{data.get('date_reporting')}

------------------------------------------------

PERFORMANCE

TRI : {data.get('tri')}
TVPI : {data.get('tvpi')}
DPI : {data.get('dpi')}
RVPI : {data.get('rvpi')}

------------------------------------------------

PORTEFEUILLE

Nombre de participations :
{data.get('nombre_participations')}

------------------------------------------------

GOUVERNANCE

{chr(10).join(data.get('decisions_importantes', []))}

------------------------------------------------

RISQUES

{chr(10).join(data.get('risques', []))}

------------------------------------------------

ALERTES

{chr(10).join(data.get('alertes', []))}

"""
    return note
