def decalage_message(message, decalage):
    resultat = ""  # Chaîne qui contiendra le message codé final
    
    for caractere in message:  # On parcourt chaque lettre du message
        # Si c'est une lettre minuscule
        if 'a' <= caractere <= 'z':
            # Trouver la position de la lettre dans l'alphabet (0 à 25)
            position = ord(caractere) - ord('a')
            # Ajouter le décalage et faire le modulo 26 pour gérer les dépassements
            nouvelle_position = (position + decalage) % 26
            # Convertir cette nouvelle position en lettre
            nouveau_caractere = chr(nouvelle_position + ord('a'))
            # Ajouter au résultat
            resultat += nouveau_caractere
        
        # Si c'est une lettre majuscule
        elif 'A' <= caractere <= 'Z':
            position = ord(caractere) - ord('A')
            nouvelle_position = (position + decalage) % 26
            nouveau_caractere = chr(nouvelle_position + ord('A'))
            resultat += nouveau_caractere
        
        else:
            # Si ce n'est ni une majuscule ni une minuscule (espace, chiffre, ponctuation), on ne change pas
            resultat += caractere
    
    return resultat


# Exemple d'utilisation :
print(decalage_message("bonjour", 3))      # => erqmrxu
print(decalage_message("xyz", 2))          # => zab
print(decalage_message("Bonjour!", 5))     # => Gtsutzw!
print(decalage_message("def", -3))         # => abc
