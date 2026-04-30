# Projekt 8: Yatzy

## Målsättning
Skapa ett Yatzy-liknande kastspel med omkastning och kombinationsbedömning.

## Ska-krav
- Slumpa 5 tärningar.
- Ge spelaren två chanser till omkastning av valfria index.
- Läs in index och kasta om valda tärningar.
- Identifiera och skriv ut Yatzy, Kåk eller Tretal.
- Om ingen av dessa: skriv ut summan av tärningarna.

## Kan-krav
- Validera indexinmatning (0-4, unika, inga feltyper).
- Lägg till fler kombinationer, t.ex. par, två par, stege.
- Visa frekvenskarta för tärningarna (antal av varje värde).
- Lägg till poängsystem över flera rundor.
- Lägg till tydlig meny med nytt spel/avsluta.

## Förslag på testfall
- Hand med fem lika blir Yatzy.
- Hand med 3+2 identifieras som Kåk.
- Ogiltiga index vid omkastning hanteras utan krasch.
