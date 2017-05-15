import os

from pieces_needed_list import pieces_needed


def check_if_in(piece):
    if piece in pieces_checked:
        print('You\'ve already checked that piece. We {}'.format(pieces_checked[piece]))
    else:
        if piece in pieces_needed:
            print('Success! Save that one, we don\'t have it yet!')
            pieces_checked[piece] = 'do need that piece. Set it aside.'
        else:
            print('We already have it. Sorry.')
            pieces_checked[piece] = 'already have it.'


pieces_checked = {}

while True:

    piece_to_check_for = input('Enter game piece (first two characters then last letter i.e. 8ab) >> ')

    if piece_to_check_for.lower() == 'quit':
        break

    check_if_in(piece_to_check_for)
    input('Press enter to continue or \"quit\" to exit... ')

    if piece_to_check_for.lower() == 'quit':
        break

    os.system('cls' if os.name == 'nt' else 'clear')
