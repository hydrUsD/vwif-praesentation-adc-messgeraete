---
title: "Rückfragen-Drill"
tags: [VWIF, Q&A, Drill]
---

# Rückfragen-Drill

## Ablauf (20 min)

1. **Runde 1 (≈ 8 min):** im Messwert-Trainer Modus „Rückfragen“ mit Filter **„nur ⭐“** – die wahrscheinlichsten Fragen aus [[02_QA_Vorbereitung]], gemischt.
2. **Runde 2 (≈ 10 min):** die neuen Fragen **N1–N13** unten in zufälliger Reihenfolge (im Trainer ohne Filter enthalten, oder jemanden vorlesen lassen).
3. **30 s pro Antwort, laut.** Struktur: *Frage kurz wiederholen → 1-Satz-Antwort → 1 Satz Begründung/Beispiel.*
4. Nach jeder Antwort: **sicher / wackelig / falsch**. Wackelig und falsch → Musterantwort einmal laut nachsprechen.
5. **Schnell-Runde** „Zahlen auf Zuruf“ (2 min). Die übrigen Fragen aus 02 ohne ⭐ sind optional.

> [!tip] Sicher wirken, auch wenn du unsicher bist
> - „Gute Frage – …“ nur einmal pro Fragerunde, sonst wirkt es wie eine Floskel.
> - Ehrliches „Das weiß ich nicht sicher, ich schaue es nach“ ist **besser** als raten.
> - Frage nicht verstanden? „Meinst du eher … oder …?“ – das ist erlaubt und professionell.

---

## Neue Rückfragen (ergänzend zu 02_QA_Vorbereitung)

> [!note] Kennzeichnung
> Diese Antworten stammen aus allgemeinem Lehrbuchwissen `[LB]`. Rechenwerte sind nachgerechnet.

| ✓ | Nr. | Frage | Musterantwort (30 s) |
|---|---|---|---|
| ☐ | N1 | Was heißt „OL“ auf dem Display? | *Overload/Over Limit*: Messwert liegt über dem Bereich (größeren Bereich wählen); bei Widerstand/Durchgang: offener Kreis bzw. unendlich großer Widerstand. |
| ☐ | N2 | Analog- oder Digitalmultimeter – was ist besser? | Digital: genauer ablesbar, hochohmig (10 MΩ), Autorange. Analog: zeigt Trends und Schwankungen besser, aber Ablesefehler und meist niederohmiger (z. B. 20 kΩ/V). Viele DMMs haben deshalb zusätzlich einen Bargraph. |
| ☐ | N3 | Was ist ein Komparator? | Vergleicht zwei Spannungen und gibt 1 oder 0 aus, je nachdem, welche größer ist. Grundbaustein von Flash- und SAR-Wandlern. |
| ☐ | N4 | Wie groß wäre ein Shunt für 10 A, wenn 100 mV abfallen sollen? | R = U/I = 0,1 V / 10 A = **10 mΩ**; Leistung P = I²·R = **1 W** → deshalb wird der 10-A-Bereich warm und ist oft zeitlich begrenzt. |
| ☐ | N5 | Warum hat das Multimeter eine mA- **und** eine 10-A-Buchse? | Unterschiedliche Shunts und Sicherungen: kleiner Strom → größerer Shunt für genug Messspannung; großer Strom → sehr kleiner, belastbarer Shunt. |
| ☐ | N6 | Effektivwert vs. Gleichrichtwert? | Effektivwert = Wert mit gleicher Wärmewirkung wie Gleichspannung. Einfache Messgeräte messen den Gleichrichtwert und multiplizieren mit dem Sinus-Formfaktor **≈ 1,11** – stimmt nur bei Sinus. TRMS misst echt. |
| ☐ | N7 | Was ist Autorange? | Das Messgerät wählt den Messbereich selbst; ist der Wert zu groß („OL“), schaltet es eine Stufe höher. |
| ☐ | N8 | Wie viele Bit entsprechen 2000 Counts? | log₂(2000) ≈ **11 Bit** – ein 3½-stelliges DMM löst also ungefähr wie ein 11-Bit-ADC auf. |
| ☐ | N9 | Was passiert, wenn U_ein größer als U_ref ist? | Der ADC gibt den Maximalwert aus (10 Bit: 1023) – der Messwert ist dann falsch. Liegt die Spannung über dem zulässigen Pinwert, kann der Eingang beschädigt werden → Spannungsteiler davor. |
| ☐ | N10 | Warum gerade 10 MΩ und nicht noch mehr? | Kompromiss: hoch genug für kleinen Belastungsfehler, aber nicht so hoch, dass eingestreute Störspannungen („Geisterspannungen“) zu stark werden. |
| ☐ | N11 | Wie oft misst ein Multimeter pro Sekunde? | Einfache Geräte mit integrierendem Wandler nur einige Messungen pro Sekunde (Datenblatt prüfen). Für schnelle Signale nimmt man ein Oszilloskop mit schnellem (Flash-)Wandler. |
| ☐ | N12 | Was ist der Unterschied zwischen Multimeter und Oszilloskop? | Multimeter zeigt einen (gemittelten) Zahlenwert und ist genau. Oszilloskop zeigt den zeitlichen Verlauf des Signals, tastet sehr schnell ab, ist dafür grober in der Auflösung. |
| ☐ | N13 | Du sagst „±½ LSB“ – aber beim SAR-Beispiel war der Rest fast 1 LSB. Was stimmt? | Beides, je nach Bezug: Der ADC entscheidet nur, *in welcher Stufe* die Spannung liegt. Bezieht man den Code auf die **Stufenmitte** (bzw. rundet), ist der Fehler höchstens ±½ LSB. Beim **reinen Abrunden** auf die Stufenuntergrenze, wie in meinem Rechenbeispiel, sind es 0 bis 1 LSB. |

---

## Schnell-Runde: Zahlen auf Zuruf (2 min)

Jemand nennt das Stichwort, du die Zahl (oder du deckst die rechte Spalte ab).

| Stichwort | Zahl |
|---|---|
| DMM-Eingangswiderstand | 10 MΩ |
| Teiler 2 × 1 MΩ an 10 V, DMM | 4,76 V |
| … mit Zeigerinstrument | 1,43 V |
| 5 V / 25 Ω mit 1-Ω-Shunt | 192 mA |
| 10 Bit, 5 V – LSB | 4,88 mV |
| 2,5 V → Arduino-Code | 512 |
| 8-Bit-Flash – Komparatoren | 255 |
| 10 kHz bei 15 kHz Abtastung | 5 kHz Alias |
| SAR 11,3 V (4 Bit, 16 V) | 1011₂ = 11 |
| ±(1 % + 2 D) bei 100,0 V | 98,8 … 101,2 V |
| 3½ Stellen | 1999 / 2000 Counts |
