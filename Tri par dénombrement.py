#TRI par Denombrement

#declaration dun tableau vide qui stock les élément à trier
table = [None, None, None, None, None]

#declaration dun tableau vide qui dénombre (les nombres a trier sont entre 0 et 10)
Denombre = [0,0,0,0,0,0,0,0,0,0,0]

#declaration dun tableau vide qui stock les éléments trié (résultat)
result = [None, None, None, None, None]

#remplissage dun tableau de taille 5=N
for i in range(0,5):
# Le maximum des nombres est k=10
    table[i]= int(input("entrer une valeur entre >=0 et <=10: "))

#comptage des apparition  
for i in range(0,5):
    Denombre[table[i]] = Denombre[table[i]]+1
#comptage des positionnements des nombres    
for i in range(1,11):
    Denombre[i] = Denombre[i]+Denombre[i-1]
#remplissage du tableau result
for i in range(0,5):
    result[Denombre[table[i]]-1]=table[i]
    Denombre[table[i]]=Denombre[table[i]]-1
    


###################################################################          
#affichage du tableau trié
print(result)
print("\nLa complexité du tri en matiere doperation = O(max(N,k)") 
