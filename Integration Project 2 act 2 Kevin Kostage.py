#Kevin Kostage
#This is the prolouge to a text adventure game
#code explanation:
#Credit to: Jario, Professor Vanselow
#this is from my previous project that I decided not to continue on do to
# the difficulty and coding block I had with adding on that project. This
# function is here so I can meet the requirment from the previous sprint.

def sprint_1_legacy():
    #This is the process of checking and doing the operations.
    print('Running Operation check...')
    #(**) it raises an integer or float to a certain power.
    # Ex: 2**3 = 8
    exponent = 2 ** 3
    #(*) multiplies an integer or float together.
    #Ex: 2 * 3 = 6
    multiply = 2 * 3
    #(/) divides an integer or float, turns integer into a float.
    #Ex: 2/3 = 0.3333333333333333333 6/3 = 2
    divide = 4 / 2
    #(//) divides an integer or float, but does not keep the remainder.
    #Ex: 19 // 10 = 1
    floor_divide = 4 // 2
    #(%) divides an integer or float, but only keeps the remainder.
    #Ex: 19 // 10 = 9
    modulus = 19 % 10
    #(+) adds integer or floats together.
    #Ex: 2 + 2
    addition = 2 + 2
    #(-) subtracts integer or floats.
    #Ex: 4 - 2 = 2
    subtraction = 4 - 2
    if exponent == 8: print("Completed 1/7")
    if multiply == 6: print("Completed 2/7")
    if divide == 2.0: print("Completed 3/7")
    if floor_divide == 2: print("Completed 4/7")
    if modulus == 9: print("Completed 5/7")
    if addition == 4: print("Completed 6/7")
    if subtraction == 2:
        print("Completed 7/7")
        print("Operation Check Completed.")
sprint_1_legacy()

print('\n')
print("Hello..." * 2)
#(string operator)(*) multiplies how many times a string is printed.
#Ex: print("hello" * 2) = "hello" "hello"
print("Hi! " + "My name is gang man " + "and...")
#(string operator)(+) adds strings together.
#Ex: "addi" + "tion" = "addition"
print('Welcome to the Prolouge of "THE ADVENTURE STARTS WITH YOU!"')
#user name will be used through out the prolouge
user_name = input("Please state your character's name: ", )

#function is meant for easy editing and tracking of my dialouge
def dialouge_ncp_1():
    #space meant to improve user readability
    print('\n')
    print('Hello', user_name + '!')
    print('\n')
    print('Prolouge Act 1:')
    print('\n')
    print('You wake up in a forest surrounded by trees and foilage.')
    print('You look around to see a pathway...')
    print('\n')
    print('You see a golden siloete of a woman at the end of the pathway.')
    print('The siloete in a calm voice beckons you to her.You follow the voice.')
    print('As you walk towards her, pink characters and symbols start appearing')
    print('around the pathway and your hands starts to hurt.You stop to look at')
    print('your hands and to your surprise the back of both of your hands have')
    print('golden hearsymbols that seems to eminate all colors imaginable. You')
    print('look up from your hands to see that the golden siloete is suddenly')
    print('in front of you.')

    print('\n')
    print('Golden Siloete: Hello' + user_name + ', it seems that you')
    print('have finally woke up from your coma. Do you remember anything?')
    print('\n')
    print('*Type (1),(2), or (3) to select the following phrases')

    print('\n')
    print('(1): "WHY DO I HAVE GOLDEN HEARTS ON MY HANDS!?!?!')
    print('(2): "If I was in a coma then why am I not in a hospital... wait am')
    print('I dreaming!?!?"')
    print('(3): "Only thing I remember is my name, nothing else."')
    #reason why it is not a while statement is that I wanted a secret option
    # in dialouge
dialouge_ncp_1()

dialouge_P1 = int(input())
if dialouge_P1 == 1:
    print('Golden Siloete: I gave you those runes to protect you.')
