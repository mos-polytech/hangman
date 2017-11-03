import argparse
import sys

from hangman.main import start_game


parser = argparse.ArgumentParser(description='Hangman game CLI')
parser.add_argument('command', nargs=1, help=(
    'What to do?\n'
    'Possible commands are: new|help'
))


def main():
    commands = {
        'new': start_game,
        'help': parser.print_help,
    }

    try:
        args = parser.parse_args()
        command = commands[args.command[0]]

        command()
    except Exception as e:
        print(e)
        sys.exit(1)
    except KeyboardInterrupt:
        print()
        print('Bye!')
        sys.exit(0)
