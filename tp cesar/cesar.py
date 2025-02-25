import random

# Fonction de chiffrement
def chiffrer(message: str, decalage: int) -> str:
    resultat = ""
    decalage = decalage % 26  # Gérer les décalages supérieurs à 26
    for caractere in message:
        # Chiffrement des majuscules
        if caractere.isupper():
            resultat += chr((ord(caractere) + decalage - 65) % 26 + 65)
        # Chiffrement des minuscules
        elif caractere.islower():
            resultat += chr((ord(caractere) + decalage - 97) % 26 + 97)
        # Autres caractères restent inchangés
        else:
            resultat += caractere
    return resultat

# Fonction de déchiffrement
def dechiffrer(message_chiffre: str, decalage: int) -> str:
    return chiffrer(message_chiffre, -decalage)

# Déchiffrement par force brute
def brute_force_attack(message_chiffre: str):
    print("\n=== Déchiffrement par Force Brute ===")
    for i in range(1, 26):
        tentative = dechiffrer(message_chiffre, i)
        print(f"Décalage {i} : {tentative}")

# Menu interactif
def menu():
    while True:
        print("\n=== MENU ===")
        print("1. Chiffrer un message")
        print("2. Déchiffrer un message")
        print("3. Déchiffrement par Force Brute (Casser un code sans connaître le décalage)")
        print("4. Quitter")

        choix = input("\nChoisissez une option (1, 2, 3 ou 4) : ")

        if choix == "1":
            message = input("Entrez le message à chiffrer : ")
            choix_decalage = input("Voulez-vous un décalage aléatoire ? (o/n) : ").lower()
            if choix_decalage == 'o':
                decalage = random.randint(1, 25)
                print(f"Décalage aléatoire choisi : {decalage}")
            else:
                decalage = int(input("Entrez le décalage (ex : 3) : "))
            message_chiffre = chiffrer(message, decalage)
            print(f"\nMessage chiffré : {message_chiffre}")

        elif choix == "2":
            message_chiffre = input("Entrez le message à déchiffrer : ")
            decalage = int(input("Entrez le décalage (utilisé pour le chiffrage) : "))
            message_dechiffre = dechiffrer(message_chiffre, decalage)
            print(f"\nMessage déchiffré : {message_dechiffre}")

        elif choix == "3":
            message_chiffre = input("Entrez le message chiffré à casser : ")
            brute_force_attack(message_chiffre)

        elif choix == "4":
            print("\nAu revoir !")
            break

        else:
            print("\nOption invalide. Veuillez choisir 1, 2, 3 ou 4.")

# Lancer le menu
menu()
