player1=input("enter player1 shape:")
player2=input("enter player2 shape:")
if(player1=="paper" and player2=="rock" or player1=="scissors"and player2=="paper" or player1=="rock"and player2=="scissors" ):
    print("player1 win")
elif (player1=="paper"and player2=="paper" or player1=="scissors"and player2=="scissors" or player1=="rock"and player2=="rock"):
    print("It is a tie")
else:
    print("palyer2 win")   
again=input("Do you want to play again (Y for yes, N for no):")
while (again=="Y"):
    player1=input("enter player1 shape:")
    player2=input("enter player2 shape:")
    if(player1=="paper" and player2=="rock" or player1=="scissors"and player2=="paper" or player1=="rock"and player2=="scissors" ):
        print("player1 win")
    elif (player1=="paper"and player2=="paper" or player1=="scissors"and player2=="scissors" or player1=="rock"and player2=="rock"):
        print("It is a tie")
    else:
        print("palyer2 win")
else:
        print("Game over")
