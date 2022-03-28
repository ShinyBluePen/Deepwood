# Deepwood
#
# Michael D. Petty
#
# v0.1.0 : 26 FEB 2022 : Begin tutorial "making Zelda in python".
# v0.2.0 : 26 MAR 2022 : Tutorial process complete.
# v0.3.0 : xx xxx xxxx : Code cleanup complete.
# v0.3.1 : xx xxx xxxx : Initial code optimization complete.

from settings import *

#   pygame
#   random
#   time
#   sys
#   os.path.join() as jn

from world import World


class Game:
    """
    Creates the game object which creates the World and runs it.

    Returns: Game object
    Functions: draw, main_menu, run
    Attributes: screen, clock, icon, caption, start_over, game_over, world
    """

    def __init__(self):
        pygame.init()
        self.screen = WINDOW
        self.clock = CLOCK
        self.icon = ICON
        self.caption = MAIN_MENU_SPLASH
        self.start_game = True
        self.game_over = False
        self.world = World()

        self.main_theme = pygame.mixer.Sound(jn("assets", jn("audio", "main.ogg")))
        self.main_theme.play(loops=-1).set_volume(0.1)

    def draw(self):
        # Window
        fps = round(self.clock.get_fps(), 2)
        location = LOCATION_LIST[0]
        self.caption = pygame.display.set_caption(f"Deepwood - {location} - [{fps}]")

        # Graphics
        self.screen.fill(WATER_COLOR)
        self.world.draw()
        pygame.display.update()

    def main_menu(self):
        while True:
            self.draw()
            self.clock.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            if self.start_game:
                self.run()

    def run(self):
        while True:
            self.draw()
            self.clock.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_m:
                        self.world.toggle_menu()

            if self.game_over:
                self.game_over = False
                self.main_menu()

            # Debugging


def main():
    Deepwood = Game()
    Deepwood.main_menu()


if __name__ == "__main__":
    main()
