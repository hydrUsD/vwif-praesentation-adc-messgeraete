---
title: "Vortragstraining – Stichwortkarte, Überleitungen, Timing"
tags: [VWIF, Vortrag]
---

# Vortragstraining (15-Min-Fassung)

## Einstieg und Schluss – wörtlich auswendig

> [!quote] Einstieg (Folie 1 → 2)
> „Guten Morgen! Ich zeige euch heute, was eigentlich passiert, wenn wir mit dem Multimeter messen – und wie aus einer analogen Spannung am Ende eine Zahl auf dem Display wird.“

> [!quote] Schluss (Folie 15)
> „Zusammengefasst: Erstens – Voltmeter parallel und hochohmig, Amperemeter in Reihe und niederohmig. Zweitens – der ADC tastet ab, quantisiert und codiert, und die Bitzahl bestimmt die Auflösung. Drittens – im Multimeter läuft alles auf eine Spannungsmessung mit einem ADC hinaus. Vielen Dank für eure Aufmerksamkeit – habt ihr Fragen?“

**Warum auswendig?** Die ersten 30 Sekunden entscheiden über die Nervosität, und der letzte Satz bleibt beim Publikum hängen. Alles dazwischen sprichst du frei nach Stichworten.

---

## Stichwortkarte

Zum Ausdrucken oder als zweiter Bildschirm. Pro Folie höchstens 5 Stichworte und die Zahl, die du nennen musst.

| # | Folie | Stichworte | Zahl/Merksatz | Soll-Ende |
|---:|---|---|---|---:|
| 1 | Titel | Begrüßung · Multimeter · Spannung → Zahl | – | 0:20 |
| 2 | Messkette | 5 Glieder · meine 3 Teile | – | 1:00 |
| 3 | Warum? | analog stufenlos · digital endlich · ADC = Brücke | – | 1:45 |
| 4 | Voltmeter | parallel · hochohmig · 10 MΩ · Belastungsfehler | **4,76 V** statt 5 V (Zeiger 1,43 V) | 3:00 |
| 5 | Amperemeter | in Reihe · niederohmig · Shunt U = I·R · Bürdenspannung | **192 mA** statt 200 mA | 4:15 |
| 6 | Messbereich *(opt.)* | Vorwiderstand Reihe · Shunt parallel · n | R_V = (n−1)·Rᵢ → **99 kΩ** | 5:15 |
| 7 | U-/I-richtig *(opt.)* | kleines R → spannungsrichtig · großes R → stromrichtig | – | 6:00 |
| 8 | Sicherheit | Strombuchse = Kurzschluss · Buchse–Schalter–Bereich · CAT I–IV | CAT IV = Zähler | 7:00 |
| 9 | ADC-Idee | Abtasten · Quantisieren · Codieren · Treppe | – | 8:00 |
| 10 | Auflösung | 2ⁿ · LSB = U_ref/2ⁿ · ±½ LSB · Arduino | **4,88 mV** · **512** | 9:15 |
| 11 | Nyquist | > 2·f_max · Aliasing · Wagenrad · Tiefpass | CD 44,1 kHz | 10:15 |
| 12 | Verfahren | Flash schnell · SAR Arduino · Dual-Slope Multimeter · ΣΔ fein | 255 Komparatoren (8 Bit) | 11:30 |
| 13 | SAR *(opt.)* | Zahlenraten · Bit für Bit · n Schritte | **1011₂ = 11** | 12:30 |
| 14 | Multimeter | Teiler · Shunt · ADC · Counts · Toleranz lesen | **98,8 … 101,2 V** | 13:45 |
| 15 | Fazit | 3 Take-aways · Danke · Fragen | – | 14:30 |

---

## Zeit-Checkpoints

Bei Probevortrag 1 und 2 jeweils die Uhrzeit am **Ende** der Folie eintragen.

| Checkpoint | Soll | Durchgang 1 | Durchgang 2 | Reaktion, wenn > 30 s zu spät |
|---|---:|---:|---:|---|
| Ende Folie 5 | 4:15 | | | 30–60 s zu spät: Folie 7 überspringen (spart 0:45) · > 60 s: Folie 6 + 7 (spart 1:45) |
| Ende Folie 8 | 7:00 | | | Folie 11: CD-Beispiel weglassen |
| Ende Folie 12 | 11:30 | | | Folie 13 überspringen (→ spart 1:00) |
| Ende Folie 14 | 13:45 | | | Fazit nur die 3 Take-aways, kein Zusatz |

