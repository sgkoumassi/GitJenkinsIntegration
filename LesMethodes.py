#coding:utf-8
"""les methodes"""

class Humain:
	lieu_habitation="Terre"

	def __init__(self,nom,age):
		self.nom=nom
		self.age = age

	def parler(self,message): # methode stadard
		print("{} a dit : {}".format(self.nom,message))

	def changer_planete(cls,nouvelle_planete):
		Humain.lieu_habitation= nouvelle_planete

	changer_planete = classmethod(changer_planete)

	def definition():
		print ("L'humain est le plus grand")

	definition = staticmethod(definition)
	

Humain.definition()