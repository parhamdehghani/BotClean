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
