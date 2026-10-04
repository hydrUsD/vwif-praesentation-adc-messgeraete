---
title: "Übungen – Rechnen, Fehler finden, Teach-back"
tags: [VWIF, Übungen]
---

# Übungen

> [!info] Benutzung
> Erst selbst rechnen bzw. laut antworten, **dann** die Lösung aufklappen (Klick auf den Pfeil). Die Zahlen sind **absichtlich andere** als in der Präsentation – so merkst du, ob du die Formel kannst und nicht nur das Ergebnis auswendig weißt. Alle Lösungen wurden mit Python nachgerechnet.

---

## R – Rechenaufgaben

### R1 · Belastungsfehler (Folie 4)
Spannungsteiler $R_1 = R_2 = 100\,\text{k}\Omega$ an $12\,\text{V}$. Du misst über $R_2$ mit einem DMM ($R_i = 10\,\text{M}\Omega$). Was zeigt es an, und wie groß ist der Fehler?

> [!success]- Lösung
> $R_2 \parallel R_i = \frac{100\,\text{k} \cdot 10\,\text{M}}{10{,}1\,\text{M}} \approx 99{,}01\,\text{k}\Omega$
> $U_2 = 12\,\text{V} \cdot \frac{99{,}01}{100 + 99{,}01} \approx \mathbf{5{,}97\,V}$ (statt 6,00 V) → Fehler **≈ −0,5 %**.
> **Merke:** Hier ist $R_2$ 100-mal kleiner als $R_i$ → Fehler klein. Bei 1 MΩ (Folie 4) war der Fehler ≈ 10-mal größer (4,8 % statt 0,5 %).

### R2 · Bürdenspannung (Folie 5)
Eine Last von $10\,\Omega$ hängt an $3\,\text{V}$. Das Amperemeter hat $R_i = 0{,}5\,\Omega$. Welcher Strom wird angezeigt, und wie groß ist die Bürdenspannung?

> [!success]- Lösung
> $I = \frac{3\,\text{V}}{10{,}5\,\Omega} \approx \mathbf{285{,}7\,mA}$ (statt 300 mA, **≈ −4,8 %**)
> Bürdenspannung $U = I \cdot R_i \approx 0{,}286\,\text{A} \cdot 0{,}5\,\Omega \approx \mathbf{0{,}14\,V}$.

### R3 · Vorwiderstand (Folie 6)
Messwerk: Vollausschlag $50\,\mu\text{A}$, $R_i = 2\,\text{k}\Omega$. Es soll bis $30\,\text{V}$ messen. Wie groß muss der Vorwiderstand sein?

> [!success]- Lösung
> Vollausschlag ohne Erweiterung: $50\,\mu\text{A} \cdot 2\,\text{k}\Omega = 0{,}1\,\text{V}$ → $n = 30 / 0{,}1 = 300$
> $R_V = (n-1) \cdot R_i = 299 \cdot 2\,\text{k}\Omega = \mathbf{598\,k\Omega}$
> Probe: $(598 + 2)\,\text{k}\Omega \cdot 50\,\mu\text{A} = 30\,\text{V}$ ✓

### R4 · Shunt (Folie 6)
Gleiches Messwerk ($50\,\mu\text{A}$, $2\,\text{k}\Omega$) soll bis $1\,\text{mA}$ messen. Wie groß ist der Shunt?

> [!success]- Lösung
> $n = 1\,\text{mA} / 50\,\mu\text{A} = 20$
> $R_N = \frac{R_i}{n-1} = \frac{2000\,\Omega}{19} \approx \mathbf{105{,}3\,\Omega}$
> Typischer Fehler: $R_i/n = 100\,\Omega$ – dann fließen durchs Messwerk 1 mA · 100/2100 ≈ 47,6 µA statt 50 µA.
> Probe: Messwerk 50 µA, Shunt $0{,}1\,\text{V} / 105{,}3\,\Omega = 950\,\mu\text{A}$ → zusammen 1 mA ✓

### R5 · LSB bei anderem ADC (Folie 10)
12-Bit-ADC, $U_\text{ref} = 3{,}3\,\text{V}$ (typisch für viele moderne Mikrocontroller). Wie groß sind LSB und Quantisierungsfehler? Welcher Code entsteht bei $1{,}65\,\text{V}$?

> [!success]- Lösung
> $U_\text{LSB} = 3{,}3\,\text{V} / 4096 \approx \mathbf{0{,}806\,mV}$ · Quantisierungsfehler $\pm\frac12$ LSB $\approx \mathbf{\pm 0{,}40\,mV}$
> Code $= \lfloor 1{,}65 \cdot 4096 / 3{,}3 \rfloor = \mathbf{2048}$ (genau die Hälfte von 4096 – wie 512 bei 10 Bit).