elif dialouge_P1 == 2:
    print('Golden Siloete: Do not be silly ' + user_name + ', you are not ')
    print('dreaming and I will explain everything to you when we get to your')
    print('new home.')
elif dialouge_P1 == 3:
    print('Golden Siloete: oh dear this seems to be worse than I thought.')
else:
    print('You stand there in silence...')

#function is meant for easy editing and tracking of my dialouge
def dialouge_ncp_2():
    print('\n')
    print('Golden Siloete: My name is Freya the goddess of love, peace, and')
    print('all of that jazz.')
    print('You are here because you are very special person. I chose you')
    print('because you are the only person in the world that is capable of ')
    print('stoping the great evil that would bring havoc to this world soon.')
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
    print('a shining gemstone on a pedastal, a crystal lamp, and a viel that')
    print('is constantly moving.')
    print('\n')
    print('Freya: What object do you like the most? Go on. Walk to the object')
    print('that interests you the most.')
    print('\n')
    print("* Each object represents the elemental affinity you will recieve,")
    print(' you cannot choose again, so choose wisely.')
    print('\n')
    print('(1): The Cozy Fireplace (Fire)')
    print('(2): The Rose with the Silver Vase (Plant)')
    print('(3): The Golden Water Fountian (Water)')
    print('(4): The Shining Gemstone (Earth)')
    print('(5): The Crystal Lamp (Electric)')
    print('(6): The Flowing Viel (Air)')
dialouge_ncp_2()

#these if statements decide what element the use will have
#the while statements are to prevent unwanted inputs
element_affinity = int(input())
while (element_affinity < 1 or element_affinity > 6):
    print('pleaser answer again!')
    element_affinity = int(input())
if element_affinity == 1:
    print('*You chose The Cozy Fireplace!*')
    print('*You gained Fire affinity!*')
    print('A book was spewed out of the fireplace!')
elif element_affinity == 2:
    print('*You chose The Rose with the Silver Vase!*')
    print('*You gained Plant affinity!*')
    print('The Rose transformed into a book!')
elif element_affinity == 3:
    print('*You chose The Golden Water Fountain!*')
    print('*You gained Water affinity!*')
    print('The Water Fountain spewed out a book!')
elif element_affinity == 4:
    print('*You chose The Shining Gemstone!*')
    print('*You gained Earth affinity!*')
    print('The Gemstone cracked itself open to reveal a book!')
elif element_affinity == 5:
    print('*You chose The Crystal Lamp!*')
    print('*You gained Electric affinity!*')
    print('The Lamp all of the sudden flashed a blinding light that revealed')
    print('book!')
elif element_affinity == 6:
    print('*You chose The Flowing Viel!*')
    print('*You gained Air affinity!*')
    print('The Viel twirlled around and revealed a book!')

def dialouge_ncp_3():
    print('\n')
    print('The book open to reveal a page with drawing of a hand')
    print('')
    print('Freya: Place your hand on the book, my dear.')
    print('\n')
    print('You put your hand on the book')
    print('*Welcome to the Stat select book! Please pick your stats ranging')
    print('from 1 - 10 and the total has to equal to 31*')
dialouge_ncp_3()

#the user gets to choose out their stats from 1-10 and it must add up to 31

u_s_s = int(input('Strength: ' , ))
u_s_p = int(input('Perception: ', ))
u_s_a = int(input('Agility: ' , ))
u_s_e = int(input('Endurance: ' , ))
u_s_l = int(input('Luck: ' , ))
u_s_i = int(input("Inteligence: " , ))
u_s_total = (u_s_s + u_s_p + u_s_a + u_s_e + u_s_l + u_s_i)
#print(u_s_total)
#scafolding meant for debugging and check to see what was wrong
#each while statement is to limit the inputs the user can make in their stats

