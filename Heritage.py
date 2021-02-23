#coding:utf-8
"""les attributs / principe d'ancapsulation"""

#Classe mere

class Vehicule:
	 def __init__(self,nom,qEssence):
	 	self.nom = nom
	 	self.qEssence =qEssence


	 def se_deplacer(self):
	 	print("Le Vehicule {} se deplace ...".format(self.nom))
		

#class fille
class Voiture(Vehicule):
	def __init__(self,nomV,qEssenceV,puissance):
	 	Vehicule.__init__(self,nomV, qEssenceV)
	 	self.puissance = puissance

	def se_deplacer(self):
	 	print("Je roule vite ...!")

class Avion(Vehicule):
	def __init__(self,nomA,qEssenceA,marchandise):
		Vehicule.__init__(self, nomA, qEssenceA)
		self.marchandise = marchandise

	def se_deplacer(self):
	 	print("Je vol  ...!")
#Programme principal
voiture1 = Voiture("Bougatti verron", 90, 500)
voiture1.se_deplacer()
print(voiture1.puissance, "CH")

Avion1 = Avion("Boeing", 6000, "Missiles solsol")
Avion1.se_deplacer()
print(Avion1.marchandise)



		