# Projekt 14: Wordle

## Målsättning
Skapa ett Wordle-liknande ordspel med "färgkodad" feedback per bokstav.

## Ska-krav
- Välj ett hemligt ord med fast längd (t.ex. 5 bokstäver).
- Ge spelaren ett begränsat antal gissningar.
- Efter varje gissning: markera bokstäver som rätt plats, fel plats eller inte finns.
- Kontrollera att gissningen har rätt längd.
- Spelet avslutas med vinst vid rätt ord eller förlust när försök tar slut.

## Kan-krav
- Kontrollera att gissat ord finns i en ordlista.
- Hantera dubbla bokstäver korrekt enligt Wordle-logik.
- Lägg till valbar ordlängd.
- Lägg till dagligt ord eller slumpat ord.
- Spara statistik: vinstprocent och gissningsfördelning.

## Förslag på testfall
- Rätt ord på första försöket ger vinst.
- Gissning med fel längd nekas.
- Feedback för rätt/fel plats fungerar på ord med upprepade bokstäver.

possible_words = ["house", "about", "other", "world", "would", "great", "small", "light", "night", "point"]