### R6 · Arduino rückwärts (Folie 10)
Arduino Uno (10 Bit, 5 V): `analogRead()` liefert **820**. Welche Spannung liegt an? Welchen Wert liefert er bei **3,3 V**? (Rechenregel wie auf Folie 10: Code = U · 1024 / U_ref, **abgerundet**.)

> [!success]- Lösung
> $U = 820 \cdot 5\,\text{V} / 1024 \approx \mathbf{4{,}00\,V}$
> Code bei 3,3 V: $\lfloor 3{,}3 \cdot 1024 / 5 \rfloor = \lfloor 675{,}8 \rfloor = \mathbf{675}$

### R7 · 12 V am Arduino messen (Rückfrage-Klassiker)
Du willst eine 12-V-Batterie mit dem Arduino (max. 5 V) messen. Davor schaltest du einen Spannungsteiler $R_1 = 15\,\text{k}\Omega$ (oben), $R_2 = 10\,\text{k}\Omega$ (unten, am ADC). (a) Welche Spannung sieht der ADC? (b) Welcher Code? (c) Wie rechnet man im Programm zurück?

> [!success]- Lösung
> (a) $U_\text{ADC} = 12 \cdot \frac{10}{25} = \mathbf{4{,}8\,V}$ (< 5 V ✓)
> (b) Code $= \lfloor 4{,}8 \cdot 1024 / 5 \rfloor = \mathbf{983}$
> (c) $U_\text{Batt} = \text{Code} \cdot \frac{5}{1024} \cdot \frac{R_1+R_2}{R_2} = 983 \cdot \frac{5}{1024} \cdot 2{,}5 \approx \mathbf{12{,}0\,V}$

### R8 · Abtasttheorem & Alias (Folie 11)
(a) Ein Signal enthält Frequenzen bis $3\,\text{kHz}$. Wie schnell muss mindestens abgetastet werden? (b) Ein $7\text{-kHz}$-Ton wird mit $10\,\text{kHz}$ abgetastet. Was „hört“ man?

> [!success]- Lösung
> (a) $f_A > 2 \cdot 3\,\text{kHz} = \mathbf{6\,kHz}$ (mehr als, nicht gleich!)
> (b) $7\,\text{kHz} > f_A/2 = 5\,\text{kHz}$ → Aliasing: $f_\text{alias} = 10 - 7 = \mathbf{3\,kHz}$

### R9 · SAR selbst durchführen (Folie 13)
(a) 4 Bit, $U_\text{ref} = 16\,\text{V}$ (1 LSB = 1 V), $U_\text{ein} = 6{,}7\,\text{V}$. Spiele die 4 Schritte durch.
(b) 🎓 8 Bit, $U_\text{ref} = 2{,}56\,\text{V}$ (1 LSB = 10 mV), $U_\text{ein} = 1{,}003\,\text{V}$.

> [!success]- Lösung (a)
> | Schritt | Test | Vergleich | ≤ 6,7 V? | Bit |
> |---|---|---|---|---|
> | 1 | 8 | 8 V | nein | 0 |
> | 2 | 4 | 4 V | ja | 1 |
> | 3 | 2 | 4 + 2 = 6 V | ja | 1 |
> | 4 | 1 | 6 + 1 = 7 V | nein | 0 |
>
> Ergebnis **0110₂ = 6** → 6 V (Rest 0,7 V < 1 LSB).
> **Achtung Rückfrage:** Der Fehler ist hier 0,7 V, also mehr als ½ LSB. „±½ LSB“ gilt nur, wenn man den Code auf die Stufenmitte bezieht (6,5 V) bzw. rundet; beim reinen Abrunden liegt der Fehler zwischen 0 und 1 LSB (siehe [[10_Rueckfragen_Drill]] N13).

> [!success]- Lösung (b)
> Vergleiche: 1,28 ✗ → 0 · 0,64 ✓ → 1 · 0,96 ✓ → 1 · 1,12 ✗ → 0 · 1,04 ✗ → 0 · 1,00 ✓ → 1 · 1,02 ✗ → 0 · 1,01 ✗ → 0
> Ergebnis **01100100₂ = 100** → 1,00 V.

### R10 · Genauigkeitsangabe lesen (Folie 14)
Ein DMM zeigt im 6-V-Bereich (Auflösung 1 mV) **5,000 V**. Datenblatt: ±(0,5 % v. Mw. + 3 Digits). In welchem Bereich liegt der wahre Wert?

> [!success]- Lösung
> 0,5 % von 5,000 V = 0,025 V · 3 Digits = 3 × 1 mV = 0,003 V → ±0,028 V
> Wahrer Wert: **4,972 … 5,028 V**

### R11 · Counts (Folie 14)
Ein 4000-Count-DMM steht im 4-V-Bereich. (a) Welche Auflösung? (b) Du misst 4,5 V – was passiert?

