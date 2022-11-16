from Game.Game import Game
from Players.Playerç import Player

if __name__ == '__main__':
    #game = Game()
    #player = Player()
    track = Track()
    game_state = GameState()
    game_state.reset()
    # game.run(track, player)
    print(track.print_track(4, 5))

