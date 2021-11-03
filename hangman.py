class hangmanGame:
    def __init__(self, secret_word):
        self.secret_word = secret_word

        self.guesses = []

        self.dict_of_parts = {1 : "HEAD", 2 : "BODY", 3 : "LEFT_ARM",
                                4 : "RIGHT_ARM", 5 : "LEFT_LEG", 6 : "RIGHT_LEG"}

        self.hangman_Guy = []

        self.finished = False
        self.win_status = False

    def get_censored_word(self):
        censored_word = ''

        for c in self.secret_word:
            if c in self.guesses:
                censored_word += c
            else:
                censored_word += '*'

        return censored_word

    def make_guess(self):
        character = input("Make a guess: \n")
        self.guesses.append(character)

        if (character not in self.secret_word) and len(self.hangman_Guy) < 6:
            self.hangman_Guy.append( self.dict_of_parts[len(self.hangman_Guy)+1] ) # Maybe confusing
        elif len(self.hangman_Guy) >= 6:
            self.finished = True



    def check_game_finished(self):
        if len(self.hangman_Guy) >= 6:
            self.finished = True
            return
        for c in self.secret_word:
            if c not in self.guesses:
                self.finished = False
                return

        self.finished = True
        return

    def get_Win_status(self):
        if len(self.hangman_Guy) < 6:
            return True
        else:
            return False

    def play_game(self):
        while (new_game.finished == False):
            new_game.make_guess()

            print( new_game.get_censored_word() )
            print( new_game.hangman_Guy )

            new_game.check_game_finished()

        if new_game.get_Win_status() == True:
            print("Congratulations you have won!")
        else:
            print("Sorry you lost.")




secret_word = str(input("Type in your word: \n"))
new_game = hangmanGame(secret_word)
new_game.play_game()