> [!success]- Lösung
> (a) 4,000 V → **1 mV**
> (b) **Manuell** im 4-V-Bereich: über dem Anzeigeumfang → Anzeige **„OL“** (Overload). **Mit Autorange:** das Gerät schaltet selbst in den 40-V-Bereich → Anzeige 4,50 V mit 10 mV Auflösung.

### R12 · Flash-Komparatoren (Folie 12)
Wie viele Komparatoren brauchen ein 6-Bit- und ein 10-Bit-Flash-Wandler? Was folgt daraus?

> [!success]- Lösung
> $2^6 - 1 = \mathbf{63}$ · $2^{10} - 1 = \mathbf{1023}$ → Aufwand wächst exponentiell, deshalb sind Flash-Wandler auf wenige Bit beschränkt.

### R13 · 🎓 Quantisierungsrauschen
Theoretischer Signal-Rausch-Abstand eines idealen 12-Bit-ADC?

> [!success]- Lösung
> $\text{SNR} \approx 6{,}02 \cdot 12 + 1{,}76 = \mathbf{74\,dB}$

---

## F – Fehler finden („Ein Azubi sagt …“)

Finde den Fehler und formuliere die richtige Aussage in **einem** Satz.

**F1:** „Für die Strommessung halte ich das Multimeter einfach parallel an die Lampe.“
> [!success]- Lösung
> Falsch angeschlossen: Amperemeter **in Reihe**, sonst Kurzschluss über den Shunt.

**F2:** „Mein 10-Bit-ADC an 5 V hat ein LSB von 4,88 mV – also misst er auf 4,88 mV genau.“
> [!success]- Lösung
> **Auflösung ≠ Genauigkeit:** 4,88 mV ist nur die Stufenbreite. Referenz-, Offset- und Linearitätsfehler kommen dazu – bei einer 5-V-Referenz mit ±1 % Toleranz sind das allein schon bis zu 50 mV.

**F3:** „Für ein 1-kHz-Signal reicht eine Abtastrate von genau 2 kHz.“
> [!success]- Lösung
> Es muss **mehr als** das Doppelte sein ($f_A > 2 f_\text{max}$). Bei genau 2 kHz kann man im ungünstigsten Fall immer die Nulldurchgänge treffen.

**F4:** „Für die Voltmeter-Erweiterung rechne ich $R_V = R_i / (n-1)$.“
> [!success]- Lösung
> Vertauscht: Das ist die **Shunt**-Formel. Voltmeter: $R_V = (n-1) \cdot R_i$ (Reihe → großer Widerstand).

**F5:** „±(1 % + 2 Digits) heißt 1 % vom Messbereich.“
> [!success]- Lösung
> Beim DMM: 1 % **vom Messwert** (v. Mw.) + 2 Einheiten der letzten Stelle. „% vom Endwert“ gilt bei der Güteklasse analoger Instrumente.

**F6:** „Mein Multimeter hat CAT II 1000 V, damit darf ich am Zählerplatz messen.“
> [!success]- Lösung
> Am Zählerplatz ist **CAT IV** nötig. Die Spannungsangabe ersetzt nicht die Kategorie.

**F7:** „Ein 8-Bit-Flash-Wandler braucht 256 Komparatoren.“
> [!success]- Lösung
> $2^8 - 1 = 255$ – zwischen 256 Stufen liegen 255 Schwellen.

---

## T – Teach-back (60 s laut erklären, Stoppuhr)

Stell dir vor, ein Mit-Azubi im 1. Lehrjahr fragt dich. Keine Fachwort-Ketten – erklären, nicht aufzählen. Danach mit der Checkliste prüfen.

| Nr. | Auftrag | Muss drin sein |
|---|---|---|
| T1 | „Warum muss ein Voltmeter hochohmig sein?“ | parallel · Messstrom · Belastungsfehler · Beispiel 4,76 V |
| T2 | „Wie misst ein Multimeter eigentlich Strom?“ | in Reihe · Shunt · U = I·R · intern Spannungsmessung · Bürdenspannung |
| T3 | „Was macht ein ADC?“ | Abtasten · Quantisieren · Codieren · Treppe · Bitzahl → Stufen |
| T4 | „Was ist Aliasing?“ | zu langsam abgetastet · falsche niedrigere Frequenz · > 2 f_max · Tiefpass · Wagenrad |
| T5 | „Warum steckt im Multimeter ein Dual-Slope-Wandler und kein Flash?“ | Multimeter braucht Genauigkeit, nicht Tempo · störfest · Netzbrummen · Flash zu grob/teuer |

> [!tip] Selbstcheck
> Alle Punkte genannt **und** unter 60 s? → ✅. Sonst: Musterantwort in [[02_QA_Vorbereitung]] bzw. Sprechernotiz in [[01_Folieninhalt_und_Varianten]] lesen und T sofort wiederholen.
