---
title: "20-min-Lernplan – DAC-Vortrag heute"
tags: [VWIF, DAC, Lernplan]
---

# 20-min-Lernplan: „Vom Bit zurück zum Signal“

> [!info] Spielregeln
> - **Erst abrufen, dann nachsehen** – das Abrufen ist das eigentliche Lernen.
> - Stoppuhr bereitlegen, Blatt + Stift.
> - Interaktiv: [DAC-Trainer](https://claude.ai/artifact/K8UNUj2Kbf35vGjgmjNM26) (privat, nur mit deinem Claude-Konto) oder offline `08_DAC-Trainer.html` in diesem Ordner.

| Zeit | Block | Was du tust |
|---|---|---|
| 0:00–0:02 | **Kaltstart** (Unterlagen zu!) | Auf ein Blatt: die Kette (Mikrofon → … → Lautsprecher), die Formel U_aus = Code/2ⁿ · U_ref, die **3 Take-aways**. Dann mit dem [[dac/03_Spickzettel|DAC-Spickzettel]] vergleichen. |
| 0:02–0:07 | **Karteikarten** | DAC-Trainer → Karteikarten → nur **R-2R-Netzwerk** und **Sinus & Filter** (14 Karten). Antwort **laut** sagen, dann umdrehen. |
| 0:07–0:09 | **Rechnen** | DAC-Trainer → Rechnen & Fehler: **U1, U2, U5, U7** und **F1–F4**. |
| 0:09–0:16 | **Probevortrag** (stehend, laut, Stoppuhr) | Nur mit der [[#Stichwortkarte]], **Einstieg und Schluss wörtlich**. Ziel **5:00–5:45**. Ende Folie 4 bei ≈ 3:05? Danach 1 min: schwächste Stelle einmal wiederholen. |
| 0:16–0:20 | **Rückfragen** | DAC-Trainer → Rückfragen → **„nur ⭐“**. Wenn die Zeit knapp wird: nur **Q2, Q5, Q6, Q8, Q11**, je 20 s laut. |

> [!warning] Nur 5 Minuten?
> Einstieg + Schluss je 1× laut · Rechenbeispiel 1101 → 6,5 V einmal durchsprechen · ⭐-Fragen Q5 (warum R-2R) und Q11 (wozu Tiefpass) laut beantworten.

---

## Einstieg und Schluss – wörtlich

> [!quote] Einstieg
> „Hallo zusammen! Wir speichern heute fast alles digital – Musik, Videos, Messwerte. Aber hören, sehen und bewegen können wir nur analog. Wie die Zahlen wieder zu einem Signal werden, zeige ich euch in den nächsten fünf Minuten.“

> [!quote] Schluss
> „Zusammengefasst: Erstens – der DAC macht aus einem Code eine Spannung, Stufe für Stufe. Zweitens – im R-2R-Netzwerk reichen dafür zwei Widerstandswerte, weil sich der Beitrag mit jeder Stufe halbiert. Drittens – aus der Treppe wird mit einem Tiefpass ein glattes Signal, und Sinus und Cosinus kommen aus derselben Tabelle. Danke fürs Zuhören – habt ihr Fragen?“

---

## Stichwortkarte

| # | Folie | Stichworte | Zahl/Merksatz | Soll-Ende |
|---:|---|---|---|---:|
| 1 | Titel | digital speichern · analog hören/bewegen | – | 0:15 |
| 2 | Wozu? | Festplatte = Zahlen · Lautsprecher braucht Spannung · Kette · Gegenstück zum ADC | CD: 44 100 Werte/s, 16 Bit | 1:00 |
| 3 | Code → Spannung | Formel · 16 Stufen · LSB · Bitgewichte · **Publikum fragen: 1101?** · Treppe | **1101 → 4 + 2 + 0,5 = 6,5 V** · max 7,5 V | 1:55 |
| 4 | R-2R | gewichtet wäre R…128R · nur R und 2R · Beitrag halbiert je Stufe · Stufen anhängen · OpAmp-Puffer | ½ · ¼ · ⅛ · 1/16 | 3:05 |
| 5 | Sinus/Cosinus | Tabelle · Takt · Treppe → Tiefpass · Cosinus = Index + 4 · Schrittmotor · Abtasttheorem | **16 kHz / 16 = 1 kHz** · unter 8 kHz | 4:15 |
| 6 | Praxis *(opt.)* | Bit = Feinheit · Rate = Frequenz · ESP32 8 Bit + Cosinus · Audio 24 Bit Sigma-Delta | – | 5:00 |
| 7 | Fazit | 3 Take-aways · Danke · Fragen | – | 5:30 |

> [!tip] Zeit-Checkpoint
> Ende Folie 4 später als **3:30** → Folie 6 weglassen: „Wie gute DACs in der Praxis aussehen, erzähle ich gern bei Rückfragen.“ Ohne Folie 6 sparst du 45 s (Soll ohne Folie 6: 4:45).

## Überleitungen

| Von → nach | Satz |
|---|---|
| 2 → 3 | „Was macht so ein DAC eigentlich genau mit einer Zahl?“ |
| 3 → 4 | „Und wie baut man das in Hardware?“ |
| 4 → 5 | „Jetzt kann ich einzelne Spannungen ausgeben – aber wie wird daraus ein Signal, zum Beispiel ein Sinus?“ |
| 5 → 6 | „Ganz kurz noch, worauf man bei echten DACs achtet.“ |
| 5 → 7 *(ohne 6)* | „Damit sind wir einmal von der Zahl zurück zum Signal gekommen. Zusammengefasst …“ |
