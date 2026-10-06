# Vom Messwert zur Zahl – Voltmeter, Amperemeter & ADC

Präsentationsvorlage für **VWIF – Ausbildungsinhalte 022: Grundlagen der Elektrotechnik**
Thema: *Analog-Digital-Wandler, Amperemeter und Voltmeter* · Termin: **Fr, 02.10.2026** · Dauer: **15 Min (kürzbar auf 10 Min)**

## Inhalt des Repos

| Datei | Zweck | Öffnen mit |
|---|---|---|
| [`01_Folieninhalt_und_Varianten.md`](01_Folieninhalt_und_Varianten.md) | **Hauptdokument**: alle 15 Folien mit Kernaussage, Folieninhalt, 2–3 Darstellungsvarianten, Sprechernotiz, Zeitplan | Obsidian |
| [`slides/praesentation.tex`](slides/praesentation.tex) | Fertiges, kompilierbares **Beamer-Deck** (16:9) mit Schaltbildern & Diagrammen als Referenz/Vorschau | TeXstudio + MiKTeX |
| [`02_QA_Vorbereitung.md`](02_QA_Vorbereitung.md) | Wahrscheinliche Rückfragen mit Musterantworten | Obsidian |
| [`03_Spickzettel.md`](03_Spickzettel.md) / [`spickzettel/spickzettel.tex`](spickzettel/spickzettel.tex) | 1-Seiten-Spickzettel (Formeln, Zahlen, Zeitplan) | Obsidian / TeXstudio |
| [`04_Quellen.md`](04_Quellen.md) | Quellenverzeichnis inkl. Kurzfassung für eine Quellenfolie | Obsidian |
| [`05_Recherche_Nachschlagewerk.md`](05_Recherche_Nachschlagewerk.md) / [`recherche/recherche.tex`](recherche/recherche.tex) | **Recherche-Nachschlagewerk**: alle Rechercheergebnisse thematisch, mit Schnellnavigation, Formelindex, Glossar und Quellenkürzel je Fakt (TeX-Version mit klickbarem Inhaltsverzeichnis/Lesezeichen) | Obsidian / TeXstudio |
| [`lernen/06_Lernplan_2h.md`](lernen/06_Lernplan_2h.md) | **2-h-Lernplan** für den Tag vor dem Vortrag: Blöcke mit Uhrzeiten, Abrufübungen, zwei Probevorträge, Rückfragen-Drill | Obsidian |
| [`lernen/07_Karteikarten.md`](lernen/07_Karteikarten.md) | 50 Karteikarten (Format für das Obsidian-Plugin Spaced Repetition) | Obsidian |
| [`lernen/08_Uebungen.md`](lernen/08_Uebungen.md) | Rechenaufgaben R1–R13 mit aufklappbaren Lösungen, Fehleraufgaben F1–F7, Teach-back T1–T5 | Obsidian |
| [`lernen/09_Vortragstraining.md`](lernen/09_Vortragstraining.md) | Einstieg/Schluss wörtlich, Stichwortkarte mit Soll-Zeiten, Checkpoints, Überleitungen, Notfallpläne | Obsidian / Ausdruck |
| [`lernen/10_Rueckfragen_Drill.md`](lernen/10_Rueckfragen_Drill.md) | Drill-Ablauf, neue Rückfragen N1–N13, „Zahlen auf Zuruf“ | Obsidian |
| [`lernen/11_Messwert-Trainer.html`](lernen/11_Messwert-Trainer.html) | Interaktiver Trainer (offline): Karteikarten, Rechnen mit Eingabe, Rückfragen mit 30-s-Timer | Browser |

## Ablauf für morgen früh (≈ 60–75 Min)

