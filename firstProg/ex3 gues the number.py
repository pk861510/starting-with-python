#no of guses = 9;
#print number of guses left
#number of guses he took to finish
#game over

number= 19
gues = 1
print("you have only 9 guses")
while(gues<=9):

    n=int(input("guess the number : "))
    if(number==n):
        print("\n Congrats the Game is Over\n","And you took only",gues,"Attempt to finish the game")
        break
    else:
        if n>number:
            print("Sorry you guess greater number",end="\t")
            print("\nTry again \n", 9 - gues, "attempt left to finish the game\n")
        else:
            print("Sorry you guess lesser number",end="")
            print("\nTry again \n", 9 - gues, "attempt left to finish the game\n")

    gues=gues+1;
if gues>9:
    print("Sorry you excid maximum number of chance")