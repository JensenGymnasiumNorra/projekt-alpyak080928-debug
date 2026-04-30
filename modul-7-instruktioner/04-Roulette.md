# Projekt 4: Roulette

## Målsättning
Bygg en roulette-simulator med saldo, satsningar och korrekt utbetalning.

## Ska-krav
- Startsaldo ska vara 1000 kr.
- Användaren ska kunna satsa på nummer, färg eller jämnt/udda.
- Kontrollera att insats inte överstiger saldo.
- Slumpa vinnande nummer mellan 0 och 36.
- Presentera vinnande nummer och relevanta egenskaper.
- Uppdatera saldo med korrekt utbetalning (35:1 för nummer, 1:1 för färg/paritet).
- Spelet fortsätter tills användaren avslutar eller saldot är slut.

## Kan-krav
- Validera all inmatning med tydliga felmeddelanden.
- Lägg till statistik: antal rundor, vinst/förlust, högsta saldo.
- Stöd för flera insatser i samma runda.
- Lägg till europeisk regel för 0 (varken röd/svart eller jämn/udda).
- Spara spelhistorik i fil.

## Förslag på testfall
- Satsning större än saldo stoppas.
- Vinst på nummer ger högre utbetalning än färg/paritet.
- 0 hanteras korrekt vid färg och paritet.

