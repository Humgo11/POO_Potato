
import pyxel


class Game: #classe qui cree le jeu et qui possede la boucle de jeu
    def __init__(self,width,height,nom_jeu):
        self.width = width
        self.height = height
        self.nom = "Potato"
        self.player = Player("JOUEUR1")
        self.x = 0
        self.y = 0
        
         

        pyxel.init(self.width, self.height)
        
        pyxel.run(self.update, self.draw)
        list_mob = []
        

    def update(self):
        
        if self.player.is_alive(): # boucle du jeu qui verifie si le joueur est mort
            #ici si le player est vivant
            pass #mettre la suite du jeu ici



        else:#si le joueur est mort
            print(self.player.nom, "est mort")

        

    def draw(self):
        pyxel.cls(0)
        
        



class Player: #classe qui cree le joueur
    def __init__(self,nom):
        self.nom = nom
        self.x = 0
        self.y = 0
        self.defense = 0
        self.attaque = 1
        self.vie = 4 #vie initiale


    def degats(self,nb_degats):
        """
        Fonction qui prend en parametre le nb de degats a enlever au joueur
        et lui enlève
        """
        self.vie -= nb_degats


    def is_alive(self):
        """
        Fonction qui renvoie True si le joueur est vivant (vie>0)
        """
        if self.vie > 0:
            return True
        
        else:
            return False
        
    def draw_health(self):
        for i in range(self.vie):
            pyxel.rect(8*i, 0, 8, 8, 1+i)
            # pyxel.blt(x, y, img, u, v, w, h)
        
        
        
    def draw(self):
        pass

class Mob:
    def __init__(self, life, damage, attack_speed, speed):
        """initialisation de la creation de mob"""
        self.life = life
        self.damage = damage
        self.attack_speed = attack_speed
        self.speed = speed
    
    def update(self):
        pass
    
    def draw(self):
        pass
    
    def degat(self):
        """change la vie du mob"""
        pass


















Game(128,128,"Game")