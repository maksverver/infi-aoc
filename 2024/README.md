Deze directory bevat oplossingen voor de Infi Advent of Code 2024 opgave:
Sneeuwvlokken en sneeuwblokken (https://aoc.infi.nl/2024).

Er zijn twee oplossingen, beide geschreven in Python:

 1. [solve-compact.py](solve-compact.py)

    Een volledige oplossing in één scriptbestand.

 2. [solve-verbose.py](solve-verbose.py)

    Een iets algemenere oplossing die het probleem opsplitst in het simuleren
    van het programma ([machine.py](machine.py)) en het identificeren van wolken
    ([floodfill.py](floodfill.py)). Het theoretische voordeel is dat de code
    beter herbruikbaar en uitbreidbaar is, hoewel het praktische nut hiervan
    natuurlijk beperkt is. Ook is deze oplossing iets sneller omdat de
    instructies van de machine maar één keer geïnterpreteerd hoeven te worden.

Beide oplossingen lezen de invoer uit `input.txt` en schrijven de antwoorden
naar standaard uitvoer. Voorbeeld:

```shell
$ python3 solve-compact.py
4926
16
```
