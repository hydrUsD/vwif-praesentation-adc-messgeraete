# Phase 3 – Qualitäts-Gate (Rubrik B)

## Prüfschritte
1. `verify_dac.py`: R-2R per Knotenanalyse (alle 16 Codes = Formel), Toleranzstudie (MSB-2R +2 % → −15 mV, −2 % → +36 mV), Sinus-/Cosinus-Tabelle, alle Übungswerte – ok.
2. Beamer kompiliert (Lang- und Kurzfassung), keine Overfull-Boxen; Folien optisch geprüft.
3. App-Laufzeittest (Chromium, 400 px, hell/dunkel): keine Fehler, 28 Karten / 18 Aufgaben / 23 Rückfragen (8 ⭐).
4. Unabhängiger Review-Subagent: 15 Befunde, 0 Rechenfehler.

## Umgesetzte Befunde
| # | Befund | Umsetzung |
|---|---|---|
| 1 | „Strom halbiert sich“ gilt streng nur im Strommodus | überall „Beitrag halbiert sich je Stufe“ + Thevenin-Erklärung; Strommodus als Rückfrage-Extra |
| 2 | Cosinus „4 früher“ mehrdeutig | einheitlich „ab Index + 4“ |
| 3 | Lernplan überladen | Karten auf 14 (R-2R + Sinus), Einstieg/Schluss im Probevortrag, Kurz-Drill Q2/Q5/Q6/Q8/Q11 |
| 4 | Wikilinks mehrdeutig | `[[dac/…]]` |
| 5 | Offline-App fehlte | `lernen/08_DAC-Trainer.html` |
| 6 | Arduino Uno R4 hat DAC | Q18 + Karte präzisiert |
| 7–15 | Monotonie „2 % zu groß“, ESP32 (/255, Varianten → Q23), „unter 8 kHz“, Ausgaberate, Backup-Nummern, IDs, Checkpoint, Mermaid gespiegelt, `*und*` | umgesetzt |
| Aktivierung | Publikum nicht einbezogen | Frage „Was kommt bei 1101 raus?“ auf Folie 3 |

## Bewertung (Schwelle ≥ 7)
| Dimension | Review | nachher |
|---|---:|---:|
| Korrektheit | 8 | 9 |
| Didaktische Eignung | 8 | 8 |
| Ziel-/Format-Treue | 9 | 9 |
| Scope-Treue | 9 | 9 |
| Klarheit | 8 | 9 |
| Aktivierung | 6 | 8 |
