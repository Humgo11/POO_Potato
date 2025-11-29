import pyxel
import webbrowser


class Game: #classe qui cree le jeu et qui possede la boucle de jeu
    def __init__(self,width,height,nom_jeu):
        self.width = width
        self.height = height
        self.nom = nom_jeu
        self.hitbox = True
        

        pyxel.init(self.width, self.height)
        self.player = Player("JOUEUR1")
        self.liste_mob = []
        pyxel.run(self.update, self.draw)
        

    def update(self):
        
        if self.player.is_alive(): # boucle du jeu qui verifie si le joueur est mort
            #ici si le player est vivant
            #mettre la suite du jeu ici
            self.player.move()
            
        else:#si le joueur est mort
            print(self.player.nom, "est mort")
            
        #test de la mort des Mobs
        for mobs in self.liste_mob:
            if mobs.is_alive() == True:
                self.liste_mob.remove(mobs)


        
            
            
        



    def draw(self):
        pyxel.cls(0)
        
        if self.hitbox:
            self.player.draw_hitbox()

        self.player.draw()
            



class Player: #classe qui cree le joueur
    def __init__(self,nom):
        self.nom = nom
        self.x = pyxel.width//2 -2 #faire spawn le perso au milieu de l'écran
        self.y = pyxel.height//2 -2
        self.defense = 0
        self.attaque = 1
        self.vie = 4 #vie initiale
        self.vitesse = 1 #vitesse de deplacement 
        self.regeneration = 1#% de vie par secondes

    def move(self):
        """déplacement avec les touches de direction"""
        
        if pyxel.btn(pyxel.KEY_RIGHT) or pyxel.btn(pyxel.KEY_D):
            
            if (self.x < pyxel.width-5) :#eviter de sortir de l'écran
                self.x = self.x + self.vitesse

        if pyxel.btn(pyxel.KEY_LEFT) or pyxel.btn(pyxel.KEY_Q):
            if (self.x > 0) :
                self.x = self.x - self.vitesse
                

        if pyxel.btn(pyxel.KEY_DOWN) or pyxel.btn(pyxel.KEY_S):
            if (self.y < pyxel.height-5) :
                self.y = self.y + self.vitesse
        if pyxel.btn(pyxel.KEY_UP) or pyxel.btn(pyxel.KEY_Z):
            if (self.y > 0) : 
                self.y = self.y - self.vitesse

        

        

        
    def draw_hitbox(self):
        pyxel.rect(self.x-1,self.y-1,7,7,9) #7= taille player + 2 pour que l'on voie un peu le rectangle

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



    def draw(self):
        pyxel.rect(self.x,self.y,5,5,6)
        self.draw_health()

    def draw_health(self):
       """affiche le nb de coeur restant en haut à gauche """
       for i in range(self.vie):
           pyxel.rect(8*i, 0, 8, 8, 1+i)
           # pyxel.blt(x, y, img, u, v, w, h)
    
        # pyxel.rectb(0, 0, 32, 8, 2)#barre de vie sous forme de barre de vie
        # pyxel.rect(1, 1, 30, 6, 3)




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
    
    def is_alive(self):
        """donne de l'or au joueur et disparaitsi false"""
        if self.life > 0:
            return True
        elif self.life <= 0:
            return False
        


"""si joueur quitte la partie par le menu copier coller ça
ATTENTION: NE PAS METTRE DANS UNE BOUCLE"""
#webbrowser.open_new("https://www.youtube.com/watch?v=xvFZjo5PgG0")
Game(128,128,"JEU")