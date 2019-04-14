from random import randint

game_running = True
game_results = []

def calc_monster_attack(attack_min, attack_max):
    return randint(attack_min, attack_max)

def game_end(winner_name):
    print('---' * 7)
    print(f'{winner_name} won the game!')    

while game_running == True:

    counter = 0

    new_round = True
    player = {'name': 'Miii', 'attack': 11, 'heal': 17, 'health': 100}
    monster = {'name': 'Brute', 'attack_min': 10, 'attack_max': 20, 'health': 100}

    print('---' * 7)
    print('Enter Player Name:')
    player['name'] = input()
    print('\n')
    print('---' * 7)    
    print(player['name'] + ' has ' + str(player['health']) + ' health.')
    print(monster['name'] + ' has ' + str(monster['health']) + ' health.')
    print('---' * 7)    
    print('Let\'s get started')
    print('Choose your first move...')    

    while new_round == True:
        counter += 1

        player_won = False
        monster_won = False
        
        print('---' * 7)
        print('Please select an action')
        print('1) Attack')
        print('2) Heal')
        print('3) Exit Game')
        print('4) Show Results')

        player_choice = input()

        if player_choice == '1': 
            print('You Chose Attack')
            monster['health'] -= player['attack']
            
            if monster['health'] <= 0:
                player_won = True
            else:    
                player['health'] -= calc_monster_attack(monster['attack_min'], monster['attack_max'])
                
                if player['health'] <=0:
                    monster_won = True

        elif player_choice == '2':
            print('You Chose Heal')
            player['health'] += player['heal']
            
            player['health'] -= calc_monster_attack(monster['attack_min'], monster['attack_max'])
            
            if player['health'] <=0:
                    monster_won = True

        elif player_choice == '3':
            print('You Chose Exit Game')
            new_round = False
            game_running = False
        
        elif player_choice== '4':
            for player_result in game_results: 
                print(player_result)

        else:
            print('Invalid choice')

        if player_won == False and monster_won == False:
            print(monster['name'] + ' has ' + str(monster['health']) + ' health left.')
            print(player['name'] + ' has ' + str(player['health']) + ' health left.')

        elif player_won:
            game_end(player['name'])
            round_result = {'name': player['name'], 'health': player['health'], 'rounds': counter}
            game_results.append(round_result)
            print(f'Total Rounds Played: {counter}')
            new_round = False
        elif monster_won:
            game_end(monster['name'])
            round_result = {'name': monster['name'], 'health': monster['health'], 'rounds': counter}
            game_results.append(round_result)
            print(f'Total Rounds Played: {counter}')
            new_round = False