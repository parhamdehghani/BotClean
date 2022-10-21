"""
The goal of Artificial Intelligence is to create a rational agent (Artificial Intelligence 1.1.4). An agent gets input from the environment through sensors and acts on the environment with actuators. In this challenge, you will program a simple bot to perform the correct actions based on environmental input.

Meet the bot MarkZoid. It's a cleaning bot whose sensor is a head mounted camera and whose actuators are the wheels beneath it. It's used to clean the floor.

The bot here is positioned at the top left corner of a 5*5 grid. Your task is to move the bot to clean all the dirty cells.

Input Format

The first line contains two space separated integers which indicate the current position of the bot.
The board is indexed using Matrix Convention
5 lines follow representing the grid. Each cell in the grid is represented by any of the following 3 characters: 'b' (ascii value 98) indicates the bot's current position, 'd' (ascii value 100) indicates a dirty cell and '-' (ascii value 45) indicates a clean cell in the grid.

Note If the bot is on a dirty cell, the cell will still have 'd' on it.

Output Format

The output is the action that is taken by the bot in the current step, and it can be either one of the movements in 4 directions or cleaning up the cell in which it is currently located. The valid output strings are LEFT, RIGHT, UP and DOWN or CLEAN. If the bot ever reaches a dirty cell, output CLEAN to clean the dirty cell. Repeat this process until all the cells on the grid are cleaned.

Sample Input #00

0 0
b---d
-d--d
--dd-
--d--
----d
Sample Output #00

RIGHT
Resultant state

-b--d
-d--d
--dd-
--d--
----d
Sample Input #01

0 1
-b--d
-d--d
--dd-
--d--
----d
Sample Output #01

DOWN
Resultant state

----d
-d--d
--dd-
--d--
----d
Task

We write the function next_move that takes in 3 parameters posr, posc being the co-ordinates of the bot's current position and board which indicates the board state to print the bot's next move.

"""

#!/usr/bin/python3

# Head ends here


def next_move(posr, posc, board):
    import random
    condition = False
    check_table = [[posr,posc],[posr,posc+1],[posr+1,posc],[posr,posc-1],[posr-1,posc]]
    for new_pos in check_table:
        if (new_pos[0]>=0 and new_pos[0]<=4) and (new_pos[1]>=0 and new_pos[1]<=4):
            if board[new_pos[0]][new_pos[1]] == 'd':
                condition = True
                i,j = new_pos
                if (i==posr and j>posc):
                    move = 'RIGHT'
                if (i==posr and j<posc):
                    move = 'LEFT'
                if (i<posr and j==posc):
                    move = 'UP'
                if (i>posr and j==posc):
                    move = 'DOWN'
                if (i==posr and j==posc):
                    move = 'CLEAN'

                print(move)
                break
    if condition == False:
        for _ in range(10):
            i,j = random.choice(check_table[1:])
            if (i>=0 and i<=4) and (j>=0 and j<=4):
                if (i==posr and j>posc):
                    move = 'RIGHT'
                if (i==posr and j<posc):
                    move = 'LEFT'
                if (i<posr and j==posc):
                    move = 'UP'
                if (i>posr and j==posc):
                    move = 'DOWN'

                print(move)
                break

# Tail starts here

if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    next_move(pos[0], pos[1], board)
