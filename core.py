import pygame
import time

class GameEngine:
    def __init__(self, width, height):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        self.entities = []
        self.player = None
        self.clock = pygame.time.Clock()

    def add_entity(self, entity):
        self.entities.append(entity)
        if isinstance(entity, Player):
            self.player = entity

    def update(self):
        keys = pygame.key.get_pressed()
        x_move, y_move = 0, 0
        if keys[pygame.K_UP]:
            y_move = -1
        if keys[pygame.K_DOWN]:
            y_move = 1
        if keys[pygame.K_LEFT]:
            x_move = -1
        if keys[pygame.K_RIGHT]:
            x_move = 1
        self.player.move(x_move, y_move)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.player.alive = False
        for entity in self.entities:
            entity.update()
        self.check_collisions()
        self.screen.fill((0, 0, 0))
        for entity in self.entities:
            pygame.draw.rect(self.screen, entity.color, (entity.x, entity.y, entity.width, entity.height))
        pygame.display.update()
        self.clock.tick(120)

    def check_collisions(self):
        for entity in self.entities:
            if isinstance(entity, Player):
                continue
            if entity.x == self.player.x and entity.y == self.player.y:
                self.player.alive = False

class Entity:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.alive = True

    def update(self):
        pass

class Player(Entity):
    def move(self, x_move, y_move):
        self.x += x_move
        self.y += y_move

def display_splash_screen():
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Infrared Game Engine")
    font = pygame.font.Font(None, 36)
    text = font.render("Made With Infrared Interactive Engine", True, (255, 255, 255))
    text_rect = text.get_rect()
    text_rect.centerx = screen.get_rect().centerx
    text_rect.centery = screen.get_rect().centery
    screen.blit(text, text_rect)
    pygame.display.update()
    pygame.time.wait(3000)
