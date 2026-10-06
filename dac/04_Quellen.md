---
title: "Quellen – DAC"
tags: [VWIF, DAC, Quellen]
---

# Quellen

| Kürzel | Quelle | Wofür |
|---|---|---|
| [ADI MT-015] | Kester, W.: *MT-015 Tutorial – Basic DAC Architectures II: Binary DACs*. Analog Devices. <https://www.analog.com/media/en/training-seminars/tutorials/MT-015.pdf> | R-2R (Spannungs-/Strommodus, 2n Widerstände, Verhältnis 2:1), Nachteile gewichteter Widerstände |
| [DSPGuide 3] | Smith, S. W.: *The Scientist and Engineer's Guide to Digital Signal Processing*, Kap. 3.3 „Digital-to-Analog Conversion“. <https://www.dspguide.com/ch3/3.htm> | Treppe (Zero-Order Hold), Rekonstruktionsfilter bis f_s/2 |
| [ESP-IDF DAC] | Espressif: *ESP-IDF Programming Guide – Digital To Analog Converter (DAC), ESP32*. <https://docs.espressif.com/projects/esp-idf/en/stable/esp32/api-reference/peripherals/dac.html> | ESP32: 2 × 8 Bit, GPIO25/26, Cosinus-Generator, DMA |
| [DE-WP R2R] | Wikipedia: *R2R-Netzwerk*. <https://de.wikipedia.org/wiki/R2R-Netzwerk> | Bitgewichte durch Halbierung je Stufe, Innenwiderstand R, Toleranzanforderung MSB |
| [DE-WP DAU] | Wikipedia: *Digital-Analog-Umsetzer*. <https://de.wikipedia.org/wiki/Digital-Analog-Umsetzer> | Überblick Verfahren, Begriffe |
| [WP DDS] | Wikipedia: *Direct digital synthesis*. <https://en.wikipedia.org/wiki/Direct_digital_synthesis> | Sinus aus Wertetabelle + DAC + Tiefpass |
| [Tek R-2R] | Tektronix: *Tutorial: Digital to Analog Conversion – The R-2R DAC*. <https://www.tek.com/en/blog/tutorial-digital-analog-conversion-r-2r-dac> | Ergänzende Erklärung R-2R |
| [Sim] | Eigene Nachrechnung: `_prep/verify_dac.py` (Knotenanalyse R-2R, alle 16 Codes, Toleranzstudie, Sinus-/Cosinus-Tabelle, CD-Datenrate) | alle Zahlen im Vortrag |

> [!note] Lehrbuchwissen
> CD-Format (16 Bit, 44,1 kHz), Sigma-Delta-Prinzip, Mikroschrittbetrieb beim Schrittmotor, I/Q-Signale: allgemeines Lehrbuchwissen, nicht einzeln belegt.
