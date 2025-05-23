from pyAesCrypt import encryptFile, decryptFile

buffer_size = 64 * 1024
password = "toto"

# Chemin des fichiers
input_file = "input/TP Cryptographie César ROUVEL.pdf"
encrypted_file = "encrypted/TP Cryptographie César ROUVEL.pdf.aes"
decrypted_file = "output/TP Cryptographie César ROUVEL.pdf"

# Chiffrement du fichier
encryptFile(input_file, encrypted_file, password, buffer_size)
print("Fichier chiffré avec succès.")

# Déchiffrement du fichier
decryptFile(encrypted_file, decrypted_file, password, buffer_size)
print("Fichier déchiffré avec succès.")
