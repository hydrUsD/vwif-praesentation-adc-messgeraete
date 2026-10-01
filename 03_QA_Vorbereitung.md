---
title: "Q&A-Vorbereitung – wahrscheinliche Rückfragen"
tags: [VWIF, Präsentation, Q&A]
---

# Q&A-Vorbereitung

> [!tip] Antwort-Technik
> 1. Frage kurz **wiederholen** („Die Frage war, warum …“) – verschafft Denkzeit und alle haben sie gehört.
> 2. **Kurze Antwort zuerst** (1 Satz), dann ggf. Begründung.
> 3. Wenn du es nicht weißt: „Gute Frage – das schaue ich nach und gebe dir danach Bescheid.“ Das ist völlig in Ordnung.
>
> ⭐ = sehr wahrscheinliche Frage · 🎓 = Profi-Wissen, nur wenn jemand tiefer bohrt

---

## Teil 1 – Voltmeter & Amperemeter

### ⭐ Was passiert, wenn ich ein Amperemeter parallel anschließe?
**Kurz:** Kurzschluss. **Begründung:** Das Amperemeter hat fast 0 Ω. Parallel zu einer Spannungsquelle fließt ein sehr großer Strom → die Gerätesicherung löst aus; ohne (geeignete) Sicherung drohen Zerstörung, Lichtbogen, Verletzung.

### ⭐ Und wenn ich ein Voltmeter in Reihe schalte?
**Kurz:** Ungefährlich, aber die Schaltung funktioniert nicht mehr. **Begründung:** Mit ≈ 10 MΩ in Reihe fließt praktisch kein Strom. Das Voltmeter zeigt dann ungefähr die Quellspannung an, weil fast die gesamte Spannung an seinem großen Innenwiderstand abfällt.

### ⭐ Warum soll ein Voltmeter hochohmig und ein Amperemeter niederohmig sein?
Weil beide die Schaltung **so wenig wie möglich verändern** sollen: Das Voltmeter liegt parallel – es soll keinen Strom „abzweigen“. Das Amperemeter liegt in Reihe – es soll keine Spannung „wegnehmen“.

### Was ist die Bürdenspannung?
Der Spannungsabfall am Amperemeter (am Shunt + Sicherung + Leitungen). Er fehlt der eigentlichen Schaltung und verfälscht v. a. Messungen in Kreisen mit kleiner Spannung. Im Datenblatt oft als „Burden Voltage“ in mV/A angegeben.

### Wie misst man Strom, ohne den Stromkreis aufzutrennen?
Mit einer **Stromzange**. Bei Wechselstrom arbeitet sie wie ein Transformator (Stromwandler), für Gleichstrom braucht man eine Zange mit **Hall-Sensor**, der das Magnetfeld um den Leiter misst.

### Wie misst ein Multimeter einen Widerstand?
Es schickt einen bekannten, kleinen Konstantstrom durch das Bauteil und misst die Spannung → $R = U / I$. Darum: **Widerstand nur im spannungsfreien Zustand messen.**

### Wie bekommt ein Messwerk mehrere Messbereiche? *(Backup-Folie 6)*
Voltmeter: Vorwiderstand in Reihe, $R_V = (n-1) R_i$. Amperemeter: Shunt parallel, $R_N = R_i/(n-1)$. Beispiel: 100 µA/1 kΩ auf 10 V → 99 kΩ.

### Spannungsrichtig oder stromrichtig? *(Backup-Folie 7)*
Kleine Widerstände → spannungsrichtig (Voltmeter direkt am Bauteil). Große Widerstände → stromrichtig (Amperemeter direkt am Bauteil).

---

## Teil 2 – Sicherheit

### ⭐ Was bedeutet „CAT III 600 V“ auf dem Multimeter?
Das Gerät ist für Messungen in der **Gebäudeinstallation** (Verteiler, fest angeschlossene Geräte) bis **600 V** gegen Erde ausgelegt und hält dort die zu erwartenden Überspannungsimpulse aus. Es darf auch in den niedrigeren Kategorien (CAT II, CAT I) verwendet werden, **nicht** in CAT IV.

### Welche Kategorie hat eine normale Steckdose?
Ein Gerät, das an der Steckdose betrieben wird, ist **CAT II**. Die Steckdose als Teil der festen Installation wird je nach Quelle CAT II bzw. – wenn sie nahe am Verteiler liegt – CAT III zugeordnet. Faustregel: im Zweifel die höhere Kategorie wählen.

### Gilt die Kategorie auch für die Messleitungen?
Ja. Die **niedrigste** Einstufung aller Teile (Gerät, Messleitungen, Prüfspitzen, Zubehör) gilt für die gesamte Messanordnung.

### Die Sicherung im Multimeter ist durchgebrannt – kann ich irgendeine einsetzen?
**Nein.** Nur eine gleichwertige Sicherung laut Herstellerangabe (Nennstrom, Nennspannung und vor allem **Schaltvermögen**). Eine normale Feinsicherung kann bei hohen Kurzschlussströmen einen Lichtbogen nicht sicher löschen.

### Darf ich als Azubi an 230 V messen?
Arbeiten an elektrischen Anlagen sind nach **DGUV Vorschrift 3** Elektrofachkräften bzw. elektrotechnisch unterwiesenen Personen unter Leitung und Aufsicht einer Elektrofachkraft vorbehalten. → Bei uns gilt die betriebliche Regelung bzw. die Anweisung des Ausbilders.

---

