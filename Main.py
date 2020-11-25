"""Kevin's Integration Project: prologue to a text adventure game."""
__author__ = 'Kevin Kostage'

# Kevin Kostage
# This is the prologue to a text adventure game
# Credit to: Jario, Professor Vanselow

def sprint_1_legacy():
    """This is from my previous project that I decided not to continue on do to
    the difficulty and coding block I had with adding on to the project. This
    function is here so I can meet the requirement from the previous sprint."""
    # This is the process of checking and doing the operations.
    print('**Running Operation check...**')
    # (**): it raises an integer or float to a certain power.
    # Ex: 2**3 = 8
    exponent = 2 ** 3
    # (*): multiplies an integer or float together.
    # Ex: 2 * 3 = 6
    multiply = 2 * 3
    # (/): divides an integer or float, turns integer into a float.
    # Ex: 2/3 = 0.3333333333333333333 6/3 = 2
    divide = 4 / 2
    # (//): divides an integer or float, but does not keep the remainder.
    # Ex: 19 // 10 = 1
    floor_divide = 4 // 2
    # (%): divides an integer or float, but only keeps the remainder.
    # Ex: 19 // 10 = 9
    modulus = 19 % 10
    # (+): adds integer or floats together.
    # Ex: 2 + 2
    addition = 2 + 2
    # (-): subtracts integer or floats.
    # Ex: 4 - 2 = 2
    subtraction = 4 - 2
    if exponent == 8:
        print("** Completed 1/7 **")
    if multiply == 6:
        print("** Completed 2/7 **")
    if divide == 2.0:
        print("** Completed 3/7 **")
    if floor_divide == 2:
        print("** Completed 4/7 **")
    if modulus == 9:
        print("** Completed 5/7 **")
    if addition == 4:
        print("** Completed 6/7 **")
    if subtraction == 2:
        print("** Completed 7/7 **")
        print("** Operation Check Completed. **")

    print('\n')
    print("Hello..." * 2)
    # (string operator)(*): multiplies how many times a string is printed.
    # Ex: print("hello" * 2) = "hello" "hello"
    print("Hi! " + "My name is gang man " + "and...")
    # (string operator)(+): adds strings together.
    # Ex: "addi" + "tion" = "addition"
sprint_1_legacy()

def dialogue_ncp_1():
    """This function's purpose is that it gives the intro dialogue for the user
    when they start the game and gives the user the first dialogue
    options in the game"""
    print('Welcome to the Prologue of "THE ADVENTURE STARTS WITH YOU!"')
    # The user name will be used through out the prologue.
    print('')  # These printed spaces are meant for better reading for the
    # user.
    user_name = input("Please state your character's name: ", )
    print('\n')  # These are also meant for better reading.
    print('Hello ', user_name + '!')
    print('\n')
    print('Prologue Act 1:')
    print('\n')
    print('You wake up in a forest surrounded by trees and foliage.')
    print('You look around to see a pathway...')
    print('\n')
    print('You see a golden silhouette of a woman at the end of the pathway.')
    print('The silhouette in a calm voice beckons you to her.')
    print('\n')
    print('As you walk towards her, pink characters and symbols ')
    print('start appearing around the pathway and your hands starts to hurt.')
    print('You stop to look at your hands and to your surprise the back of ')
    print('both of your hands have golden heart symbols that seems to')
    print('emanate all colors imaginable. You look up from your hands to ')
    print('see that the golden silhouette is suddenly in front of you.')
    print('\n')
    print('Golden Silhouette: Hello ' + user_name + ', it seems that you')
    print('have finally woke up from your coma. Do you remember anything?')
    print('\n')
    print('** Type (1),(2), or (3) to select the following phrases **')
    print('\n')
    print('(1): "WHY DO I HAVE GOLDEN HEARTS ON MY HANDS!?!?!')
    print('(2): "If I was in a coma then why am I not in a hospital...')
    print('wait am I dreaming!?!?"')
    print('(3): "Only thing I remember is my name, nothing else."')

    # The variables that are in the while loop with the try and except
    # operators prevents strings inputs crashing the game. What the while loop
    # does is that keeps on asking for a variable with valid number and it
    # won't crash if it receives a string.
    while True:
        try:
            dialogue_p1 = int(input('Type 1-3 to select a dialogue option: '))
            break
        except ValueError:
            print('** Use a valid integer **')

    if dialogue_p1 == 1:
        print('\n')
        print('Golden Silhouette: I gave you those runes to protect you.')

    elif dialogue_p1 == 2:
        print('\n')
        print('Golden Silhouette: Do not be silly ' + user_name + ' , you')
        print('are not dreaming and I will explain everything to you when')
        print('we get to your new home.')

    if dialogue_p1 == 3:
        print('\n')
        print('Golden Silhouette: oh dear this seems to be worse than I')
        print('thought.')

    # this is the secret option for people who do not select properly.
    else:
        print('\n')
        print('You stand there in silence...')

