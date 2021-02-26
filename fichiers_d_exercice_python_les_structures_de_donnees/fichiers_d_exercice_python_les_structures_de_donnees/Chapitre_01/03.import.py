import csv
import codecs
"""with codecs.open('Chapitre_01\departement.csv', encoding='utf8', errors='replace') as dept:
    rd = csv.reader(dept, delimiter=',')
    departements = []
    for r in rd:
        departements.append(r[2])"""
#print(departements)
#pour ajouter des elements
#departements.extend(['Geneve','Valais','Niger','Togo'])
#pour inserer un element à une position x
#departements.insert(0,'Neuchatel')
#supprimer le dernier element sans le recuperer
#del(departements[9])
#print(departements)
#Pour supprimer le dernier element de la liste
#print(departements.pop())
#pour trier
#print(sorted(departements))
#Pour renverser/ une list
##departements.reverse()
#print(departements)
#departements.sort()
"""utilisation de l'argument key dans sort()"""
# tri sur les entier
#departements.sort(key=int)
#tri avec une expression lambda en partant de la derniere lettre
#departements.sort(key= lambda l : l[-1])
# tri avec le rensersement total de chaine avec le slicing
#departements.sort(key= lambda l : l[::-1])
#departements+='Benin'
"""operateur de anpacking : attribut le premier element
de la liste à l1 et le reste à l2)
"""
#l1, *l2=departements
"""Partir de la fin de la liste pour recuperer une chaine spécifique
l1=departements[-len('Benin'):]
#joindre la liste
l2=''.join(l1)
print(l2)
print(l1) """

""" Traduire chaque element de la liste majuscule
 grace la fonction map()"""
#Lmap=list(map(lambda d: d.upper(), departements))
""" La meme chose avec la methode de comprehesion des liste"""
#Lcl=[d.upper() for d in departements] 
# la longeur totale des element de liste
#lt=sum(len(d) for d in departements)
#Liste de element commencant par A, N et T
#f=list(filter(lambda d: d[0] in ['A','N','T'],departements))
#print(Lmap)
#print(f)
#print(Lcl)
#print(lt)
""" Les tuples
t1 = tuple(departements)
print(t1) """

""" Les sets """
with codecs.open('Chapitre_01\departement.csv', encoding='utf8', errors='replace') as dept:
    rd = csv.reader(dept, delimiter=',')
    monSet = set(r[2] for r in rd)
monSet.add('Niger')
monSet.update(['Togo','Mali','RDC'])
# initilaiser un set à partir d'une liste
Afrique = set(['Algerie','RDC','Tunisie','Maroc'])
#print(Afrique)
# tester la presence d'un element dans un set
if 'Maroc' in Afrique: Afrique.remove('Maroc') 
#ou directement avec la methode discard
Afrique.discard('Maroc')
#Operation sur les sets
print(len(monSet & Afrique)) #intersection
print(len(monSet | Afrique))  # union
print(len(monSet - Afrique)) # difference
print(len(monSet ^ Afrique)) # difference symetrique


