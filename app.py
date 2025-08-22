import streamlit as st
from models.rapport import Rapport, AnsvarigPerson
from rapportgenerering.skapa_dokument import skapa_dokument

st.title("Minidemo: Veckorapport")

with st.form("rapportform"):
    sammanfattning = st.text_area("Sammanfattning")
    aktivitet = st.text_input("Aktivitet")
    timmar = st.number_input("Timmar", min_value=0.0, step=0.5)
    kommentar = st.text_input("Kommentar")
    ansvarig = st.selectbox("Ansvarig", ["Marcus", "Lambros", "Slavko"])
    submitted = st.form_submit_button("Spara till Word")

if submitted:
    try:
        rapport = Rapport(
            sammanfattning=sammanfattning,
            aktivitet=aktivitet,
            timmar=timmar,
            kommentar=kommentar,
            ansvarig=AnsvarigPerson(ansvarig)  # Konvertera sträng till enum
        )
        skapa_dokument(rapport)
        st.success("Word-dokument skapat: rapport_output.docx")
        with open("rapport_output.docx", "rb") as f:
            st.download_button("Ladda ner Word-dokument", f, file_name="rapport_output.docx")
    except Exception as e:
        st.error(f"Fel: {e}")