dialogue_ncp_1()

def dialogue_ncp_2():
    """this function is for another set of dialogue that I found easier to
    put it in as a function to edit the dialogue more freely, this function
    does welcome the user into the element selection menu"""
    print('\n')
    print('Golden Silhouette: My name is Freya the goddess of love, peace, ')
    print('and all of that jazz.')
    print('You are here because you are very special person. I chose you')
    print('because you are the only person in the world that is capable of ')
    print('stopping the great evil that would bring havoc to this world soon.')
    print('\n')
    print('Freya snapped her fingers and suddenly the surroundings change')
    print('into a desolate wasteland and a single person standing over all')
    print('the destruction.')
    print('\n')
    print('Freya: this is what will happen if you fail your mission.')
    print('\n')
    print('She snapped her fingers and once again the surroundings change')
    print('into a cozy cabin with a lit fire place, a coffee table with a')
    print('beautiful Rose encased in a shiny silver vase, a fountain that')
    print('spews water into a golden bowl that sparks in the light,')
    print('a shining gemstone on a pedestal, a crystal lamp, and a veil that')
    print('is constantly moving.')
    print('\n')
    print('Freya: What object do you like the most? Go on... Walk to the '
          'object')
    print('that interests you the most.')
    print('\n')
    print("** Each object represents the elemental affinity you will receive,")
    print('you cannot choose again, so choose wisely. **')
    print('\n')
    print('(1): The Cozy Fireplace (Fire)')
    print('(2): The Rose with the Silver Vase (Plant)')
    print('(3): The Golden Water Fountain (Water)')
    print('(4): The Shining Gemstone (Earth)')
    print('(5): The Crystal Lamp (Electric)')
    print('(6): The Flowing Veil (Air)')
dialogue_ncp_2()

# I had to make this variables in the global scope because they would be
# undefined if it was not. However, there was another solution which was
# argument passing, although I do not know how to do it in a way so that the
# file won't crash, so I resort to using global variables even though they
# are not allowed.
global element_affinity
def element_selection_menu():
    """This function's purpose is to have the user select their main element
    for the battle mechanic and to affect the appearance of their
    'signature.' """

    # the global variable also has to be inside the function to prevent
    # crashing
    global element_affinity

    while True:
        try:
            element_affinity = int(input('Type 1-6 to select element: ', ))
            break
        except ValueError:
            print('** Use a valid integer **')

    while element_affinity < 1 or element_affinity > 6:
        print('please answer again!')

        while True:
            try:
                element_affinity = int(input('Type 1-6 to select element: ', ))
                break
            except ValueError:
                print('** Use a valid integer **')

    if element_affinity == 1:
        print('\n')
        print('** You chose The Cozy Fireplace! **')
        print('\n')
        print('** You gained Fire affinity! **')
        print('\n')
        print('A book was spewed out of the fireplace!')
    elif element_affinity == 2:
        print('\n')
        print('** You chose The Rose with the Silver Vase! **')
        print('\n')
        print('** You gained Plant affinity! **')
        print('\n')
        print('The Rose transformed into a book!')
    elif element_affinity == 3:
        print('\n')
        print('** You chose The Golden Water Fountain! **')
        print('\n')
        print('** You gained Water affinity! **')
        print('\n')
        print('The Water Fountain spewed out a book!')
    elif element_affinity == 4:
        print('\n')
        print('** You chose The Shining Gemstone! **')
        print('\n')
        print('** You gained Earth affinity! **')
        print('\n')
        print('The Gemstone cracked itself open to reveal a book!')
    elif element_affinity == 5:
        print('\n')
        print('** You chose The Crystal Lamp! **')
        print('\n')
        print('** You gained Electric affinity! **')
        print('\n')
        print('The Lamp all of the sudden flashed a blinding light that')
        print('revealed book!')
    elif element_affinity == 6:
        print('\n')
        print('** You chose The Flowing Veil! **')
        print('\n')
        print('** You gained Air affinity! **')
        print('\n')
        print('The Veil twirled around and revealed a book!')
