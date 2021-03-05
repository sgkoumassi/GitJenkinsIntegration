#coding : utf-8

#Soulution 1  

import random
random_attack = True
random_damage = 0

print("\n LE COMBAT COMMENCE !!! ;-)")

joueur1 = input("joueur1 choisissez votre super pseudo : \n")
joueur2 = input("joueur2 choisissez votre ragnar pseudo : \n")


# 1ere attaque
print( " {} a l'attaque !! ".format(joueur1))
random_attack = random.randint(0, 1)
random_damage1 = bool(random_attack)
nombre_de_vie_joueur1 = 250

if random_attack == True:
	print("Pfffffff wawwwww: attaque reussit !!")
	random_damage1 =random.randint(0,100)
	nombre_de_vie_joueur1 = nombre_de_vie_joueur1 + random_damage1


else:
	print("Merde !!  : attaque ratte !!")
	random_damage1 = 0
	nombre_de_vie_joueur1 = nombre_de_vie_joueur1 - 10

# 2eme attaque
print( " {} a l'attaque !! ".format(joueur2))
random_attack = random.randint(0, 1)
random_damage2 = bool(random_attack)
nombre_de_vie_joueur2 = 250

if random_attack == True:
	print("Pfffffff wawwwwww: attaque reussit !!")
	random_damage2 =random.randint(0,100)
	nombre_de_vie_joueur2 = nombre_de_vie_joueur2 + random_damage2

else:
	print("Merde !!  : attaque ratte !!")
	random_damage2 = 0
	nombre_de_vie_joueur2 = nombre_de_vie_joueur2 -10

# 3eme attaque

print( " {} a l'attaque !! ".format(joueur1))
random_attack = random.randint(0, 1)
if nombre_de_vie_joueur1 > 250:
	print ("vous  avez accumulez {} vies , reussissez votre prochaine attaque pour \
                                                augmanté votre chances de gagner ce combat ;-) ".format(nombre_de_vie_joueur1))
else :
	print ("votre nombre_de_vie est en baisse : {} vies , ne ratter as votre prochaine attaque ;-)".format(nombre_de_vie_joueur1))
		                                    

random_damage1 = random_damage1 + bool(random_attack)

if random_attack == True:
	print("Pfffffff wawwww : attaque reussit !!")
	random_damage1 = random.randint(0,100)
	nombre_de_vie_joueur1 = nombre_de_vie_joueur1 + random_damage1
   
else:
	print("Merde !!  : attaque ratte")
	random_damage1 =  0
	nombre_de_vie_joueur1 = nombre_de_vie_joueur1 -10

# 4 eme attaque

print( " {} a l'attaque !! ".format(joueur2))
random_attack = random.randint(0, 1)
if nombre_de_vie_joueur2 > 250:
	print ("vous  avez accumulez {} vies , reussissez votre prochaine attaque pour \
		                                    augmanté votre chances de gagner ce combat ;-) ".format(nombre_de_vie_joueur2))
else :
	print ("votre nombre_de_vie est en baisse : {} vies , ne ratter as votre prochaine attaque ;-)".format(nombre_de_vie_joueur2))
random_damage2 = random_damage2 + bool(random_attack)

if random_attack == True:
	print("Pfffffff wawwwww : attaque reussit !!")
	random_damage2 = random.randint(0,100)
	nombre_de_vie_joueur2 = nombre_de_vie_joueur2 + random_damage2

else:
	print("Merde !!  : attaque reussit")
	random_damage2 = 0
	nombre_de_vie_joueur2 = nombre_de_vie_joueur2 -10


# Resultat finial

if nombre_de_vie_joueur1 > nombre_de_vie_joueur2 :
	print( " Le combat est remporte par {} !! Bravoo  ".format(joueur1))

elif nombre_de_vie_joueur1 == nombre_de_vie_joueur2:
	print( " Les deux combattants sont a egalité !! ")
else :
	print( " Le combat est remporte par {} !! Bravoo  ".format(joueur2))







