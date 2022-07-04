def filsG(T,i):
    return (T[2*i+1])

def filsD(T,i):
    return (T[2*i+2])


def Entasser(T,i,MAX):
    max=None
    if(2*i+1<=MAX):
        if T[i]<filsG(T,i):
            Permut=T[i]
            T[i]=T[2*i+1]
            T[2*i+1]=Permut
            Entasser(T,2*i+1,MAX)
            Entasser(T,i,MAX)
    if(2*i+2<=MAX):
        if T[i]<filsD(T,i):
            Permut=T[i]
            T[i]=T[2*i+2]
            T[2*i+2]=Permut
            Entasser(T,2*i+2,MAX)
            Entasser(T,i,MAX)
       
def CreerUnTas(T,D,F):
    for i in range(F,D-1,-1):
        Entasser(T,i,F)
        
def TriTas(T,D,F):
    for i in range(D,F+1):
        CreerUnTas(T,D,F)
        B[i]=T[0]
        T[0]=-1
#declaration dun tableau vide
table = [None,None,None,None,None]
B = [None,None,None,None,None]
#remplissage dun tableau de taille 5
for i in range(0,5):
    table[i]= int(input("entrer une valeur: "))
    
TriTas(table,0,4)

print(table)
#inverser le tableau résultat B qui contient les élements triés du plus grand au plus petit
B.reverse()
#afficher le tableau résultat
print(B)