
##################################################################     
#PIVOT Function
def Pivot(T,X,Y):
    P=Y
    j=X

    while (j<=Y):
        if(j<=P):
            if(T[j]<=T[P]):
                j=j+1
            else:
                O=T[j]
                T[j]=T[P]
                T[P]=O
                P=j
                j=j+1
       
            
        else:
            if(T[j]>=T[P]):
                j=j+1
            
            else:
                O=T[j]
                T[j]=T[P]
                T[P]=O
                P=j
                j=j+1
               
       
            
    return (P)

##################################################################
#QuickSort Function
def QuickSort(T,X,Y):
    Q=Pivot(T,X,Y)
    print(Q)
    if(X<Q):
        print(T)
        if(Q==Y):
            QuickSort(T,X,Q-1)
        else:
           QuickSort(T,X,Q) 
    if(Y>Q):
        print(T)
        QuickSort(T,Q+1,Y)

##################################################################

#declaration dun tableau vide
table = [None,None,None,None,None]

#remplissage dun tableau de taille 5
for i in range(0,5):
    table[i]= int(input("entrer une valeur: "))
    
QuickSort(table,0,4)

#affichage
print ("Le dernier résultat")
print (table)