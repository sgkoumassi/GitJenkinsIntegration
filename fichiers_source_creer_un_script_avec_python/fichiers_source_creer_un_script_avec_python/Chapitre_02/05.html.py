__author__ = 'Soul'

""" Application permettant de lire des page wikipedia"""
import httplib2
import re


class HTTPConnection:
    """ Gère une instance de connexion HTTP """

    def __init__(self, langue):
        self.langue = langue

    def get(self, page):
        """ retrouve une page"""
        h = httplib2.Http(".cache")

        # assert isinstance(page, str)

        self.url = "http://{0}.wikipedia.org/wiki/{1}".format(
            self.langue,
            #page.replace(' ', '_')
            # Avec les regular expression
            re.sub(r' ', ' ', page)
        )

        reponse, contenu = h.request(self.url, "GET")
        print(reponse)


# HTTPConnection().get("http://fr.wikipedia.org/wiki/Kruder_und_Dorfmeister")
HTTPConnection("fr").get("Kruder und Dorfmeister")
