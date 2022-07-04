#Gnom Sort
#declaration dun tableau vide
table = [None, None, None, None, None]

#remplissage dun tableau de taille 5
for i in range(0,5):
    table[i]= int(input("entrer une valeur: "))
    
    
#Gnom Sort
i=0
while (i<4):
    if(table[i]>table[i+1]):
        permut=table[i]
        table[i]=table[i+1]
        table[i+1]=permut
        i=i-1
        if(i<0):
            i=i+1
    else:
        i=i+1
    
           
#affichage du tableau trié
print (table)