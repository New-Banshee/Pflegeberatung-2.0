
import streamlit as st

st.set_page_config(page_title="PflegeStart 2.0", layout="wide")
st.title("🧭 PflegeStart 2.0 – für An- und Zugehörige")
st.markdown("""Ein interaktives Informations- und Beratungswerkzeug auf Grundlage des §7a SGB XI und der Pflegeberatung in Bayern.**

🧠 *Ein studentisches Projekt im Rahmen des berufsbegleitenden Studiengangs B.Sc. Pflegewissenschaft*  
📚 *Themenschwerpunkt: Teilhabe- und Sozialrecht, Betreuungsrecht*  
🔎 *Modul: Zertifikat zur Pflegeberatung nach §7a SGB XI*
""")

# Menü
themenwahl = st.radio(
    "Bitte wählen Sie ein Thema:",
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
    ],
    horizontal=False
)

# Inhalte pro Thema
if themenwahl == "Begriffsklärungen":
    st.header("📘 Begriffsklärungen")
    st.markdown("""
    **Pflegebedürftigkeit (§14 SGB XI):**  
    Personen gelten als pflegebedürftig, wenn sie aufgrund gesundheitlicher Beeinträchtigungen in ihrer Selbstständigkeit oder ihren Fähigkeiten auf Dauer (voraussichtlich für mindestens sechs Monate) in relevantem Umfang Hilfe benötigen – etwa bei Körperpflege, Ernährung, Mobilität oder Alltagsbewältigung.

    **Pflegegrad (§15 SGB XI):**  
    Die Einstufung erfolgt in Pflegegrade 1 bis 5 (mittels eines pflegefachlich begründeten Begutachtungsinstruments, welches in 6 Module gegliedert ist) durch den Medizinischen Dienst (MD) oder Medicproof (bei Privatversicherten). Maßgeblich ist der Grad der Selbstständigkeit.

    **Pflegefachpersonen:**  
    Pflegefachpersonen sind Personen mit einer dreijährigen Pflegeausbildung und bestandenem Staatsexamen. Dazu gehören: Pflegefachfrau / Pflegefachmann (seit 2020 – neue generalistische Ausbildung) (PflBG, § 1), frühere Bezeichnungen: Krankenschwester/-pfleger, Gesundheits- und Krankenpflegerinnen/-pfleger, Altenpflegerinnen/-pfleger. Gemeint sind examinierte Pflegefachpersonen, also Personen mit staatlich anerkannter Ausbildung in der Alten-, Kranken- oder Kinderkrankenpflege. 

    **Angehörige & Zugehörige:**  
    Angehörige sind zumeist Verwandte, Zugehörige auch Personen ohne verwandtschaftliches Verhältnis, z. B. enge Freunde oder Nachbarn.

    **Pflegekasse vs. Krankenkasse:**  
    Pflegekassen sind eigenständige Träger unter dem Dach der Krankenkassen. Anträge sind bei der Pflegekasse zu stellen
     (SGB XI § 46, Abs. 1).""")

