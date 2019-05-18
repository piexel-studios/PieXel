import pygame, threading, os
from PIL import Image
class Texture:
    def __init__(self, texture_name):
        self.img = pygame.image.load(texture_name)
        self.texture_name = texture_name
        self.rect = self.img.get_rect()
    def resize(self, size):
        img = Image.open(self.texture_name)
        img = img.resize(size) 
        img.save('resized/'+self.texture_name[len('textures/'):], self.texture_name[-3:])
        self.__init__('resized/'+self.texture_name[len('textures/'):])



class Coord:
    

    def __init__(self, coord):
        self.coord = coord
        

    def __repr__(self):
        return str(self.coord)
        

    def __getitem__(self, i):
        return self.coord[i]
    

    def __add__(self, other):
        return Coord((self[0] + other[0], self[1] + other[1]))


    def __sub__(self, other):
                return Coord((self[0] - other[0], self[1] - other[1]))
        

    def __mul__(self, other):
        return Coord((self[0] * other[0], self[1] * other[1]))


    def __eq__(self, other):
        return self.coord[1] == other.coord[1]


    def __gt__(self, other):
        return self.coord[1] > other.coord[1]


    def __lt__(self, other):
        return self.coord[1] < other.coord[1]


class Entity:
    
    def __init__(self, position=Coord((0,0))):
        self.position = position
        self.velocity = Coord((0, 0))
        self.acceleration = (0, 0)


    def __step(self):
        self.velocity = (self.velocity[0] + self.acceleration[0],
                         self.velocity[1] + self.acceleration[1])

        self.position = (self.position[0] + self.velocity[0],
                         self.position[1] + self.velocity[1])


    def accelerate(self, change_in_acceleration):
        self.acceleration = (self.acceleration[0] + change_in_acceleration[0],
                             self.acceleration[1] + change_in_acceleration[1])





class Screen:
    
    def __init__(self, sky_color=(18, 171, 255), size=(640,640), blocks_in_screen=10):
        self.size = size
        self.width = size[0]
        self.height = size[1]
        self.sky_color = sky_color
        self.screen = pygame.display.set_mode(size)
        self.blocks_in_screen = blocks_in_screen
        self.block = round(self.width/blocks_in_screen), round(self.height // blocks_in_screen)
        self.t_size = round(self.width/10)
        self.textures = self.find_textures()
        self.display = pygame.display
    
    def start_window(self):
        pygame.display.init()
    def draw_screen(self):
        for x in range(0, self.width, self.width//10):
            for y in range(0, self.height, self.height//10):
                if y/self.t_size <= 5:
                    pass
                elif y/self.t_size == 6:
                    self.screen.blit(self.textures['dirt.png'].img, Coord((x,y)))
                else:
                    self.screen.blit(self.textures['dirt2.png'].img, Coord((x,y)))
    
    def update(self):
            pygame.display.flip()
    
    def find_textures(self, dir='textures/', format='.png', resize=False):
        textures = {}
        for i in os.listdir(dir):
            if i.endswith(format):
                textures[i] = Texture(dir+i)
                if resize:
                    textures[i].resize(self.t_size)
        return textures


class Player(Entity, Screen):
    
    def __init__(self, skin=Texture('skins/better_character.png'), char_pos=None):
        if char_pos is None:
            self.char_pos = Coord((0, Screen.block[1]*4))
        else:
            self.pos = Coord(char_pos)
        self.skin = skin
    def draw(self, coords=None):
        if coords is None:
            coords = self.char_pos
        self.screen.blit(self.skin.img, self.pos())
    def move(self, new_pos=Coord((1,0))):
        self.skin.rect.move(tuple(new_pos)-tuple(self.pos))
        self.pos = new_pos