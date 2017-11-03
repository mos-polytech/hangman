from hangman.game import Game
from hangman.players import HumanPlayer
from hangman.round import Round


def start_game():
    game = Game()
    player1 = HumanPlayer()

    player2_class = player1.select_other_player()
    player2 = player2_class()

    while True:
        winner = game.get_winner()

        if winner:
            print('Winner is {}'.format(winner))
            break

        if player1.should_change_turns():
            print('Changed turns!')
            player1, player2 = player2, player1
            print('Guessing: {}, opponent: {}'.format(
                player1.id,
                player2.id,
            ))

        word = player1.quess_new_word()
        current_round = Round(word)
        print('New word is guessed!')

        while not current_round.is_finished():
            print(current_round.mask_word())
            current_round.draw_field()
            print()
            letter = input('Letter: ')
            current_round.try_letter(letter)


        current_round.draw_result()
        game.add_round(current_round, player1, player2)
