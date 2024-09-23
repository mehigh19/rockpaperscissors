import random

h=['rock','paper','scissors']

host =h[random.randint(0,2)]
player=False
player_count=0
host_count=0

while player == False:
    player_pick=input('rock, paper or scissors ? ')
    print(f'Player picked {player_pick} while host picked {host}')
    print('__________________________________________________')
    player=True
    if player_pick == 'rock' or player_pick == 'paper' or player_pick == 'scissors':
        if player_pick == host:
            print('it was a tie, no points added')
        if player_pick == 'rock' and host == 'paper':
            print('host won, paper beats rock')
            host_count+=1
        if player_pick == 'rock' and host == 'scissors':
            print('player won, rock beats scissors')
            player_count+=1
        if player_pick == 'paper' and host == 'rock':
            print('player won, paper beats rock')
            player_count+=1
        if player_pick == 'paper' and host == 'scissors':
            print('host won, scissors beats paper')
            host_count+=1
        if player_pick == 'scissors' and host == 'rock':
            print('host won, scissors beats rock')
            host_count+=1
        if player_pick == 'scissors' and host == 'paper':
            print('player won, scissors beats paper')
            player_count+=1
    else:
        print('check your spelling, input rock paper os scissors please')

    next_game=input('next game ? y/n ')
    if next_game == 'y':
        player=False
        host =h[random.randint(0,2)]
    else:
        print('Game Over')
        if player_count == host_count:
            print(f'The game ended up in a tie of {host_count} points')
        else:
            if player_count > host_count:
                print(f'Player won !! He had {player_count} points ! Congratulations')
            else:
                print(f'Host won !! He had {host_count} points ! Congratulations')