import os, requests, pandas as pd, streamlit as st
ES = os.getenv("ES_URL", "http://localhost:9200")
INDEX = os.getenv("ES_INDEX", "events")
st.set_page_config(page_title="DeepSurveilTrack", layout="wide")
st.title("DeepSurveilTrack – Monitoring")
sev = st.selectbox("Severity", ["all","low","medium","high","critical"])
limit = st.number_input("Limit", 10, 5000, 1000, 50)
def fetch():
    must = []
    if sev != "all": must.append({"term":{"severity":sev}})
    q = {"bool":{"must":must}} if must else {"match_all":{}}
    body = {"query":q, "size":int(limit), "sort":[{"timestamp":"desc"}]}
    r = requests.get(f"{ES}/{INDEX}/_search", json=body); r.raise_for_status()
    return pd.DataFrame([h["_source"] for h in r.json()["hits"]["hits"]])
df = fetch()
st.dataframe(df, use_container_width=True)
if not df.empty:
    st.subheader("Stats")
    st.bar_chart(df["severity"].value_counts())
    st.line_chart(df.sort_values("timestamp")["score"])
    st.download_button("Export CSV", df.to_csv(index=False), "events.csv", "text/csv")
