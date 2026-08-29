def save_fund(data):

    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    cursor.execute(

        """
        INSERT INTO funds
        (
            nom_fonds,
            date_reporting,
            tri,
            tvpi,
            dpi,
            rvpi,
            valeur_liquidative,
            montant_engage
        )

        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """,

        (

            data.get("nom_fonds"),

            data.get("date_reporting"),

            data.get("tri"),

            data.get("tvpi"),

            data.get("dpi"),

            data.get("rvpi"),

            data.get("valeur_liquidative"),

            data.get("montant_engage")

        )
    )

    conn.commit()

    conn.close()
