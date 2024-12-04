import streamlit as st
from sidebar import sidebar
from custom_components import table, counter
import pandas as pd


sidebar()

table("Tabelle")
counter()

# csv_result = st.file_uploader(
#     "Upload a CSV file", type=["csv"], accept_multiple_files=False
# )


# if csv_result:
#     df = pd.read_csv(csv_result, delimiter=";")
#     st.write("You uploaded the following CSV file:")
#     st.dataframe(df)