---

## Überleitungen

Ein Satz am Ende jeder Folie, der zur nächsten führt. Dann wirkt der Vortrag wie aus einem Guss.

| Von → nach | Überleitungssatz |
|---|---|
| 1 → 2 | „Damit ihr wisst, wohin die Reise geht, hier erst einmal der rote Faden.“ |
| 2 → 3 | „Bevor wir ins Detail gehen: Warum brauchen wir das überhaupt?“ |
| 3 → 4 | „Bevor irgendetwas umgewandelt werden kann, muss man aber erst einmal richtig messen. Fangen wir mit der Spannung an.“ |
| 4 → 5 | „Beim Strom ist es genau umgekehrt.“ |
| 5 → 6 | „Wie kommt so ein Messgerät eigentlich zu verschiedenen Messbereichen?“ |
| 6 → 7 | „Und wenn ich Spannung und Strom gleichzeitig messen will, muss ich mich entscheiden …“ |
| 7 → 8 | „Bevor wir zum ADC kommen, ein Punkt, der in der Praxis wirklich wichtig ist: die Sicherheit.“ |
| *5 → 8 (ohne 6/7)* | „Ein Punkt ist dabei in der Praxis besonders wichtig: die Sicherheit.“ |
| 8 → 9 | „Jetzt haben wir eine Spannung sauber gemessen – aber wie wird daraus eine Zahl? Dafür gibt es den ADC.“ |
| 9 → 10 | „Wie fein diese Treppe ist, hängt von der Bitzahl ab.“ |
| 10 → 11 | „Das war die Feinheit in der Höhe – aber wie oft muss ich eigentlich hinschauen?“ |
| 11 → 12 | „Und wie macht so ein Wandler das technisch? Da gibt es verschiedene Bauarten.“ |
| 12 → 13 | „Schauen wir uns den SAR-Wandler aus dem Arduino einmal genauer an.“ |
| 13 → 14 | „Jetzt haben wir alle Bausteine – und die stecken alle in einem Gerät, das ihr jeden Tag benutzt.“ |
| *12 → 14 (ohne 13)* | „Jetzt haben wir alle Bausteine – und die stecken alle in einem Gerät, das ihr jeden Tag benutzt.“ |
| 14 → 15 | „Damit sind wir einmal durch die ganze Messkette gegangen. Zusammengefasst …“ |

---

## Selbstbewertung Probevortrag

Direkt nach jedem Durchgang ausfüllen (1 = schlecht, 3 = gut).

| Kriterium | D1 | D2 | Notiz |
|---|---:|---:|---|
| Einstieg flüssig, ohne Ablesen | | | |
| Zeit eingehalten (14:00–14:45) | | | |
| Überleitungen gesagt | | | |
| Zahlen richtig genannt (4,76 V · 192 mA · 4,88 mV · 512 · 98,8…101,2 V) | | | |
| Ins Publikum geschaut statt auf die Folie | | | |
| Füllwörter („ähm“, „sozusagen“) selten | | | |
| Schluss mit 3 Take-aways + klarer Frage-Einladung | | | |
| **Schwächste 2 Folien:** | | | → in Block 4 üben |

---

## Notfallpläne

| Situation | Was du tust/sagst |
|---|---|
| **Zeit wird knapp** (Checkpoint verpasst) | Optionale Folie überspringen: „Wie man den Messbereich erweitert, zeige ich gern bei Rückfragen – ich springe direkt zur Sicherheit.“ |
| **Blackout** | Auf die Folie schauen, Kernaussage (fett) vorlesen, dann Stichwortkarte. Eine kurze Pause wirkt souverän, nicht unsicher. |
| **Rückfrage mitten im Vortrag** | Kurz beantworten, wenn ≤ 20 s; sonst: „Gute Frage – darauf komme ich gleich auf Folie X“ bzw. „… nehme ich gern am Ende auf.“ |
| **Frage, die du nicht beantworten kannst** | „Das weiß ich gerade nicht sicher – ich schaue es nach und gebe dir danach Bescheid.“ (Nicht raten!) |
| **Technik streikt** | PDF-Version auf USB-Stick; Notfalls frei am Whiteboard: Messkette aufzeichnen und daran entlang erzählen. |
| **Rechenfehler auf der Folie bemerkt** | Kurz korrigieren: „Kleine Korrektur – richtig ist …“, dann weiter. |
