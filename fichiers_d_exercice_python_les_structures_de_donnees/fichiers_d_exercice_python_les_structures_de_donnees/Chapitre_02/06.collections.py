import csv
import codecs
import collections

with codecs.open('Chapitre_01\departement.csv', encoding='utf8', errors='replace') as dept:
    rd = csv.reader(dept, delimiter=',')
    codes, departements = zip(*((r[1], r[2]) for r in rd))

# compter le nombre de dept par initial
test = dict(collections.Counter(d[0] for d in departements))
print(test['A'])
#afficher les 5 premier nombres
test2 = collections.Counter(d[0] for d in departements)
print(test2.most_common(5))