element_selection_menu()

def dialogue_ncp_3():
    """this is another function meant for dialogue, this dialogue welcomes
    the user into the stat selection menu."""
    print('\n')
    print('The book open to reveal a page with drawing of a hand')
    print('')
    print('Freya: Place your hand on the book, my dear.')
    print('\n')
    print('You put your hand on the book')
    print('\n')
    print('** Welcome to the Stat select book! Please pick your stats ranging')
    print('from 1 - 10 and the total has to equal to 31 **')
dialogue_ncp_3()

# the global variable is here for the same reason on line 174.
global user_move_set
def stat_selection_menu():
    """The function's purpose is for the user to select their stats that
    would be used for the battle mechanic later in the prologue(note: the
    battle mechanic is not in the project)"""
    # The global variable are also needed inside the function to prevent
    # crashing.
    global user_move_set

    # The user gets to choose out their stats from 1-10 and it must add up to
    # 31 the reason why the inputs are all grouped up together, instead of
    # being prompted separately is that it would be more frustrating for the
    # user not being able to see all the stats together because they have to
    # manually add them together

    while True:
        try:
            u_s_str = int(input('Strength: ', ))
            u_s_prc = int(input('Perception: ', ))
            u_s_agi = int(input('Agility: ', ))
            u_s_end = int(input('Endurance: ', ))
            u_s_lck = int(input('Luck: ', ))
            u_s_int = int(input("Intelligence: ", ))
            u_s_total = (u_s_str + u_s_prc + u_s_agi + u_s_end + u_s_lck +
                         u_s_int)
            break
        except ValueError:
            print('** Use a valid integer **')
    # scaffolding meant for debugging
    # print(u_s_total)

    # each while loop that mentions a stat variable has to be not in between
    # 1-10, caps the amount of points the user can have in their stats.
    while u_s_str >= 11 or u_s_str < 1:
        print('** Make inputs between 1-10 **')  # error message when user
        # types in a number not in between 1-10.
        while True:
            try:
                u_s_str = int(input('Strength: ', ))
                u_s_prc = int(input('Perception: ', ))
                u_s_agi = int(input('Agility: ', ))
                u_s_end = int(input('Endurance: ', ))
                u_s_lck = int(input('Luck: ', ))
                u_s_int = int(input("Intelligence: ", ))
                u_s_total = (u_s_str + u_s_prc + u_s_agi + u_s_end + u_s_lck +
                             u_s_int)
                # print(u_s_total)
                break
            except ValueError:
                print('** Use a valid integer **')

    while u_s_prc >= 11 or u_s_prc < 1:
        print('** Make inputs between 1-10 **')

        while True:
            try:
                u_s_str = int(input('Strength: ', ))
                u_s_prc = int(input('Perception: ', ))
                u_s_agi = int(input('Agility: ', ))
                u_s_end = int(input('Endurance: ', ))
                u_s_lck = int(input('Luck: ', ))
                u_s_int = int(input("Intelligence: ", ))
                u_s_total = (u_s_str + u_s_prc + u_s_agi + u_s_end + u_s_lck +
                             u_s_int)
                # print(u_s_total)
                break
            except ValueError:
                print('** Use a valid integer **')

    while u_s_agi >= 11 or u_s_agi < 1:
        print('** Make inputs between 1-10 **')

        while True:
            try:
                u_s_str = int(input('Strength: ', ))
                u_s_prc = int(input('Perception: ', ))
                u_s_agi = int(input('Agility: ', ))
                u_s_end = int(input('Endurance: ', ))
                u_s_lck = int(input('Luck: ', ))
                u_s_int = int(input("Intelligence: ", ))
                u_s_total = (u_s_str + u_s_prc + u_s_agi + u_s_end + u_s_lck +
                             u_s_int)
                # print(u_s_total)
                break
            except ValueError:
                print('** Use a valid integer **')

    while u_s_end >= 11 or u_s_end < 1:
        print('** Make inputs between 1-10 **')

        while True:
            try:
                u_s_str = int(input('Strength: ', ))
                u_s_prc = int(input('Perception: ', ))
                u_s_agi = int(input('Agility: ', ))
                u_s_end = int(input('Endurance: ', ))
                u_s_lck = int(input('Luck: ', ))
                u_s_int = int(input("Intelligence: ", ))
                u_s_total = (u_s_str + u_s_prc + u_s_agi + u_s_end + u_s_lck +
                             u_s_int)
                # print(u_s_total)
                break
            except ValueError:
                print('** Use a valid integer **')

    while u_s_lck >= 11 or u_s_lck < 1:
        print('** Make inputs between 1-10 **')

        while True:
            try:
                u_s_str = int(input('Strength: ', ))
                u_s_prc = int(input('Perception: ', ))
                u_s_agi = int(input('Agility: ', ))
                u_s_end = int(input('Endurance: ', ))
                u_s_lck = int(input('Luck: ', ))
                u_s_int = int(input("Intelligence: ", ))
                u_s_total = (u_s_str + u_s_prc + u_s_agi + u_s_end + u_s_lck +
                             u_s_int)
                # print(u_s_total)
                break
            except ValueError:
                print('** Use a valid integer **')

    while u_s_int >= 11 or u_s_int < 1:
        print('** Make inputs between 1-10 **')

        while True:
            try:
                u_s_str = int(input('Strength: ', ))
                u_s_prc = int(input('Perception: ', ))
                u_s_agi = int(input('Agility: ', ))
                u_s_end = int(input('Endurance: ', ))
                u_s_lck = int(input('Luck: ', ))
                u_s_int = int(input("Intelligence: ", ))
                u_s_total = (u_s_str + u_s_prc + u_s_agi + u_s_end + u_s_lck +
                             u_s_int)
                # print(u_s_total)
                break
            except ValueError:
                print('** Use a valid integer **')

    # this loop prevents the user from having the total amount of stat points
    # to be less than or greater than 31 for balancing reasons
    while u_s_total != 31:
        print('** Make total inputs equal to 31 **')

        while True:
            try:
                u_s_str = int(input('Strength: ', ))
                u_s_prc = int(input('Perception: ', ))
                u_s_agi = int(input('Agility: ', ))
                u_s_end = int(input('Endurance: ', ))
                u_s_lck = int(input('Luck: ', ))
                u_s_int = int(input("Intelligence: ", ))
                u_s_total = (u_s_str + u_s_prc + u_s_agi + u_s_end + u_s_lck +
                             u_s_int)
                # print(u_s_total)
                # each if statement is supposed to decide the users move set
                # and their signature's appearance based on their highest stat
                # and elemental type
                break
            except ValueError:
                print('** Use a valid integer **')

    # For some reason every time I put the rest of the stat variables in
    # parenthesis it thinks the strength stat is greatest no matter what, so I
    # just made a more direct and longer version of the if statement and this
    # version works. Although it does not look as good as the one before,
    # this one works.
    # The code for the stats before change, ex: if u_s_str > (u_s_prc and
    # u_s_agi and u_s_lck and u_s_end and u_s_int):

    if u_s_str > u_s_prc and u_s_str > u_s_agi and u_s_str > u_s_end \
            and u_s_str > u_s_lck and u_s_str > u_s_int:
        # Move sets are meant for a later continuation of the project. The
        # move set variable is meant for actual turn base  battling.
        # However, it will not be in this continuation
        user_move_set = 1
        if user_move_set == 1:  # I had to make an if statement for the
            # user_move_set variable or the variable would not work in the
            # next function
            print('\n')
            print('** You have astounding strength! **')
        print('\n')
        print('You take your hand off the book...')
        print('You hear a voice but you cannot see the person who is'
              ' speaking...')
        print('?: You bench press children for fun! I can see why Freya'
              ' chose you')
        # print(user_move_set) #scafolding

    elif u_s_prc > u_s_str and u_s_prc > u_s_agi and u_s_prc > u_s_end \
            and u_s_prc > u_s_lck and u_s_prc > u_s_int:
        user_move_set = 2
        if user_move_set == 2:
            print('\n')
            print('** You have very keen senses **')
        print('\n')
        print('You take your hand off the book...')
        print('You hear a voice inside your head...')
        print('?: You already know where I am?! I can see why Freya chose'
              ' you.')

    elif u_s_agi > u_s_str and u_s_agi > u_s_prc and u_s_agi > u_s_end \
            and u_s_agi > u_s_lck and u_s_agi > u_s_int:
        user_move_set = 3
        if user_move_set == 3:
            print('\n')
            print('** You are incredibly fast **')
        print('\n')
        print('You take your hand off the book...')
        print('You hear a voice but you cannot see the person who is'
              ' speaking...')
        print('?: I bet you can dodge a bullet! I can see why Freya chose '
              'you.')

    elif u_s_end > u_s_str and u_s_end > u_s_prc and u_s_end > u_s_agi \
            and u_s_end > u_s_lck and u_s_end > u_s_int:
        user_move_set = 4
        if user_move_set == 4:
            print('\n')
            print('** You are quite sturdy **')
        print('\n')
        print('You take your hand off the book...')
        print('You hear a voice but you cannot see the person who is'
              ' speaking...')
        print('?: Nothing can move you! I can see why Freya chose you.')

    elif u_s_lck > u_s_str and u_s_lck > u_s_prc and u_s_lck > u_s_agi \
            and u_s_lck > u_s_end and u_s_lck > u_s_int:
        user_move_set = 5
        if user_move_set == 5:
            print('\n')
            print('** You have intense luck **')
        print('\n')
        print('You hear a voice but you cannot see the person who is'
              ' speaking...')
        print('?: You can bankrupt casinos! I can see why Freya chose you.')

    elif u_s_int > u_s_str and u_s_int > u_s_prc and u_s_int > u_s_agi \
            and u_s_int > u_s_end and u_s_int > u_s_lck:
        user_move_set = 6
        if user_move_set == 6:
            print('\n')
            print('** You are quick whited **')
        print('\n')
        print('You take your hand off the book...')
        print('You hear a voice but you cannot see the person who ')
        print('is speaking... Due to your intellect you deduce the voice is ')
        print('coming from inside of you.')
        print('?: You already know where I am?! I can see why Freya chose'
              ' you.')

    # these nested while and if statements in the else statement are meant for
    # when the user has their highest stat equal to another stat. Instead of
    # forcing a move set on the user or doing anything more convoluted,
    # I decided that the user should make the decision of what their special
    # should be.
    else:
        print('')
        print('** What stat do you want to specialize in? **')
        print('(1): Strength ')
        print('(2): Perception')
        print('(3): Agility')
        print('(4): Endurance')
        print('(5): Intelligence')
        print('(6): Luck')
        print('')

        while True:
            try:
                optional_specialization = int(input('Type 1-6 to select what '
                                                    'stat-power to specialize '
                                                    'in: ', ))
                break
            except ValueError:
                print('** Use a valid integer **')

        while optional_specialization < 1 or optional_specialization > 6:
            print('** please enter again! **')

            while True:
                try:
                    optional_specialization = int(input())
                    break
                except ValueError:
                    print('** Use a valid integer **')

        # I made the if-statement for the user_move_set variable in each
        # if-statement for the optional_specialization variable
        # for debugging and the fact that I need to use the variable at
        # least once or else the next function would not recognize the
        # variable.
        if optional_specialization == 1:
            user_move_set = 1
            if user_move_set == 1:
                print('\n')
                print('** You have the power of Strength! **')
            print('\n')
            print('You take your hand off the book...')
            print('?: You bench press children for fun! I can see why Freya')
            print('chose you.')
        elif optional_specialization == 2:
            user_move_set = 2
            if user_move_set == 2:
                print('\n')
                print('** You have the power of Perception! **')
            print('\n')
            print('You take your hand off the book...')
            print('?: You might have an eagle eye! I can see why Freya chose')
            print('you.')
        elif optional_specialization == 3:
            user_move_set = 3
            if user_move_set == 3:
                print('\n')
                print('** You have the power of Agility! **')
            print('\n')
            print('You take your hand off the book...')
            print('?: I bet you can dodge a bullet! I can see why Freya')
            print('chose you.')
        elif optional_specialization == 4:
            user_move_set = 4
            if user_move_set == 4:
                print('\n')
                print('** You have the power of Endurance! **')
            print('\n')
            print('You take your hand off the book...')
            print('?: Nothing can move you! I can see why Freya chose you.')
        elif optional_specialization == 5:
            user_move_set = 6
            if user_move_set == 6:
                print('\n')
                print('** You have the power of Intelligence! **')
            print('\n')
            print('You take your hand off the book...')
            print('?: Are you a chess champion?! I can see why Freya chose')
            print('you.')
        elif optional_specialization == 6:
            user_move_set = 5
            if user_move_set == 5:
                print('\n')
                print('** You have the power of Luck! **')
            print('\n')
            print('You take your hand off the book...')
            print('?: You can bankrupt casinos! I can see why Freya chose')
            print('you.')
