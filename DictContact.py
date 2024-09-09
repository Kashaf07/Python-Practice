contact={}
running = True
while running:
    command = input('A)Add D)Delete L)Look up Q)Quit P)Print:')
    if command == 'A' or command == 'a':
        name = input('Enter name to add:')
        num = int(input('Enter Number:'))
        contact['name'] = num
    elif command == 'D' or command == 'd':
        name = input('Enter name to delete:')
        del contact['name']
    elif command == 'L' or command == 'l':
        name = input('Enter name:')
        print(name, contact[name])
    elif command == 'P' or command == 'p':
        print('Contacts are:',contact)
    elif command == 'Q' or command == 'q':
        running = False
    else:
        print(command,'is not valid command!')
