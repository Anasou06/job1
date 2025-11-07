def t(taille):
    q=""
    ind=taille
    for _ in range(taille): 
        q+="|"
        for p in range(taille):
            if p ==ind-1 :
                q+=" "
            else :
                q+="#"
        ind-=1
        q+="|"
        q+="\n"
    return q
    

print(t(2))
