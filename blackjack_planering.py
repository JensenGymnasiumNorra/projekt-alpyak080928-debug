import random



# Tutorial för Blackjack (Snabbt)
def visa_tutorial():
   
    print("     BLACKJACK - TUTORIAL     ")
    print("MÅL: Kom närmre 21 än dealern utan att gå över.")
    print()
    print("KORTVÄRDEN:")
    print("  2-10  = Siffervärdet")
    print("  J/Q/K = 10 poäng")
    print("  A     = 1 eller 11 (automatiskt)")
    print()
    print("SÅ HÄR SPELAR DU:")
    print("  1. Du och dealern får 2 kort var")
    print("  2. Dealerns ena kort är dolt")
    print("  3. Hit = ta ett kort, Stand = stanna")
    print("  4. Går du över 21 förlorar du direkt")
    print("  5. Dealern drar tills han har 17+")
    print("  6. Närmast 21 vinner")


# Skapa kortleken
def skapa_kortlek():
    suits  = ["♣", "♠", "♦", "♥"]
    values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    kortlek = []
    for suit in suits:
        for value in values:
            kortlek.append(suit + " " + value)
    return kortlek


# Blanda kortleken
def blanda(kortlek):
    random.shuffle(kortlek)
    return kortlek


# Dela ut korten
def dra_kort(kortlek):
    return kortlek.pop()


#  Räknavärdet på korten
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


# Kolla för blackjack
def har_blackjack(hand):
    return rakna_varde(hand) == 21 and len(hand) == 2


#Visa korten
def visa_korten(spelar_hand, dealer_hand, dolt=True):
    print()
    print("Dina kort:      ", spelar_hand)
    if dolt:
        print("Dealerns kort:   [Dolt]", dealer_hand[1])
    else:
        print("Dealerns kort:  ", dealer_hand)
    print()
    print("Ditt värde:     ", rakna_varde(spelar_hand))
    if dolt:
        print("Dealerns synliga:", rakna_varde([dealer_hand[1]]))
    else:
        print("Dealerns värde:  ", rakna_varde(dealer_hand))
    print()


# Spelarens tur
def spelarens_tur(spelar_hand, dealer_hand, kortlek):
    while True:
        val = input("Hit (h) eller Stand (s)? ").strip().lower()
        if val == "h":
            spelar_hand.append(dra_kort(kortlek))
            visa_korten(spelar_hand, dealer_hand, dolt=True)
            if rakna_varde(spelar_hand) > 21:
                print("Over 21 - du sprack!")
                return False
            if rakna_varde(spelar_hand) == 21:
                print("Exakt 21!")
                return True
        elif val == "s":
            print("Du stannar.")
            return True
        else:
            print("Skriv h eller s.")


# Dealerns tur
def dealerns_tur(dealer_hand, kortlek):
    print("Dealern vänder sitt dolda kort...")
    while rakna_varde(dealer_hand) < 17:
        dealer_hand.append(dra_kort(kortlek))
        print("Dealern drar:", dealer_hand[-1])


# Avgör vinnare 
def avgör_vinnare(spelar_hand, dealer_hand, insats):
    sp = rakna_varde(spelar_hand)
    dp = rakna_varde(dealer_hand)
    print("==============================")
    print("Ditt värde:    ", sp)
    print("Dealerns värde:", dp)
    print("==============================")
    if sp > 21:
        print("Du sprack - du förlorade", insats, "kr")
        return -insats
    elif dp > 21:
        print("Dealern sprack - du vann", insats, "kr!")
        return insats
    elif sp > dp:
        print("Du vann", insats, "kr!")
        return insats
    elif sp < dp:
        print("Dealern vann - du förlorade", insats, "kr")
        return -insats
    else:
        print("Oavgjort - du får tillbaka din insats")
        return 0


# Välj insats
def valj_insats(krediter):
    while True:
        print("Du har", krediter, "kr")
        try:
            insats = int(input("Hur mycket vill du satsa? "))
            if insats <= 0:
                print("Insatsen måste vara mer än 0.")
            elif insats > krediter:
                print("Du har inte råd med det.")
            else:
                return insats
        except ValueError:
            print("Skriv ett heltal.")



def main():
    visa_tutorial()

    krediter = 500
    print("Du börjar med", krediter, "kr")
    print()

    while krediter > 0:
        print("──────────────────────────────")

        # Välj pengarna
        insats = valj_insats(krediter)

        # Skapa och blanda kortlek
        kortlek = blanda(skapa_kortlek())

        # Dela ut kort
        spelar_hand = [dra_kort(kortlek), dra_kort(kortlek)]
        dealer_hand = [dra_kort(kortlek), dra_kort(kortlek)]

        # Visa korten
        visa_korten(spelar_hand, dealer_hand, dolt=True)

        # Kolla om det finnns blackjack direkt
        if har_blackjack(spelar_hand) and har_blackjack(dealer_hand):
            print("Båda har Blackjack - oavgjort!")
            vinst = 0
        elif har_blackjack(spelar_hand):
            print("BLACKJACK! Du vann", insats, "kr!")
            vinst = insats
        elif har_blackjack(dealer_hand):
            print("Dealern har Blackjack! Du förlorade", insats, "kr")
            visa_korten(spelar_hand, dealer_hand, dolt=False)
            vinst = -insats
        else:
            # Spelarens tur
            fortsatt = spelarens_tur(spelar_hand, dealer_hand, kortlek)

            # Dealerns tur (bara om spelaren e kvar)
            if fortsatt:
                dealerns_tur(dealer_hand, kortlek)
                visa_korten(spelar_hand, dealer_hand, dolt=False)

            # Avgör vinnaren
            vinst = avgör_vinnare(spelar_hand, dealer_hand, insats)

        # Uppdatera pengar
        krediter += vinst
        print("Ditt saldo:", krediter, "kr")
        print()

        if krediter <= 0:
            print("Du har inga krediter kvar - spelet är slut!")
            break

        # Spela igen?
        igen = input("Spela igen? (j/n): ").strip().lower()
        if igen != "j":
            print("Tack för att du spelade! Slutsaldo:", krediter, "kr")
            break

main()