# Phase 3 – Qualitäts-Gate (Rubrik B: Deliverables)

## Prüfschritte
1. **Empirisch:** `verify_uebungen.py <app.html>` rechnet alle Übungs-, Präsentations- und Rückfragen-Zahlen nach und prüft die App-Toleranzen (inkl. „Fehlformel R4 darf nicht akzeptiert werden“). Ergebnis: alle Werte korrekt.
2. **Laufzeit-Test der App** (Playwright/Chromium, 400 px, hell + dunkel): keine JS-Fehler, kein horizontales Scrollen. Geprüft: Flip, Bewertung, Abschluss-Banner, Eingabeprüfung, Rückfragen-Timer, gemerkte „Nochmal“-Karten nach Neuladen, gemischte MC-Optionen.
3. **Unabhängiger Review-Subagent** (paper-reviewing, zweckentfremdet): 19 Befunde, davon 0 Rechenfehler. Die Wikilinks und die Soll-Zeiten der Stichwortkarte bestätigte er als korrekt.

## Umgesetzte Review-Befunde
| # | Befund | Umsetzung |
|---|---|---|
| 1 | ±½ LSB vs. Abrunden | Karte präzisiert, Hinweis in R9a, neue Rückfrage N13 (MD + App) |
| 2 | R6b-Rundungsregel fehlt | Regel „abgerundet“ in Frage (MD + App) |
| 3 | R4 trennt Formelfehler nicht | neu: 1 mA, n = 20, R_N = 105,3 Ω (falsch: 100 Ω), Toleranz ±0,5 |
| 4 | MC-Lösung immer 2. Option | Optionen werden je Durchgang gemischt |
| 5–7, 16 | Zeitblöcke unrealistisch / Drill widersprüchlich | Plan neu getaktet (Probevorträge je 18 min, Block 2 entschlackt, Drill in zwei Runden, Notfall-Drill nach Durchgang 2, Sprachmemo-Tipp), Gewichtung korrigiert |
| 8 | Checkpoint-Reaktion überkompensiert | gestuft: 30–60 s → Folie 7, > 60 s → 6 + 7 |
| 9 | Flash „je Stufe“ | „je Schwelle (2ⁿ − 1)“ (MD + App) |
| 10 | F2 pedantisch | F2 neu: nur Auflösung ≠ Genauigkeit (mit 50-mV-Beispiel) |
| 11 | R11b mehrdeutig | manuell → OL; Autorange → 40-V-Bereich |
| 12 | Toleranzen zu eng | R2 ±1, P2 ±0,03, R5 ±0,005 |
| 13 | Antwort blitzt beim Kartenwechsel auf | Rückdrehung ohne Animation |
| 14 | Kein Speicher, Bewertungen vermischt | „Nochmal“-Karten in localStorage; LCD zählt nur noch Rechnen |
| 15 | „5 Zahlen“ uneinheitlich | 192 mA statt 1011₂ |
| 17 | `::` im Infotext erzeugt Müllkarten | umformuliert |
| 18 | Kleinkram | R1-Merksatz, Link + Offline-Kopie, Docstring/Prüfumfang des Skripts |
| 19 | Interleaving nur dem Namen nach | „verteilte Wiederholung“ benannt; echtes Mischen morgen früh (App → Mischen) |

## Bewertung nach Überarbeitung (Schwelle ≥ 7)
| Dimension | Review vorher | nachher | Begründung |
|---|---:|---:|---|
| Korrektheit | 8 | 9 | alle Zahlen skriptgeprüft; Konventionsfrage LSB aufgelöst |
| Didaktische Eignung | 7 | 8 | realistische Blöcke, Abruf vor Lesen, Teach-back, verteilte Wiederholung |
| Ziel-/Format-Treue | 8 | 9 | Obsidian-MD + interaktive App + Offline-Kopie, 15-Min-Fassung |
| Scope-Treue | 8 | 8 | Zusatzwissen [LB]/🎓 gekennzeichnet, Präsentationsinhalt unverändert |
| Klarheit | 7 | 8 | Drill-Ablauf eindeutig, mehrdeutige Aufgaben präzisiert |
| Aktivierung | 8 | 9 | gemischte MC, kein Aufblitzen, Timer, Eingabeprüfung |

**Transparente Grenze:** Für Rückfragen bleiben 20 statt der geplanten ~25 min, plus 2 min „Zahlen auf Zuruf“. Die gewonnene Zeit ging bewusst an die Probevorträge, weil 15-min-Blöcke für 14:30 Vortrag nicht realistisch waren.
