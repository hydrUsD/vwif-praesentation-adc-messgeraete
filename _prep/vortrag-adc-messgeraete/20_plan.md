# Umsetzungsplan

Ablage: neuer Ordner `lernen/` im Repo (Obsidian-kompatibel), plus ein interaktives Lernmaterial (Artifact).

| Nr. | Deliverable | Inhalt | Lernmethode |
|---|---|---|---|
| L1 | `lernen/06_Lernplan_2h.md` | Minutengenauer 2-h-Ablauf mit Checkboxen, Pausen, Selbsteinschätzung vorher/nachher | Verteiltes Üben, Interleaving, Confidence-Calibration |
| L2 | `lernen/07_Karteikarten.md` | ~40 Abrufkarten (Obsidian *Spaced Repetition*-Format `Frage::Antwort`), nach Themen getaggt | Retrieval Practice |
| L3 | `lernen/08_Uebungen.md` | Rechenaufgaben mit **neuen** Zahlen (Transfer), SAR selbst durchführen, Fehleraufgaben („Azubi sagt …, was ist falsch?“), Teach-back-Aufträge; Lösungen eingeklappt | Worked-Example-Fading, Erroneous Examples, Teach-back |
| L4 | `lernen/09_Vortragstraining.md` | Stichwortkarte je Folie, Überleitungssätze, Einstieg/Schluss wörtlich, Zeit-Checkpoints, Selbstbewertungsbogen für Probevorträge, Notfallpläne (Zeit knapp, Blackout, Technik) | Generierung, Selbstüberwachung |
| L5 | `lernen/10_Rueckfragen_Drill.md` | Drill-Ablauf (Zufallsreihenfolge, 30-s-Antworten) + ~10 neue Rückfragen mit Musterantwort (`[LB]` markiert) | Retrieval unter Zeitdruck |
| L6 | Interaktives Lernmaterial (lernmaterial-Skill) | Karteikarten, Quiz (MC + Rechnen mit Eingabe), Rückfragen-Simulation | Retrieval, sofortiges Feedback |

## Qualitäts-Gate Phase 3
1. Alle Zahlen in L3/L5/L6 per Python nachrechnen (Skript im _prep-Ordner).
2. Unabhängiger Review-Subagent (paper-reviewing-Prinzip, zweckentfremdet): prüft Fakten, Eindeutigkeit der Aufgaben, Konsistenz mit 01–05; meldet nur Probleme + Fix.
3. Bewertung nach quality-rubric B, Schwellenwert alle Dimensionen ≥ 7.
4. Commit + Push ins Repo.
