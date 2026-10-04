# Recherche: Vortragsvorbereitung „Vom Messwert zur Zahl"

Grundlage: vorhandene, bereits recherchierte und nachgerechnete Materialien im Repo (keine neue Websuche nötig). Phase 2 = Material-Analyse auf Lerntauglichkeit + Lückensuche.

## Befunde (verdichtet)

| Material | Was es leistet | Lücke für das Lernen |
|---|---|---|
| 01_Folieninhalt_und_Varianten.md | Kernaussagen, Inhalte, Sprechernotizen, Zeitplan je Folie | Keine **Überleitungssätze** zwischen Folien, keine **Stichwortkarte** (3–5 Wörter/Folie), keine **Zeit-Checkpoints** (kumulierte Uhrzeit) |
| 02_QA_Vorbereitung.md | 30 Rückfragen mit Musterantworten | Nur zum Lesen (passiv); einige naheliegende Ausbilder-Fragen fehlen (z. B. „OL“-Anzeige, Analog- vs. Digitalmessgerät, Komparator, Shunt für 10 A, Gleichrichtwert vs. Effektivwert) |
| 03_Spickzettel.md | Alle Formeln/Zahlen auf einer Seite | Nur feste Beispielzahlen → kein Transfer-Training mit **variierten Werten** |
| 05_Recherche_Nachschlagewerk.md | Faktenbasis mit Quellenkürzeln | Gut als Lösungsreferenz, nicht als Übung |
| slides/praesentation.tex | Visuelle Vorlage, \note-Sprechertexte | – |

**Typische Verwechslungsgefahren (für Fehleraufgaben):**
- LSB: $U_\text{ref}/2^n$ (Konvention hier) vs. $U_\text{ref}/(2^n-1)$ (manche Tutorials) → nicht verunsichern lassen, Konvention nennen.
- Nyquist: „mehr als doppelt“ ($>$), nicht „gleich doppelt“.
- Flash: $2^n-1$ Komparatoren (nicht $2^n$).
- Vorwiderstand $(n-1)R_i$ vs. Shunt $R_i/(n-1)$ – vertauschbar.
- Spannungsrichtig ↔ stromrichtig (kleines R ↔ großes R) – vertauschbar.
- Genauigkeitsangabe: Prozent **vom Messwert**, nicht vom Messbereich (beim DMM); Güteklasse (analog) dagegen vom **Endwert**.

## Bewertung (quality-rubric A)

| Dimension | Score | Begründung |
|---|---|---|
| Genauigkeit / Faktentreue | 8/10 | Alle Zahlen am 01.10. programmatisch nachgerechnet; Fakten quellenbelegt, Lehrbuchwissen als `[LB]` markiert |
| Quellenqualität | 7/10 | Datenblatt (ICL7106), BG-Handreichung, Fluke, Hochschulskript; einige Sekundärquellen (Tutorial-Seiten) |
| Scope-Treue | 9/10 | Exakt die 15 Folien + Backup + Q&A |
| Relevanz / Gewichtung | 9/10 | ⭐-Markierung priorisiert wahrscheinliche Fragen |
| Vollständigkeit | 7/10 | Für den Vortrag vollständig; für das Lernen fehlen Übergänge, Transferaufgaben, einige Rückfragen (s. o.) – werden in Phase 3 ergänzt |

Gesamt: 8,0 – Schwellenwert erreicht. Lücken sind Lern-Lücken, keine Fakten-Lücken.

## Lücken / Risiken
- Neue Rückfragen werden aus Lehrbuchwissen ergänzt → als `[LB]` kennzeichnen.
- Risiko Zeitüberzug bei Folien 4/5/10/14 (je 1:15) → Timing-Checkpoints üben.
