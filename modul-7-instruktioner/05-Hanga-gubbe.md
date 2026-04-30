# Projekt 5: Hänga gubbe

## Målsättning
Bygg en spelbar version av Hänga gubbe med liv, bokstavsgissningar och vinst/förlust.

## Ska-krav
- Programmet väljer ett hemligt ord.
- Loopa så länge spelaren har liv kvar och ordet inte är komplett.
- Läs in en bokstav per drag.
- Kontrollera om bokstaven redan gissats.
- Uppdatera visning av ordet vid rätt gissning.
- Minska liv vid fel gissning.
- Skriv ut tydligt om spelaren vann eller förlorade.

## Kan-krav
- Visa använda bokstäver sorterat.
- Hantera ord med flera lika bokstäver korrekt.
- Validera att input är exakt en bokstav.
- Välj ord slumpmässigt från lista eller fil.
- Rita enkel ASCII-gubbe som utvecklas med antalet fel.

## Förslag på testfall
- Rätt bokstav uppdaterar alla positioner.
- Samma bokstav flera gånger ger varning utan att ta liv.
- Fel bokstav minskar liv och spelet avslutas vid 0.

