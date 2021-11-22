from src.data.core.Game import Game
from src.config.constants import screens

game = Game()

while game.isRunning:
    if game.selectedScreen == screens.MAIN_MENU:
        game.main_menu()
    else:
        game.start_game()
