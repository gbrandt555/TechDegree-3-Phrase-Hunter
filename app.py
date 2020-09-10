from phrasehunter.game import Game
from phrasehunter.phrase import Phrase



if __name__ == "__main__":
    
    
    game = Game()
    game.start()
    print("The phrase was: {}!".format(game.active_phrase.phrase))
    phrase = Phrase(game.phrases)
    
    
    
    
    



