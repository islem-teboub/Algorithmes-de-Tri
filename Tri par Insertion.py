#TRI INSERTION
#declaration dun tableau vide
table = [None, None, None, None, None]

#remplissage dun tableau de taille 5
for i in range(0,5):
    table[i]= int(input("entrer une valeur: "))
    
    
#tri par insertion
for i in range(0,5):
    for j in range(i,0,-1):
        if(table[j]<table[j-1]):
           aux=table[j]
           table[j]=table[j-1]
           table[j-1]=aux
           
#affichage du tableau trié
print (table)