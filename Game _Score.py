# The game() function in a program lets a user play a game and returns the score as an integer. You need to read a file “Hiscore.txt” which is either blank or contains the previous Hi-score. You need to write a program to update the Hi-score whenever game() breaks the Hi-Score.

def game():
    return 38

score=game()    

with open("game_score.txt") as f:
    hi_score=int(f.read())

if score>hi_score:
    with open("game_score.txt","w") as f:
        f.write(str(score))