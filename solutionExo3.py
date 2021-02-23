#coding : utf-8

"""
Exercice python : 

    Creer un programme simulant un combat qui respecte les contraintes suivantes :

     - Deux joueurs, auquels on demandera de choisir  un pseudo
     - Les deux combattants demarrent avec 250 points de vie chacun
     - le combat se deroule en 4 attaques(joueur&,joueur1, j1,J2)
     - chaque attaque est  une tantative ( si ele reussit, le joueur infligera un ombre de degats entre 0 et 100 
                                           si elle échoue, l'attaque est ratee et c'est au tour de l'autre joueur)
 """

#Soulution 1  

import random

joueur1 = input("joueur1 choisissez votre pseudo : \n")
nombre_de_vie_joueur1 = 250
domage_joueur1 = 0

joueur2 = input("joueur2 choisissez votre pseudo : \n")
nombre_de_vie_joueur2 = 250
domage_joueur2 = 0

random_attack = True
random_damage = 0

print("\n LE COMBAT COMMENCE !!! ;-)")



# 1ere attaque
input()
print( " {} a l'attaque !! ".format(joueur1))
random_attack = random.randint(0, 1)
random_damage1 = bool(random_attack)


if random_attack == True:
	random_damage1 =random.randint(0,100)
	print(f"{joueur2} subit une attaque de {joueur1} qui lui inflige {random_damage1} points de degats !!")
	nombre_de_vie_joueur2 -=random_damage1
	domage_joueur2 += random_damage1


else:
	print(f"{joueur1} a rate son attaque !!")
	
	

# 2eme attaque
input()
print( " {} a l'attaque !! ".format(joueur2))
random_attack = random.randint(0, 1)
random_damage2 = bool(random_attack)


if random_attack == True:
	random_damage2 =random.randint(0,100)
	print(f"{joueur1} subit une attaque de {joueur2} qui lui inflige {random_damage2} points de degats !!")
	nombre_de_vie_joueur1 -=random_damage2
	domage_joueur1 += random_damage2

else:
	print(f"{joueur2} a rate son attaque !!")
	
	

# 3eme attaque
input()
print( " {} a l'attaque !! ".format(joueur1))
random_attack = random.randint(0, 1)
random_damage1 = bool(random_attack)
if nombre_de_vie_joueur1 > 250:
	print ("vous  avez accumulez {} vies , reussissez votre prochaine attaque pour \
		                                    augmanté votre chances de gagner ce combat ;-) ".format(nombre_de_vie_joueur1))
else :
	print ("votre nombre_de_vie est en baisse : {} vies , ne ratter as votre prochaine attaque ;-)".format(nombre_de_vie_joueur1))
		                                    



if random_attack == True:
	random_damage1 = random.randint(0,100)
	print(f"{joueur2} subit une attaque de {joueur1} qui lui inflige {random_damage1} points de degats !!")
	nombre_de_vie_joueur2 -=random_damage1
	domage_joueur2 += random_damage1 
   
else:
	print(f"{joueur1} a rate son attaque !!")
	
	

# 4 eme attaque
input()
print( " {} a l'attaque !! ".format(joueur2))
random_attack = random.randint(0, 1)
random_damage2 =bool(random_attack)
if nombre_de_vie_joueur2 > 250:
	print ("vous  avez accumulez {} vies , reussissez votre prochaine attaque pour \
		                                    augmanté votre chances de gagner ce combat ;-) ".format(nombre_de_vie_joueur2))
else :
	print ("votre nombre_de_vie est en baisse : {} vies , ne ratter as votre prochaine attaque ;-)".format(nombre_de_vie_joueur2))


if random_attack == True:
	random_damage2 = random.randint(0,100)
	print(f"{joueur1} subit une attaque de {joueur2} qui lui inflige {random_damage2} points de degats !!")
	nombre_de_vie_joueur1 -=random_damage2
	domage_joueur1+=random_damage2

else:
	print(f"{joueur2} a rate son attaque !!")
	
	


# Resultat finial
input()
if nombre_de_vie_joueur1 > nombre_de_vie_joueur2 :
	print( f" {joueur1} remporte le combat avec {nombre_de_vie_joueur1} vies restant et {domage_joueur1} degats subit !! Bravoo  ")

elif nombre_de_vie_joueur1 == nombre_de_vie_joueur2:
	print( " Les deux combattants sont a egalité !! ")
else :
	print( f" {joueur2} remporte le combat avec {nombre_de_vie_joueur2} vies restant et {domage_joueur2} degats subit !! Bravoo  ")







