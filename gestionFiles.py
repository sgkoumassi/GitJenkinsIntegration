#coding:utf-8

import pickle

class Player:
	def __init__(self,nom,level):
		self.nom=nom
		self.level=level

	def whoami(self):
		print("{}  ({})".format(self.nom,self.level))



"""p1 = Player("Soul", 13)
 # enregistrement de l'objet

with open ("player.data","wb") as fic:
	record = pickle.Pickler(fic)
	record.dump(p1)"""



# reciperation de l'objet
with open ("player.data","rb") as fic:
	get_record = pickle.Unpickler(fic)
	PlayerONE = get_record.load()


PlayerONE.whoami()
