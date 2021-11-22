from src.data.core.Game import Game

game = Game()

while game.isRunning:
    if game.selectedScreen == 'main_menu':
        game.main_menu()
    else:
        game.start_game()
