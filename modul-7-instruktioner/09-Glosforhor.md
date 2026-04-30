# Projekt 9: Glosförhör

## Målsättning
Skapa ett glosförhör med dictionary, poängräkning och feedback.

## Ska-krav
- Skapa dictionary med minst fem engelska ord och svenska översättningar.
- Använd en poängvariabel.
- Loopa med items för att fråga alla glosor.
- Jämför svar utan att stora/små bokstäver påverkar.
- Skriv ut totalpoäng i slutet.

## Kan-krav
- Slumpa ordning på glosor.
- Visa rätt svar vid fel.
- Lägg till flera språkpar eller teman.
- Ge sammanfattning med procent och betygsintervall.
- Spara högsta poäng i fil.

## Förslag på testfall
- Rätta svar ger poängökning.
- Fel svar ger ingen poäng men fortsatt körning.
- Svar med blandade stora/små bokstäver bedöms korrekt.



glosor = {
    "house": "hus",
    "cat": "katt",
    "dog": "hund",
    "car": "bil",
    "tree": "träd",
}

glosor_svenska = [
    "hus",
    "katt",
    "hund",
    "bil",
    "träd",
]

glosor_engelska = [
    "house",
    "cat",
    "dog",
    "car",
    "tree",
]