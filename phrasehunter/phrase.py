class Phrase:
    
    def __init__(self, phrase):
        self.phrase = phrase

    
    def display(self, guesses):
        for letter in self.phrase:
            if letter in guesses:
                print("{}".format(letter),end=" ")
            else:
                print("_",end=" ")
    

    def check_guess(self, guess):
        return guess in self.phrase
    

    def check_complete(self, guesses):
        for letter in self.phrase:
            if letter not in guesses:
                return False
        return True    




