from getpass import getpass
# Non OOP
# Bank Version 1
# Single Account

name = str(input("What is your name: "))
accountName = name.lower()
accountBalance = 100
accountPassword = str(getpass("What is your password: "))

if accountName == 'guha':
    accountBalance = 0
    print("Get some money guhy")
elif accountName == 'oliver':
    accountBalance = 500
    print("damn oli good to see you again") 
elif accountName == 'jake':
       accountBalance = 10000
       print("Hi myself")

while True:
    print('\nPress b to get the balance')
    print('Press d to make a deposit')
    print('Press w to make a withdrawl')
    print('Press s to show the account')    
    print('Press q to quit')
    
    action = input("What do you want to do? ")
    action = action.lower() #
    action = action[0]
    
    if action == 'b':
        print('\nGet Balance:')
        userPassword = getpass('Please enter your password: ')
        if userPassword != accountPassword:
            print('Incorrect Password')
        else:
            print('Your balance is: ', accountBalance)
    elif action == 'd':
        deposit = float(input('\nEnter the amount you would like to deposit: '))
        userPassword = getpass('Please enter your password: ')
        if userPassword != accountPassword:
            print('Incorrect Password')
        else:
            if deposit < 0:
                print("Please enter a positive amount")
            else:
                accountBalance += deposit 
    elif action == 'w':
        withdrawl = float(input('\nEnter the amount you would like to withdrawl: '))
        userPassword = getpass('Please enter your password: ')
        if userPassword != accountPassword:
            print('Incorrect Password')
        else:
            if withdrawl < 0:
                print("Please enter a positive amount")
            else:
                accountBalance -= withdrawl
    elif action == 's':
        userPassword = getpass('\nPlease enter your password: ')
        if userPassword != accountPassword:
            print('Incorrect Password')
        else:
            print("Name:", accountName, 
                "\nBalance:", accountBalance,
                "\nPassword:", accountPassword)      
    elif action == 'q':
        print("\nThanks for your service", accountName)
        exit()