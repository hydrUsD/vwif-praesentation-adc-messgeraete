# Recherche: DAC (Phase 2)

## Befunde (verdichtet)
| # | Befund | Quelle / Verifikation |
|---|---|---|
| 1 | Ausgangsspannung eines n-Bit-DAC: U = Code / 2ⁿ · U_ref; LSB = U_ref / 2ⁿ; Maximalwert (2ⁿ−1)/2ⁿ · U_ref (erreicht U_ref nie ganz) | [DE-WP DAU], Python: R-2R-Knotenanalyse für alle 16 Codes = Formel ✓ |
| 2 | R-2R: nur zwei Widerstandswerte im Verhältnis 2:1, n Bit → 2n Widerstände; jeder Knoten halbiert → MSB ½, dann ¼, ⅛ … | [ADI MT-015], [DE-WP R2R]; Sim: 1101 an 8 V → 6,5 V ✓ |
| 3 | Bin. gewichtetes Netzwerk: viele Werte, 8 Bit → Verhältnis 1:128, schwer genau zu fertigen, nicht inhärent monoton | [ADI MT-015]; Python 2⁷ = 128 ✓ |
| 4 | R-2R-Innenwiderstand = R → Last würde Spannung verfälschen → OpAmp-Puffer | [DE-WP R2R]; Sim: an Last R halbiert sich 6,5 V → 3,25 V ✓ |
| 5 | Toleranz kritisch v. a. beim MSB; Sim 8 Bit: MSB-2R +2 % → Schritt 127→128 = −15 mV (Ausgang *sinkt*, nicht monoton) | [DE-WP R2R]; Python ✓ |
| 6 | DAC-Ausgang ist Treppe (Zero-Order Hold); analoger Rekonstruktions-Tiefpass entfernt Anteile > f_s/2 und glättet | [DSPGuide Kap. 3] |
| 7 | Sinus aus Wertetabelle (Lookup-Table) → DAC → Tiefpass = Prinzip der Direct Digital Synthesis (Funktionsgeneratoren) | [WP DDS] |
| 8 | Cosinus = gleiche Tabelle, um ¼ Periode versetzt gelesen (16-Punkt-Tabelle: 4 Einträge) | Python: Tabelle 128+round(127·sin) und cos-Tabelle identisch ✓ |
| 9 | 16 Werte/Periode bei 16 kHz → 1 kHz; Nyquist: f_out < 8 kHz | Python ✓ |
| 10 | Audio-CD: 16 Bit (65 536 Stufen), 44,1 kHz, Stereo → 1,4112 Mbit/s ≈ 10,6 MB/min | Python ✓ (Lehrbuchwissen) |
| 11 | ESP32: zwei 8-Bit-DAC-Kanäle (GPIO25/26), eingebauter Cosinus-Generator, DMA-Dauerausgabe (Audio) | [ESP-IDF DAC] |

## Bewertung (Rubrik A)
| Dimension | Note | Begründung |
|---|---:|---|
| Genauigkeit | 9 | Alle Zahlen nachgerechnet, R-2R per Knotenanalyse simuliert |
| Quellenqualität | 8 | Hersteller-Tutorial (ADI), Datenblatt/Doku (Espressif), Lehrbuch (DSPGuide), Wikipedia nur ergänzend |
| Scope-Treue | 9 | DAC-Funktion + Sinus/Cosinus-Hinweis abgedeckt; Details nur für Q&A |
| Relevanz | 9 | Neue Beispiele (8-V-4-Bit, Audio, Funktionsgenerator, ESP32), kein Arduino/Multimeter |

Lücken: keine kritischen. Sinc-Kompensation bewusst nicht im Vortrag (zu tief).

## Plan (freigegeben: „direkt durchziehen“)
Folien (Soll-Ende): 1 Titel 0:15 · 2 Wozu? 1:00 · 3 Code→Spannung 1:55 · 4 R-2R 3:05 · 5 Sinus/Cosinus 4:15 · 6 Praxis ⏩ optional 5:00 · 7 Fazit 5:30 (ohne 6: 4:45)
Deliverables: dac/01–04 .md, dac/slides/dac.tex, dac/lernen/05–07 .md + 08 Trainer (.html), Artifact; Gate: Review-Subagent + Rubrik B + Push über Mac.
