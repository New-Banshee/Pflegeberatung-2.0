import streamlit as st

st.set_page_config(page_title="Pflege-FAQ", layout="wide")
st.title("🧭 Pflege-FAQ – Orientierung rund um die Pflegeberatung")

st.markdown("""**Ein interaktives Informations- und Beratungswerkzeug auf Grundlage des §7a SGB XI und der Pflegeberatung in Bayern für Betroffene, An- und Zugehörige sowie Interessierte.**

🧠 *Studentisches Projekt im Rahmen des berufsbegleitenden Studiengangs B.Sc. Pflegewissenschaft an der Katholischen Universität Eichstätt-Ingolstadt*  
🔎 *Modul: Zertifikat zur Pflegeberatung nach §7a SGB XI*  
👤 *Erstellt von: Jennifer Zimmermann B. Sc. & Christina Papacek-Zimmermann B. Sc. im Sommersemester 2025*
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
        "Literatur & Quellen"
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
Die Prüfung mündet in einem Gutachten für die Pflegekasse (§18 SGB XI).

**Pflegefachpersonen:**  
Examinierte Fachpersonen mit dreijähriger Ausbildung und Staatsexamen. Dazu gehören z. B. Pflegefachfrau/-mann, Gesundheits- und Krankenpflegerin/-pfleger oder Altenpflegerin/-pfleger (§1 PflBG).

**Pflegekasse vs. Krankenkasse:**  
Pflegekassen sind eigenständige Träger der Pflegeversicherung, organisiert unter dem Dach der Krankenkassen (§46 SGB XI).

**Angehörige & Zugehörige:**  
Angehörige im rechtlichen Sinne sind zumeist Familienmitglieder – etwa Eltern, Kinder, Geschwister oder Ehepartner. Auch angeheiratete Verwandte wie Schwiegertöchter oder -söhne zählen dazu.  
Zugehörige sind nahestehende Personen ohne verwandtschaftliches Verhältnis, z. B. enge Freunde oder Lebensgefährtinnen und Lebensgefährten.

⚠️ **Rechtlich relevant:**  
Bei bestimmten Leistungen – wie Verhinderungspflege oder Pflegezeit – ist der Verwandtschaftsgrad oder das Zusammenleben in häuslicher Gemeinschaft entscheidend (§39 SGB XI, PflegeZG).  
Nicht alle Leistungen können von Zugehörigen geltend gemacht oder abgerechnet werden, selbst wenn sie aktiv in die Pflege eingebunden sind.

🛑 **Wichtig:**  
In rechtlichen Fragen – etwa bei der Verhinderungspflege oder der Pflegezeit – ist **maßgeblich**, ob ein **Verwandtschaftsverhältnis**, eine **häusliche Gemeinschaft** oder eine **erwerbsmäßige Pflege** vorliegt. Diese Kriterien entscheiden über **Höhe und Anspruch auf Leistungen** (vgl. §39 Abs. 2–3 SGB XI).
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

    st.caption("📅 Stand: Mai 2025 – Beträge gemäß Pflegeunterstützungs- und -entlastungsgesetz (PUEG)")

    st.warning("🔎 Hinweis: Die hier aufgeführten Beträge basieren auf dem aktuellen Gesetzesstand laut Pflegeunterstützungs- und -entlastungsgesetz (PUEG). Die konsolidierten Gesetzestexte im Internet (z. B. SGB XI) können zum Abrufzeitpunkt noch ältere Beträge enthalten.")

    geld, sach, entlast, hinweis = daten[auswahl]
    st.success(f"Leistungsübersicht für Pflegegrad {auswahl}")
    st.markdown(f"💶 **Pflegegeld:** {geld}  🧾 **Pflegesachleistung:** {sach}  🧹 **Entlastungsbetrag:** {entlast}")
    st.info(hinweis)

    # Landespflegegeld Bayern
    st.markdown("""
---

### 🔷 Landespflegegeld Bayern (zusätzlich zum Pflegegeld)
Pflegebedürftige Personen mit **mindestens Pflegegrad 2** und **Hauptwohnsitz in Bayern** können zusätzlich zum Pflegegeld das **Landespflegegeld** beantragen.

💶 **1.000 € jährlich** (einmal pro Kalenderjahr)  
📬 Antragstellung über das **Landesamt für Pflege in Amberg**

🔗 [Weitere Informationen & Antragsformulare](https://www.lfp.bayern.de/landespflegegeld/) *(abgerufen: 01. Juli 2025)*
""")

    st.markdown("---")
    st.subheader("📌 Erläuterung der Leistungen")
    st.markdown("""
**Wer erhält die Leistungen?**  
Pflegegeld wird gemäß §37 SGB XI an die pflegebedürftige Person ausgezahlt – nicht direkt an pflegende An- und Zugehörige. Es ist zweckgebunden für die häusliche Versorgung.

**Ambulant vs. stationär:**  
Ambulant: Leistungen erfolgen zu Hause – Pflegegeld, Sachleistungen oder Kombination möglich (§38 SGB XI).  
Stationär: Sachleistungen nach §43 SGB XI in einer Einrichtung. Eigenanteil nach §43c SGB XI fällt zusätzlich an.

**Entlastungsbetrag (§45b SGB XI):**  
Zusätzlich 131 €/Monat für anerkannte Unterstützungsleistungen (z. B. Haushaltshilfe, Betreuungsangebote).  
❗ **Wichtig:** Der Entlastungsbetrag ist **ausschließlich bei häuslicher Versorgung** vorgesehen – bei vollstationärer Pflege entfällt der Anspruch.  
📅 *Der genannte Betrag in Höhe von 131 € gilt laut Pflegeunterstützungs- und -entlastungsgesetz (PUEG) ab Mai 2025.*  
🚫 Keine Barauszahlung möglich.

**Unterscheidung der Leistungsarten (§36–38 SGB XI):**
- Pflegesachleistung (§36): Professionelle Pflegefachpersonen erbringen die Pflegeleistungen zu Hause. Die Pflegekasse bezahlt die Pflegeeinrichtung oder den ambulanten Pflegedienst direkt.  
- Pflegegeld (§37): Geldleistung an die pflegebedürftige Person zur Organisation der Pflege, z. B. durch An- und Zugehörige oder private Pflegepersonen.  
- Kombinationsleistung (§38): Kombination aus Pflegegeld und Sachleistung, wenn die Pflege teilweise selbst organisiert und teilweise durch professionelle Pflege erbracht wird.
""")


elif themenwahl == "Antragstellung & Zugang":
    st.header("📬 Antragstellung & Zugang zu Leistungen")
    st.markdown("""
**Pflegegrad :**  
Der Antrag erfolgt formlos bei der Pflegekasse (z. B. telefonisch oder schriftlich). Leistungen werden frühestens ab dem Antragsdatum gewährt.

**Begutachtung:**  
Eine Gutachterin oder Gutachter des Medizinischen Dienstes (gesetzlich Versicherte) oder von Medicproof (Privatversicherte) prüft die Selbstständigkeit im häuslichen Umfeld anhand gesetzlicher Kriterien.

**Pflegeberatung (§7a SGB XI):**  
Die Pflegekasse ist verpflichtet, innerhalb von zwei Wochen nach Antragseingang eine kostenfreie, individuelle Pflegeberatung durch eine geschulte Fachkraft anzubieten.

**„Reha vor Pflege“ (§31 SGB XI):**  
Vor der Gewährung von Leistungen aus der Pflegeversicherung ist zu prüfen, ob vorrangig medizinische oder berufliche Rehabilitationsmaßnahmen in Frage kommen.
    """)


elif themenwahl == "Ansprechpartner & Zuständigkeit":
    st.header("📞 Ansprechpartner & regionale Zuständigkeit (Bayern)")
    st.markdown("""
**Pflegekasse:**  
Erste Anlaufstelle für Anträge, Beratung und Koordination rund um die Pflegeversicherung. Dort erfolgt auch die Antragstellung für Pflegegrade und Leistungen nach dem SGB XI.

**Pflegestützpunkte:**  
Bieten neutrale, trägerübergreifende Beratung für Pflegebedürftige und Angehörige – auch zu regionalen Unterstützungsangeboten. In Bayern sind sie in vielen Landkreisen verfügbar.

**Bezirke in Bayern (Landesrecht & §27b SGB XII):**  
In Bayern sind die **Bezirke** zuständig für die **Hilfe zur Pflege nach dem SGB XII** – sowohl bei ambulanter, teilstationärer als auch stationärer Pflege.  
Diese Leistung greift, wenn die Pflegeversicherung nicht ausreicht und das eigene Einkommen/Vermögen die Pflegekosten nicht deckt.  
📍Die Zuständigkeit eines Bezirks beginnt, wenn der tatsächliche Aufenthalt dort seit mindestens zwei Monaten besteht (§27b SGB XII).  
⚠️ Wichtig: Die Leistungen der **Pflegeversicherung** (SGB XI) werden weiterhin von der **Pflegekasse** erbracht – unabhängig vom Wohnort.

**Sozialamt:**  
Verantwortlich für ambulante Hilfe zur Pflege (z. B. Haushaltshilfen), wenn Einkommen und Vermögen der pflegebedürftigen Person nicht ausreichen. Auch Ansprechpartner für ergänzende Sozialleistungen.

**Wichtig:**  
Maßgeblich für die Zuständigkeit ist der tatsächliche Aufenthaltsort der pflegebedürftigen Person – nicht der formale Wohnsitz.
    """)


elif themenwahl == "Entlastung für An- und Zugehörige":
    st.header("🤝 Entlastung & Unterstützung für An- und Zugehörige")

    st.markdown("""
**Pflegekurse (§45 SGB XI):**  
Kostenlose Schulungen für pflegende Angehörige und ehrenamtlich Pflegende – vor Ort oder digital.

**Verhinderungs- & Kurzzeitpflege (§39, §42 SGB XI):**  
Ab dem 1. Juli 2025 gilt ein **gemeinsames Jahresbudget** für beide Leistungen:
- **Bis zu 3.539 € pro Kalenderjahr** (Pflegegrad 2–5)
- **Maximal 8 Wochen Ersatzpflege**
- **Pflegegeld wird währenddessen für bis zu 8 Wochen zur Hälfte weitergezahlt**
- **Keine sechsmalige Vorpflegezeit mehr erforderlich**
- Vorher genutzte Beträge aus dem ersten Halbjahr 2025 werden angerechnet

**Pflegezeit & Familienpflegezeit (PflegeZG):**  
Gesetzlich geregelte Möglichkeiten der Freistellung für berufstätige Angehörige zur Pflege naher Verwandter (z. B. Elternzeitähnlich oder stufenweise).

**Entlastungsbetrag (§45b SGB XI):**  
- Monatlich 131 € zusätzlich für anerkannte Angebote im Alltag  
- **Nur bei häuslicher Pflege nutzbar**, nicht bei vollstationärer Versorgung  
- Keine Barauszahlung möglich  
- Zweckgebunden z. B. für Alltagsbegleitung, Haushaltshilfen oder anerkannte Dienstleister

📅 *Stand: Juli 2025 – gemäß Pflegeunterstützungs- und -entlastungsgesetz (PUEG)*  
🔗 [Quelle: Bundesgesundheitsministerium – Änderungen ab Juli 2025](https://www.bundesgesundheitsministerium.de/presse/pressemitteilungen/das-aendert-sich-zum-1-juli-in-der-pflege.html)
    """)


elif themenwahl == "Rechtliche Betreuung":
    st.header("👤 Rechtliche Betreuung & Einwilligung")

    st.markdown("""
**Anordnung einer rechtlichen Betreuung (§1814 BGB):**  
Eine Betreuung wird vom Amtsgericht angeordnet, wenn eine volljährige Person aufgrund von Krankheit oder Behinderung ihre Angelegenheiten ganz oder teilweise nicht mehr selbst regeln kann. Die Betreuung erfolgt in den konkret erforderlichen Aufgabenkreisen.

**Einwilligungsvorbehalt (§1825 BGB):**  
Wenn zur Abwendung erheblicher Gefahren für die betreute Person notwendig, kann das Gericht zusätzlich einen Einwilligungsvorbehalt anordnen – z. B. bei finanzieller Selbstgefährdung. Rechtsgeschäfte bedürfen dann der Zustimmung des Betreuers.

**Pflegeberatung & Leistungsanträge (§7a SGB XI):**  
Ist eine rechtliche Betreuung eingerichtet, benötigt es für Anträge auf Pflegeleistungen, Beratung oder Wohnraumanpassung ggf. die Zustimmung oder Mitwirkung des rechtlichen Betreuers.

**Alternative: Vorsorgevollmacht:**  
Durch eine rechtzeitig erteilte Vorsorgevollmacht können selbstbestimmt Vertrauenspersonen benannt werden, um im Bedarfsfall rechtswirksam zu handeln – ohne gerichtliche Betreuung.
    """)


elif themenwahl == "Wohnraumanpassung & Hilfsmittel":
    st.header("🏠 Wohnraumanpassung & Hilfsmittel")

    st.markdown("""
**Wohnumfeldverbessernde Maßnahmen (§40 SGB XI):**  
Pflegebedürftige mit anerkanntem Pflegegrad können für Maßnahmen zur Verbesserung des Wohnumfelds einen **Zuschuss von bis zu 4.000 €** beantragen. Dazu zählen z. B. der Einbau eines barrierefreien Bades, eines Treppenlifts oder einer Türverbreiterung. Die Maßnahme muss dazu dienen, die häusliche Pflege zu ermöglichen oder zu erleichtern.

**Hilfsmittel:**  
Zu den typischen Pflegehilfsmitteln gehören z. B. Pflegebett, Rollator, Toilettenstuhl oder Hausnotrufsysteme. Voraussetzung ist eine **ärztliche Verordnung** und die **Genehmigung durch die Krankenkasse**. Es können ggf. Zuzahlungen anfallen. Unterschieden wird zwischen technischen Hilfsmitteln und zum Verbrauch bestimmten Pflegehilfsmitteln (z. B. Einmalhandschuhe).

**Ziel:**  
Zweck dieser Leistungen ist die **Ermöglichung häuslicher Pflege** sowie die **Wiederherstellung, Stabilisierung oder Förderung der Selbstständigkeit** der pflegebedürftigen Person.
    """)


elif themenwahl == "Teilhabe & Reha":
    st.header("🧩 Teilhabe am Leben in der Gesellschaft")

    st.markdown("""
**Ziel der Teilhabeleistungen:**  
Pflegebedürftige Menschen und Menschen mit Behinderung sollen möglichst selbstbestimmt leben können – trotz Einschränkungen.  
Die Pflegeversicherung (§5 SGB XI) und die Eingliederungshilfe (SGB IX) unterstützen dabei mit alltagspraktischen und sozialen Hilfen. Besonders gefördert werden Angebote zur Teilhabe am sozialen Leben, wie z. B. Alltagsbegleitung oder Freizeitangebote.

**Rehabilitation vor Pflege (§31 SGB XI):**  
Bevor Leistungen aus der Pflegeversicherung bewilligt werden, ist zu prüfen, ob medizinische oder berufliche Reha-Maßnahmen vorrangig sind. Ziel ist die Wiederherstellung der Selbstständigkeit. Reha-Anträge können von der Pflegekasse angestoßen werden.

**Eingliederungshilfe (§99 SGB IX):**  
Für Menschen mit (drohender) Behinderung stellt die Eingliederungshilfe Leistungen zur Teilhabe bereit. Zuständig sind in Bayern in der Regel die **Bezirke**. Leistungen umfassen z. B. Assistenzdienste, Mobilitätshilfen oder Unterstützungsangebote in Schule und Arbeit.

**Teilhabeplan (§19 SGB IX):**  
Bei komplexem Hilfebedarf und mehreren beteiligten Leistungsträgern wird ein **Teilhabeplanverfahren** eingeleitet. Es koordiniert die Leistungen trägerübergreifend, stellt den Bedarf fest und sichert eine abgestimmte Hilfeplanung.
    """)


elif themenwahl == "Widerspruch & Klagewege":
    st.header("⚖️ Widerspruch & rechtliche Durchsetzung")

    st.markdown("""
**Widerspruch (§84 SGG):**  
Gegen einen ablehnenden oder fehlerhaften Bescheid kann innerhalb eines Monats schriftlich Widerspruch eingelegt werden. Der Widerspruch bewirkt eine erneute Prüfung durch die Pflegekasse.

**Verpflichtungsklage (§54 SGG):**  
Wenn eine beantragte Leistung zu Unrecht abgelehnt oder gar nicht bearbeitet wurde, kann Klage vor dem Sozialgericht erhoben werden. Ziel ist die gerichtliche Durchsetzung der beantragten Leistung.

**Untätigkeitsklage (§88 SGG):**  
Erfolgt innerhalb von drei Monaten keine Entscheidung über den Antrag oder Widerspruch, kann beim Sozialgericht Untätigkeitsklage erhoben werden.

**Anfechtungsklage (§54 SGG):**  
Gegen belastende Verwaltungsakte – z. B. Rückforderungen oder Kürzungen – kann Anfechtungsklage erhoben werden, um die Entscheidung aufheben zu lassen.

**Vorläufige Leistungen (§39 SGB I):**  
Während eines laufenden Widerspruchs- oder Klageverfahrens kann die Pflegekasse auf Antrag vorläufige Leistungen gewähren – z. B. wenn ein zu niedriger Pflegegrad festgestellt wurde, aber ein höherer beantragt ist.
    """)


elif themenwahl == "Literatur & Quellen":
    st.header("Literatur & Quellen")

    st.markdown("""
### Gesetzestexte (Gesetze im Internet)
- **Sozialgesetzbücher I, IX, XI**  
  [www.gesetze-im-internet.de](https://www.gesetze-im-internet.de)  
  *(Suchbegriffe: „SGB I“, „SGB IX“, „SGB XI“ – jeweils aktuelle Version abrufbar)*  
- **Pflegeberufegesetz (PflBG)**  
  [PflBG – Gesetz über die Pflegeberufe](https://www.gesetze-im-internet.de/pflbg/) *(Stand: 01. Juli 2025)*

### Bundesministerien & Institutionen
- [Bundesministerium für Gesundheit (BMG)](https://www.bundesgesundheitsministerium.de)  
- [Verhinderungspflege – BMG](https://www.bundesgesundheitsministerium.de/verhinderungspflege.html)  
- [GKV-Spitzenverband: Pflegeberatung nach §7a SGB XI](https://www.gkv-spitzenverband.de)  
- [Pflegelotse der Pflegekassen](https://www.pflegelotse.de)  
- [Wege zur Pflege (BMFSFJ)](https://www.wege-zur-pflege.de)
- [Pflegeleistungen ab 2025 – Merkblatt für Beihilfeberechtigte (BVA)](https://www.bva.bund.de/SharedDocs/Downloads/DE/Bundesbedienstete/Gesundheit-Vorsorge/Beihilfe/Merkblaetter/Pflegeleistungen_ab_2025.pdf?__blob=publicationFile&v=1) *(Stand: Juli 2025)*

### Weiterführende Fachliteratur
- **Beyer, T.** (2025). *Recht für die Soziale Arbeit* (4., aktualisierte Auflage). Nomos.  
- **Mazur, S.** (2024). *Betreuungsrecht* (19. Auflage, Stand: 1.3.2024). dtv / C.H. Beck.  
- **Nomos Verlagsgesellschaft** (2024). *Gesetze für die Soziale Arbeit* (14. Auflage, Stand: 24.07.2024). Nomos.

---

ℹ️ *Alle externen Links führen zu offiziellen, frei zugänglichen Informationsportalen. Es besteht keine kommerzielle Absicht.*
    """)
