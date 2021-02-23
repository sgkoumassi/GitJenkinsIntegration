#coding:utf-8
"""
identifiant = "Soul"
mot_de_pass = "power"

print ("Interface de connexion  !!")

userId = input("Entrez votre identifiant : \n")
password= input("Entrez votre mot de passe :\n")

if userId == identifiant and password == mot_de_pass:
	print(" Vous etes connecté \n Bienvenue {}".format(identifiant))
else: 
	print("identifiant ou mot_de_pass incorrect !!")

# Boucle While

conpteur=0

while conpteur <5:
	print("Je teste la boucle while")
	conpteur+=1

lancer_jeu =True
print("")

while lancer_jeu:
	choixMenu =input("> ")

	if choixMenu == "again":
		continue
	elif choixMenu =="quit":
		lancer_jeu = False
	elif choixMenu == "hello":
 		print("Bonjour !!")
 	

print("See u soon ....... !!")

"""
# Les fonctions

def show_inventory(*liste_item):
	for item in liste_item:
		print(item)

show_inventory("epée", "mana")
show_inventory("bouclier", "sabre")

ttc = lambda prixHT : prixHT + (prixHT * 20/100)

print(ttc(34))