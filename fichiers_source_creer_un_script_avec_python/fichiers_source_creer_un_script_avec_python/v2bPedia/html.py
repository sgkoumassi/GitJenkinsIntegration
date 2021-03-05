__author__ = 'rudi'

import httplib2
import sys

class HTTPConnection:
    """Gère une instance de connexion HTTP"""
    PYVERSION = 2

    def __init__(self, langue: str):
        self.langue = langue # c'est une variable de l'instance
        HTTPConnection.PYVERSION = sys.version_info[0]


    def get(self, page: str) -> None:
        """ récupère une page Wikipedia
            :returns None
            :param page: Page Wikipedia à récupérer
        """
        h = httplib2.Http(".cache")

        self.url = "http://{0}.wikipedia.org/wiki/{1}".format(
            self.langue,
            page.replace(' ', '_')
        )
        reponse, contenu = h.request(self.url, "GET")

        cles = ['content-location', 'age', 'status', 'last-modified']
        mareponse = { c: reponse[c] for c in cles }

        for c, v in mareponse.items():  # remplace iteritems() qui existait en Python 2
            print("%(c)s = %(v)s" % locals())


HTTPConnection('fr').get('Kruder und Dorfmeister')

