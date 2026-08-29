import sqlite3


DB_PATH = "data/funds.db"


def create_database():

    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    cursor.execute("""

    CREATE TABLE IF NOT EXISTS funds (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        nom_fonds TEXT,

        date_reporting TEXT,

        tri REAL,

        tvpi REAL,

        dpi REAL,

        rvpi REAL,

        valeur_liquidative REAL,

        montant_engage REAL

    )

    """)

    conn.commit()

    conn.close()
