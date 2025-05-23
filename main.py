import streamlit as st

st.set_page_config(page_title="PflegeStart 2.0", layout="wide")
st.title("🧭 PflegeStart 2.0 – für An- und Zugehörige")

st.markdown("""**Ein interaktives Informations- und Beratungswerkzeug auf Grundlage des §7a SGB XI und der Pflegeberatung in Bayern.**

🧠 *Ein studentisches Projekt im Rahmen des berufsbegleitenden Studiengangs B.Sc. Pflegewissenschaft an der Katholischen Universität Eichstätt-Ingolstadt*  
📚 *Themenschwerpunkt: Teilhabe- und Sozialrecht, Betreuungsrecht*  
🔎 *Modul: Zertifikat zur Pflegeberatung nach §7a SGB XI*
""")

# Navigation
themenwahl = st.radio(
    "🗂️ Bitte wählen Sie ein Thema:",
    [
        "Begriffsklärungen",
        "Leistungen nach Pflegegrad",
        "Antragstellung & Zugang",
        "Ansprechpartner & Zuständigkeit",
        "Entlastung für An- und Zugehörige",
        "Rechtliche Betreuung",
        "Wohnraumanpassung & Hilfsmittel",
        "Teilhabe & Reha",
        "Widerspruch & Klagewege"
    ]
)

# --- Themenbereich 1 ---
if themenwahl == "Begriffsklärungen":
    st.header("📘 Begriffsklärungen")
    st.markdown("""
**Pflegebedürftigkeit (§14 SGB XI):**  
Eine Person gilt als pflegebedürftig, wenn sie aufgrund gesundheitlicher Beeinträchtigungen dauerhaft (mindestens sechs Monate) in ihrer Selbstständigkeit eingeschränkt ist und regelmäßig Hilfe benötigt.

**Pflegegrad (§15 SGB XI):**  
Die Einstufung erfolgt durch den Medizinischen Dienst (MD) oder Medicproof nach einem Begutachtungssystem mit sechs Modulen. Es gibt fünf Pflegegrade (1–5), je nach Schwere der Beeinträchtigung.

**Pflegefachpersonen:**  
Examinierte Pflegekräfte mit dreijähriger Ausbildung und Staatsexamen. Dazu gehören z. B. Pflegefachfrau/-mann, Gesundheits- und Krankenpflegerin/-pfleger oder Altenpflegerin/-pfleger (PflBG §1).

**Angehörige & Zugehörige:**  
Angehörige sind meist Familienmitglieder, Zugehörige können auch enge Bezugspersonen wie Nachbarn oder Freunde sein.

**Pflegekasse vs. Krankenkasse:**  
Pflegekassen sind eigenständige Träger der Pflegeversicherung, organisiert unter dem Dach der Krankenkassen (§46 SGB XI).
""")

# --- Themenbereich 2 ---
elif themenwahl == "Leistungen nach Pflegegrad":
    st.header("📊 Leistungen nach Pflegegrad")

    daten = {
        "1": ("–", "–", "131 €", "Nur Entlastungsbetrag – keine Geld- oder Sachleistung (§45b SGB XI)"),
        "2": ("347 €", "796 €", "131 €", "Pflegegeld an die pflegebedürftige Person – nicht an Angehörige (§37 SGB XI)"),
        "3": ("599 €", "1.497 €", "131 €", "Kombinationsleistung möglich (§38 SGB XI)"),
        "4": ("800 €", "1.859 €", "131 €", "Ambulant höhere Leistungen, stationär mit Eigenanteil (§43c SGB XI)"),
        "5": ("990 €", "2.299 €", "131 €", "Stationäre Pflege mit einrichtungsbezogenem Eigenanteil (§43 SGB XI)")
    }

    auswahl = st.selectbox("Pflegegrad auswählen:", list(daten.keys()), index=0)

    st.caption("📅 Stand: Mai 2025 – gemäß Pflegeunterstützungs- und -entlastungsgesetz (PUEG)")

    geld, sach, entlast, hinweis = daten[auswahl]
    st.success(f"Leistungsübersicht für Pflegegrad {auswahl}")
    st.markdown(f"💶 **Pflegegeld:** {geld}  🧾 **Pflegesachleistung:** {sach}  🧹 **Entlastungsbetrag:** {entlast}")
    st.info(hinweis)

    st.markdown("---")
    st.subheader("📌 Erläuterung der Leistungen")
    st.markdown("""
**Wer erhält die Leistungen?**  
Pflegegeld wird gemäß §37 SGB XI an die pflegebedürftige Person ausgezahlt – nicht direkt an pflegende Angehörige. Es ist zweckgebunden für die häusliche Versorgung.

**Ambulant vs. stationär:**  
- *Ambulant:* Leistungen erfolgen zu Hause – Pflegegeld, Sachleistungen oder Kombination möglich (§38 SGB XI).  
- *Stationär:* Sachleistungen nach §43 SGB XI in einer Einrichtung. Eigenanteil nach §43c SGB XI fällt zusätzlich an.

**Entlastungsbetrag (§45b SGB XI):**  
Zusätzlich 131 €/Monat für anerkannte Unterstützungsleistungen (z. B. Haushaltshilfe, Betreuungsangebote). Keine Barauszahlung möglich.
""")

