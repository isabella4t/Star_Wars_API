import funct

def menu():
    """
    Display a menu of three items, including 'exit'.
    """
    exit = False
    while not exit:
        print('1. Find Person')
        print('2. Find Homeworld')
        print('3. Find Films')
        print('4. Exit')
        choice = input('Make a selection: ')
        if choice ==  '1':
            print('1. URL')
            print('2. Number')
            choice = input("Do you want to enter a URL or Number? ")
            if choice ==  '1':
                ans = input("Enter a character's url: ")
                funct.viewper(ans)
            elif choice == '2':
                ans = input("Enter a character's number: ")
                funct.viewperson(ans)
            else:
                print('Unknown')
        elif choice == '2':
            ans = input("Enter a planet's url: ")
            funct.viewhome(ans)
        elif choice == '3':
            ans = input("Enter a movie's url: ")
            funct.viewfilm(ans)
        elif choice == '4':
            print('exiting...')
            exit = True
        else:
            print('Unrecognized input: ' + choice)

menu()
