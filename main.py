import streamlit as st

st.set_page_config(page_title="Pflege-FAQ", layout="wide")
st.title("🧭 Pflege-FAQ – Orientierung rund um die Pflegeberatung")

st.markdown("""**Ein interaktives Informations- und Beratungswerkzeug auf Grundlage des §7a SGB XI und der Pflegeberatung in Bayern für Betroffene, An- und Zugehörige sowie Interessierte.**

🧠 *Studentisches Projekt im Rahmen des berufsbegleitenden Studiengangs B.Sc. Pflegewissenschaft an der Katholischen Universität Eichstätt-Ingolstadt*  
🔎 *Modul: Zertifikat zur Pflegeberatung nach §7a SGB XI*  
👤 *Erstellt von: Jennifer Zimmermann & Christina Papacek-Zimmermann im Sommersemester 2025*
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
        "Widerspruch & Klagewege",
        "📚 Literatur & Quellen"
    ]
)

# --- Themenbereich 1 ---
if themenwahl == "Begriffsklärungen":
    st.header("📘 Begriffsklärungen")
    st.markdown("""
**Pflegebedürftigkeit (§14 SGB XI):**  
Pflegebedürftig ist eine Person, die wegen gesundheitlicher Beeinträchtigungen dauerhaft (mindestens sechs Monate) in ihrer Selbstständigkeit eingeschränkt ist und regelmäßig Hilfe benötigt.  
Der Gesetzgeber sieht Pflegebedürftigkeit als grundsätzlich beeinflussbaren Zustand, der durch Maßnahmen wie Rehabilitation oder Pflegeberatung verbessert oder stabil gehalten werden kann (vgl. §18b SGB XI, §31 SGB XI).

**Pflegegrad (§15 SGB XI):**  
Die Einstufung erfolgt durch den Medizinischen Dienst (MD) oder Medicproof nach einem Begutachtungssystem mit sechs Modulen. Es gibt fünf Pflegegrade (1–5), je nach Schwere der Beeinträchtigung.
Die Prüfung mündet in einem Gutachten für die Pflegekasse (§18, SGB XI).

**Pflegefachpersonen:**  
Examinierte Fachpersonen mit dreijähriger Ausbildung und Staatsexamen. Dazu gehören z. B. Pflegefachfrau/-mann, Gesundheits- und Krankenpflegerin/-pfleger oder Altenpflegerin/-pfleger (PflBG §1).

**Angehörige & Zugehörige:**  
Angehörige im rechtlichen Sinne sind zumeist Familienmitglieder – etwa Eltern, Kinder, Geschwister oder Ehepartner. Auch angeheiratete Verwandte wie Schwiegertöchter oder -söhne zählen dazu.  
Zugehörige sind nahestehende Personen ohne verwandtschaftliches Verhältnis, z. B. enge Freunde oder Lebensgefährtinnen und Lebensgefährten.

⚠️ **Rechtlich relevant:**  
Bei bestimmten Leistungen – wie Verhinderungspflege oder Pflegezeit – ist der Verwandtschaftsgrad oder das Zusammenleben in häuslicher Gemeinschaft entscheidend (§39 SGB XI, PflegeZG).  
Nicht alle Leistungen können von Zugehörigen geltend gemacht oder abgerechnet werden, selbst wenn sie aktiv in die Pflege eingebunden sind.
**Angehörige & Zugehörige:**  
Der Begriff "Angehörige" umfasst insbesondere Familienmitglieder und Personen, die mit der pflegebedürftigen Person **bis zum zweiten Grad verwandt oder verschwägert** sind (z. B. Eltern, Kinder, Geschwister, Schwiegerkinder).  
"Zugehörige" sind nahestehende Personen ohne formale Verwandtschaft – z. B. Freunde, Nachbarinnen oder Lebensgefährten.

🛑 **Wichtig:** In rechtlichen Fragen – etwa bei der Verhinderungspflege oder der Pflegezeit – ist **maßgeblich**, ob ein **Verwandtschaftsverhältnis**, eine **häusliche Gemeinschaft** oder eine **erwerbsmäßige Pflege** vorliegt.  
Diese Kriterien entscheiden über **Höhe und Anspruch auf Leistungen** (vgl. §39 Abs. 2–3 SGB XI).

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
Pflegegeld wird gemäß §37 SGB XI an die pflegebedürftige Person ausgezahlt – nicht direkt an pflegende An- und Zugehörige. Es ist zweckgebunden für die häusliche Versorgung.

**Ambulant vs. stationär:**  
- *Ambulant:* Leistungen erfolgen zu Hause – Pflegegeld, Sachleistungen oder Kombination möglich (§38 SGB XI).  
- *Stationär:* Sachleistungen nach §43 SGB XI in einer Einrichtung. Eigenanteil nach §43c SGB XI fällt zusätzlich an.

**Entlastungsbetrag (§45b SGB XI):**  
Zusätzlich 131 €/Monat für anerkannte Unterstützungsleistungen (z. B. Haushaltshilfe, Betreuungsangebote). 
❗ **Wichtig:** Der Entlastungsbetrag ist **ausschließlich bei häuslicher Versorgung** vorgesehen – bei vollstationärer Pflege entfällt der Anspruch.  
📅 *Der genannte Betrag in Höhe von 131 € gilt laut Pflegeunterstützungs- und -entlastungsgesetz (PUEG) ab Mai 2025.*
🚫Keine Barauszahlung möglich.

**Unterscheidung der Leistungsarten (§36–38 SGB XI):**  
- **Pflegesachleistung (§36):** Professionelle Pflegefachpersonen erbringen die Pflegeleistungen zu Hause. Die Pflegekasse bezahlt die Pflegeeinrichtung oder den ambulanten Pflegedienst direkt.  
- **Pflegegeld (§37):** Geldleistung an die pflegebedürftige Person zur Organisation der Pflege, z. B. durch An- und Zugehörige oder private Pflegepersonen.  
- **Kombinationsleistung (§38):** Kombination aus Pflegegeld und Sachleistung, wenn die Pflege teilweise selbst organisiert und teilweise durch professionelle Pflege erbracht wird.
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
  **Pflegekurse (§45 SGB XI):** Kostenlose Schulungen für pflegende Angehörige und ehrenamtlich Pflegende.
- **Verhinderungspflege (§39 SGB XI):**  
    - Bis 30.06.2025: Bis zu 1.612 €/Jahr (plus max. 843 € aus Kurzzeitpflege umwidmungsfähig → max. 2.528 €).  
    - Ab 01.07.2025: Einführung eines **gemeinsamen Jahresbetrags** für Verhinderungs- und Kurzzeitpflege: **bis zu 3.539 €/Jahr**.  
      Die sechsmalige Vorpflegezeit entfällt. Anspruch ab Pflegegrad 2.
- **Kurzzeitpflege (§42 SGB XI):** Vorübergehende stationäre Pflege – bis zu 1.774 €/Jahr.
- **Pflegezeit & Familienpflegezeit (PflegeZG):** Freistellungsmöglichkeiten für berufstätige Angehörige zur Pflege naher Verwandter.
- **Entlastungsbetrag (§45b SGB XI):** 131 €/Monat – ausschließlich bei häuslicher Pflege nutzbar (nicht bei stationärer Pflege!). Keine Barauszahlung möglich.
    """)
    st.caption("📅 Stand: Juli 2025")


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
- **Ziel:** Selbstbestimmte Teilhabe trotz Pflegebedürftigkeit (SGB XI) oder Behinderung (SGB IX).
            Dabei fördert die Pflegeversicherung gemäß §5 SGB XI (seit PSG II) gezielt auch Leistungen zur sozialen Teilhabe und Unterstützung im Alltag, um Pflegebedürftigen ein möglichst selbstbestimmtes Leben zu ermöglichen. 
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

elif themenwahl == "📚 Literatur & Quellen":
    st.header("📚 Literatur & Quellen")

    st.markdown("""
### Gesetzestexte (Gesetze im Internet)
- Sozialgesetzbuch XI: [SGB XI – Soziale Pflegeversicherung](https://www.gesetze-im-internet.de/sgb_11/) (abgerufen:01/Juli/2025)
- Sozialgesetzbuch IX: [SGB IX – Rehabilitation und Teilhabe](https://www.gesetze-im-internet.de/sgb_9/) (abgerufen:01/Juli/2025)
- Sozialgesetzbuch I / SGG: [SGB I](https://www.gesetze-im-internet.de/sgb_1/), [SGG](https://www.gesetze-im-internet.de/sgg/) (abgerufen:01/Juli/2025)

### Bundesministerien & offizielle Informationen
- Bundesgesundheitsministerium: [www.bundesgesundheitsministerium.de](https://www.bundesgesundheitsministerium.de) (abgerufen:01/Juli/2025)
- Infos zur Verhinderungspflege (BMG): [Verhinderungspflege](https://www.bundesgesundheitsministerium.de/verhinderungspflege.html)(abgerufen:01/Juli/2025) 
- Pflegewegweiser Bayern: [pflegewegweiser-bayern.de](https://www.pflegewegweiser-bayern.de) (abgerufen:01/Juli/2025)
- Verbraucherzentrale zur Pflege: [www.verbraucherzentrale.de](https://www.verbraucherzentrale.de) (abgerufen:01/Juli/2025)

### Weiterführende Empfehlungen
- [Pflegeberatung nach §7a SGB XI – GKV Spitzenverband](https://www.gkv-spitzenverband.de)
- [Pflegelotse der Pflegekassen](https://www.pflegelotse.de)
- [Wege zur Pflege (BMFSFJ)](https://www.wege-zur-pflege.de)
""")

