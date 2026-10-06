---
title: "Spickzettel – DAC"
tags: [VWIF, DAC, Spickzettel]
---

# Spickzettel: DAC (1 Seite)

## Formeln
| Größe | Formel | Beispiel (4 Bit, U_ref = 8 V) |
|---|---|---|
| Stufen | 2ⁿ | 16 |
| LSB | U_ref / 2ⁿ | 0,5 V |
| Ausgang | U_aus = Code / 2ⁿ · U_ref | 1101₂ = 13 → **6,5 V** |
| Maximum | (2ⁿ − 1) / 2ⁿ · U_ref | 1111₂ → 7,5 V |
| Bitgewichte | ½ · ¼ · ⅛ · 1/16 · U_ref | 4 V · 2 V · 1 V · 0,5 V |
| Signalfrequenz | f = Takt / Werte pro Periode | 16 kHz / 16 = **1 kHz** |
| Abtasttheorem | f_Signal < Takt / 2 | unter 8 kHz |
| Cosinus-Versatz | Index + ¼ der Tabellenlänge | 16 Werte → **+4** |

## R-2R in 4 Sätzen
1. Nur zwei Werte: **R** (Längszweig) und **2R** (Querzweige + Abschluss); n Bit → 2n Widerstände.
2. Bit = 1 → Zweig an U_ref, Bit = 0 → an Masse.
3. Rechts von jedem Knoten: Ersatzquelle mit R, + Längs-R = 2R, mit dem nächsten 2R-Zweig → Teiler 1 : 1 → **Beitrag halbiert sich pro Stufe** → binäre Gewichte.
4. Innenwiderstand R → **OpAmp-Puffer** am Ausgang.

## Sinus-Tabelle (16 Werte, 8 Bit, Mitte 128)
`128 177 218 245 255 245 218 177 128 79 38 11 1 11 38 79`
Cosinus: dieselbe Tabelle ab Index + 4 → `255 245 218 177 128 …`

## Zahlen auf Abruf
| | |
|---|---|
| CD-Audio | 16 Bit · 44,1 kHz · 2 Kanäle → 1,41 Mbit/s ≈ 10,6 MB/min |
| 16 Bit | 65 536 Stufen |
| 8 Bit | 256 Stufen; bei 3,3 V: LSB ≈ 12,9 mV |
| ESP32 | 2 × 8-Bit-DAC (GPIO25/26), Cosinus-Generator |
| Gewichtete Widerstände 8 Bit | R … 128R (Verhältnis 1 : 128) |
| R-2R an Last R | 6,5 V → 3,25 V (deshalb Puffer) |

## Kette
Mikrofon → ADC → Speicher (Festplatte/SSD) → **DAC** → Verstärker → Lautsprecher
