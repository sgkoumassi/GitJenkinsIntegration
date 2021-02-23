#coding:utf-8
try:
    #bloc auto netoyant car le with assure la fermeture du fichier
    with open("data.txt","r") as f:
        for l in f.readlines():
            print(int(l.strip()))
except IOError as err:
    print("Erreur IO :..dans la lecture du fichier.", err)
except ValueError:
    print("Erreur Concersion...")
except:
    print("Erreur Inconnue...")

