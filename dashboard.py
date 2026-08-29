import sqlite3

import pandas as pd

import streamlit as st

import plotly.express as px

conn = sqlite3.connect("data/funds.db")

df = pd.read_sql(

    "SELECT * FROM funds",

    conn

)

st.title("Dashboard")

if not df.empty:

    col1, col2, col3 = st.columns(3)

    col1.metric(

        "TRI moyen",

        round(df["tri"].mean(), 2)

    )

    col2.metric(

        "TVPI moyen",

        round(df["tvpi"].mean(), 2)

    )

    col3.metric(

        "Nombre fonds",

        len(df)

    )

    fig = px.bar(

        df,

        x="nom_fonds",

        y="tri",

        title="TRI par fonds"

    )

    st.plotly_chart(fig)

else:

    st.info("Aucune donnée")