stat_selection_menu()

global signature_color
global signature_description
def signature_creation():
    """This function only prints dialogue for the story and gives your
    'signature' based on your choices from the element selection and stat
    selection."""

    global signature_color
    global signature_description
    global element_affinity
    if element_affinity == 1:
        signature_color = 'crimson '  # colors for the signature
        # move set_1 = ('fire ball')

    elif element_affinity == 2:
        signature_color = 'green '
        # move set_1 = ('vine wrap')

    elif element_affinity == 3:
        signature_color = 'blue '
        # move set_1 = ('water cutter')

    elif element_affinity == 4:
        signature_color = 'crystal '
        # move set_1 = ('shard spew')

    elif element_affinity == 5:
        signature_color = 'golden '
        # move set_1 = ('zip zap')

    elif element_affinity == 6:
        signature_color = 'silver '
        # move set_1 = ('air cutter')

    if user_move_set == 1:
        signature_description = 'Muscular Grizzly Bear '
        # signature_name = 'Egon'
        # move_set_special = 'Amplification'  # amplifies attacks for 5 rounds

    elif user_move_set == 2:
        signature_description = 'Miniature Griffin '
        # signature_name = 'Mordecai'
        # move_set_special = 'Surgical eye'  # higher critical chance overall

    elif user_move_set == 3:
        signature_description = 'snake with wings '
        # signature_name = 'Dio'
        # move_set_special = 'Time freeze'  # freeze time and the enemy for
        # two turns

    elif user_move_set == 4:
        signature_description = 'Tortoiseshell cat '
        # signature_name = 'Tank'
        # move_set_special = 'Negate'  # negate damage next turn or a turn
        # before

    elif user_move_set == 5:
        signature_description = ('Jack-o-lope with a cute bowler hat with four'
                                 ' leaf clover on it ')
        # signature_name = 'Baccarat'
        # move_set_special = 'Four Leaf Sight'  # higher chance to dodge and
        # better accuracy

    elif user_move_set == 6:
        signature_description = 'Satori with a monocle and a bow tie '
        # signature_name = 'Sir'
        # move_set_special = 'Battle Strategy'  # predict enemy move and
        # predict the best move to counter for to counter for one turn

    print('\n')
    print('You feel that warmth in your chest grow larger.')
    print('\n')
    print('?: Brace yourself kid, the synthesis is almost complete.')
    print('\n')
    print('All of the sudden, you became engulfed in colorful flames.')
    print('However, the flame is not burning you...')
    print('When the flames die down and your vision returns to you')
    print('A ' + signature_color + signature_description + 'is staring at')
    print('you.')
    print('\n')
    print('TO BE CONTINUED...')
    print('End of prologue Act 1.')

    # print('What do you do?')
    # print('(1): *Scream*')
    # print('(2): *punch it*')
    # print('(3): *stand calmly*')

    # These comments are meant for the next continuation for the project
    # which will lead into the second act of the prologue and hopefully a
    # battle system in place but i just wanted to end it at a cliff
    # hanger since this is obviously getting too long...

    # If you want the explanation of what a signature is, it is essentially a
    # stand from jojo meets pokemon. I always had this game idea since i was
    # a teen and if my future detective career doesnt pan out i was planning
    # on making this game as my back up plan


