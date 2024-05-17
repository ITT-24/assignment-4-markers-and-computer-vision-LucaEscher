## Distanz Funktion

```
schreibe mir eine Funktion, die den abstand zwischen zwei punkten in einem Koordinaten system wiedergibt

ChatGPT
Um eine Funktion zu schreiben, die den Abstand zwischen zwei Punkten in einem Koordinatensystem berechnet, kannst du den euklidischen Abstand verwenden. Die Formel für den euklidischen Abstand zwischen zwei Punkten 
(
x
1
,
y
1
)
(x1,y1) und 
(
x
2
,
y
2
)
(x2,y2) lautet:

Abstand
=
(
x
2
−
x
1
)
2
+
(
y
2
−
y
1
)
2
Abstand= 
(x2−x1) 
2
 +(y2−y1) 
2
 
​	
 

Hier ist eine Python-Funktion, die diese Berechnung durchführt:

python
Code kopieren
import math

def berechne_abstand(punkt1, punkt2):
    """
    Berechnet den euklidischen Abstand zwischen zwei Punkten.

    :param punkt1: Ein Tupel (x1, y1) mit den Koordinaten des ersten Punktes.
    :param punkt2: Ein Tupel (x2, y2) mit den Koordinaten des zweiten Punktes.
    :return: Der Abstand zwischen den beiden Punkten.
    """
    x1, y1 = punkt1
    x2, y2 = punkt2
    abstand = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return abstand

# Beispiel:
punkt1 = (3, 4)
punkt2 = (7, 1)
abstand = berechne_abstand(punkt1, punkt2)
print(f"Der Abstand zwischen den Punkten {punkt1} und {punkt2} beträgt {abstand:.2f} Einheiten.")
Erläuterung:
Importieren der Bibliothek: Wir importieren die math-Bibliothek, um die Quadratwurzel (math.sqrt) berechnen zu können.
Definition der Funktion: Die Funktion berechne_abstand nimmt zwei Punkte als Parameter, wobei jeder Punkt durch ein Tupel 
(
x
,
y
)
(x,y) dargestellt wird.
Berechnung des Abstands: Innerhalb der Funktion werden die Koordinaten der Punkte extrahiert und die euklidische Distanz berechnet.
Beispielverwendung: Es wird gezeigt, wie die Funktion mit zwei Beispielpunkten aufgerufen und das Ergebnis ausgegeben wird.
Die Funktion gibt den Abstand zwischen den beiden Punkten im Koordinatensystem zurück.
```
