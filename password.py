import random
import string


def genereaza_parola(lungime):
    caractere = string.ascii_letters +string.digits +string.punctuation
    return ''.join(random.choice(caractere) for _ in range (lungime))

print("Parola generata: ", genereaza_parola(12))