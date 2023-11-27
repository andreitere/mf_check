import streamlit as st
import pandas as pd
import time
import requests
import lxml
from datetime import datetime
st.set_page_config(layout="wide")

posturi = pd.read_html("https://repartitie.ms.ro/public-loc.html")

page = requests.get("https://repartitie.ms.ro/public-loc.html")
tree = lxml.html.fromstring(page.content)

data = tree.xpath("/html/body/span[1]/font/text()")

posturi = pd.concat(posturi)
df1_cols = [x for x in posturi.columns if x.endswith(".1")]
df2_cols = [x for x in posturi.columns if not x.endswith(".1") and not x.startswith("Unnamed")]
posturidf1 = posturi[df1_cols]
posturidf1.columns = df2_cols
total = pd.concat([posturidf1, posturi[df2_cols]])
with st.container():
    while True:
        st.empty()
        result = total.query("Specialitate == 'MEDICINĂ DE FAMILIE'")["Bcd"].iloc[0]
        st.text(f"Locuri ramase mf: {result} -> {data[0]} ({datetime.now().strftime('%H:%M')})")
        time.sleep(30)