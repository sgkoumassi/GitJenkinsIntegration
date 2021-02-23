#coding:utf-8
"""les attributs / principe d'ancapsulation"""

class Humain:
	"""Cette class represente un humain"""

	def __init__(self,nom,age):
		self.nom =nom
		self._age = age

	def _getAge(self):
		try :
			return self._age
		except AttributeError :
			print("L'age n'existe plus !!")

	def _setAge(self,nouvel_age):
		if nouvel_age < 0 :
			self._age = 0
		else:
			self._age = nouvel_age

	def _delAge(self):
		del self._age


	# property (<getter>, <setter>, <deletter>, <helper>)

	age = property(_getAge,_setAge,_delAge, " Je suis l'age d'un hmain" )

hi = Humain("Soul",30)

print(hi.age)

del hi.age

print(hi.age)


help(Humain)