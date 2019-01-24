try:
    import time,sys,random
    username = ''
    password = ''
    username1 = ''
    password1 = ''
    usernames = []
    passwords = []
    scores_list = []
    scores_dict = {}
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
            #dice1 = 3
            #dice2 = 3
            # Get the total
            total = dice1 + dice2
            if dice1 == dice2:
                # If they roll a double then they roll another one
                dice3 = random.randint(1,6)
                #print(dice3)
                print('You got a double!')
                total +=dice3
            #print(total)
            if player_playing == 1:
                # If their score is above 0
                # If the total is even add 10
                if total % 2 == 0:
                    score1+=10
                    score1+=total
                # If it's odd minus 5
                else:
                    if score1-5 > 0:
                        score1-=5
                        score1+=total
                    else:
                        score1 = 0
                #score1+=total
                print('Player one, your score is',score1)
                # Make sure it doesn't look like a cascade of dice related nonsense
                time.sleep(1)
                player_playing = 2
            else:
                # Do it all again
                if total % 2 == 0:
                    score2+=10
                    score2+=total
                else:
                    if score2-5 > 0:
                        score2-=5
                        score2+=total
                    else:
                        score2 = 0

                #score2+=total
                print('Player two, your score is',score2)
                time.sleep(1)
                if rounds_o<5:
                    print('Now for round',rounds_o+1)
                player_playing = 1
                rounds_o+=1
            rounds +=1
        while score1 == score2:
            # If their score is equal at the end
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
            # See who won
            print('Player one, you have won')
            global username
            winner = score1
            winner_name = username
        else:
            print('Player two you have won')
            global username1
            winner = score2
            winner_name = username1
        # Write the score and name to leaderboard file
        file_leader = open('leaderboard.txt','a+')
        file_leader.write('%s,%d\n' % (winner_name,winner))
        file_leader.close()
        menu()
        
    def sort2(value):
        return int(value[1])
    def leaderboard():
        # Opens file
        file = open('leaderboard.txt','r')
        # Strips the newline, and splits the values at the comma
        line = file.readline().strip().split(',')
        while len(line) > 1:
            # Append the lines to the list
            scores_list.append(line)
            line = file.readline().strip().split(',')
        file.close()
        # Sort the list
        scores_list.sort(key = sort2,reverse=True)
        #print(str(scores_list)[1:-1])
        # Print the leaderboard
        for x in scores_list:
            print(x[0],x[1])
        menu()
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
            # Magical game
            game()
        elif choice == '2':
            #Exits
            sys.exit()
        elif choice == '3':
            #Shows the leaderboard
            leaderboard()
        else:
            #Error handling
            print('That option is not available, try again.')
            time.sleep(1)
            print('')
            menu()

    def login():
        global username
        global password
        username = input('Enter your username, player one: ')
        password = input('Enter your password, player one: ')
        auth(username,password,1)
    def login1():
        global username1
        global password1
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
            # Checks if the password is the same
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
    #game()
    login()
    #leaderboard()
# Let them leave nicely
except KeyboardInterrupt as x:
    print('\nSee you later!!!')