elif themenwahl == "Leistungen nach Pflegegrad":
    st.header("📊 Leistungen nach Pflegegrad")

    daten = {
        "1": ("0 €", "0 €", "125 €", "Nur Entlastungsbetrag – keine Geld- oder Sachleistung"),
        "2": ("316 €", "724 €", "125 €", "Pflegegeld an pflegebedürftige Person – nicht an Angehörige"),
        "3": ("545 €", "1.363 €", "125 €", "Kombinationsleistung möglich (§38 SGB XI)"),
        "4": ("728 €", "1.693 €", "125 €", "Ambulant höher, stationär Eigenanteil"),
        "5": ("901 €", "2.095 €", "125 €", "Stationäre Pflege mit Eigenanteil nach §43c SGB XI")
    }

    auswahl = st.selectbox("Pflegegrad auswählen:", list(daten.keys()), index=0)
    geld, sach, entlast, hinweis = daten[auswahl]

    st.success(f"Leistungsübersicht für Pflegegrad {auswahl}")
    st.markdown(f"💶 **Pflegegeld:** {geld}  🧾 **Pflegesachleistung:** {sach}  🧹 **Entlastungsbetrag:** {entlast}")
    st.info(hinweis)

    st.markdown("---")

    st.subheader("📌 Erläuterung der Leistungen")

    st.markdown(f"""
    **Wer erhält die Leistungen?**  
    Pflegegeld gemäß **§37 SGB XI** wird an die **pflegebedürftige Person selbst** gezahlt – nicht automatisch an pflegende Angehörige.  
    Die Verwendung ist **zweckgebunden zur Sicherstellung der häuslichen Versorgung**.

    **Was bedeutet ambulant und stationär?**  
    - **Ambulant:** Leistungen erfolgen **zu Hause** oder in einer betreuten Wohnform – Pflegegeld oder Sachleistung oder Kombination (§38 SGB XI).  
    - **Stationär:** Bei Unterbringung in einer **Pflegeeinrichtung** werden Sachleistungen gemäß **§43 SGB XI** erbracht.  
      Der Eigenanteil ist einrichtungsbezogen und nicht nach Pflegegrad gestaffelt (**§43c SGB XI**).

    **Entlastungsbetrag (§45b SGB XI):**  
    Der monatliche Betrag von **125 €** steht zusätzlich zur Verfügung – für haushaltsnahe Dienstleistungen, Alltagsbegleiter, Betreuungsangebote.  
    Er ist **nicht auszahlbar** und muss über anerkannte Anbieter abgerechnet werden.

    **Hinweis:**  
    Bei Pflegegrad 1 besteht kein Anspruch auf Pflegegeld oder Sachleistungen, wohl aber auf den Entlastungsbetrag.
    """)

    st.info(hinweis)

elif themenwahl == "Antragstellung & Zugang":
    st.header("📬 Antragstellung & Zugang zu Leistungen")
    st.markdown("""
    - **Pflegegrad beantragen:** Antrag erfolgt formlos (der Antrag muss nicht zwingend auf einem bestimmten Formular gestellt werden). Es reicht zunächst eine formlose Mitteilung (z. B. per Telefon, Brief oder E-Mail), in der man sagt, dass man einen Pflegegrad beantragen möchte, bei der Pflegekasse der versicherten Person.
    - **Begutachtung durch MDK/Medicproof**: erfolgt nach Terminvereinbarung im häuslichen Umfeld.
    - **Pflegeberatung nach §7a SGB XI:** innerhalb von 2 Wochen anzubieten – unterstützt bei Organisation, Auswahl und Antragstellung.
    - **Leistungen beginnen frühestens mit dem Datum des Antrags.**
    - **Reha-Anträge** können bei Rentenversicherung oder Krankenkasse gestellt werden („Reha vor Pflege“ – §31 SGB XI).
    """)

elif themenwahl == "Ansprechpartner & Zuständigkeit":
    st.header("📞 Ansprechpartner und regionale Zuständigkeit (Bayern)")
    st.markdown("""
    In Bayern ist entscheidend, **wo sich die pflegebedürftige Person aufhält** (nicht: wo sie gemeldet ist).

    - **Pflegekasse:** zuständig für Einstufung, Pflegeberatung, häusliche Pflegeleistungen
    - **Pflegestützpunkte:** bieten individuelle Beratung und Koordination vor Ort
    - **Bezirke Bayern (§3 AVSG, §27b SGB XII):**  
      übernehmen Leistungen der **stationären Hilfe zur Pflege** oder Leistungen für Menschen mit Behinderung, z. B. Eingliederungshilfe.
      - Voraussetzung: Aufenthalt seit mind. **2 Monaten** im jeweiligen Bezirk
      - Leistungen über **Sozialhilfe nach SGB XII**

    - **Sozialamt (Landratsamt/Stadt):** zuständig für ambulante Hilfe zur Pflege bei niedrigem Einkommen

    **💡 Tipp:** Im Zweifel beide kontaktieren – Pflegekasse & Pflegestützpunkt.
    """)

