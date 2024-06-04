from commands.games.hangman.hangman import HangmanGame

def hm_start(bot, message):
    global game
    word_list = ['пенис', 'жопа', 'вазелин', 'пидорас', 'даун', 'далбоёб', 'петух', 'отчим', 'уебан']
    game = HangmanGame(word_list)
    game.choose_word()
    bot.reply_to(message, "Давайте начнем игру в виселицу! Угадайте слово: " + game.display_word())
    
def hm_game(bot, message):
    global game
    if game is None or game.game_over:
        pass
    else:
        guess = message.text.lower()
        if len(guess) == 1 and guess.isalpha():
            result = game.guess(guess)
            bot.reply_to(message, result)
        else:
            bot.reply_to(message, "Пожалуйста, введите только одну букву")
