---
title: "Q&A-Vorbereitung – DAC"
tags: [VWIF, DAC, Q&A]
---

# Q&A-Vorbereitung: DAC

> [!info] Legende
> ⭐ = sehr wahrscheinliche Frage · Antwortstruktur: *1 Satz Antwort → 1 Satz Begründung/Beispiel* (≈ 30 s) · `[B1]` = passende Backup-Folie

## Grundlagen

| ⭐ | Nr. | Frage | Musterantwort |
|---|---|---|---|
| ⭐ | Q1 | Was ist der Unterschied zwischen ADC und DAC? | Der ADC macht aus einer analogen Spannung eine Zahl, der DAC aus einer Zahl wieder eine Spannung. Beide arbeiten mit Stufen (LSB) und einem Takt – der DAC ist quasi der ADC rückwärts. |
| ⭐ | Q2 | Warum erreicht der DAC nie ganz U_ref? | Der größte Code ist 2ⁿ − 1, also kommt maximal (2ⁿ − 1)/2ⁿ · U_ref heraus – beim 4-Bit-Beispiel 15/16 · 8 V = 7,5 V. Es fehlt immer genau 1 LSB. |
| | Q3 | Wie groß ist das LSB bei 8 Bit und 3,3 V? | U_ref / 2⁸ = 3,3 V / 256 ≈ 12,9 mV. |
| | Q4 | Kann ein DAC auch negative Spannungen ausgeben? | Direkt nicht – unser Sinus liegt um die Mitte (Code 128 ≈ ½ U_ref). Den Gleichanteil trennt man mit einem Kondensator ab oder verschiebt ihn mit einem OpAmp; dann schwingt das Signal um 0 V. |

## R-2R-Netzwerk

| ⭐ | Nr. | Frage | Musterantwort |
|---|---|---|---|
| ⭐ | Q5 | Warum R-2R und nicht einfach gewichtete Widerstände? | Gewichtete Widerstände brauchen für 8 Bit Werte von R bis 128 R, die alle extrem genau sein müssen. R-2R kommt mit zwei Werten aus – die lassen sich auf einem Chip viel genauer herstellen und abgleichen. `[B2]` |
| ⭐ | Q6 | Warum halbiert sich der Beitrag mit jeder Stufe? | Alles rechts von einem Knoten wirkt wie eine Spannungsquelle mit Innenwiderstand R; mit dem Längs-R sind das 2R. Zusammen mit dem 2R-Zweig am nächsten Knoten entsteht ein Spannungsteiler 1 : 1 → der Beitrag jedes Bits halbiert sich pro Stufe Richtung Ausgang. Ganz rechts beginnt es mit 2R ∥ 2R = R. (Beim Strommodus-R-2R halbiert sich tatsächlich der Strom an jedem Knoten.) `[B1]` |
| | Q7 | Wie viele Widerstände braucht ein 8-Bit-R-2R? | 2n = 16 Stück, aber nur zwei verschiedene Werte. |
| ⭐ | Q8 | Wozu der Operationsverstärker am Ausgang? | Das Netzwerk hat einen Innenwiderstand von R. Hängt man eine Last dran, bricht die Spannung ein – bei einer Last von genau R würden aus 6,5 V nur 3,25 V. Der OpAmp als Puffer liefert die Spannung, ohne das Netzwerk zu belasten. |
| | Q9 | Warum müssen die Widerstände so genau sein? | Das MSB trägt die halbe Spannung. Ist sein 2R-Zweig nur 2 % zu groß, sinkt bei 8 Bit die Spannung beim Schritt von Code 127 auf 128 sogar (−15 mV statt +10 mV) – der DAC ist dann nicht mehr monoton. `[B2]` |
| | Q10 | Was heißt „monoton“? | Steigt der Code, darf die Ausgangsspannung nie sinken. Für Regelungen ist das wichtig, sonst „schwingt“ der Regler. |

## Sinus, Tiefpass, Takt

