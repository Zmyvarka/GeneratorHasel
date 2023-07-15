import string
import random

znaki = list(string.ascii_letters + string.digits + "!@#$%^&*()")

def generuj_haslo():
    dlugosc_hasla = int(input("Ile znaków ma mieć twoje hasło? "))
    
    random.shuffle(znaki)
    haslo = []

    for _ in range(dlugosc_hasla):
        haslo.append(random.choice(znaki))


    random.shuffle(haslo)
    haslo = "".join(haslo)

    print(haslo)


while True:
    wybor = input("Czy chcesz wygenerować hasło? (Tak/Nie) ")

    if wybor == "Tak":
        wygenerowane_haslo = generuj_haslo()
        platforma = input("Do jakiej platformy przypisujesz to hasło? ")
        login = input("Podaj login do podanej platformy: ")
    
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

