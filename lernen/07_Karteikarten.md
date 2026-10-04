---
title: "Karteikarten – Voltmeter, Amperemeter & ADC"
tags: [VWIF, Karteikarten]
---

# Karteikarten (Abrufübung)

> [!info] Benutzung
> - **Ohne Plugin:** Frage lesen, Antwort **laut sagen**, dann rechts vom doppelten Doppelpunkt vergleichen (Antwort mit der Hand/einem Blatt abdecken).
> - **Mit Obsidian-Plugin „Spaced Repetition“:** Die Karten sind als einzeilige Frage-Antwort-Paare (Trenner: doppelter Doppelpunkt) mit Deck-Tags angelegt und werden automatisch erkannt.
> - Falsch beantwortete Karten hier mit ❌ markieren und am Ende des Blocks wiederholen.

## Teil A – Voltmeter & Amperemeter #flashcards/vwif/messgeraete

Wie wird ein Voltmeter angeschlossen und wie soll sein Innenwiderstand sein?::Parallel zum Bauteil; Innenwiderstand möglichst groß (ideal ∞).
Wie wird ein Amperemeter angeschlossen und wie soll sein Innenwiderstand sein?::In Reihe (Kreis auftrennen); Innenwiderstand möglichst klein (ideal 0).
Typischer Eingangswiderstand eines Digitalmultimeters im Spannungsbereich?::≈ 10 MΩ.
Was ist der Belastungsfehler?::Der Voltmeter-Innenwiderstand liegt parallel zum Messobjekt, verkleinert den wirksamen Widerstand → angezeigte Spannung zu klein.
Spannungsteiler 2 × 1 MΩ an 10 V – was zeigt ein DMM (10 MΩ) über R2 an?::4,76 V statt 5,00 V (−4,8 %).
Gleicher Teiler, analoges Zeigerinstrument 20 kΩ/V im 10-V-Bereich – Anzeige?::1,43 V (Rᵢ = 200 kΩ, −71 %).
Wie misst ein DMM intern Strom?::Über einen Shunt: U = I · R_Shunt wird als Spannung gemessen → I = U/R.
Was ist die Bürdenspannung?::Spannungsabfall am Amperemeter (Shunt + Sicherung + Leitungen), fehlt der Schaltung.
5 V an 25 Ω, Amperemeter mit 1 Ω – gemessener Strom?::192 mA statt 200 mA (−3,8 %).
Formel Vorwiderstand (Voltmeter-Bereichserweiterung)?::R_V = (n − 1) · Rᵢ
Formel Shunt / Nebenwiderstand (Amperemeter-Bereichserweiterung)?::R_N = Rᵢ / (n − 1)
Was ist der Erweiterungsfaktor n?::n = neuer Messbereich / alter Messbereich.
Messwerk 100 µA / 1 kΩ soll 10 V messen – Vorwiderstand?::n = 100 → R_V = 99 kΩ.
Spannungsrichtige Messung – wann?::Bei kleinen Widerständen (Voltmeter direkt am Bauteil; U korrekt, I etwas zu groß).
Stromrichtige Messung – wann?::Bei großen Widerständen (Amperemeter direkt am Bauteil; I korrekt, U etwas zu groß).

## Teil B – Sicherheit #flashcards/vwif/sicherheit

Was passiert, wenn das Amperemeter parallel an eine Spannungsquelle kommt?::Kurzschluss über den fast 0 Ω kleinen Shunt → Sicherung löst aus, sonst Lichtbogen/Zerstörung.
Was passiert, wenn das Voltmeter in Reihe geschaltet wird?::Ungefährlich, aber kaum Strom → Schaltung funktioniert nicht, Anzeige ≈ Quellspannung.
Welche drei Dinge prüfst du vor jeder Messung?::Buchse – Drehschalter – Messbereich.
CAT IV – wo?::Ursprung der Installation: Hausanschluss, Zähler.
CAT III – wo?::Gebäudeinstallation: Verteiler, Leistungsschalter, fest angeschlossene Verbraucher.
CAT II – wo?::Geräte mit Netzstecker (Haushaltsgeräte, Werkzeuge).
CAT I / „CAT 0“ – wo?::Stromkreise ohne direkte Netzverbindung (z. B. Batterie, Elektronik).
Welche Norm regelt die Messkategorien?::DIN EN 61010 (Kategorien heute in IEC 61010-2-030).
Gilt die CAT-Angabe nur für das Messgerät?::Nein – die niedrigste Einstufung von Gerät, Messleitungen und Zubehör gilt.

