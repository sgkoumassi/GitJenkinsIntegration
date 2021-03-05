__author__ = 'rudi'

import httplib2
import sys

class HTTPConnection:
    """Gère une instance de connexion HTTP """
    PYVERSION = 2

    def __init__(self, langue):
        self.langue = langue
        # HTTPConnection.PYVERSION =  sys.version_info[0]
        HTTPConnection.PYVERSION = len(langue)
        self.PYVERSION = len(langue)

    def get(self, page):
        """retrouve une page"""
        h = httplib2.Http(".cache")

        # assert isinstance(page, str)

        self.url = "http://{0}.wikipedia.org/wiki/{1}".format(
            self.langue,
            page.replace(' ', '_')
        )

        reponse, contenu = h.request(self.url, "GET")
        print(HTTPConnection.PYVERSION)
        print(self.PYVERSION)
        print(reponse)


# HTTPConnection().get("http://fr.wikipedia.org/wiki/Kruder_und_Dorfmeister")
# HTTPConnection("fr").get("Kruder und Dorfmeister")
h1 = HTTPConnection("fr")
print(HTTPConnection.PYVERSION)
h2 = HTTPConnection("français")

print(h1.PYVERSION)
print(h2.PYVERSION)
print(HTTPConnection.PYVERSION)
