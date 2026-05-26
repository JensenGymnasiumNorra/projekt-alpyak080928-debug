import random
# Skapa en kortlek
kortlek = []

suits = ["♣", "♠", "♦", "♥"]
values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

for suit in suits:
    for value in values:
        kortlek.append(suit +" "+ value)

random.shuffle(kortlek)

# Tutorial
print("BLACKJACK SNABB TUTORIAL")
print()
print(" MÅL: Kom närmare 21 än dealern utan att gå över.")
print()
print("KORTVÄRDEN:")
print("  2-10  = Sitt eget siffervärde")
print("  J/Q/K = 10 poäng")
print("  A  = 1 eller 11 (väljs automatiskt för bästa värde)")
print()
print("SÅ HÄR SPELAR Man:")
print("  1. Du och dealern får 2 kort var.")
print("  2. Dealerns ena kort är dolt.")
print("  3. Välj: Ta ett kort (Hit) eller Stanna (Stand).")
print("  4. Går du över 21 förlorar du direkt.")
print("  5. Dealern vänder sitt dolda kort och drar tills han har 17+.")
print("  6. Närmast 21 vinner!")
print()

# Dela ut 2 kort vardera
spelar_hand = [kortlek.pop(), kortlek.pop()]
dealer_hand = [kortlek.pop(), kortlek.pop()]

# Räkna värde på korten
def rakna_varde(hand):
    varde = 0
    antal_ess = 0

    for kort in hand:
        rank = kort.split()[-1]
        if rank in ["J", "Q", "K"]:
            varde += 10
        elif rank == "A":
            antal_ess += 1
            varde += 11
        else:
            varde += int(rank)

    while varde > 21 and antal_ess > 0:
        varde -= 10
        antal_ess -= 1

    return varde

# Kolla blackjack
def har_blackjack(hand):
    return rakna_varde(hand) == 21 and len(hand) == 2

# Visa korten
def visa_korten():
    print("Dina kort:    ", spelar_hand)
    print("Dealerns kort:  [Dolt]", dealer_hand[1])
    print()
    print("Spelarens värde:", rakna_varde(spelar_hand))
    print("Dealerns synliga värde:", rakna_varde([dealer_hand[1]]))

visa_korten()

# Kolla spelaren
if har_blackjack(spelar_hand):
    print("\nBLACKJACK! Du fick 21 direkt!")

# Kolla dealern
if har_blackjack(dealer_hand):
    print("\nDealern vänder sitt dolda kort:", dealer_hand)
    print("Dealern har BlackJack! Du förlorade.")

# Spelarens tur
# Dealerns tur
# Avgör vinnaren
# Spela igen