import streamlit as st
import pandas as pd
from pathlib import Path



st.subheader("予測：土曜日")
df_sat = pd.read_csv("data/pred_df_sat.csv")
df_sat = df_sat[["買い目","horse_name","odds_over","tansho_odds","pred","kitaiti"]]
st.dataframe(df_sat)


# st.subheader("予測：日曜日")
# df_sun = pd.read_csv("data/pred_df_sun.csv")
# df_sun = df_sun[["買い目","horse_name","odds_over","tansho_odds","pred","kitaiti"]]
# st.dataframe(df_sun)




