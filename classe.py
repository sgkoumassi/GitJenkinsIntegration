class maclass:
    """
la methode init qui est le construb=cteur en python.
    """
    def __init__(self, saison, episode):
        self.saison=saison
        self.episode=episode

    def maMethode(self):
        print("Ceci est une methode python")

ep = maclass(7,5)
print(ep.saison,ep.episode )
    
