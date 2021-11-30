
import turtle, math, random
"""
    #Exemple
tortue = turtle.Turtle()
tortue.forward(50)
tortue.left(90)                
tortue.forward(50)
input()
"""





"""
    #Exo1.1
Matortue = turtle.Turtle()
Matortue.circle(50)
input()
"""





"""
    #Exo1.2
Matortue = turtle.Turtle()
for i in range(4):
    Matortue.forward(50)
    Matortue.left(90)
input()
"""





"""
    #Exo2.1
n=0
Matortue = turtle.Turtle()
while (n != 1000000):
    Matortue.forward(n)
    Matortue.left(90)
    n=n+1
input()
"""





"""
    #Exo2.2
turtle.speed(1000000)
n=1
Matortue = turtle.Turtle()
while (n != 1000000):
    Matortue.circle(n+10,n+10,n+10)
    n=n+1
input()
"""






"""
    #Exo3

n=10

turtle.delay(0)
tortues=[]

for i in range(n):
    var = turtle.Turtle()
    tortues.append(var)
    var.color(random.random(),random.random(),random.random())

while True:
    for i in tortues:
        i.forward(10)
        i.left(random.randint(-180,180))

input()
"""






"""
    #Algo tri insertion
def tri_insertion(tab): 
    # Parcour de 1 à la taille du tab
    for i in range(1, len(tab)): 
        k = tab[i] 
        j = i-1
        while j >= 0 and k < tab[j] : 
                tab[j + 1] = tab[j] 
                j -= 1
        tab[j + 1] = k
tab = [98, 22, 15, 32, 2, 74, 63, 70]
tri_insertion(tab) 
print ("Le tableau trié est:")
for i in range(len(tab)): 
    print ("% d" % tab[i])
"""






"""
    #Algo tri fusion
def tri_fusion(tableau):
    if  len(tableau) <= 1: 
        return tableau
    pivot = len(tableau)//2
    tableau1 = tableau[:pivot]
    tableau2 = tableau[pivot:]
    gauche = tri_fusion(tableau1)
    droite = tri_fusion(tableau2)
    fusionne = fusion(gauche,droite)
    return fusionne
#Tri fusion fonction de fusion de 2 listes
def fusion(tableau1,tableau2):
    indice_tableau1 = 0
    indice_tableau2 = 0    
    taille_tableau1 = len(tableau1)
    taille_tableau2 = len(tableau2)
    tableau_fusionne = []
    while indice_tableau1<taille_tableau1 and indice_tableau2<taille_tableau2:
        if tableau1[indice_tableau1] < tableau2[indice_tableau2]:
            tableau_fusionne.append(tableau1[indice_tableau1])
            indice_tableau1 += 1
        else:
            tableau_fusionne.append(tableau2[indice_tableau2])
            indice_tableau2 += 1
    while indice_tableau1<taille_tableau1:
        tableau_fusionne.append(tableau1[indice_tableau1])
        indice_tableau1+=1
    while indice_tableau2<taille_tableau2:
        tableau_fusionne.append(tableau2[indice_tableau2])
        indice_tableau2+=1
    return tableau_fusionne
tableau = [11, 222, 3, 899, 24, 5, 46, 67]
print(tableau)
tableau_trie = tri_fusion(tableau)
print(tableau_trie)
"""
"""
    #Exo4
n=10

turtle.delay(0)
tortues=[]

for i in range(n):
    shape = random.randint(1,10) 
    x = random.randint(-450,450)
    y = random.randint(-450,450)
    var = turtle.Turtle()
    var.penup()
    tortues.append(var)
    var.color(random.random(),random.random(),random.random())
    var.shape('circle')
    var.shapesize(shape,shape)
    var.setpos(x,y)


def distance (t1,t2):
    math.sqrt((t1.pos()[0]-t2.pos()[0])**2 + (t1.pos()[1]-t2.pos()[1])**2)
def manger(i,j):
    j.shapesize(j.shapesize()[0]+i.shapesize()[0],j.shapesize()[0]+i.shapesize()[0])
    i.ht()
    tortues.remove(i)
    

while True:
    for i in tortues:
        if i.pos()[0] > 500:
            #gauche
        elif i.pos()[1] > 500:
            #bas
        elif i.pos()[0] < -500:
            #droit
        elif i.pos()[1] < -500:
            #haut
        else:


        i.forward(10)
        i.left(random.randint(-180,180))
        for j in tortues:
            if i != j :
                if i.distance(j) <  (i.shapesize()[0]+j.shapesize()[0])*5:
                    if i.shapesize()[0] <= j.shapesize()[0]:
                        manger(i,j)
"""