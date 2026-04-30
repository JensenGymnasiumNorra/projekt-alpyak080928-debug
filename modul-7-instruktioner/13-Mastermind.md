# Projekt 13: Mastermind

## Målsättning
Bygg Mastermind där spelaren gissar en hemlig kod med återkoppling efter varje försök.

## Ska-krav
- Generera en hemlig kod med fasta regler (t.ex. 4 siffror).
- Låt spelaren gissa koden i flera omgångar.
- Efter varje gissning: visa antal rätt siffra på rätt plats.
- Visa även antal rätt siffra på fel plats.
- Avsluta med vinst när koden är rätt eller förlust när försök tar slut.

## Kan-krav
- Låt spelaren välja kodlängd och antal försök.
- Lägg till färger/symboler i stället för siffror.
- Visa historik över alla tidigare gissningar.
- Validera inmatning strikt (längd, teckentyp).
- Lägg till poäng baserat på antal försök kvar.

## Förslag på testfall
- Fulltäff ger direkt vinst.
- Delvis rätt gissning ger korrekt återkoppling.
- Fel längd eller ogiltiga tecken hanteras utan krasch.
