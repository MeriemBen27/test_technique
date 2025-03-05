

def DPMR(L: list, min : int, max:int, num : int):
    
    """ La consition d'arret"""
    if min >= max:
        return min
    
    c= (min+max)//2

    """ si num est superieur ou inférieur à c le centre, si oui appel récursif """
    if num > L[c] :
        min=c
        print("nouveau min", min)
        print("le centre", c)
        print(min)
        return DPMR(L, min+1, max, num)
    
    
    elif num < L[c]:
        max=c
        print("nouveau max", max)
        print("le centre", c)
        print(max)
        return DPMR(L, min, max-1, num)




    




import random

"""définition de la liste et trie en ordre croissant"""
min=20
max=50
len=10

L= [random.randint(min,max) for i in range(len)]
L.sort()
print(L)
"""Introduire le nombre à inserer dans la liste """
print("Donner le nombre que vous souhaiter insérer :")
num = int(input())

i= DPMR(L, 0, len - 1, num)
print(i)
L.insert(i, num)
print(L)
