---
title: "Übungen & Rückfragen-Drill – DAC"
tags: [VWIF, DAC, Übungen]
---

# Übungen & Rückfragen-Drill

> [!info] Zahlen sind absichtlich andere als auf den Folien – so prüfst du, ob du die Formel kannst. Alle Lösungen sind mit Python nachgerechnet (`_prep/verify_dac.py`).

## Rechnen

**U1** · 4-Bit-DAC, U_ref = 8 V: Welche Spannung bei **1010**?
> [!success]- Lösung
> 1010₂ = 10 → 10 · 0,5 V = **5,0 V** (4 V + 1 V)

**U2** · Gleicher DAC: Welcher Code für **3 V**?
> [!success]- Lösung
> 3 V / 0,5 V = 6 → **0110₂**

**U3** · 8-Bit-DAC, U_ref = 2,56 V: LSB? Spannung bei Code **200**?
> [!success]- Lösung
> LSB = 2,56 V / 256 = **10 mV** · 200 · 10 mV = **2,00 V**

**U4** · 10-Bit-DAC, U_ref = 5 V: größte Ausgangsspannung?
> [!success]- Lösung
> 1023 / 1024 · 5 V ≈ **4,995 V** (es fehlt 1 LSB ≈ 4,9 mV)

**U5** · Sinus-Tabelle mit **32 Werten**, DAC-Takt **48 kHz**: Signalfrequenz?
> [!success]- Lösung
> 48 kHz / 32 = **1,5 kHz**

**U6** · Unsere 16-Werte-Tabelle soll einen **2-kHz**-Sinus liefern. Welcher Takt?
> [!success]- Lösung
> 2 kHz · 16 = **32 kHz** (oder bei 16 kHz jeden zweiten Wert ausgeben)

**U7** · Tabelle mit **32 Werten**: um wie viele Einträge versetzt liest man den Cosinus?
> [!success]- Lösung
> ¼ · 32 = **8**

**U8** · DAC-Takt 48 kHz: höchste Signalfrequenz?
> [!success]- Lösung
> unter 48 / 2 = **24 kHz**

**U9** · R-2R-DAC (4 Bit, 8 V) gibt bei 1010 leer 5 V aus. Was misst du an einer Last von genau R ohne Puffer?
> [!success]- Lösung
> Innenwiderstand R + Last R → Spannungsteiler 1 : 1 → **2,5 V**

## Fehler finden („Ein Azubi sagt …“)

**F1:** „Ein 8-Bit-R-2R-DAC braucht Widerstände von R bis 128R.“
> [!success]- Lösung
> Das gilt für **gewichtete** Widerstände. R-2R braucht nur **R und 2R**.

**F2:** „Der DAC liefert direkt einen glatten Sinus, das Filter ist nur Zierde.“
> [!success]- Lösung
> Am DAC ist es eine **Treppe**; erst der **Tiefpass** (Rekonstruktionsfilter) macht daraus einen glatten Sinus.

**F3:** „Mit 16 kHz Takt kann ich auch einen 10-kHz-Sinus ausgeben.“
> [!success]- Lösung
> Abtasttheorem: Signal **< halber Takt** → **unter 8 kHz**.

**F4:** „4-Bit-DAC an 8 V: Code 1111 gibt 8 V aus.“
> [!success]- Lösung
> **15/16 · 8 V = 7,5 V** – U_ref wird nie ganz erreicht.

## Teach-back (je 45 s laut, Stoppuhr)

| Nr. | Auftrag | Muss drin sein |
|---|---|---|
| T1 | „Warum brauchen wir überhaupt einen DAC?“ | digital speichern · analog hören/bewegen · Kette · Gegenstück zum ADC |
| T2 | „Wie funktioniert ein R-2R-Netzwerk?“ | zwei Werte · Schalter an U_ref/Masse · Beitrag halbiert sich je Stufe · Bitgewichte · Puffer |
| T3 | „Wie macht man aus Zahlen einen Sinus – und den Cosinus?“ | Tabelle · Takt · Treppe · Tiefpass · ¼ Periode versetzt · Abtasttheorem |

## Rückfragen-Drill

Die Fragen stehen mit Musterantworten in [[dac/02_QA_Vorbereitung|DAC-Q&A]] und im DAC-Trainer (Modus „Rückfragen“, Filter „nur ⭐“). Ablauf: Frage lesen → **30 s laut antworten** → aufdecken → sicher / wackelig / falsch. Wackelige einmal mit der Musterantwort nachsprechen.

**Die 8 ⭐-Fragen:** Q1 ADC vs. DAC · Q2 nie ganz U_ref · Q5 warum R-2R · Q6 warum halbiert · Q8 wozu OpAmp · Q11 wozu Tiefpass · Q12 2-kHz-Sinus · Q15 wo Sinus + Cosinus

> [!tip] Wenig Zeit? Diese 5 zuerst: **Q2, Q5, Q6, Q8, Q11** (je 20 s).
