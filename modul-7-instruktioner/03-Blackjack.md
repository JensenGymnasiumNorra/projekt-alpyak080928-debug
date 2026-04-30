# Projekt 3: Blackjack

## Målsättning
Bygg ett fungerande Blackjack med poängräkning, dealerlogik och vinstvillkor.

## Ska-krav
- Implementera berakna_poang(hand).
- Hantera J, Q, K som 10 poäng.
- Hantera Ess dynamiskt som 11 eller 1 för att undvika att bli tjock.
- Låt dealern dra kort tills dealern har minst 17 poäng.
- Jämför slutpoäng och avgör vinnare korrekt.

## Kan-krav
- Skapa riktig kortlek med kort som inte kan dras två gånger.
- Stöd för hit/stand-val under spelarens tur.
- Hantera blackjack på första given (naturlig 21).
- Visa handens kort snyggt, inklusive dolt dealerkort i början.
- Lägg till saldo och insatssystem.

## Förslag på testfall
- Hand med Ess som måste byta mellan 11 och 1.
- Dealer stannar på 17+.
- Vinst, förlust och oavgjort testas separat.
