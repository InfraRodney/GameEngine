from core import *

engine = GameEngine(800, 600)
player = Player(0, 0, 50, 50, (255, 0, 0))
engine.add_entity(player)
display_splash_screen()

running = True
while running:
    engine.update()
    if not engine.player.alive:
        running = False

pygame.quit()
