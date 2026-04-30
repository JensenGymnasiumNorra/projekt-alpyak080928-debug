# Projekt 7: Minröjaren

## Målsättning
Implementera logiken för att räkna minor runt en ruta och fylla spelplanen med rätt siffror.

## Ska-krav
- Implementera funktionen count_adjacent_mines.
- Kontrollera alla 8 grannrutor runt given position.
- Hantera kanter/horn utan indexfel.
- Låt minor (M) vara oförändrade.
- Loopa genom hela planen och ersätt tomma rutor med antal intilliggande minor.

## Kan-krav
- Dela upp kod i tydliga hjälp-funktioner.
- Skriv tester för horn, kanter och mitt-ruta.
- Lägg till funktion för att visa dold/synlig spelplan.
- Implementera flood fill för tomma rutor (extra).
- Lägg till vinstvillkor för komplett spelversion.

## Förslag på testfall
- Hornruta med minor i närheten räknas korrekt.
- Mittruta räknar alla 8 grannar korrekt.
- Mina-ruta förblir M efter uppdatering.