1. **Beamer-PDF erzeugen (5 Min):** `slides/praesentation.tex` in TeXstudio öffnen → *pdfLaTeX* zweimal laufen lassen (MiKTeX fragt ggf. nach dem Installieren von `circuitikz`/`pgfplots` → bestätigen). Das PDF ist deine visuelle Vorlage.
2. **Firmenvorlage befüllen (30–40 Min):** `01_Folieninhalt_und_Varianten.md` in Obsidian neben PowerPoint öffnen und Folie für Folie übertragen:
   - Folientitel = Überschrift, **Kernaussage** = Highlight-/Textbox unten
   - pro Folie **eine** Darstellungsvariante wählen (A = am schnellsten umzusetzen)
   - Schaltbilder/Diagramme: aus dem Beamer-PDF als Bild übernehmen (*Snipping Tool* / `Win+Shift+S`) oder mit PowerPoint-Formen nachbauen
   - Sprechernotizen in das Notizfeld von PowerPoint kopieren
3. **10-Min-Fassung vorbereiten (2 Min):** Folien 6, 7, 13 hinter die Danke-Folie verschieben (= Backup).
4. **Proben (15–20 Min):** 2× laut mit Stoppuhr durchsprechen, danach `02_QA_Vorbereitung.md` (⭐-Fragen) lesen.
5. **Spickzettel drucken:** `spickzettel/spickzettel.tex` kompilieren (1 Seite A4).

## 15 Min ↔ 10 Min

| Fassung | Folien | Sprechzeit |
|---|---|---|
| 15 Min | 1–15 | 14:30 |
| 10 Min | ohne 6, 7, 13 (→ Backup) + gekürzte Notizen bei 3, 8, 11 | 9:10 |

Im Beamer-Deck umschalten: in `slides/praesentation.tex` Zeile `\kurzfassungfalse` → `\kurzfassungtrue`. Die optionalen Folien landen dann automatisch hinter der Fazit-Folie als „Backup“.

**Alternative Reihenfolge** (falls dir das lieber ist): ADC-Teil (9–13) vor die Messgeräte (4–8) ziehen und mit Folie 14 abschließen – die Messkette auf Folie 2 funktioniert für beide Reihenfolgen.

## Hinweise zum Beamer-Deck

- **Firmenfarben:** in der Präambel `akzent` und `akzent2` (RGB) anpassen.
- **Sprechernotizen im PDF:** `\setbeameroption{show notes on second screen=right}` einkommentieren.
- Inhalte wurden mit pdfLaTeX (TeX Live 2023) testkompiliert; MiKTeX installiert fehlende Pakete automatisch nach.

## Fachliche Prüfung

Alle Rechenbeispiele (LSB-Werte, Belastungsfehler, Bürdenspannung, Messbereichserweiterung, SAR-Beispiel, Genauigkeitsangabe, Zeitplan-Summen) wurden programmatisch nachgerechnet. Quellen: siehe [`04_Quellen.md`](04_Quellen.md).

## Zweiter Vortrag: DAC – Digital-Analog-Wandler (Ordner `dac/`)

| Datei | Inhalt | Öffnen mit |
|---|---|---|
| [`dac/01_Folieninhalt_und_Varianten.md`](dac/01_Folieninhalt_und_Varianten.md) | 7 Folien (~5:30 min, kürzbar auf 4:45) mit Layoutvarianten, Sprechernotizen, Backup-Folien | Obsidian / Copilot-Vorlage |
| [`dac/slides/dac.tex`](dac/slides/dac.tex) | Beamer-Folien inkl. R-2R-Schaltbild, Kennlinie, Sinus/Cosinus-Plot | TeXstudio |
| [`dac/02_QA_Vorbereitung.md`](dac/02_QA_Vorbereitung.md) · [`03_Spickzettel`](dac/03_Spickzettel.md) · [`04_Quellen`](dac/04_Quellen.md) | Rückfragen (⭐ wahrscheinlich), Spickzettel, Quellen | Obsidian |
| [`dac/lernen/`](dac/lernen/) | 20-min-Lernplan + Stichwortkarte, 28 Karteikarten, Übungen/Drill, interaktiver DAC-Trainer (offline) | Obsidian / Browser |