while u_s_s >= 11 or u_s_s < 1:
    print('Make inputs less than or equal to 10')
    u_s_s = int(input('Strength: ' , ))
    u_s_p = int(input('Perception: ', ))
    u_s_a = int(input('Agility: ' , ))
    u_s_e = int(input('Endurance: ' , ))
    u_s_l = int(input('Luck: ' , ))
    u_s_i = int(input("Inteligence: " , ))
    u_s_total = (u_s_s + u_s_p + u_s_a + u_s_e + u_s_l + u_s_i)
    #print(u_s_total)

while u_s_p >= 11 or u_s_p < 1:
    print('Make inputs less than or equal to 10')
    u_s_s = int(input('Strength: ' , ))
    u_s_p = int(input('Perception: ', ))
    u_s_a = int(input('Agility: ' , ))
    u_s_e = int(input('Endurance: ' , ))
    u_s_l = int(input('Luck: ' , ))
    u_s_i = int(input("Inteligence: " , ))
    u_s_total = (u_s_s + u_s_p + u_s_a + u_s_e + u_s_l + u_s_i)
    #print(u_s_total)

while u_s_a >= 11 or u_s_a < 1:
    print('Make inputs less than or equal to 10')
    u_s_s = int(input('Strength: ' , ))
    u_s_p = int(input('Perception: ', ))
    u_s_a = int(input('Agility: ' , ))
    u_s_e = int(input('Endurance: ' , ))
    u_s_l = int(input('Luck: ' , ))
    u_s_i = int(input("Inteligence: " , ))
    u_s_total = (u_s_s + u_s_p + u_s_a + u_s_e + u_s_l + u_s_i)
    #print(u_s_total)

while u_s_e >= 11 or u_s_e < 1:
    print('Make inputs less than or equal to 10')
    u_s_s = int(input('Strength: ' , ))
    u_s_p = int(input('Perception: ', ))
    u_s_a = int(input('Agility: ' , ))
    u_s_e = int(input('Endurance: ' , ))
    u_s_l = int(input('Luck: ' , ))
    u_s_i = int(input("Inteligence: " , ))
    u_s_total = (u_s_s + u_s_p + u_s_a + u_s_e + u_s_l + u_s_i)
    #print(u_s_total)

while u_s_l >= 11 or u_s_l < 1:
    print('Make inputs less than or equal to 10')
    u_s_s = int(input('Strength: ' , ))
    u_s_p = int(input('Perception: ', ))
    u_s_a = int(input('Agility: ' , ))
    u_s_e = int(input('Endurance: ' , ))
    u_s_l = int(input('Luck: ' , ))
    u_s_i = int(input("Inteligence: " , ))
    u_s_total = (u_s_s + u_s_p + u_s_a + u_s_e + u_s_l + u_s_i)
    #print(u_s_total)

while u_s_i >= 11 or u_s_i < 1:
    print('Make inputs less than or equal to 10')
    u_s_s = int(input('Strength: ' , ))
    u_s_p = int(input('Perception: ', ))
    u_s_a = int(input('Agility: ' , ))
    u_s_e = int(input('Endurance: ' , ))
    u_s_l = int(input('Luck: ' , ))
    u_s_i = int(input("Inteligence: " , ))
    u_s_total = (u_s_s + u_s_p + u_s_a + u_s_e + u_s_l + u_s_i)
    #print(u_s_total)

while u_s_total != 31:
    print('Make total inputs equal to 31')
    u_s_s = int(input('Strength: ' , ))
    u_s_p = int(input('Perception: ', ))
    u_s_a = int(input('Agility: ' , ))
    u_s_e = int(input('Endurance: ' , ))
    u_s_l = int(input('Luck: ' , ))
    u_s_i = int(input("Inteligence: " , ))
    u_s_total = (u_s_s + u_s_p + u_s_a + u_s_e + u_s_l + u_s_i)
    #print(u_s_total)
#each if statement is supposed to decide the user's moveset and signature based
#on their highest stat and elemental type

if u_s_s > (u_s_p or u_s_a or u_s_e or u_s_l or u_s_i):
    user_moveset = 1
    print('*You have austounding stregth!*')
    print('\n')
    print('You take your hand off the book...')
    print('You hear a voice but you cannot see the person who is speaking...')
    print('?: You benchpress children for fun! I can see why Freya chose you.')
    #print(user_moveset) #scafolding