| ⭐ | Nr. | Frage | Musterantwort |
|---|---|---|---|
| ⭐ | Q11 | Wozu braucht man den Tiefpass? Was passiert ohne? | Ohne Filter bleibt die Treppe mit ihren Kanten – das sind hochfrequente Anteile oberhalb des halben Takts, beim Audio zum Beispiel als Störgeräusch. Der Tiefpass (Rekonstruktionsfilter) lässt nur den gewünschten Sinus durch. |
| ⭐ | Q12 | Wie würdest du einen 2-kHz-Sinus erzeugen? | Entweder den Takt auf 32 kHz verdoppeln oder bei 16 kHz nur jeden zweiten Tabellenwert ausgeben (8 Werte pro Periode). So arbeiten Funktionsgeneratoren mit Direct Digital Synthesis (DDS). |
| | Q13 | Was passiert, wenn ich ein Signal über dem halben Takt ausgeben will? | Das geht nicht korrekt – das Abtasttheorem gilt auch rückwärts. Bei 16 kHz Takt muss das Signal unter 8 kHz bleiben; darüber entstehen falsche Frequenzen. |
| | Q14 | Reichen 16 Werte pro Periode? | Für die Demonstration ja – der Tiefpass glättet. Mehr Werte machen die Treppe feiner und das Filtern leichter; in der Praxis nimmt man oft 256 oder mehr Werte pro Periode. |
| ⭐ | Q15 | Wo braucht man Sinus und Cosinus gleichzeitig? | Zum Beispiel beim Schrittmotor im Mikroschrittbetrieb: Spule A bekommt einen sinus-, Spule B einen cosinusförmigen Strom, dann dreht er gleichmäßig. Auch in der Funktechnik (I/Q-Signale) und bei Messgebern (Resolver) braucht man das Paar. |
| | Q16 | Warum ist der Cosinus „geschenkt“? | cos(x) = sin(x + 90°). 90° sind eine Viertelperiode – bei 16 Tabellenwerten liest man also ab Index + 4 (4 Einträge voraus). |
| | Q17 | Woher kommt der Takt? | Von einem Timer im Mikrocontroller (oft mit DMA, damit die CPU frei bleibt). Bei Audio liefert ihn die digitale Audioschnittstelle, zum Beispiel I²S. |

## Praxis

| ⭐ | Nr. | Frage | Musterantwort |
|---|---|---|---|
| | Q18 | Hat der Arduino Uno einen DAC? | Der klassische Uno R3 nicht: `analogWrite()` erzeugt PWM, erst mit RC-Tiefpass entsteht eine (wellige) Gleichspannung – ein „Ersatz-DAC“. Der neuere Uno R4 hat dagegen einen echten 12-Bit-DAC an Pin A0. |
| | Q19 | Wie viele Bit hat ein Audio-DAC? | CD-Qualität: 16 Bit (65 536 Stufen, ≈ 96 dB Dynamik). HiFi- und Studio-DACs meist 24 Bit, gebaut als Sigma-Delta-Wandler. |
| | Q20 | Was ist ein Sigma-Delta-DAC? | Er arbeitet mit sehr hohem Takt und nur wenigen Stufen (oft 1 Bit). Durch die schnelle Folge und einen Filter entsteht im Mittel eine sehr feine Auflösung – deshalb ist er Standard bei Audio. |
| | Q21 | Was ist die Einschwingzeit? | Die Zeit, bis der Ausgang nach einem Codewechsel bis auf ±½ LSB beim neuen Wert angekommen ist. Sie begrenzt, wie schnell ein DAC Werte ausgeben kann. |
| | Q22 | Welche Datenmenge braucht CD-Audio? | 44 100 Werte/s · 16 Bit · 2 Kanäle ≈ 1,41 Mbit/s, also rund 10,6 MB pro Minute (unkomprimiert). |
| | Q23 | Erreicht der ESP32-DAC auch nie U_ref? | Espressif rechnet mit Code/255 · VDD – dort entspricht Code 255 der vollen Versorgungsspannung, eine andere Normierung. Das Prinzip „Stufen von 1 LSB“ bleibt gleich. Nur ESP32 und ESP32-S2 haben DACs, S3/C3/C6 nicht. |

> [!tip] Wenn du etwas nicht weißt
> „Das weiß ich gerade nicht sicher – ich schaue es nach und sage dir Bescheid.“ Nicht raten.
