
from data import *
from creature import Creature

class Animal(Creature):
    def __init__(self, pos, groups, image):
        super().__init__(pos, groups, image)

    def deer(self):
        self.image = deer_sprite

        if self.sex == "male":
            self.description = "A buck deer.  It has a crown of antlers."
        elif self.sex == "female":
            self.description = "A timid doe deer."
        else:
            self.description = "Some kind of deer.  It makes you nervous."

    def bird(self):
        self.image = bird_sprite
        self.description = "A colourful songbird.  It's singing a lovely song!"

    def frog(self):
        self.image = frog_sprite
        self.description = "A fat frog.  It looks delicious."

    def bear(self):
        self.image = bear_sprite
        self.description = "A frightening looking bear."

    def insect(self):
        self.image = insect_sprite
        self.description = "A lowly bug.  It might sting you if you try to grab it."

    def slug(self):
        self.image = slug_sprite
        self.description = "A slimy slug.  Considered a delicacy to the spider-people."

    def fox(self):
        self.image = fox_sprite
        self.description = "A crafty fox."
