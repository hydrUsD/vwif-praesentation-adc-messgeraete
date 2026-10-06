---
title: "Karteikarten – DAC"
tags: [VWIF, DAC, Karteikarten]
---

# Karteikarten (Abrufübung)

> [!info] Benutzung
> Frage lesen, Antwort **laut sagen**, dann rechts vom doppelten Doppelpunkt vergleichen. Mit dem Obsidian-Plugin „Spaced Repetition“ werden die Karten automatisch erkannt.

## Grundlagen #flashcards/vwif/dac-grundlagen

Was macht ein DAC?::Er wandelt einen digitalen Code (Binärzahl) in eine analoge Spannung um – das Gegenstück zum ADC.
Warum braucht man einen DAC, wenn doch digital gespeichert wird?::Lautsprecher, Motoren und unsere Sinne arbeiten analog; gespeicherte Zahlen (Festplatte, Stream) müssen wieder zu einer Spannung werden.
Formel für die Ausgangsspannung eines n-Bit-DAC?::U_aus = Code / 2ⁿ · U_ref
4-Bit-DAC, U_ref = 8 V – wie groß ist 1 LSB?::8 V / 16 = 0,5 V.
Bitgewichte beim 4-Bit-DAC mit 8 V (MSB → LSB)?::4 V · 2 V · 1 V · 0,5 V (½, ¼, ⅛, 1/16 von U_ref).
4 Bit, 8 V: Welche Spannung bei 1101?::13 · 0,5 V = 4 + 2 + 0,5 = 6,5 V.
Warum erreicht ein DAC nie ganz U_ref?::Der größte Code ist 2ⁿ − 1 → max. (2ⁿ − 1)/2ⁿ · U_ref, es fehlt genau 1 LSB (4 Bit, 8 V: 7,5 V).
Wie sieht der DAC-Ausgang direkt am Wandler aus?::Als Treppe – jeder Wert wird bis zum nächsten gehalten.

## R-2R-Netzwerk #flashcards/vwif/dac-r2r

Welche Widerstandswerte braucht ein R-2R-Netzwerk?::Nur zwei: R (Längszweig) und 2R (Querzweige + Abschluss).
Wie viele Widerstände hat ein 8-Bit-R-2R?::2n = 16.
Was macht ein Bit im R-2R-Netzwerk?::Bit = 1 schaltet seinen 2R-Zweig an U_ref, Bit = 0 an Masse.
Warum bekommt jedes Bit sein richtiges Gewicht?::Rechts von jedem Knoten wirkt das Netz wie eine Quelle mit R; + Längs-R = 2R; mit dem nächsten 2R-Zweig → Teiler 1 : 1 → Beitrag halbiert sich pro Stufe → ½, ¼, ⅛ …
Nachteil gewichteter Widerstände gegenüber R-2R?::Viele verschiedene Werte (8 Bit: R bis 128R), schwer genau zu fertigen.
Wozu der OpAmp am Ausgang des R-2R?::Puffer: Das Netzwerk hat Innenwiderstand R; eine Last würde die Spannung verfälschen (an Last R: 6,5 V → 3,25 V).
Warum ist die Toleranz beim MSB besonders kritisch?::Das MSB trägt die halbe Spannung; ist sein 2R-Zweig nur 2 % zu groß, ist ein 8-Bit-DAC nicht mehr monoton (127 → 128: −15 mV).

## Sinus, Cosinus & Filter #flashcards/vwif/dac-sinus

Wie erzeugt man mit einem DAC einen Sinus?::Eine Periode als Wertetabelle speichern und die Werte im festen Takt an den DAC geben; ein Tiefpass glättet.
Formel Signalfrequenz bei Tabellen-Ausgabe?::f = Takt / Werte pro Periode (16 kHz / 16 = 1 kHz).
Wozu der Tiefpass hinter dem DAC?::Rekonstruktionsfilter: entfernt die Treppenkanten (Anteile über dem halben Takt) → glattes Signal.
Wie bekommt man den Cosinus zum Sinus?::Dieselbe Tabelle, um ¼ Periode (90°) versetzt lesen – bei 16 Werten ab Index + 4 (4 Einträge voraus).
Wo braucht man Sinus und Cosinus gleichzeitig?::Z. B. Schrittmotor im Mikroschrittbetrieb (Spule A Sinus, Spule B Cosinus), Funktechnik (I/Q), Resolver.
Gilt das Abtasttheorem auch beim DAC?::Ja – das ausgegebene Signal muss unter dem halben Takt liegen (16 kHz → < 8 kHz).
Wie erzeugt ein Funktionsgenerator mit DDS einen Sinus?::Tabelle + Takt + DAC + Tiefpass; die Frequenz ändert er über die Schrittweite durch die Tabelle.

## Praxis #flashcards/vwif/dac-praxis

Was bestimmen Bitzahl und Ausgaberate eines DAC?::Bitzahl = Feinheit der Treppe; Ausgaberate begrenzt die höchste Frequenz (unter der halben Rate).
Welchen DAC hat ein ESP32?::Zwei 8-Bit-DAC-Kanäle (GPIO25/26) mit eingebautem Cosinus-Generator.
Welche Auflösung und Rate hat CD-Audio?::16 Bit, 44,1 kHz, Stereo → ≈ 1,41 Mbit/s.
Welche Bauart haben Audio-DACs meistens?::Sigma-Delta (hoher Takt, wenige Stufen, Filter) – typisch 24 Bit.
Hat der Arduino Uno einen echten DAC?::Der klassische Uno R3 nein (analogWrite() = PWM, erst mit RC-Tiefpass eine wellige Gleichspannung); der Uno R4 hat einen 12-Bit-DAC an A0.
Die 3 Take-aways des Vortrags?::1) DAC = Code → Spannung, Treppe 2) R-2R: zwei Werte, Beitrag halbiert sich je Stufe 3) Treppe + Tiefpass = glattes Signal; Sinus/Cosinus aus einer Tabelle, Abtasttheorem gilt auch rückwärts.
