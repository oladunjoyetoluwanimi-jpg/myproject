import sys
import random


def guess_number(name="Player One"):
    game_count = 0
    player_wins = 0

    def play_geuss_number():
        nonlocal name
        nonlocal player_wins

        playerchoice = input(
            f"\n{name},geuss which number I am thinking of ... 1, 2, or 3.\n\n"

        )
        if playerchoice not in ["1", "2","3",]:
            print(f"{name}, please enter 1, 2,3 ")
            return play_geuss_number()
        computerchoice = random.choice("123")
        computer = int(computerchoice)

        print(f"\n{name},You chose: {playerchoice}")
        print(
            f"I was thinking about the number{computerchoice}.\n"

        )
        player= int(playerchoice)
        computer =int(computerchoice)

        def decide_winner(player, computer):
            nonlocal name
            nonlocal player_wins

            if player == computer:
                player_wins +=1
                return f"{name},you win!"
            else:
                return f"sorry,{name}. Better luck next time"
        game_result =decide_winner(player, computer)

        print(game_result)

        nonlocal game_count
        game_count += 1
        print(f"\nGame Count:{game_count}")
        print(f"\n{name}'s wins: {player_wins}")
        print(f"\nYour winning percentage: {player_wins/game_count:.2%}")
        print(f"\nPlay again, {name}?")
        while True:
            playagain = input("\n Yes or \n Q to Quit\n")
            if playagain.lower() not in ['y', 'q']:
                continue
            else:
                break

            if playagain.lower()=="y":
                return play_geuss_number()
            else:
                print("\n win")
                print('Thank you for playing\n')
                if__name__ == "__main__"