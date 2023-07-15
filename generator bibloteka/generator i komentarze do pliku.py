import string
import random
#definiowanie listy znaków z jakich będą składały się hasła
znaki = list(string.ascii_letters + string.digits + "!@#$%^&*()")

#funkcja generująca hasła oparta o randomowe losowanie znaków z listy znaki i wrzucanie ich do pustej listy hasło 
def generuj_haslo():
    dlugosc_hasla = int(input("Ile znaków ma mieć twoje hasło? "))
    
    random.shuffle(znaki)
    haslo = []

    for _ in range(dlugosc_hasla):
        haslo.append(random.choice(znaki))


    random.shuffle(haslo)
    #usuwanie tradycyjnych przerywników w listach żeby wynik końcowy nie był pełny przecinków i kwadratowych nawiasów
    haslo = "".join(haslo)

    print(haslo)

#pętla zmuszajaca użytkownika do podjęcia decyzji na temat generowania hasła
while True:
    wybor = input("Czy chcesz wygenerować hasło? (Tak/Nie) ")

    if wybor == "Tak":
        wygenerowane_haslo = generuj_haslo()
        platforma = input("Do jakiej platformy przypisujesz to hasło? ")
        login = input("Podaj login do podanej platformy: ")
        #funkcja open otwierajaca plik oraz funkcja write która wysyła do owego pliku hasło o raz informacje z nim związane
        with open("test.txt", "a") as f:
                f.write(f"Platforma: {platforma}\n")
                f.write(f"Login: {login}\n")
                f.write(f"Hasło: {wygenerowane_haslo}\n")

        print("Hasło zostało zapisane w pliku test.txt")
    elif wybor == "Nie":
        print("Zamykanie programu")
        break
    else:
        print("Niepoprawna wiadomość, proszę wpisać Tak lub Nie ")
    continue

