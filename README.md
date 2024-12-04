
# EVOLUTION DEMOGRAPHIQUE : MODELE DE MALTHUS

Ce projet fait l'étude de l'évolution d'une population (humaine, animale, bactérienne, virale ...) voire une croissance économique (en adaptant le jargon, bien sûr) grâce au modèle de Malthus. 

Ce travail peut se révéler utile aux débutants sur python, aux lycéens, aux étudiants en premier cycle d'études supérieures...


## A propos du code

Le code est structuré en quaatre parties: 
* Les affichages titre et auteur
* Les imports nécessaires
* La solution de l'équation différentielle générée par le modèle de Malthus
* Le corps du programme et les affichages finales

Il permet de voir, selon votre vouloir, soit l'allure globale de la courbe de l'évolution  de la population, soit la valeur quasi exacte de la population après un temps que vous spécifierez.

Pour ce fait, nous avons utilisé deux librairies python : Numpy et matplotlib, ainsi que la fonction python round() pour la conversion de la valeur finale. 

Afin d'utiliser le code, vous aurez besoin d'avoir les coefficients de natalité et mortalité de la population par rapport à un temps défini et fini (jours, semaines, mois, années...) 

Sachant que le modèle de Malthus est exponentiel, nous avons demandé a ce code de ne donner que l'allure de la courbe de l'évolution ou la valeur du nombre de la population à un moment précis du temps.

Il n'y a donc pas des points d'inflexion ni de calcul de limite. Cependant, dans le cas où l'évolution est décroissante, à l'infini, la valeur tendra vers zéro, ce qui traduit l'extinction de la population. 


## Le modèle de Malthus

Posons: 
* a = Taux de natalité
* b = Taux de mortalité
* r = a - b
* t = le temps (l'instant considéré)
* N(t) = Nombre d'invidus à l'instant t
* N_0 = Nombre initial d'invidus
* $\delta$ t = variation du temps

On a: 

N(t + $\delta$ t) = N(t) + [ $\delta$ t (aN(t) -bN(t))]

i.e la valeur de la population après un instant est donnée par la valeur à l'instant considéré au départ plus la variation du temps multipliée par la différence du nombre de la population influencé par les natalités et mortalités.  

Ainsi, N(t + $\delta$ t) = $\delta$ t (a - b)N(t)

[N(t + $\delta$ t) - N(t)] / $\delta$ t = rN(t)

Donc N'(t) = rN(t)

Après résolution de l'équation différentielle qui est de la forme y'(t) = ay(t), on trouve:

N(t) = N_0 * exp(rt)

**Etude de limite: 
si r > 0, alors l'évolution est croissante et la limite de N en plus l'infini est plus l'infini.

si r < 0, alors l'évolution est décroissante et la limite est zéro. 
