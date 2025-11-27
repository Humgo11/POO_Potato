
import pyxel


class Game:
    def __init__(self,width,height,nom_jeu):
        self.width = width
        self.height = height
        self.nom = nom_jeu

        pyxel.init(self.width, self.height)
        self.x = 0
        pyxel.run(self.update, self.draw)

    def update(self):
        pass
    
    def draw(self):
        pyxel.cls(0)
        pass
























Game(128,128,"Game")