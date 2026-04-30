# Projekt 10: Tre i rad

## Målsättning
Bygg ett komplett Tre i rad med spelplan, turer och korrekt vinstkontroll.

## Ska-krav
- Skapa en spelplan på 3x3.
- Låt två spelare turas om att placera X och O.
- Validera att vald ruta är ledig och inom planen.
- Kontrollera vinst efter varje drag (rader, kolumner, diagonaler).
- Hantera oavgjort när planen är full utan vinnare.

## Kan-krav
- Lägg till möjlighet att spela flera rundor med totalställning.
- Gör inmatningen mer användarvänlig (t.ex. A1, B2, C3).
- Lägg till meny och val av symboler.
- Lägg till funktionalitet för att göra planen större.

## Förslag på testfall
- Vinst i rad, kolumn och diagonal upptäcks korrekt.
- Ogiltigt drag på upptagen ruta stoppas.
- Full plan utan vinnare ger oavgjort.
