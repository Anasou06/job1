def decalage(message, lettre):
    resultat=""
    for caractere in message:
        if "a" <= caractere <= "z":
            position=ord(caractere)-ord("a")
            new_position=(position+lettre)%26
            new_caractere=chr(new_position+ord("a"))
            resultat+= new_caractere

        elif "A" <= caractere <= "Z":
            position=ord(caractere)-ord("A")
            new_position=(position+lettre)%26
            new_caractere=chr(new_position+ord("A"))
            resultat+= new_caractere

        else:
            resultat=caractere

    return resultat
    
 
 

print(decalage("kilimini",2))