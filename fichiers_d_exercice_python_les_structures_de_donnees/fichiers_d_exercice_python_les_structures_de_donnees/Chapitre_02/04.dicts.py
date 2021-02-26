import csv
import codecs

with codecs.open('Chapitre_01\departement.csv', encoding='utf8', errors='replace') as dept:
    rd = csv.reader(dept, delimiter=',')
    """recuperer deux tuple à partir du fichier ouvert
    codes = tuple(r[1] for r in rd)
    dept.seek(0) 
    departements = tuple(r[2] for r in rd)"""

    #recuperer deux tuple à partir du fichier ouvert
    #on cree un tuple de tuple
    #codes, departements=zip(*((r[1], r[2]) for r in rd))
    #dictutu=dict(((r[1], r[2]) for r in rd))
    #avec methode de comprehension de dictionnaire
    dictutu2={r[1]: r[2] for r in rd}
#print("codes: {}".format(codes))
#print("departements: {}".format(departements))
"""on peut directement créer un dictionnaire à partir
d'un tuple de tuple"""

#melange = dict(zip(codes, departements))
print(dictutu2)

