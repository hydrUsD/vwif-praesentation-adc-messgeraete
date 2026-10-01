---
title: "Quellenverzeichnis"
tags: [VWIF, Quellen]
stand: 2026-10-01
---

# Quellenverzeichnis

> [!info] Hinweis zur Nutzung
> Für die Abschlussfolie bzw. ein Quellen-Backup reichen meist **3–5 Quellen** (die mit ★ markierten). Alle Online-Quellen wurden am **01.10.2026** abgerufen. Zitierweise: Autor/Herausgeber, *Titel*, Jahr/Stand, URL (Abruf).

## A) Analog-Digital-Wandler

| | Quelle | Genutzt für |
|---|---|---|
| ★ | Lattmann, M.: *Digitaltechnik – Kapitel 10: Analog-Digital-Wandler* (Skript, SwissEduc). https://www.swisseduc.ch/informatik/hardware/analog_digital_wandler/docs/script.pdf | Wandlerverfahren (Flash, SAR, Zählverfahren, Dual-Slope), Quantisierungsfehler ±½ LSB, Missing Codes, Auflösung ≠ Genauigkeit |
| | ElektronikPraxis: *ADC und DAC – das müssen Sie wissen*. https://www.elektronikpraxis.de/adc-und-dac-das-muessen-sie-wissen-a-6a0f66b98d47358230bad75369307944/ | Abtastung/Quantisierung, Stufenzahl 8/16 Bit, LSB-Beispiele |
| ★ | ingHUB: *Messtechnik – Abtasttheorem & Aliasing*. https://inghub.de/lessons/messtechnik/aliasing.html | Nyquist-Shannon, Aliasing-Beispiel (10 kHz bei 15 kHz), Anti-Aliasing-Tiefpass |
| | Universität Ulm: *Analog-Digital und Digital-Analog Wandler* (Vorlesungsfolien). https://www.uni-ulm.de/fileadmin/website_uni_ulm/iui.inst.130/Mitarbeiter/oubbati/RobotikWS1113/Folien/ADDAWandler.pdf | Weiterführend / Vertiefung |
| | Thiede, A.: *Elektronik für den Maschinenbau*, Kap. 5 (Uni Paderborn). https://groups.uni-paderborn.de/hfe/lehre/Script_elt_5.pdf | Weiterführend: Quantisierungsrauschen |
| ★ | Analog Devices / Intersil: *ICL7106/ICL7107 – 3½ Digit A/D Converters* (Datenblatt). https://www.analog.com/media/en/technical-documentation/data-sheets/icl7106-icl7107.pdf | Dual-Slope-ADC im Multimeter, 2000 Counts, Störunterdrückung |
| | SiliconWit: *ADC and Analog Signal Acquisition (ATmega328P)*. https://siliconwit.com/education/embedded-programming-atmega328p/adc-analog-signal-acquisition/ | Arduino-Uno-ADC: 10 Bit SAR, 13 Takte, 125 kHz ADC-Takt, ≈ 9,6 kSPS |
| | Microchip: *ATmega328P – Datenblatt* (Primärquelle zum Arduino-ADC). https://www.microchip.com/en-us/product/atmega328p | Zum Nachschlagen bei Detailfragen (Kapitel „Analog-to-Digital Converter“) |

## B) Voltmeter, Amperemeter, Messfehler

| | Quelle | Genutzt für |
|---|---|---|
| ★ | Elektroniktutor: *Spannungs- und Strommessung*. https://www.elektroniktutor.de/elektrophysik/ui_mess.html | Innenwiderstände ideal/real, spannungs-/stromrichtige Messung, Formeln Messbereichserweiterung |
| | Elektronik-Labor / ELEXS: *Messbereichserweiterung beim Voltmeter*. https://www.elektronik-labor.de/elexs/messen1.html | Beispiel 100 µA / 1 kΩ → 99 kΩ Vorwiderstand |
| ★ | Fluke: *ABC der Digitalmultimeter* (Anwendungsbericht, dt.). https://www.calplus.de/fileuploader/download/download/?d=0&file=custom%2Fupload%2Ffluke-abc-der-dmms-de-cp.pdf | 3½ Stellen/Counts, Genauigkeitsangabe ±(1 % + 2 Digits), TRMS, Sicherungen |
| | Fluke: *ABCs of DMMs* (engl.). https://media.fluke.com/ade6b718-4577-4b57-903b-b10600664c67_original%20file.pdf | Englische Originalfassung |

## C) Sicherheit / Messkategorien

| | Quelle | Genutzt für |
|---|---|---|
| | BG ETEM: *Auswahl handgehaltener Multimeter*. https://medien.bgetem.de/medienportal/artikel/UzAyNw--/@@download/download | Weiterführend (nicht im Detail ausgewertet) |
| ★ | BGHM: *Hilfsmittel für die Praxis – Auswahl sicherer handgehaltener Multimeter*. https://www.bghm.de/fileadmin/user_upload/Arbeitsschuetzer/Fachthemen/Elektrotechnik/Auswahl_geeigneter_Handmultimeter.pdf | CAT II–IV mit Absicherung/Kurzschlussstrom, Anforderungen an Messleitungen (DIN EN 61010-031) und Sicherungen |
| | Gossen Metrawatt: *Measuring categories per IEC 61010-1*. https://www.gossenmetrawatt.de/en/knowledge/measuring-and-test-technology/measuring-categories-per-iec-61010-1/ | Kategorie-Beispiele, „CAT 0“ |
| | Wikipedia: *Messkategorie*. https://de.wikipedia.org/wiki/Messkategorie | Überblick, Norm IEC 61010-2-030 |

## D) Normen (nur Verweis, nicht frei verfügbar)

- DIN EN 61010-1 (VDE 0411-1): Sicherheitsbestimmungen für elektrische Mess-, Steuer-, Regel- und Laborgeräte – Teil 1: Allgemeine Anforderungen
- DIN EN 61010-2-030: Besondere Bestimmungen für Prüf- und Messstromkreise (Messkategorien)
- DIN EN 61010-031: Sicherheitsbestimmungen für handgehaltene Messleitungen und Zubehör
- DGUV Vorschrift 3: Elektrische Anlagen und Betriebsmittel

## E) Weiterführende Lehrbücher (Standardwerke in der Ausbildung)

- *Fachkunde Elektrotechnik*, Verlag Europa-Lehrmittel – Kapitel Messtechnik
- *Tabellenbuch Elektrotechnik*, Verlag Europa-Lehrmittel – Formeln Messbereichserweiterung, Messkategorien

> [!warning] Ehrlichkeitshinweis
> Die Lehrbücher (E) und das Microchip-Datenblatt wurden für dieses Dokument **nicht** im Detail ausgewertet, sondern als Nachschlagewerke empfohlen. Typische Richtwerte in der Wandler-Vergleichstabelle (Folie 12) sind bewusst als „≈“ gekennzeichnet – die Bereiche variieren je nach Hersteller.

## Kurzfassung für eine Quellenfolie (copy & paste)

```
Quellen (Abruf 01.10.2026)
• Lattmann: Digitaltechnik Kap. 10 – Analog-Digital-Wandler (swisseduc.ch)
• Elektroniktutor: Spannungs- und Strommessung (elektroniktutor.de)
• Fluke: ABC der Digitalmultimeter
• Analog Devices: Datenblatt ICL7106/ICL7107
• BGHM: Auswahl sicherer handgehaltener Multimeter; DIN EN 61010
```
