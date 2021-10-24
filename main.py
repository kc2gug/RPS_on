import random

rpsp_dict  = {"Rock": ("Scissors", "Lizard"),
              "Paper": ("Rock", "Spock"),
              "Scissors": ("Paper", "Lizard")}

game_note = """============================
= GAME: ROCK PAPER SCISSORS + 2
= 
= CHOOSE ROCK/PAPER/SCISSORS to see if you win!!
= """
print(game_note)


def play_the_game(rpsp2):
    comp_val, val = random.choice(list(rpsp2.items()))

    print("=\n= LETS PLAY!!")

    for names, values in rpsp2.items():
        print("=\t\t"+names)

    user_val = input("= Enter one of the choices > ")

    print("=\n= You chose:      "+str(user_val))
    print("= Computer chose: "+comp_val)
    print("=")

    f = open("dataset.dat", "a")

    to_write=""
    try:
        if comp_val == user_val:
            to_write="=    TIE GAME"
        elif comp_val in rpsp2[user_val]:
            to_write="=    YOU WIN!!!!"
        else:
            to_write="=    ALL OF YOUR BASE ARE BELONG TO US!! :-) !!"
    except:
        to_write="= \""+str(user_val)+"\" IS NOT AN OPTION.\n= Please play again!"

    print(to_write)


do_runrun=True
while do_runrun:
    play_the_game(rpsp_dict)
    play_again = input("=\n= Play Again?[Y/N] > ").lower()
    if play_again != "y":
        do_runrun=False