signature_creation()

def requirement_filler():
    """This function's purpose is to just fill out the rest of the sprint
    requirements for the project that the game cannot fill out"""
    print('\n')
    print('Running Requirement Check...')
    not_statement_1 = 1

    if not (not_statement_1 == 2):
        print('Requirement Check 1/3')

    and_statement_1 = 2
    and_statement_2 = 2

    if and_statement_1 and and_statement_2 == 2:
        print('Requirement Check 2/3')

    variable_1 = 100
    variable_2 = 23
    variable_list = [50, 100]

    if variable_1 and variable_2 not in variable_list:
        print('Requirement Check 3/3')

    print('** If you like my game, press (1), if you do not like my game')
    print('press any other number. **')

    while True:
        try:
            i_e_requirement = int(input('Please press (1) to like my '
                                        'game: '))
            break
        except ValueError:
            print('** Use a valid integer **')

    if i_e_requirement == 1:
        print('** Thank you! Have a great day! **')
    else:
        print('** You made me sad. **')
        print('Self destructing in:')
        for x in range(3, 0, -1):
            print(x)
        print('** Just kidding have a nice day! **')
requirement_filler()

def ps_message_requirement(ps_message):
    """this function's purpose is to print that I like your dog and to fill
    out the parameter requirement"""
    print(ps_message)
ps_message_requirement('** ps: I like your dog **')

print('Project Finished Date: 11', '21', '2020', sep='-')
print('Shutting Down', end='...')
