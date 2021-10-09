# Energiesparplan-Updater (Windows only)
> Hi, ich hatte folgendes Problem: Ungefähr alle 30 Sekunden hat sich die Einstellung meines Energiesparplans geändert. Im Internet konnte ich keine Lösung finden, also dachte ich, schreibe ich ein kleines Programm. Das folgende Programm läuft bei mir dauerhaft im Hintergrund, und setzt alle 25 Sekunden den Energiesparplan fest.

Führe folgenden Befehl aus:
```
powercfg /list
```
Die Rückgabe müsste dann ungefähr so aussehen:
```
GUID des Energieschemas: 381b4222-f694-41f0-9685-ff5bb260df2e  (Ausbalanciert)
GUID des Energieschemas: 8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c  (Höchstleistung)
GUID des Energieschemas: a1841308-3541-4fab-bc81-f71556f20b4a  (Energiesparmodus)
```
Nun ersetzt du im Python Code die vorhandene GUID mit der GUID des gewünschten Energiesparplans:
```
plan = "8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c"
```
Das war's schon, nun öffnet ihr das Programm und wartet 25 Sekunden. Danach sollte die Ausgabe so aussehen:
```
1 | Erfolgreich, warte 25 Sekunden bevor neustart.
2 | Erfolgreich, warte 25 Sekunden bevor neustart.
3 | Erfolgreich, warte 25 Sekunden bevor neustart.
```
  - Die Zahl vor dem "|" zeigt die ID an, damit du sehen kannst, wie oft der Vorgang schon durchgeführt wurde.
  - Die Nachricht danach kannst du beliebig anpassen, es hat mir so aber am besten gefallen.
