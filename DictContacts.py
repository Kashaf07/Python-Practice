contacts = {}
running = True

while running:
    command = input('A) Add D) Delete L) Look up Q) Quit P) Print: ')

    if command == 'A' or command == 'a':
        name = input('Enter name to add: ')
        num = int(input('Enter Number: '))
        contacts[name] = num
    elif command == 'D' or command == 'd':
        name = input('Enter name to delete: ')
        if name in contacts:
            del contacts[name]
        else:
            print(name, 'is not in your contacts.')
    elif command == 'L' or command == 'l':
        name = input('Enter name: ')
        if name in contacts:
            print(name, contacts[name])
        else:
            print(name, 'is not in your contacts.')
    elif command == 'P' or command == 'p':
        print('Contacts are:', contacts)
    elif command == 'Q' or command == 'q':
        running = False
    else:
        print(command, 'is not a valid command!')

