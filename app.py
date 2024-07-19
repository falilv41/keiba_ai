import streamlit as st
import pandas as pd
from pathlib import Path



st.subheader("予測：7月20日")
df_sat = pd.read_csv("data/pred_df_0720.csv")
df_sat = df_sat[["買い目","odds_over","tansho_odds","pred","kitaiti"]]
st.dataframe(df_sat)


st.subheader("予測：7月21日")
df_sun = pd.read_csv("data/pred_df_0721.csv")
df_sun = df_sun[["買い目","horse_name","odds_over","tansho_odds","pred","kitaiti"]]
st.dataframe(df_sun)




