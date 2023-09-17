import os

import dodatek_importowany
import dodatek_zapis

print("-----------------------")
lista = dodatek_zapis.wczytaj()
print(f"TEST: >{lista[0]}<")
print(f"Poprawnie wczytano liste, {lista}")
Y = dodatek_importowany.zaladuj_dodatek()

while True:
    print("-----------------------")
    print("[OPCJE/OPERACJE]:")
    print(f"[1 - wyszukaj {Y}]")
    print(f"[2 - dodaj {Y}]")
    print(f"[3 - usuń {Y}]")
    print(f"[4 - popraw {Y}]")
    print(f"[5 - zamineń {Y}e]")
    print("[6 - zapisz]")
    print("[7 - wczytaj]")
    print("[8 - zobacz liste]")
    print("[9 - o programie]")
    print("[10 - wyjdź]")
    print("-----------------------")
    wybor = input("Wybieram: ").lower()

    if wybor == "1" or wybor == "wyszukaj " + Y + "":
        dodatek_importowany.czyszczenie_ekranu()
        print(dodatek_importowany.sprawdz(dodatek_importowany.funkcja_pytania(), lista))

    elif wybor == "2" or wybor == "dodaj " + Y + "":
        print(f"Czy chcesz dodać {Y} z przodu?")
        wynik = input("tak/nie: ").lower()
        if wynik == "tak" or wynik == "t":
            dodatek_importowany.czyszczenie_ekranu()
            lista = dodatek_importowany.dodaj(dodatek_importowany.funkcja_pytania(), lista, True)
        else:
            dodatek_importowany.czyszczenie_ekranu()
            lista = dodatek_importowany.dodaj(dodatek_importowany.funkcja_pytania(), lista)

    elif wybor == "3" or wybor == "usuń " + Y + "":
        dodatek_importowany.czyszczenie_ekranu()
        lista = dodatek_importowany.usun(dodatek_importowany.funkcja_pytania(), lista)

    elif wybor == "4" or wybor == "popraw" + Y + "":
        dodatek_importowany.czyszczenie_ekranu()
        lista = dodatek_importowany.popraw(dodatek_importowany.funkcja_pytania(), lista)

    elif wybor == "5" or wybor == "zamień":
        dodatek_importowany.czyszczenie_ekranu()
        dodatek_importowany.zamien(dodatek_importowany.funkcja_pytania(), lista)

    elif wybor == "6" or wybor == "zapisz":
        dodatek_importowany.czyszczenie_ekranu()
        dodatek_zapis.zapisz(lista)

    elif wybor == "7" or wybor == "wczytaj":
        dodatek_importowany.czyszczenie_ekranu()
        dodatek_zapis.wczytaj()

    elif wybor == "8" or wybor == "zobacz liste":
        dodatek_importowany.czyszczenie_ekranu()
        print(*lista, sep="|")

    elif wybor == "9" or wybor == "o programie":
        dodatek_importowany.czyszczenie_ekranu()
        print("Nazwa: Uniwersalny Menażer OpenS.")
        print("Autor: Dawid Cisiński")
        print("Wersja: 1.0 (owoce)")
        print(dodatek_importowany.zaladuj_dodatek(True))
        print(dodatek_zapis.zaladuj_dodatek_zapis(True))
        print(f"TEST: >{lista[1]}<")
        print(f"Poprawnie wczytano liste, {lista}")

    elif wybor == "10" or wybor == "wyjdź":
        dodatek_importowany.czyszczenie_ekranu()
        input("Wciśnij dowolny klawisz...")
        os.system('cls')
        break

    else:
        dodatek_importowany.czyszczenie_ekranu()
        print("ERROR! [01] wybierz cyfrę od 1-4")

# Autor: Dawid Cisiński
