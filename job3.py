def t(taille):
    q=""
    for i in range(taille): 
        q+="|"
        for p in range(taille):
            if p == taille-p:
                q+=""
            else :
                q+="#"
        q+="|"
        q+="\n"
    return q
    

print(t(10))
