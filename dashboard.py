import streamlit as st
import pandas as pd

st.set_page_config(
layout="wide"
)

df=pd.read_csv(
"data/gold/dashboard.csv"
)

st.title(
"🏎️ Formula 1 2025 Analytics"
)

c1,c2,c3,c4=st.columns(4)

c1.metric(
"Pilotos",
df.driver.nunique()
)

c2.metric(
"Equipes",
df.team.nunique()
)

c3.metric(
"Pontos",
int(df.points.sum())
)

c4.metric(
"Vitórias",
int(df.wins.sum())
)

st.divider()

aba1,aba2,aba3=st.tabs([

"👨 Pilotos",

"🏢 Equipes",

"📈 Estatísticas"

])

with aba1:

    st.subheader(
    "Pontuação dos Pilotos"
    )

    st.bar_chart(

    df.set_index(

    "driver"

    )[

    "points"

    ]

    )

    st.dataframe(
    df
    )

with aba2:

    equipe=(

    df

    .groupby(

    "team"

    )

    [

    "points"

    ]

    .sum()

    .sort_values(

    ascending=False

    )

    )

    st.bar_chart(
    equipe
    )

with aba3:

    st.line_chart(

    df.set_index(

    "driver"

    )[

    "avg_finish"

    ]

    )

    st.bar_chart(

    df.set_index(

    "driver"

    )[

    "wins"

    ]

    )

st.success(
"Dashboard carregado"
)