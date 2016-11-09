print('Welcome to the world famous Dr. NIM game')
print(' ')
print('Dr. NIM guarantees that you cannot win this game!')
print(' ')
print('Here are the rules:')
print('#1 - You are playing against Dr. NIM.')
print('#2 - Since you cannot win, he is allowing you to go first.')
print('#3 - You can choice to remove 1, 2, or 3 marbles from the jar.')
print('#4 - After you choose how many to take, Dr. NIM gets a turn.')
print('#5 - You may only take marbles that are available.')
print('#6 - No cheating!!!!!')
print(' ')
print('The winner is the person who can leave only one marble')
print(' ')

items = 21
print('There are {} marbles in the jar'.format(items))
    
while True:
    while True:
       takes = int(raw_input('How many marbles would you take?  '))
       if takes in [1, 2, 3] and takes < items:
            break
       print('You are trying to cheat!')

    nim = 4 - takes
    print('Dr. NIM takes {}'.format(nim))

    items = items - takes - nim

    if items == 1:
        print('There is now {} marble remaining in the jar'.format(items))
        print "Dr. NIM WINS!!!!"
        break
    print('There are now {} marbles remaining in the jar'.format(items))
    
raw_input('press any key to exit.')