elif u_s_p > (u_s_s or u_s_a or u_s_e or u_s_l or u_s_i):
    user_moveset = 2
    print('*You have very keen senses*')
    print('\n')
    print('You take your hand off the book...')
    print('You hear a voice inside your head...')
    print('?: You already know where I am?! I can see why Freya chose you.')

elif u_s_a > (u_s_s or u_s_p or u_s_e or u_s_l or u_s_i):
    user_moveset = 3
    print('*You are incredibly fast*')
    print('\n')
    print('You take your hand off the book...')
    print('You hear a voice but you cannot see the person who is speaking...')
    print('?: I bet you can dodge a bullet! I can see why Freya chose you.')

elif u_s_e > (u_s_s or u_s_p or u_s_a or u_s_l or u_s_i):
    user_moveset = 4
    print('*You are quite sturdy*')
    print('\n')
    print('You take your hand off the book...')
    print('You hear a voice but you cannot see the person who is speaking...')
    print('?: Nothing can move you! I can see why Freya chose you.')

elif u_s_l > (u_s_s or u_s_p or u_s_a or u_s_e or u_s_i):
    user_moveset = 5
    print('*You have intense luck*')
    print('\n')
    print('You hear a voice but you cannot see the person who is speaking...')
    print('?: You can bankrupt casinos! I can see why Freya chose you.')


elif u_s_i > (u_s_s or u_s_p or u_s_a or u_s_e or u_s_l):
    user_moveset = 6
    print('*You are quick whitted*')
    print('\n')
    print('You take your hand off the book...')
    print('You hear a voice but you cannot see the person who is speaking...')
    print('Due to your intelect you deduce the voice is comming from inside')
    print('of you.')
    print('?: You already know where I am?! I can see why Freya chose you.')

# these nested while and if statements in the else statement are meant for
# when the user has their highest stat equal to another stat. Instead of
# forcing a moveset or doing anything more convuluted, I decided that
# the user should make the decision of what their special should be.

else:
    print('*What stat do you want to specialize in?*')
    print('(1): Strength ')
    print('(2): Perception')
    print('(3): Agility')
    print('(4): Endurance')
    print('(5): Inteligent')
    print('(6): Luck')
    optional_specialization = int(input())

    while (optional_specialization < 1 or optional_specialization > 6):
        print('pleaser answer again!')
        optional_specialization = int(input())

    if optional_specialization == 1:
        user_moveset = 1
        print('*You have the power of Stregth!*')
        print('\n')
        print('You take your hand off the book...')
        print('?: You benchpress children for fun! I can see why Freya')
        print('chose you.')
        print(user_moveset)
    elif optional_specialization == 2:
        user_moveset = 2
        print('*You have the power of Perception!*')
        print('\n')
        print('You take your hand off the book...')
        print('?: You might have an eagle eye! I can see why Freya chose')
        print('you.')

    elif optional_specialization == 3:
        user_moveset = 3
        print('*You have the power of Agility!*')
        print('\n')
        print('You take your hand off the book...')
        print('?: I bet you can dodge a bullet! I can see why Freya')
        print('chose you.')

    elif optional_specialization == 4:
        user_moveset = 4
        print('*You have the power of Endurance!*')
        print('\n')
        print('You take your hand off the book...')
        print('?: Nothing can move you! I can see why Freya chose you.')

    elif optional_specialization == 5:
        user_moveset = 6
        print('*You have the power of Inteligence!*')
        print('\n')
        print('You take your hand off the book...')
        print('?: Are you a chess champion?! I can see why Freya chose')
        print('you.')
    elif optional_specialization == 6:
        user_moveset = 5
        print('*You have the power of Luck!*')
        print('\n')
        print('You take your hand off the book...')
        print('?: You can bankrupt casinos! I can see why Freya chose')
        print('you.')

