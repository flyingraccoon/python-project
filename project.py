try:
    import time,sys
    usernames = []
    passwords = []
    def menu():
        # Rules
        print('Welcome to the dice game.')
        print('The rules are: ')
        print('1) You need 2 players so grab a friend')
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
        username = input('Enter your username: ')
        password = input('Enter your password: ')
        auth(username,password)

    def auth(name,password):
        file1 = open('username.txt','r')
        auth_data = file1.readlines()
        for i in range(len(auth_data)):
            if i%2 == 0:
                usernames.append(auth_data[i][:-1])
            else:
                passwords.append(auth_data[i][:-1])
        file1.close()
        try:
            if password != passwords[usernames.index(name)]:
                print('Authentication error')
                login()
            else:
                menu()
        except ValueError as e:
            print('Authentication error')
            login()
        print(user_names)
        print(passwords)

    login()
except KeyboardInterrupt as x:
    print('\nSee you later!!!')

