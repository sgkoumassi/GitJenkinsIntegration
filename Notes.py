#coding:utf-8


""" 
Les chaine de carractere : les methode chaine tavaillent sur copie , et pas la chaine elle meme !!
"""
"""# La classe str :   help(str)
                    str.upper(), str.lower(), str.capitalise(), str.title()
                    str.center(<largeur>,<caractere_de_remplissage>)
                    str.find(<chaine>,<debut>,<fin>)
                    str.trip() , str.replace(<ancienne>,<nouvelle>,<occurences_a_modifier>)
                    str.isalpha(), str.isdigit(), str.isdecimal(), str.lower(), str.isupper()
                    str.isidenfier(), str.iskeyword()
"""


""" Les liste :  les methode de lite travaille sur la liste elle meme, et non sur une copie """
""""
#cration d'une liste 
inventaire1= list()             # liste vide
inventaire2 = list["arc"]*10    # initilise la liste avec 10 fois arc
inventaire3 = range(20)         # initilise ue liste croissante
liste[:]                        # affiche tous les element de la liste
liste[x]                        # affiche  l' element d'indice x
liste[-x]                       # affiche xème element en paartant de la fin
liste[:x]                       # affiche les x premiers elements 
liste[x:]                       # affiche les x derniers elements 
liste[A:B]                      # affiche de l'element d'indice  A à l'element d'indice B
len(<liste>)                    # Donne la taille de la liste
liste.append("element")         # ajoute un element à la fin de la liste
liste.insert(<indice_element>, <element_à_inserer>) 
liste.remove(<element>)  = del liste[indice_element
liste.index(<element>)          # donne l'indice d'un element de la liste
liste.sort()                    # tri croissant
liste.reverse()                 # inverse les element de la liste
liste.count(<element>)          # donne le nombre d'occurence d'un element
"separateur".join(liste)

"""

liste1 = ["arc", "epée", "potion de mana","bouclier","technique de combat"]

for k,v in enumerate(liste1):
	print("Element d'indice {} --> {}".format(k,v))


"""
les Tuple :  c'est une sequence d'ojetect imuables, sauf en cas d'affectation multiple
              mon_tuple = ()        # tuple vide
              mon_tuple = x,        # tuple avec une seul valuer x
              mon_tuple = (x,)      # tuple avec une seul valeur x
              mon_tuple = (x,y)     # tuple avec des valeur x et y
              mon_tuple[x]          # valeur d'indice x

"""
mon_tuple = (3,5)

print("le tuple est : {}".format(mon_tuple))


""" Les Dictionnaires : ce sont des tableau associatif : help(dict)
                    
dico ={}                                  # dico vide
dico{<cle>:<valeur>, <cle2>:<valeur2>}    # dico avec des valeurs
dico[<clé>]                               # acces à une valeur
dico[<clé>] = <valeur>                    #ajout et modification"
dico.pop[<clé>] ou del dico[<clé>]

def maFonction (**parametres)            # Foncion avec des parametre només 
def maFonction (*parametres)             # Foncion avec des parametres non només  


                    """


dico = {"chat":"c'est un felin", "chien":"Le best friend de l'homme"}

for k,v in dico.items():
	print("Clé : {} --> valeur : {}".format(k,v))


"""  La gesion des fichiers :
       mode d'ouveture : r (lecture seule), w (ecriture avec remplacement), 
                         a (ecriture avec)
                         x (lecture + ecriture)
                         r+(lecture /ecriture  dans le meme fichier)





"""


with open("data.txt", "w") as fic :
	content =fic.read()
	print(content)



"""
fic = open ("data.txt", "r") 

print(fic.read())

fic.close()
"""
