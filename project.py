try:
    import time,sys,random
    usernames = []
    passwords = []
    def game():
        # Dice rolls
        score1 = 0
        score2 = 0
        rounds = 0
        rounds_o = 1
        player_playing = 1
        print('Now for round 1')
        while rounds < 10:
            dice1 = random.randint(1,6)
            dice2 = random.randint(1,6)
            total = dice1 + dice2
            if player_playing == 1:
                score1+=total
                print('Player one, your score is',score1)
                time.sleep(1)
                player_playing = 2
            else:
                score2+=total
                print('Player two, your score is',score2)
                time.sleep(1)
                if rounds_o<5:
                    print('Now for round',rounds_o+1)
                player_playing = 1
                rounds_o+=1
            rounds +=1
        while score1 == score2:
            dice3 = random.randint(1,6)
            if player_playing == 1:
                score1+=total
                print('Player one, your score is',score1)
                time.sleep(1)
                player_playing = 2
            else:
                score2+=total
                print('Player two, your score is',score2)
                time.sleep(1)
                player_playing = 1
        if score1 > score2:
            print('Player one, you have won')
        else:
            print('Player two you have won')            
    def menu():
        # Rules
        print('Welcome to the dice game.')
        print('The rules are: ')
        print('1) You need 2 players, so grab a friend')
        print('2) You each roll 2 six sided dice')
        print('3) The points are added to your score.')
        print('4) If the total is an even number, an additional 10 points are added to your score.')
        print('5) If the total is an odd number, 5 points are subtracted from your score.')
        print('6) If you roll a double, you get to roll one extra die and get the number of points rolled added to your score. ')
        print('7) The person with the highest score at the end of 5 rounds wins.')
        print('8) If you have the same score at the end of the 5 rounds, you each roll 1 die and whoever gets the highest score wins (this repeats until someone wins)')

        #Options
        print('')
        print('Option 1: Play the Game')
        print('Option 2: Quit the Game')
        print('Option 3: View the high score')
        choice = input('Choose an option, 1,2 or 3: ')

        if choice == '1':
            # Magical game which will appear
            game()
        elif choice == '2':
            sys.exit()
        elif choice == '3':
            leaderboard()
        else:
            print('That option is not available, try again.')
            time.sleep(1)
            print('')
            menu()

    def login():
        username = input('Enter your username, player one: ')
        password = input('Enter your password, player one: ')
        auth(username,password,1)
    def login1():
        username1 = input('Enter your username, player two: ')
        password1 = input('Enter your password, player two: ')
        auth(username1,password1,2)

    def auth(name,password,player):
        #print(player)
        # opens file with usernames and passwords
        file1 = open('username.txt','r')
        auth_data = file1.readlines()
        for i in range(len(auth_data)):
            if i%2 == 0:
                # Adds username to list, removing the newline
                usernames.append(auth_data[i][:-1])
            else:
                # Adds password to list, removing the newline
                passwords.append(auth_data[i][:-1])
        file1.close()
        try:
            if password == passwords[usernames.index(name)]:
                if player == 1:
                    login1()
                else:
                    menu()
            else:
                print('Authentication error')
                if player == 2:
                    login1()
                else:
                    login()
        except ValueError as e:
            print('Authentication error')
            login()

    login()
except KeyboardInterrupt as x:
    print('\nSee you later!!!')

