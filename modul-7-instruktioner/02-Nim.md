# Projekt 2: Strategispelet Nim

## Målsättning
Skapa ett spel med 21 stickor där spelare och dator turas om att ta 1-3 stickor.

## Ska-krav
- Starta med 21 stickor.
- Kör en while-loop så länge stickor finns kvar.
- Låt spelaren välja 1, 2 eller 3 stickor.
- Kontrollera att spelarens val är giltigt.
- Låt datorn ta stickor (slump 1-3, men inte fler än kvar).
- Avsluta spelet vid 0 stickor och skriv ut vinnare/förlorare enligt regeln: den som tog sista stickan förlorar.

## Kan-krav
- Implementera smart datorstrategi (vinnande Nim-logik).
- Visa historik över drag i varje runda.
- Stöd för flera matcher i rad med totalställning.
- Tydligare UI med rundnummer och kvarvarande stickor grafiskt.
- Robust felhantering av all inmatning.

## Förslag på testfall
- Spelaren anger giltiga val 1-3.
- Spelaren anger ogiltigt val (0, 4, text) och får ny chans.
- Spelet avgör korrekt utfall när sista stickan tas.

