import random

theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}


def ComputerPlace(answerNumber):
    if answerNumber == 1:
        return 'top-L'
    elif answerNumber == 2:
        return 'top-M'
    elif answerNumber == 3:
        return 'top-R'
    elif answerNumber == 4:
        return 'mid-L'
    elif answerNumber == 5:
        return 'mid-M'
    elif answerNumber == 6:
        return 'mid-R'
    elif answerNumber == 7:
        return 'low-L'
    elif answerNumber == 8:
        return 'low-M'
    elif answerNumber == 9:
        return 'low-R'


def Position(answerNum):
    if answerNum == 'top-L':
        return 1
    elif answerNum == 'top-M':
        return 2
    elif answerNum == 'top-R':
        return 3
    elif answerNum == 'mid-L':
        return 4
    elif answerNum == 'mid-M':
        return 5
    elif answerNum == 'mid-R':
        return 6
    elif answerNum == 'low-L':
        return 7
    elif answerNum == 'low-M':
        return 8
    elif answerNum == 'low-R':
        return 9


def printBoard(board):
    print (board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print (board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print (board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])


turn = 'X'
computerMove = 'O'
Mlist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
try:
    for i in range(5):
        if theBoard['top-L'] == 'X' and theBoard['top-M'] == 'X' and theBoard['top-R'] == 'X':
            print 'You won'
            break
        elif theBoard['mid-L'] == 'X' and theBoard['mid-M'] == 'X' and theBoard['mid-R'] == 'X':
            print 'You won'
            break
        elif theBoard['low-L'] == 'X' and theBoard['low-M'] == 'X' and theBoard['low-R'] == 'X':
            print 'You won'
            break
        elif theBoard['top-L'] == 'X' and theBoard['mid-L'] == 'X' and theBoard['low-L'] == 'X':
            print 'You won'
            break
        elif theBoard['top-M'] == 'X' and theBoard['mid-M'] == 'X' and theBoard['low-M'] == 'X':
            print 'You won'
            break
        elif theBoard['top-R'] == 'X' and theBoard['mid-R'] == 'X' and theBoard['low-R'] == 'X':
            print 'You won'
            break
        elif theBoard['top-L'] == 'X' and theBoard['mid-M'] == 'X' and theBoard['low-R'] == 'X':
            print 'You won'
            break
        elif theBoard['top-R'] == 'X' and theBoard['mid-M'] == 'X' and theBoard['low-L'] == 'X':
            print 'You won'
            break
        elif theBoard['top-L'] == 'O' and theBoard['top-M'] == 'O' and theBoard['top-R'] == 'O':
            print 'The computer won'
            break
        elif theBoard['mid-L'] == 'O' and theBoard['mid-M'] == 'O' and theBoard['mid-R'] == 'O':
            print 'The computer won'
            break
        elif theBoard['low-L'] == 'O' and theBoard['low-M'] == 'O' and theBoard['low-R'] == 'O':
            print 'The computer won'
            break
        elif theBoard['top-M'] == 'O' and theBoard['mid-M'] == 'O' and theBoard['low-M'] == 'O':
            print 'The computer won'
            break
        elif theBoard['top-R'] == 'O' and theBoard['mid-R'] == 'O' and theBoard['low-R'] == 'O':
            print 'The computer won'
            break
        elif theBoard['top-L'] == 'O' and theBoard['mid-M'] == 'O' and theBoard['low-R'] == 'O':
            print 'The computer won'
            break
        elif theBoard['top-R'] == 'O' and theBoard['mid-M'] == 'O' and theBoard['low-L'] == 'O':
            print 'The computer won'
            break
        else:
            print(printBoard(theBoard))
            print ('Turn for ' + turn + '. Move on which space?')
            move = input()
            theBoard[move] = turn
            Mlist.remove(Position(move))
            if turn == 'X':
                r = random.choice(Mlist)
                if r in Mlist:
                    if theBoard[ComputerPlace(r)] == ' ':
                        theBoard[ComputerPlace(r)] = computerMove
                        Mlist.remove(r)
                    else:
                        r = random.choice(Mlist)
                        theBoard[ComputerPlace(r)] = computerMove
            else:
                turn = 'X'
except(IndexError):
    print 'End of Game'

printBoard(theBoard)