elif themenwahl == "Entlastung für An- und Zugehörige":
    st.header("🤝 Entlastung & Unterstützung für Angehörige und Zugehörige")
    st.markdown("""
    - **Pflegekurse (§45 SGB XI):** kostenfrei, digital oder vor Ort – z. B. rückenschonende Mobilisation, Kommunikation, Demenz
    - **Verhinderungspflege (§39 SGB XI):** bis 1.612 €/Jahr – wenn Pflegeperson verhindert ist
    - **Kurzzeitpflege (§42 SGB XI):** z. B. nach Krankenhausaufenthalt – bis 1.774 €/Jahr
    - **Pflegezeit & Familienpflegezeit:** zeitweise Freistellung vom Beruf (§3 PflegeZG)
    - **Entlastungsbetrag (125 €/Monat):** für Betreuung, haushaltsnahe Dienstleistungen – keine Barauszahlung
    """)

elif themenwahl == "Rechtliche Betreuung":
    st.header("👤 Rechtliche Betreuung & Einwilligung")
    st.markdown("""
    - **Rechtliche Betreuung (§1814 BGB):** wird durch das Amtsgericht eingerichtet, wenn eine Person nicht mehr eigenständig handeln kann
    - **Einwilligungsvorbehalt (§1825 BGB):** zusätzlich möglich für Schutz bei finanziellen Angelegenheiten
    - **Pflegeberatung und Anträge** dürfen dann nur mit Zustimmung des Betreuers erfolgen (§7a SGB XI)
    - **Alternativen:** Vorsorgevollmacht, Betreuungsverfügung
    """)

elif themenwahl == "Wohnraumanpassung & Hilfsmittel":
    st.header("🏠 Wohnraumanpassung & Hilfsmittel")
    st.markdown("""
    - **Wohnumfeldverbessernde Maßnahmen (§40 SGB XI):**
      - Bis zu **4.000 € Zuschuss pro Maßnahme**
      - Beispiele: Badumbau, Treppenlift, Türverbreiterung
    - **Hilfsmittelversorgung:** über ärztliche Verordnung – z. B. Pflegebett, Rollator, Toilettenstuhl
    - Antragstellung erfolgt über Pflegekasse bzw. Krankenkasse
    """)

elif themenwahl == "Teilhabe & Reha":
    st.header("🧩 Teilhabe am Leben in der Gesellschaft")
    st.markdown("""
    - **Teilhabe (§1 SGB IX):** Ziel ist die selbstbestimmte Teilhabe trotz Behinderung oder Pflegebedarf
    - **Rehabilitation geht vor Pflege (§31 SGB XI)** – Reha-Antrag bei DRV oder Krankenkasse
    - **Eingliederungshilfe (§99 SGB IX):** für Menschen mit Behinderung – organisiert über Bezirke (Bayern)
    - **Teilhabeplan (§19 SGB IX):** bei komplexem oder trägerübergreifendem Bedarf
    """)

elif themenwahl == "Widerspruch & Klagewege":
    st.header("⚖️ Widerspruch & rechtliche Durchsetzung")
    st.markdown("""
    - **Widerspruch (§84 SGG):** binnen 1 Monat nach Bescheid schriftlich einlegen
    - **Verpflichtungsklage (§54 SGG):** wenn beantragte Leistung abgelehnt wurde
    - **Untätigkeitsklage (§88 SGG):** wenn die Pflegekasse nicht innerhalb von 3 Monaten entscheidet
    - **Anfechtungsklage:** gegen belastenden Verwaltungsakt
    - **Vorläufige Leistungen (§39 SGB I):** möglich, solange über höheren Pflegegrad gestritten wird
    """)
