import random


def pig_game() -> None:
    seperator: str = ('------------------------------------------------------------------------------------------------'
                      '-----------------------------------------------------------------------------------------------')
    seperator2: str = '--------------------------------------'
    while True:
        number_of_players: int = int(input('How many players are playing: '))
        if number_of_players <= 1:
            print('number of players can not be 1 or less than 1')
        else:
            break
    scores: dict = {
        f'Player {i}': 0 for i in range(number_of_players)
    }
    while running := True:
        for i in range(number_of_players):
            print(seperator)
            print(f'It is player {i + 1}\'s turn')
            while True:
                risk: str = input('Do you want to risk and roll the dice (Y for yes and N for no): ')
                while risk.upper() != 'Y' and risk.upper() != 'N':
                    if risk.upper() != 'Y' and risk.upper() != 'N':
                        print('Please type Y or N')
                    else:
                        break
                    risk = input('Do you want to risk and roll the dice (Y for yes and N for no): ')
                if risk.upper() == 'Y':
                    number_rolled: int = random.randint(1, 6)
                    print(f'Number rolled by dice = {number_rolled}')
                    if number_rolled != 1:
                        scores[f'Player {i}'] += number_rolled
                    else:
                        scores[f'Player {i}'] = 0
                        print(f'Player {i + 1}\'s score = {scores[f'Player {i}']}')
                        break
                    if scores[f'Player {i}'] >= 50:
                        print(f'Player {i+1} won the game with {scores[f'Player {i}']} points')
                        running = False
                        break
                    print(f'Player {i+1}\'s score = {scores[f'Player {i}']}')
                else:
                    print('Ok')
                    break
                if not running:
                    break
                print(seperator2)


if __name__ == '__main__':
    try:
        pig_game()
    except ValueError:
        print('Number of players can only be a number')
        pig_game()
