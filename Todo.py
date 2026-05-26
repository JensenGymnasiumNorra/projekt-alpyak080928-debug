def visa_uppgifter(lista):
    if not lista:
        print("Listan är tom.")
    else:
        print("\nTo-Do-lista:")
        for i, uppgift in enumerate(lista):
            print(f"{i}: {uppgift}")


def lagg_till_uppgift(lista):
    uppgift = input("Skriv in en ny uppgift: ")
    if uppgift.strip():
        lista.append(uppgift)
        print("Uppgift tillagd.")
    else:
        print("Tom uppgift ignorerades.")


def ta_bort_uppgift(lista):
    if not lista:
        print("Listan är tom.")
        return

    try:
        index = int(input("Ange index på uppgiften att ta bort: "))
        if 0 <= index < len(lista):
            borttagen = lista.pop(index)
            print(f"Tog bort: {borttagen}")
        else:
            print("Ogiltigt index.")
    except ValueError:
        print("Du måste ange ett heltal.")


def sortera_uppgifter(lista):
    lista.sort()
    print("Listan är sorterad alfabetiskt.")


def huvudmeny():
    uppgifter = []

    while True:
        print("\n--- MENY ---")
        print("1. Visa uppgifter")
        print("2. Lägg till uppgift")
        print("3. Ta bort uppgift")
        print("4. Sortera uppgifter")
        print("5. Avsluta")

        val = input("Välj ett alternativ: ")

        if val == "1":
            visa_uppgifter(uppgifter)
        elif val == "2":
            lagg_till_uppgift(uppgifter)
        elif val == "3":
            ta_bort_uppgift(uppgifter)
        elif val == "4":
            sortera_uppgifter(uppgifter)
        elif val == "5":
            print("Avslutar programmet.")
            break
        else:
            print("Ogiltigt val, försök igen.")


# Starta programmet
huvudmeny()