## Teil C – Analog-Digital-Wandler #flashcards/vwif/adc

Die drei Schritte eines ADC?::Abtasten – Quantisieren – Codieren.
Was macht Sample & Hold?::Hält den abgetasteten Spannungswert (Kondensator) während der Wandlung konstant.
Formel LSB?::U_LSB = U_ref / 2ⁿ
Wie viele Stufen hat ein 10-Bit-ADC?::2¹⁰ = 1024.
LSB eines 10-Bit-ADC bei 5 V?::≈ 4,88 mV.
Wie groß ist der Quantisierungsfehler?::± ½ LSB, wenn auf die Stufenmitte gerundet wird. Beim reinen Abrunden (Arduino-Rechnung) bis zu 1 LSB.
Arduino Uno: welcher Code bei 2,5 V (10 Bit, 5 V)?::512.
Arduino Uno: analogRead() = 300 → Spannung?::300 · 5 V / 1024 ≈ 1,46 V.
Ist Auflösung dasselbe wie Genauigkeit?::Nein – Auflösung = Feinheit der Stufen; Genauigkeit zusätzlich begrenzt durch Referenz-, Offset-, Linearitätsfehler.
Abtasttheorem (Nyquist-Shannon)?::f_Abtast > 2 · f_max.
Was ist Aliasing?::Bei zu langsamer Abtastung erscheint eine falsche, niedrigere Frequenz.
10-kHz-Signal mit 15 kHz abgetastet – welche Alias-Frequenz?::15 − 10 = 5 kHz.
Gegenmittel gegen Aliasing?::Anti-Aliasing-Tiefpass vor dem ADC (Anteile > f_Abtast/2 entfernen).
Warum hat die Audio-CD 44,1 kHz?::Hörgrenze ≈ 20 kHz → > 40 kHz nötig, Rest als Reserve fürs Filter.

## Teil D – Wandlerverfahren & Multimeter #flashcards/vwif/dmm

Flash-Wandler: Prinzip und Einsatz?::Ein Komparator je Schwelle (2ⁿ − 1), alle gleichzeitig → sehr schnell, grob (≈ 6–8 Bit); Oszilloskope.
Wie viele Komparatoren braucht ein 8-Bit-Flash-Wandler?::2⁸ − 1 = 255.
SAR-Wandler: Prinzip und Einsatz?::Binäre Suche Bit für Bit (n Schritte), interner DAC; Mikrocontroller (Arduino).
SAR 4 Bit, U_ref 16 V, U_ein 11,3 V – Ergebnis?::1011₂ = 11 → 11 V.
Dual-Slope: Prinzip, Vorteil, Einsatz?::Integrieren & Rückintegrieren; RC und Takt kürzen sich heraus, störfest (Netzbrummen mittelt sich bei 20 ms heraus); Multimeter.
Sigma-Delta: Eigenschaft und Einsatz?::Überabtastung + digitale Filter → sehr hohe Auflösung (≈ 16–24 Bit); Audio, Waagen.
Was bedeutet „3½ Stellen“?::3 volle Ziffern + halbe Stelle (0/1) → max. 1999 Anzeige („2000 Counts“).
6000-Count-DMM im 6-V-Bereich – Auflösung?::1 mV.
±(1 % v. Mw. + 2 Digits) bei 100,0 V – wahrer Wert?::98,8 … 101,2 V.
TRMS – was ist das?::Echt-Effektivwertmessung – korrekt auch bei nicht-sinusförmigen Signalen.
Welcher ADC-Chip ist der Multimeter-Klassiker?::ICL7106 – 3½-stelliger Dual-Slope-ADC.
Die 3 Take-aways der Präsentation?::1) Voltmeter parallel & hochohmig, Amperemeter in Reihe & niederohmig 2) ADC = Abtasten + Quantisieren + Codieren, U_LSB = U_ref/2ⁿ, f_A > 2 f_max 3) Im Multimeter: Spannungsmessung + ADC.
