import streamlit as st

st.set_page_config(page_title="PflegeStart 2.0", layout="wide")
st.title("🧭 PflegeStart 2.0 – für An- und Zugehörige")

st.markdown("""**Ein interaktives Informations- und Beratungswerkzeug auf Grundlage des §7a SGB XI und der Pflegeberatung in Bayern.**

🧠 *Ein studentisches Projekt im Rahmen des berufsbegleitenden Studiengangs B.Sc. Pflegewissenschaft an der Katholischen Universität Eichstätt-Ingolstadt*  
📚 *Themenschwerpunkt: Teilhabe- und Sozialrecht, Betreuungsrecht*  
🔎 *Modul: Zertifikat zur Pflegeberatung nach §7a SGB XI*
""")

st.warning("🔎 Dieses Tool dient der ersten Orientierung und ersetzt keine individuelle Pflegeberatung nach §7a SGB XI. Für persönliche Beratung wenden Sie sich bitte an Ihre Pflegekasse oder einen Pflegestützpunkt.")

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

elif themenwahl == "Antragstellung & Zugang":
    st.header("📬 Antragstellung & Zugang zu Leistungen")
    st.markdown("""
- **Pflegegrad beantragen:** Der Antrag erfolgt formlos bei der Pflegekasse (z. B. telefonisch oder schriftlich). Leistungen werden frühestens ab dem Antragsdatum gewährt.
- **Begutachtung:** Ein Gutachter des Medizinischen Dienstes (gesetzlich) oder Medicproof (privat) prüft die Selbstständigkeit im häuslichen Umfeld.
- **Pflegeberatung (§7a SGB XI):** Die Pflegekasse ist verpflichtet, innerhalb von zwei Wochen eine kostenfreie Pflegeberatung anzubieten.
- **„Reha vor Pflege“ (§31 SGB XI):** Vor Leistungen aus der Pflegeversicherung ist ggf. ein Antrag auf medizinische oder berufliche Rehabilitation zu prüfen.
    """)

elif themenwahl == "Ansprechpartner & Zuständigkeit":
    st.header("📞 Ansprechpartner & regionale Zuständigkeit (Bayern)")
    st.markdown("""
- **Pflegekasse:** Erste Anlaufstelle für Anträge, Beratung und Koordination.
- **Pflegestützpunkte:** Bieten neutrale, trägerübergreifende Beratung – regional verfügbar.
- **Bezirke in Bayern (§3 AVSG, §27b SGB XII):** Zuständig für Leistungen der Eingliederungshilfe und stationären Hilfe zur Pflege – vorausgesetzt, der Aufenthalt im Bezirk besteht seit mindestens zwei Monaten.
- **Sozialamt:** Zuständig für ambulante Hilfe zur Pflege (z. B. Haushaltshilfe) bei geringem Einkommen.
- **Wichtig:** Maßgeblich ist der tatsächliche Aufenthaltsort, nicht der Wohnsitz.
    """)

elif themenwahl == "Entlastung für An- und Zugehörige":
    st.header("🤝 Entlastung & Unterstützung für An- und Zugehörige")
    st.markdown("""
- **Pflegekurse (§45 SGB XI):** Kostenlose Schulungen für pflegende Angehörige (vor Ort oder online).
- **Verhinderungspflege (§39 SGB XI):** Bis zu 1.612 €/Jahr, wenn die Hauptpflegeperson z. B. wegen Krankheit verhindert ist.
- **Kurzzeitpflege (§42 SGB XI):** Vorübergehende stationäre Pflege – bis zu 1.774 €/Jahr.
- **Pflegezeit & Familienpflegezeit (PflegeZG):** Gesetzlich geregelte Freistellungsmöglichkeiten für berufstätige Angehörige.
- **Entlastungsbetrag:** 131 €/Monat – zweckgebunden z. B. für Alltagsbegleitung oder Haushaltshilfe.
    """)

elif themenwahl == "Rechtliche Betreuung":
    st.header("👤 Rechtliche Betreuung & Einwilligung")
    st.markdown("""
- **§1814 BGB:** Eine rechtliche Betreuung kann durch das Amtsgericht angeordnet werden, wenn eine Person ihre Angelegenheiten nicht mehr selbst regeln kann.
- **§1825 BGB:** Einwilligungsvorbehalt möglich, z. B. bei finanzieller Gefährdung.
- **Pflegeberatung & Leistungsanträge**: erfordern dann die Zustimmung des Betreuers (§7a SGB XI).
- **Alternative:** Vorsorgevollmacht – sollte frühzeitig geregelt sein.
    """)

elif themenwahl == "Wohnraumanpassung & Hilfsmittel":
    st.header("🏠 Wohnraumanpassung & Hilfsmittel")
    st.markdown("""
- **Wohnumfeldverbessernde Maßnahmen (§40 SGB XI):** Bis zu 4.000 € Zuschuss für Umbaumaßnahmen (z. B. barrierefreies Bad, Treppenlift).
- **Hilfsmittel:** z. B. Pflegebett, Rollator, Notrufsysteme – ärztliche Verordnung erforderlich, Genehmigung durch Krankenkasse.
- **Ziel:** Ermöglichung häuslicher Pflege und Sicherung der Selbstständigkeit.
    """)

elif themenwahl == "Teilhabe & Reha":
    st.header("🧩 Teilhabe am Leben in der Gesellschaft")
    st.markdown("""
- **Ziel gemäß §1 SGB IX:** Selbstbestimmte Teilhabe trotz Pflegebedarf oder Behinderung.
- **Rehabilitation vor Pflege (§31 SGB XI):** Vorrang der Reha-Maßnahmen prüfen.
- **Eingliederungshilfe (§99 SGB IX):** Leistungen für Menschen mit (drohender) Behinderung – zuständig: Bezirke in Bayern.
- **Teilhabeplan (§19 SGB IX):** Trägerübergreifende Koordination bei komplexem Hilfebedarf.
    """)

elif themenwahl == "Widerspruch & Klagewege":
    st.header("⚖️ Widerspruch & rechtliche Durchsetzung")
    st.markdown("""
- **Widerspruch (§84 SGG):** Innerhalb von einem Monat schriftlich gegen einen ablehnenden Bescheid einlegen.
- **Verpflichtungsklage (§54 SGG):** Wenn eine beantragte Leistung abgelehnt wird.
- **Untätigkeitsklage (§88 SGG):** Wenn keine Entscheidung innerhalb von 3 Monaten erfolgt.
- **Anfechtungsklage:** Gegen belastende Verwaltungsakte ohne Leistungsbezug.
- **Vorläufige Leistungen (§39 SGB I):** Beantragbar, wenn z. B. ein zu niedriger Pflegegrad gewährt wurde, aber Widerspruch läuft.
    """)

