import sqlite3
import json


DB_NAME = "fonds.db"


def init_db():

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS analyses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date_analyse TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            nom_document TEXT,
            projet TEXT,
            resultat_json TEXT
        )
    """)

    conn.commit()
    conn.close()


def save_analysis(
    nom_document,
    projet,
    resultat
):

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO analyses
        (
            nom_document,
            projet,
            resultat_json
        )
        VALUES (?, ?, ?)
        """,
        (
            nom_document,
            projet,
            json.dumps(
                resultat,
                ensure_ascii=False
            )
        )
    )

    conn.commit()
    conn.close()
