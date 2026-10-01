---
title: "Spickzettel – ADC, Amperemeter, Voltmeter"
tags: [VWIF, Spickzettel]
---

# Spickzettel (1 Seite)

> Druckfertige Version: `spickzettel/spickzettel.tex` (1 Seite A4).

## Die 3 Kernaussagen
1. **Voltmeter parallel & hochohmig – Amperemeter in Reihe & niederohmig**
2. **ADC = Abtasten → Quantisieren → Codieren**
3. **Im Multimeter:** jede Messung = Spannungsmessung + ADC

## Messgeräte

| | Voltmeter | Amperemeter |
|---|---|---|
| Anschluss | parallel | in Reihe |
| idealer $R_i$ | ∞ | 0 |
| real (DMM) | ≈ 10 MΩ | Shunt (mΩ … Ω) |
| Fehler | Belastungsfehler | Bürdenspannung |
| Falsch angeschlossen | in Reihe → Schaltung geht nicht, ungefährlich | parallel → **Kurzschluss!** |

- Messbereichserweiterung: $n = \frac{\text{neu}}{\text{alt}}$, $R_V = (n-1)R_i$, $R_N = \frac{R_i}{n-1}$
- Kleines R → spannungsrichtig · großes R → stromrichtig
- CAT IV Hausanschluss · CAT III Verteiler/Installation · CAT II Steckergeräte · CAT I/0 ohne Netz

## ADC – Formeln

| Größe | Formel | Beispiel (10 Bit, 5 V) |
|---|---|---|
| Stufen | $2^n$ | 1024 |
| LSB | $U_\text{ref}/2^n$ | 4,88 mV |
| Code | $\lfloor U_\text{ein} \cdot 2^n / U_\text{ref} \rfloor$ | 2,5 V → 512 |
| Spannung aus Code | $\text{Code} \cdot U_\text{ref}/2^n$ | 300 → 1,46 V |
| Quantisierungsfehler | ±½ LSB | ±2,44 mV |
| Abtasttheorem | $f_A > 2 f_\text{max}$ | CD: 44,1 kHz ↔ 20 kHz |
| Alias (einfacher Fall) | $\lvert f_A - f_\text{sig} \rvert$ | 15 kHz − 10 kHz = 5 kHz |

8 Bit 19,5 mV · 10 Bit 4,88 mV · 12 Bit 1,22 mV · 16 Bit 76 µV (je bei 5 V)

## Wandlertypen
- **Flash:** sehr schnell, grob, $2^n-1$ Komparatoren → Oszilloskop
- **SAR:** Bit für Bit (n Schritte), Kompromiss → Mikrocontroller/Arduino
- **Dual-Slope:** langsam, genau, störfest → Multimeter (ICL7106)
- **Sigma-Delta:** sehr hohe Auflösung → Audio, Waagen

## Rechenbeispiele (geprüft)
- Spannungsteiler 2 × 1 MΩ an 10 V: DMM (10 MΩ) zeigt **4,76 V** statt 5 V; Zeigerinstrument (200 kΩ) **1,43 V**
- 5 V / 25 Ω mit 1-Ω-Shunt: **192 mA** statt 200 mA
- SAR 4 Bit, $U_\text{ref}$ 16 V, 11,3 V → **1011₂ = 11**
- ±(1 % + 2 Digits) bei 100,0 V → **98,8 … 101,2 V**
- 3½ Stellen = 1999 Counts; 6000 Counts im 6-V-Bereich → 1 mV Auflösung
