{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "d1614992",
   "metadata": {},
   "outputs": [],
   "source": [
    "from IPython.display import clear_output\n",
    "\n",
    "def display_board(board):\n",
    "    clear_output()  # Remember, this only works in jupyter!\n",
    "    \n",
    "    print('   |   |')\n",
    "    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])\n",
    "    print('   |   |')\n",
    "    print('-----------')\n",
    "    print('   |   |')\n",
    "    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])\n",
    "    print('   |   |')\n",
    "    print('-----------')\n",
    "    print('   |   |')\n",
    "    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])\n",
    "    print('   |   |')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "4e5c6803",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "   |   |\n",
      " X | O | X\n",
      "   |   |\n",
      "-----------\n",
      "   |   |\n",
      " O | X | O\n",
      "   |   |\n",
      "-----------\n",
      "   |   |\n",
      " X | O | X\n",
      "   |   |\n"
     ]
    }
   ],
   "source": [
    "test_board = ['#','X','O','X','O','X','O','X','O','X']\n",
    "display_board(test_board)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "5ac10718",
   "metadata": {},
   "outputs": [],
   "source": [
    "def player_input():\n",
    "    marker = ''\n",
    "    \n",
    "    while not (marker == 'X' or marker == 'O'):\n",
    "        marker = input('Player 1: Do you want to be X or O? ').upper()\n",
    "\n",
    "    if marker == 'X':\n",
    "        return ('X', 'O')\n",
    "    else:\n",
    "        return ('O', 'X')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "02affb55",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Player 1: Do you want to be X or O? x\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "('X', 'O')"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "player_input()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "191f4dcc",
   "metadata": {},
   "outputs": [],
   "source": [
    "def place_marker(board, marker, position):\n",
    "    board[position] = marker"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "d1decc20",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "   |   |\n",
      " X | $ | X\n",
      "   |   |\n",
      "-----------\n",
      "   |   |\n",
      " O | X | O\n",
      "   |   |\n",
      "-----------\n",
      "   |   |\n",
      " X | O | X\n",
      "   |   |\n"
     ]
    }
   ],
   "source": [
    "place_marker(test_board,'$',8)\n",
    "display_board(test_board)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "7dd9c61d",
   "metadata": {},
   "outputs": [],
   "source": [
    "def win_check(board,mark):\n",
    "    \n",
    "    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top\n",
    "    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle\n",
    "    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom\n",
    "    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle\n",
    "    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle\n",
    "    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side\n",
    "    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal\n",
    "    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "4f0f1fb2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "win_check(test_board,'X')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "89a2f69c",
   "metadata": {},
   "outputs": [],
   "source": [
    "import random\n",
    "\n",
    "def choose_first():\n",
    "    if random.randint(0, 1) == 0:\n",
    "        return 'Player 2'\n",
    "    else:\n",
    "        return 'Player 1'\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "75242afd",
   "metadata": {},
   "outputs": [],
   "source": [
    "def space_check(board, position):\n",
    "    \n",
    "    return board[position] == ' '"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "fcf78b0d",
   "metadata": {},
   "outputs": [],
   "source": [
    "def full_board_check(board):\n",
    "    for i in range(1,10):\n",
    "        if space_check(board, i):\n",
    "            return False\n",
    "    return True"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "d54933e6",
   "metadata": {},
   "outputs": [],
   "source": [
    "def player_choice(board):\n",
    "    position = 0\n",
    "    \n",
    "    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):\n",
    "        position = int(input('Choose your next position: (1-9) '))\n",
    "        \n",
    "    return position\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "cd97aca2",
   "metadata": {},
   "outputs": [],
   "source": [
    "def replay():\n",
    "    \n",
    "    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "6fd87afc",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "   |   |\n",
      " X |   |  \n",
      "   |   |\n",
      "-----------\n",
      "   |   |\n",
      " X | O |  \n",
      "   |   |\n",
      "-----------\n",
      "   |   |\n",
      " X | O |  \n",
      "   |   |\n",
      "Congratulations! You have won the game!\n",
      "Do you want to play again? Enter Yes or No: no\n"
     ]
    }
   ],
   "source": [
    "print('Welcome to Tic Tac Toe!')\n",
    "\n",
    "while True:\n",
    "    # Reset the board\n",
    "    theBoard = [' '] * 10\n",
    "    player1_marker, player2_marker = player_input()\n",
    "    turn = choose_first()\n",
    "    print(turn + ' will go first.')\n",
    "    \n",
    "    play_game = input('Are you ready to play? Enter Yes or No.')\n",
    "    \n",
    "    if play_game.lower()[0] == 'y':\n",
    "        game_on = True\n",
    "    else:\n",
    "        game_on = False\n",
    "\n",
    "    while game_on:\n",
    "        if turn == 'Player 1':\n",
    "            # Player1's turn.\n",
    "            \n",
    "            display_board(theBoard)\n",
    "            position = player_choice(theBoard)\n",
    "            place_marker(theBoard, player1_marker, position)\n",
    "\n",
    "            if win_check(theBoard, player1_marker):\n",
    "                display_board(theBoard)\n",
    "                print('Congratulations! You have won the game!')\n",
    "                game_on = False\n",
    "            else:\n",
    "                if full_board_check(theBoard):\n",
    "                    display_board(theBoard)\n",
    "                    print('The game is a draw!')\n",
    "                    break\n",
    "                else:\n",
    "                    turn = 'Player 2'\n",
    "\n",
    "        else:\n",
    "            # Player2's turn.\n",
    "            \n",
    "            display_board(theBoard)\n",
    "            position = player_choice(theBoard)\n",
    "            place_marker(theBoard, player2_marker, position)\n",
    "\n",
    "            if win_check(theBoard, player2_marker):\n",
    "                display_board(theBoard)\n",
    "                print('Player 2 has won!')\n",
    "                game_on = False\n",
    "            else:\n",
    "                if full_board_check(theBoard):\n",
    "                    display_board(theBoard)\n",
    "                    print('The game is a draw!')\n",
    "                    break\n",
    "                else:\n",
    "                    turn = 'Player 1'\n",
    "\n",
    "    if not replay():\n",
    "        break\n",
    "            "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ffd6c616",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f666e38e",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
