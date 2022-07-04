#TRI A BULL
#declaration dun tableau vide
table = [None, None, None, None, None]

#remplissage dun tableau de taille 5
for i in range(0,5):
    table[i]= int(input("entrer une valeur: "))
    
    
#tris a bull
Arefaire=True
j=1
while(Arefaire==True):
    permut=False
    Arefaire=False
    for i in range(0,4,1):
        if table[i]>table[i+1]:
           permut=True
           aux=table[i]
           table[i]=table[i+1]
           table[i+1]=aux
    if(permut==True):
        Arefaire=True
        j=j+1
           
#affichage du tableau trié
print(table)
print("\nLa complexité du tri en matiere doperation = O(",j,"N )") 