## Teil 3 – Analog-Digital-Wandler

### ⭐ Was ist der Unterschied zwischen Auflösung und Genauigkeit?
**Auflösung** = wie fein die Stufen sind (kleinste unterscheidbare Änderung, 1 LSB). **Genauigkeit** = wie nah der angezeigte Wert am wahren Wert liegt. Ein 16-Bit-ADC mit ungenauer Referenzspannung löst sehr fein auf, liegt aber trotzdem daneben.

### ⭐ Warum nimmt man nicht immer einen 24-Bit-ADC?
Mehr Bit = langsamer und/oder teurer, und die zusätzlichen Bits sind oft nur noch Rauschen. Man wählt den ADC passend zur Anwendung (Geschwindigkeit vs. Auflösung, siehe Folie 12).

### ⭐ Was ist ein LSB?
*Least Significant Bit* – das niederwertigste Bit, gleichzeitig die **kleinste Spannungsstufe** des ADC: $U_\text{LSB} = U_\text{ref}/2^n$. Bei 10 Bit und 5 V: ≈ 4,88 mV.

### Was mache ich, wenn meine Spannung größer als die Referenzspannung ist (z. B. 12 V am Arduino)?
Einen **Spannungsteiler** davorschalten, der die Spannung in den erlaubten Bereich (0…5 V) bringt – im Programm wieder hochrechnen. Nie mehr als die erlaubte Spannung an den Pin legen!

### Was macht „Sample & Hold“?
Ein Kondensator speichert den Spannungswert zum Abtastzeitpunkt und hält ihn konstant, **während** der ADC wandelt. Sonst würde sich der Wert während der Wandlung ändern.

### ⭐ Was ist Aliasing – Beispiel aus dem Alltag?
Wagenrad-Effekt im Film: Rad dreht sich scheinbar langsam rückwärts, weil die Kamera zu selten „abtastet“. Abhilfe beim ADC: $f_A > 2 f_\text{max}$ und ein **Anti-Aliasing-Tiefpass** vor dem Wandler.

### Warum tastet die Audio-CD mit 44,1 kHz ab?
Der Mensch hört bis ca. 20 kHz → nach Nyquist mindestens 40 kHz nötig; der kleine Abstand zu 44,1 kHz lässt Platz für das Anti-Aliasing-Filter.

### Welcher ADC steckt im Arduino Uno?
Ein **10-Bit-SAR-Wandler** (sukzessive Approximation) im ATmega328P mit 8 umschaltbaren Eingängen (Multiplexer, beim Uno A0–A5 herausgeführt). Eine Wandlung dauert 13 ADC-Takte (bei Standardeinstellung ca. 0,1 ms).

### Was ist das Gegenstück zum ADC?
Der **DAC** (Digital-Analog-Wandler), z. B. als R-2R-Widerstandsnetzwerk. Im SAR-Wandler steckt übrigens intern ein DAC, der die Vergleichsspannung erzeugt.

### 🎓 Warum ist der Dual-Slope-Wandler so genau?
Er integriert die Eingangsspannung eine feste Zeit lang und entlädt dann mit der Referenzspannung. Weil **dieselbe** RC-Kombination und **derselbe** Takt in beiden Phasen verwendet werden, kürzen sich deren Toleranzen heraus. Wählt man die Integrationszeit als Vielfaches der Netzperiode (20 ms bei 50 Hz), mittelt sich Netzbrummen heraus.

### 🎓 Wie groß ist das Quantisierungsrauschen?
Theoretischer Signal-Rausch-Abstand eines idealen n-Bit-ADC (Sinus, Vollaussteuerung): $\text{SNR} \approx 6{,}02 \cdot n + 1{,}76\,\text{dB}$ → 16 Bit ≈ 98 dB.

### 🎓 Was sind „Missing Codes“?
Ausgangscodes, die durch Bauteiltoleranzen (Linearitätsfehler) nie ausgegeben werden. Tritt besonders bei Flash-Wandlern auf.

---

## Teil 4 – Digitalmultimeter

### ⭐ Was bedeutet „3½ Stellen“?
Drei volle Ziffern (0–9) plus eine „halbe“ vorderste Stelle, die nur 0 oder 1 anzeigen kann → max. Anzeige **1999** („2000 Counts“). Moderne Geräte zählen z. B. bis 6000 Counts.

### ⭐ Wie lese ich „±(1 % v. Mw. + 2 Digits)“?
1 % **vom angezeigten Messwert** plus 2 Einheiten der **letzten Stelle**. Anzeige 100,0 V → ±(1,0 V + 0,2 V) = ±1,2 V → wahrer Wert zwischen 98,8 V und 101,2 V.

### Was bedeutet TRMS / Echt-Effektivwert?
Ein TRMS-Multimeter misst den Effektivwert auch bei **nicht-sinusförmigen** Signalen (z. B. hinter Dimmern, Frequenzumrichtern, Schaltnetzteilen) korrekt. Einfache Geräte messen den Gleichrichtwert und rechnen mit dem Formfaktor des Sinus (1,11) um → bei verzerrten Signalen oft deutlich zu niedrige Anzeige.

### Warum zeigt das Multimeter an offenen Leitungen manchmal „Geisterspannungen“?
Wegen des hohen Eingangswiderstands (10 MΩ) reichen kapazitiv eingekoppelte Spannungen von benachbarten Leitungen aus, um eine Anzeige zu erzeugen. Abhilfe: Geräte mit niederohmigem Messmodus (z. B. „LoZ“).
