from pyAesCrypt import encryptFile, decryptFile
import os
import uuid

# Paramètres
buffer_size = 64 * 1024  # Taille du buffer (64 Ko)
password = "toto"  # Mot de passe de chiffrement


# Fonction de chiffrement avec renommage définitif
def chiffrer_dossier(dossier_source):
    for racine, sous_dossiers, fichiers in os.walk(dossier_source, topdown=False):

        # Chiffrer les fichiers avec renommage
        for fichier in fichiers:
            chemin_source = os.path.join(racine, fichier)

            # Générer un nom de fichier unique et chiffré
            nom_fichier_chiffre = str(uuid.uuid4()) + ".aes"
            chemin_dest = os.path.join(racine, nom_fichier_chiffre)

            # Chiffrement du fichier
            encryptFile(chemin_source, chemin_dest, password, buffer_size)
            print(f"Fichier chiffré : {chemin_source} -> {chemin_dest}")

            # Suppression de l'original après chiffrement
            os.remove(chemin_source)
            print(f"Fichier original supprimé : {chemin_source}")

        # Renommer les dossiers
        dossier_source_absolu = os.path.abspath(dossier_source)
        if racine != dossier_source_absolu:
            nom_dossier_chiffre = str(uuid.uuid4())
            dossier_renomme = os.path.join(os.path.dirname(racine), nom_dossier_chiffre)
            os.rename(racine, dossier_renomme)
            print(f"Dossier renommé : {racine} -> {dossier_renomme}")


# Fonction de déchiffrement sans restauration des noms d'origine
def dechiffrer_dossier(dossier_source):
    for racine, sous_dossiers, fichiers in os.walk(dossier_source, topdown=False):
        for fichier in fichiers:
            # On ne traite que les fichiers .aes
            if fichier.endswith(".aes"):
                chemin_source = os.path.join(racine, fichier)

                # Générer un nom de fichier déchiffré (aléatoire, sans .aes)
                nom_fichier_dechiffre = str(uuid.uuid4())
                chemin_dest = os.path.join(racine, nom_fichier_dechiffre)

                # Déchiffrement du fichier
                decryptFile(chemin_source, chemin_dest, password, buffer_size)
                print(f"Fichier déchiffré : {chemin_source} -> {chemin_dest}")

                # Suppression du fichier chiffré après déchiffrement
                os.remove(chemin_source)
                print(f"Fichier chiffré supprimé : {chemin_source}")

        # Les dossiers gardent leurs noms aléatoires après déchiffrement


# Menu interactif
def menu():
    while True:
        print("\n=== MENU ===")
        print("1. Chiffrer un dossier existant (renomme définitivement les fichiers et dossiers)")
        print("2. Déchiffrer un dossier existant (les noms restent aléatoires)")
        print("3. Quitter")

        choix = input("\nChoisissez une option (1, 2 ou 3) : ")

        if choix == "1":
            dossier_source = input("Entrez le chemin du dossier à chiffrer : ")
            if os.path.isdir(dossier_source):
                chiffrer_dossier(dossier_source)
                print(
                    "\nTous les fichiers ont été chiffrés avec succès, les originaux supprimés et les dossiers/fichiers renommés définitivement.")
            else:
                print("Le dossier n'existe pas. Veuillez vérifier le chemin.")

        elif choix == "2":
            dossier_source = input("Entrez le chemin du dossier à déchiffrer : ")
            if os.path.isdir(dossier_source):
                dechiffrer_dossier(dossier_source)
                print("\nTous les fichiers ont été déchiffrés avec succès, les fichiers chiffrés supprimés.")
            else:
                print("Le dossier n'existe pas. Veuillez vérifier le chemin.")

        elif choix == "3":
            print("\nAu revoir !")
            break

        else:
            print("\nOption invalide. Veuillez choisir 1, 2 ou 3.")


# Lancer le menu
menu()
