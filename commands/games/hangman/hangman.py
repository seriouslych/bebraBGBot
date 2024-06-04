import random

class HangmanGame:
    def __init__(self, word_list):
        self.word_list = word_list
        self.word = ''
        self.guessed_letters = []
        self.max_attempts = 6
        self.attempts_left = self.max_attempts
        self.game_over = False

    def choose_word(self):
        self.word = random.choice(self.word_list).lower()

    def display_word(self):
        displayed_word = ''
        for letter in self.word:
            if letter in self.guessed_letters:
                displayed_word += letter + ' '
            else:
                displayed_word += '_ '
        return displayed_word.strip()

    def guess(self, letter):
        if letter in self.word:
            self.guessed_letters.append(letter)
            if self.check_win():
                self.game_over = True
                return "Поздравляю! Вы угадали слово: " + self.word
            else:
                return "Правильно! " + self.display_word()
        else:
            self.attempts_left -= 1
            if self.attempts_left == 0:
                self.game_over = True
                return "Вы проиграли. Загаданное слово было: " + self.word
            else:
                return f"Неправильно! Осталось попыток: {self.attempts_left}. " + self.display_word()

    def check_win(self):
        for letter in self.word:
            if letter not in self.guessed_letters:
                return False
        return True
