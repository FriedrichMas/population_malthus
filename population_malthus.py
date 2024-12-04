#Affichages titre et auteur

def title(Titre):
    longueur = len(titre )
    ligne = "+" + "-" * (longueur + 2) + "+"
    ligne_vide =  "| " + " " * longueur + " |"
    contenu = "| " + titre + " |"
    vide =  " " + " " * longueur + " "
    
    print(ligne)
    print(ligne_vide)
    print(contenu)
    print(ligne_vide)
    print(ligne)
    print(vide)
    
titre= " Etude de l'évolution d'une population par la méthode de Malthus" 
title(titre) 

print("**** Realisé par MASUAMA Frédérick ****") 
print("")
print("")
print("Commençons!")
print("")


#Imports

import numpy as np
import matplotlib.pyplot as plt

#La solution de l'équation différentielle

def f (a,b,c,t):
    return c*(np.exp(a-b))*t

#Corps du programme

a = float(input('Quel est le coefficient de natalité de la population ?'))
b = float(input('Quel est le coefficient de mortalité de la population ?'))
c = int(input('Quelle est la valeur initiale de la population ?'))
k = int(input("Voulez-vous voir la courbe de l'évolution globale ou juste la valeur de la population à un instant t ?\nVeuillez renter 1 pour la courbe d'évolution globale ou 2 pour voir le nombre de la population à instant que vous souhaitez.\n Merci"))


if k == 1:
    t = np.linspace(0,50,100)
    z = f(a,b,c,t)
    
    plt.plot(t,z, label = 'population')
    plt.legend()
    plt.show()
else :
    t = int(input('Après combien de temps voulez-vous voir ?'))
    t_2 = str(input('Ce temps est en jours, semaines, années ? '))
    z = f(a,b,c,t)
    pop = round(z)
    print('La valeur de la population après', t, ' ', t_2,' est de ',z)
    print('Donc environ ', pop, ' individus.')

