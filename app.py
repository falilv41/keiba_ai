import streamlit as st
import pandas as pd
from pathlib import Path



st.subheader("予測：7月20日")
df = pd.read_csv("data/pred_df.csv")
df = df[["買い目","odds_over","tansho_odds","pred","kitaiti"]]
st.dataframe(df)
