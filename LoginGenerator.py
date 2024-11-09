import secrets
import string


print("W tym programie wygenerujesz hasło podajac swoje imie i nazwisko")


imie = input("Podaj imie: ")
nazwisko = input("Podaj nazwisko: ")


def GenerujLogin(imie, nazwisko):
    login = (imie[:3] + nazwisko[:3]).lower()
    return login

login = GenerujLogin(imie, nazwisko)


def GenerujHaslo(length=12):
    znaki = string.ascii_letters + string.digits + string.punctuation
    haslo = ''.join(secrets.choice(znaki) for _ in range(length))
    return haslo

haslo = GenerujHaslo()


print(login)
print(haslo)


