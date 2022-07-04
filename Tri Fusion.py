

##################################################################     
#Fusion Function
def Fusion(T1,X,T2,Y,T3):
    i=0
    j=0
    z=0
    while (i<X)&(j<Y):
        if (T1[i]<T2[j]):
            T3[z]=T1[i]
            i=i+1
        else:
            T3[z]=T2[j]
            j=j+1
        z=z+1
    while (i<X):
        T3[z]=T1[i]
        i=i+1 
        z=z+1
    while (j<Y):
        T3[z]=T2[j]
        j=j+1 
        z=z+1
    return (T3)
##################################################################
#Sort Function
def Tri(table):
    if (len(table)==1):
        return (table)
    else:
        milieu = int((len(table)/2))
        T1 = table[0:milieu]
        T2 = table[milieu:len(table)]
        return Fusion(Tri(T1),len(T1),Tri(T2),len(T2),table)
##################################################################

#declaration dun tableau vide
table = [None,None,None,None,None]

#remplissage dun tableau de taille 5
for i in range(0,5):
    table[i]= int(input("entrer une valeur: "))
    
Tri(table)

#affichage
print (table)