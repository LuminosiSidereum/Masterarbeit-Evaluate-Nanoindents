# Auswertung der Nanoindentierung

## Funktionsweise
Dieses Programm bereitet die Härtemessungen der Nanoindentierung für verschiedene Parametersätze auf.  
Dabei werden folgende statistische Kennzahlen berechnet:

- Mittelwert
- Minimalwert
- Maximalwert
- Positiver Fehlerbalken (+yErr)
- Negativer Fehlerbalken (-yErr)
- Standardabweichung (nur für Parametersätze)

Die Ergebnisse werden in CSV-Dateien gespeichert.

## Nutzung des Skripts
### Eingabedaten
- Das Skript erwartet eine CSV-Datei mit dem Namen `Ergebnissammlung_Härte.csv`.
- Die Datei enthält Härtemessdaten für verschiedene Proben und Parametersätze.
- Die Spaltennamen entsprechen den Probenbezeichnungen.

### Ausführung
1. Stelle sicher, dass sich die Datei `Ergebnissammlung_Härte.csv` im selben Verzeichnis wie das Skript befindet.
2. Starte das Skript `auswertung_haerte.py`
3. Das Skript wertet alle Spalten aus und erstellt separate Ergebnisse für einzelne Proben sowie für gesamte Parametersätze.
4. Die Ergebnisse werden in zwei CSV-Dateien gespeichert.
### Ausgabe
- `Ergebnissammlung_Härte_Auswertung_Proben.csv`
    Enthält die berechneten Kennzahlen für jede einzelne Probe.
- `Ergebnissammlung_Härte_Auswertung_Parameterset.csv`
    Enthält die zusammengefasste statistische Auswertung für vordefinierte Parametersätze.