#colors for the signature
#movesets are meant for a later continuation of the project
#the move set variable is meant for actual turn base battling however
#it will not be in this continuation

if element_affinity == 1:
    signature_color = ('red ')
    #moveset_1 = ('fire ball')

elif element_affinity == 2:
    signature_color = ('green ')
    #moveset_1 = ('vine wrap')

elif element_affinity == 3:
    signature_color = ('blue ')
    #moveset_1 = ('water cutter')

elif element_affinity == 4:
    signature_color = ('crystal ')
    #moveset_1 = ('shard spew')

elif element_affinity == 5:
    signature_color = ('yellow ')
    #moveset_1 = ('zip zap')

elif element_affinity == 6:
    signature_color = ('white ')
    #moveset_1 = ('air cutter')

if user_moveset == 1:
    signature_description = ('Muscular Grizzly Bear')
    signature_name = ('Egon')
    moveset_special = ('Amplification') # amplifies attacks

elif user_moveset == 2:
    signature_description = ('Miniature Griffin')
    signature_name = ('Mordecai')
    moveset_special = ('Surgical eye') # higher crit chance

elif user_moveset == 3:
    signature_description = ('Mamba with wings')
    signature_name = ('Dio')
    moveset_special = ('Time freeze') # freeze time for one turn

elif user_moveset == 4:
    signature_description = ('Tortoiseshell cat ')
    signature_name = ('Tank')
    moveset_special = ('Negate') # negate damage next turn or turn before

elif user_moveset == 5:
    signature_description = ('Jackolope with a cute bowlerhat with four leaf clover on it')
    signature_name = ('Baccarat')
    moveset_special = ('Four Leaf Sight') # more lickely to dodge and better
    #acuracy

elif user_moveset == 6:
    signature_description = ('Satori with a monocle and a bowtie ')
    signature_name = ('Sir')
    moveset_special = ('Battle Strategy') # predict enemy move and best move
    # to counter for one turn

def dialouge_ncp_4():
    print('\n')
    print('You feel that warmth in your chest grow larger.')
    print('\n')
    print('?: Brace yourself kid, the synthesis is almost complete.')
    print('\n')
    print('All of the sudden, you became engulfed in colorful flames.')
    print('However, the flame is not burning you...')
    print('When the flames die down and your vision returns to you')
    print('A ' + signature_color + signature_description + ' is staring at')
    print('you.')
    print('\n')
    print('TO BE CONTINUED...')
    print('End of prolouge Act 1.')
    #these comments are meant for the next continuation for the project
    # which will lead into the second act of the prolouge and hopefully a
    # battle system in place but i just wanted to end it at a cliff
    # hanger since this is obviously geting too long...
    #If you want the explanation of what a signature is, it is esentially a
    # stand from jojo meets pokemon. I always had this game idea since i was
    # a teen and if my future detective career doesnt pan out i was
    # planning on making this game as my back up plan.
    #print('What do you do?')
    #print('(1): *Scream*')
    #print('(2): *punch it*')
    #print('(3): *stand calmly*')
dialouge_ncp_4()
# these are the oporators and conditions that couldnt fit into my game so I
# hade to make a function that had the rest of the required oporators and
# condtions and I made an extra function with a parameter to meet the
# requirement.
def requrirements_proj():
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
    if (variable_1 and variable_2 not in variable_list):
        print('Requirement Check 3/3')

    print('If you like my game, press (1), if you do not like my game press')
    print('any other number.')
    if_else_requirement = int(input())
    if if_else_requirement == 1:
        print('Thank you! Have a great day!')
    else:
        print('You made me sad.')
        print('Self destructing in:')
        for x in range(3,0,-1):
            print(x)
        print('Just kidding have a nice day!')
requrirements_proj()


def ps_message_requirement(ps_message):
    print(ps_message)
ps_message_requirement('ps: I liek ur dog')

print('Project Finished Date: 10', '24', '2020', sep = '-')
print('Shutting Down', end = '...')
