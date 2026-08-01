def start_game(secret):
    print('Game started. Guess the number!')
    # simple check helper
    def check(guess):
        if guess == secret: return 'Correct'
        return 'High' if guess > secret else 'Low'
    print('Guess 30:', check(30))
    print('Guess 42:', check(42))