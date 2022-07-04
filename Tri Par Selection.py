#Selection Sort
#declaration dun tableau vide
#vu qu'on utilise une Structure de Données Statique, la taille des données entrées doit être préalablement déclarée.
#On suppose que les données à trier sont de taille 5 (en l'occurence, un tableau de taille 5)
table = [None, None, None, None, None]

#remplissage dun tableau de taille 5
for i in range(0,5):
    table[i]= int(input("entrer une valeur: "))
    
    
#Selection Sort
for j in range(4,-1,-1):
    for i in range(0,j,1):
        if(table[j]<table[i]):
            permut=table[j]
            table[j]=table[i]
            table[i]=permut
    
    
#affichage du tableau trié
print (table)

#La complexité au pire cas est N*N
#La complexité au meilleur cas est N