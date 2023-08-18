# Jason Buol

rooms = {
    'Cargo Bay': {'name': 'in the Cargo Bay', 'go north': 'Engineering', 'go east': 'Corridor',
                  'go south': 'Observation Deck', 'go west': 'Barracks',
                  'text': 'There is a door to the north, east, south and west.', },
    'Barracks': {'name': 'in the Barracks', 'go north': 'Mess Hall', 'go east': 'Cargo Bay',
                 'text': 'There is a door to the north and east.', 'item': 'guidebook',
                 'item_text': 'There is a guidebook on a footlocker.'},
    'Mess Hall': {'name': 'in the Mess Hall', 'go south': 'Barracks', 'text': 'There is a door to the south.',
                  'item': 'peanuts', 'item_text': 'There are some leftover peanuts on one of the tables.'},
    'Engineering': {'name': 'in Engineering', 'go east': 'Bridge', 'go south': 'Cargo Bay',
                    'text': 'There is a door to the east and south', 'item': 'translator',
                    'item_text': 'Someone left their translator on the workbench.'},
    'Bridge': {'name': 'on the Bridge', 'go west': 'Engineering', 'text': 'There is a door to the west.',
               'item': 'Svartálfar', 'item_text': 'The Svartálfar'},
    'Corridor': {'name': 'in a Corridor', 'go north': 'Engine Room', 'go west': 'Cargo Bay',
                 'text': 'There is a door to the north and west.'},
    'Engine Room': {'name': 'in the Engine Room', 'go south': 'Corridor', 'text': 'There is a door to the south.',
                    'item': 'teleporter', 'item_text': 'A teleporter has been left unattended on'
                    ' the floor.  It seems like a very careless place to leave such a sensitive piece of equipment.'},
    'Observation Deck': {'name': 'on the Observation Deck', 'go north': 'Cargo Bay', 'go east': 'Restrooms',
                         'text': 'There is a door to the north and east.', 'item': 'beer',
                         'item_text': 'The Observation Deck, what better place to find a beer.'},
    'Restrooms': {'name': 'in the Restrooms', 'go west': 'Observation Deck', 'text': 'There is a door to the west.',
                  'item': 'towel', 'item_text': 'In a completely unsurprising turn of events.  You find a towel in the'
                                                'Restroom.'}
}
directions = ['go north', 'go east', 'go south', 'go west']
current_room = rooms['Cargo Bay']
carrying = []
total_items = 0

print('\nWelcome to Escape the Svartálfar!')
print('\nIn an attempt to see the universe cheaply you have accidentally teleported into the cargo hold of a nearby\n'
      'Svartálfar ship.  You need to find your lost supplies and get the necessary protein restoratives and muscle\n'
      'relaxants to escape the ship before being discovered by the Svartálfar.  You will need to find your Guidebook,\n'
      'Teleportation Device, Translator and Towel.  You will also need to find some peanuts and beer for the necessary\n'
      'protein and relaxants for space travel.  The Svartálfar are one of the most bad-tempered, bureaucratic,\n'
      'and callous races in the galaxy, if they find you, they will throw you out of the airlock. ')
print('\nPress Enter to continue...')
input()
print('\nTo move between rooms enter go and the direction that you would like to move in.  (e.g., go west)')
print('To pick up an item that is in the room you are in enter get and the item you would like to pick up.'
      ' (e.g. get towel)')
print('If you want to quit enter quit.')

while current_room != rooms['Bridge']:
    if total_items < 6:
        print('\nYou are {}.'.format(current_room['name']))
        print(current_room['text'])
        if 'item' in current_room:
            print(current_room['item_text'])

        else:
            print('There is nothing in the room.')
        separator = ', '
        print('You are currently carrying, {}.'.format(separator.join(carrying)))
        command = input('\nWhat would you like to do?\n').lower()

        if command in directions:
            if command in current_room:
                current_room = rooms[current_room[command]]
            else:
                print('\nDue to the laws of improbability there was a small chance that walking into the\n'
                      'wall would create a new doorway for you.  Unfortunately for you this time you were\n'
                      'only rewarded with a headache.  Try an existing door next time.')
        elif len(command) == 0:
            print(
                'I am but a simple program and I do not understand what you are trying to do.  Please try a valid option.')
        elif command.split()[0] == 'get':
            item = command.split()[1]
            if item == current_room.get('item'):
                current_room.pop('item')
                carrying.append(item)
                total_items += 1
                print('You have picked it up.')


            else:
                print('\nThat item does not seem to be in this room.')

        elif command == 'quit':
            print('So long and thanks for all the fish.')
            break
        else:
            print('I am but a simple program and I do not understand what you are trying to do.  Please try a valid option.')
    else:
        print('\nCongratulations! You have found everything that you need to safely escape the Svartálfar ship.')
        print('\nThank you for playing and good luck with all your future travels.  And remember, Don''t panic.')
        break

else:
    print('\nYou have been discovered by the Svartálfar!  After torturing you by forcing you to listen to their\n'
          'poetry they have thankfully put you out of your misery by throwing you out of the airlock.')
    print('\nThank you for playing and better luck next time!')

