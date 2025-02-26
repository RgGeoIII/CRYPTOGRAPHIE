#!/bin/bash

echo "=== MISE A JOUR DU SYSTEME ==="
sudo apt update && sudo apt upgrade -y

echo "=== INSTALLATION DE PYTHON ET PIP ==="
sudo apt install python3 python3-pip -y

echo "=== VERIFICATION DE L'INSTALLATION ==="
python3 --version
pip3 --version

echo "=== INSTALLATION TERMINEE ==="
echo "Vous pouvez maintenant exécuter du code Python avec la commande : python3 votre_script.py"
