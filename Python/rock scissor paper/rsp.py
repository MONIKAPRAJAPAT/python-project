import random
l=["rock","scissor","paper"]
# '''
# rock vs paper > paper wins

# rock vs scissor > rock

# paper vs scissor > rock wins
# '''
while True:
    uc=int(input(''' 
Game Started ......................
1 YES 
2 NO | EXIT
    '''))

    print(uc)
    if uc==1:
        # pass
            for a in range(1,6):
                userInput=int(input(''' 
                1 Rock
                2 Scissor
                3 Paper
                '''))
                # user input
                if userInput==1:
                    uchoice="rock"
                elif userInput==2:
                    uchoice="Scissor"
                elif userInput==3:
                    uchoice="Scissor"
                Cchoice=random.choice(l)

            print(uchoice)
            print(Cchoice)

        # else:
        # break