__author__ = 'rudi'

import httplib2
import sys

class HTTPConnection:
    """Gère une instance de connexion HTTP """
    PYVERSION = 2

    def __init__(self, langue):
        if langue not in ['fr', 'en', 'de']:
            raise Exception("la langue n'existe pas")
        else:
            self.langue = langue
        HTTPConnection.PYVERSION =  sys.version_info[0]


    def get(self, page):
        """retrouve une page"""
        h = httplib2.Http(".cache")

        self.url = "http://{0}.wikipedia.org/wiki/{1}".format(
            self.langue,
            page.replace(' ', '_')
        )

        reponse, contenu = h.request(self.url, "GET")

        cles = ['content-location', 'age', 'status', 'last-modified']
        mareponse = { c: reponse[c] for c in cles }

        for k in mareponse:
            print('{0} = {1}'.format(k, mareponse[k]))

        for t in mareponse.items():
            print('{0} = {1}'.format(*t))




# HTTPConnection().get("http://fr.wikipedia.org/wiki/Kruder_und_Dorfmeister")
h = HTTPConnection("fr")
h.get("Kruder und Dorfmeister")
