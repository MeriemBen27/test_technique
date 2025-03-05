

def DPMR(L: list, len :int, min : int, max:int):
    c= len//2
    
    """Introduire le nombre à inserer dans la liste """
    print("Donner le nombre que vous souhaiter insérer :")
    num = int(input())
    

    if num > c :
        min=c
        print(min)
        DPMR(L, len, min, max)

    elif num < c:
        max=c
        print(max)
        DPMR(L, len, min, max)




    




import random

"""définition de la liste et trie en ordre croissant"""
first=20
last=30
len=5
L= [random.randint(first,last) for i in range(len)]
L.sort()
c=L[len//2]

print(L)
print(c)

min = L[0]
max= L[-1]
DPMR(L, len, min, max)
