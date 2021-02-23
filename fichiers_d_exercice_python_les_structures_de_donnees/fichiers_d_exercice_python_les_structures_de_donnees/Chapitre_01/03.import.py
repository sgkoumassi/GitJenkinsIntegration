import csv
import codecs
with codecs.open('Chapitre_01\departement.csv', encoding='utf8', errors='replace') as dept:
    rd = csv.reader(dept, delimiter=',')
    departements = []
    for r in rd:
        departements.append(r[2])
print(departements)
#pour ajouter des elements
departements.extend(['Geneve','Valais','Niger','Togo'])
#pour inserer un element à une position x
departements.insert(0,'Neuchatel')
#supprimer le dernier element sans le recuperer
del(departements[9])
print(departements)
#Pour supprimer le dernier element de la liste
print(departements.pop())
#pour trier
print(sorted(departements))
#Pour renverser/ une list
departements.reverse()
print(departements)
departements.sort()
print(departements)
