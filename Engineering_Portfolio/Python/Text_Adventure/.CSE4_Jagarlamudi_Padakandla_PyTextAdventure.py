# -*- coding: utf-8 -*-
from __future__ import print_function
from random import randint

#Variables Used in the Future
help = [0]
dark_a = [0]
proceed = [0]
checkpts = [0]


#General Story Functions
def vict():
    '''Victory function after winning'''
    print("Congratulations!")
    print("You won!")

def end():
    '''Game over after bad choice occurence'''
    print('Game Over.')

def miss(x):
    '''Death function from missing an attack.'''
    print('Your', x, 'attack missed. You became vulnerable and were killed.')
    end()
    
def chance(x):
    '''Chance of something happening function.'''
    chance = randint(1, 3)
    if chance == 1 or chance == 2:
        proceed[0] = 1
        print("Your", x, "attack was successful. Proceed ahead.")
    else:
        miss(x)



#Fairy Tale Story Code  
def dragon_fight3():
    '''Dragon code: dodge left or right to avoid falling dragon'''
    print()
    print("The dragon seems to be falling to the right of you, but there is a heavy wind pushing it towards your left side.")
    drag_fight3 = raw_input("Do you dodge to the 'left' or 'right'?: ")    
    if drag_fight3 == 'left':
        if checkpts[0] == 1:
            print("Checkpoint.")
            dragon_fight1()
        else:
            print("You chose to dodge to the left.")
            print("The wind blew the dragon to the left and the dragon fell on you.")     
            end()
    elif drag_fight3 == 'right':
        print("You decided that dodging to the right would the proper decision.")
        print("You dodged the dragon and have won the fight.")
        print("You run up to the princess and rescue her from the tower.")
        print("You take the princess back to the castle and return her to the king.")
        print("The king and the princess are both happy and the princess falls in love with you.")
        print("You get married to the princess and become the next king.")
        print("You lead a happy life and continue to protect your princess from any threats that appear before you.")
        vict()
    else:
        if checkpts[0] == 1:
            print("Checkpoint.")
            dragon_fight1()
        else:
            print("Not a valid answer.")
            end() 
      
def dragon_fight2():
    '''dragon code: spear or sword attack'''
    print()
    drag_fight2 = raw_input("Do you want to throw a 'spear' at the dragon or go closer and attack with a 'sword'?: ")
    if drag_fight2 == 'spear':
        print("You throw the spear at the dragon and it hits it.")
        print("The dragon died and is now falling.")
        dragon_fight3()
    elif drag_fight2 == 'sword':
        if checkpts[0] == 1:
            print("Checkpoint.")
            dragon_fight1()
        else:
            print("You ran in too close and the dragon ate you.")
            print("Try staying further back next time.")
            end()
    else:
        if checkpts[0] == 1:
            print("Checkpoint.")
            dragon_fight1()
        else:
            print("Not a valid answer.")
            end() 
    

def dragon_fight1():
    '''dragon code: run or fight the dragon choice'''
    print()
    print("You reach the top of the tower and come across the fierce dragon.")
    drag_art = """
                  /          /   
                /' .,,,,  ./         
               /';'     ,/    
              / /   ,,//,`'`      
             ( ,, '_,  ,,,' ``   
             |    /@  ,,, ;" `  
            /    .   ,''/' `,``   
           /   .     ./, `,, ` ; 
        ,./  .   ,-,',` ,,/''\,'   
       |   /; ./,,'`,,'' |   |     
       |     /   ','    /    |  
        \___/'   '     |     |  
          `,,'  |      /     `\  
               /      |        ~\  
              '       (
             :
            ; .         \-- 
          :   \         ; 
          """ 
    print(drag_art)
    drag_fight1 = raw_input("Do you want to 'fight' the dragon or 'run' from the dragon?: ")
    if drag_fight1 == 'run':
        if checkpts[0] == 1:
            print("Checkpoint.")
            tower()
        else:
            print("You are too slow and the dragon eats you while you run away.")
            end()
    elif drag_fight1 == 'fight':
        print("You decided to fight the dragon.")
        print("The final battle is about to begin.")
        dragon_fight2()
    else:
        if checkpts[0] == 1:
            print("Checkpoint.")
            tower()
        else:
            print("Not a valid answer.")
            end() 
    
def tower():
    '''tower scene code: how to reach the top of the tower'''
    print()
    print("You arrive at the dragon's tower.")
    tower = raw_input("Do you want to climb the 'side' of the tower or climb the 'stairs'?: ")
    if tower == 'side':
        if checkpts[0] == 1:
            print("Checkpoint.")
            left_right()
        else: 
            print("You decided to climb the side of the tower.")
            print("You slip off the side of the tower and die.")
            end()
    elif tower == 'stairs':
        print("You climb the stairs and safely reach the top of the tower.")
        dragon_fight1()
    else:
        if checkpts[0] == 1:
            print("Checkpoint.")
            left_right()
        else:
            print("Not a valid answer.")
            end() 
        

def left_path():
    '''code for the left path: river/bridge'''
    print()
    print("You come across a river and an old wooden bridge.")
    leftpath_choice = raw_input("Do you want to swim across the 'river' or cross the 'bridge'?: ")
    if leftpath_choice == 'river':
        print('You chose to swim across the river.')
        print('You sucessfully swim across the river.')
        tower()
    elif leftpath_choice =='bridge':
          if checkpts[0] == 1:
                print("Checkpoint.")
                left_right()
          else: 
                print('You chose to cross the bridge.')
                print('The bridge breaks as you try to cross it and you die.')
                end() 
    else:
       if checkpts[0] == 1:
            print("Checkpoint.")
            left_right()
       else:
            print("Not a valid answer.")
            end() 
    
def right_path():
    '''code for the right path: rapids/bird'''
    print()
    print("You come across some rapids and a giant bird.")
    rightpath_choice = raw_input("Do you jump across the 'rapids' or do you fly across the rapids on a 'bird'?: ")
    if rightpath_choice == 'rapids':
        if checkpts[0] == 1:
            print("Checkpoint.")
            left_right()
        else:
            print('You decided to jump across the rapids.')
            print('You get wiped out to sea and die.')
            end()    
    elif rightpath_choice == 'bird':
        print('You chose to fly across the rapids on a giant bird.')
        print('You successfully fly over the rapids.')
        tower()
    else:
        if checkpts[0] == 1:
            print("Checkpoint.")
            left_right()
        else:
            print("Not a valid answer.")
            end() 
    
def left_right():
    '''chooses the left or right path'''
    print()
    print("You go on your journey and find a two way split in your path.")
    path = raw_input("Do you want to go 'left' or 'right'?: ")
    if path == 'left':
        print('You went left.')
        left_path()
    elif path == 'right':
        print('You went right.')
        right_path()
    else:
        if checkpts[0] == 1:
            print("Checkpoint.")
            initiate_fairy_tale()
        else:
            print("Not a valid answer.")
            end() 
        
def initiate_fairy_tale():
    '''fairy tale story start'''
    print()
    print('The king has summoned you to his castle to save his daughter from the evil dragon.')
    left_right()


#Dark Story Code
def dark_finale():
    '''final code for the dark story: return to castle'''
    print("You and LEGO®las return to the kingdom, but you face many more opponents than you did on the way to the tree grove.")
    print("With LEGO®las at your side, you effortlessly weave through the hoardes of opponents and reach the castle.")
    print("When you reach the castle and tell the king about what happened, the king gets furious that his daughter was not saved.")
    print("He decides to execute you but LEGO®las tries to protect you to no avail.")
    print("You look down at the ground and a wide smile forms on your face.")
    kobk = raw_input("Do you let yourself 'die' or do you 'kill' LEGO®las?: ")
    if kobk == 'die':
        print("(From the options we gave you) You chose to be a nice friend and sacrifice yourself for LEGO®las.")
        print("You decide your last friend is the guillotine.")
        print("Congratulations!")
        print("You got the bad ending.")
    elif kobk == 'kill':
        print("Calmly and quickly, you brandish your blade and swipe at LEGO®las, his body falling to the floor, dead.")
        print("Almost immediately, the room you are in is shrouded in a united gasp of surprise and confusion.")
        print("Taking advantage of the confusion, you also cut down the king and queen.")
        print("Some of the royal guard takes action and charges at you, but you easily show them the face of death.")
        print("Using your words, you calm the royal guard and take control of the army.")
        print("Over the next 2 years, you control the kingdom and fix the problems in order to gain the trust of the citizens.")
        print("You smile like the day you killed LEGO®las and realize you have secured a role as tyrant of the kingdom.")
        print("Congratulations!")
        print("You got the good ending.")
        victory_art = """  
                <( .)>
                 //'
                //                |||
             __//_   _,,,,,    \_///|
            /___\\  (.  __\_   \_,_/
           / Q--\'  |_o \:::)  / |
          /.(|_______)\___/___/-.|
          |  / /' \ _  ~ \_  /  /
          .---/__   ""\_/""_/--'
                /\......./
               (_/_ _,,_/
                ;;;;[X];__
               /# . ._) . )-----.
              /. . . .\. /   , __>
       ((     | . . . .\|__-( __/
               \ . . . .\   |__/
                ) .--., )  >Xxx
                //  _>)/    / X|
               (/  __/     O  X|
                / __/       \ X|
                |__/         `._\  ))
                Xxx<
                / X|
               O  X|
                \ X|
                 `.|
                """
        print(victory_art)
    else:
        if checkpts[0] == 1:
            print("Checkpoint.")
            dark_finale()
        else:
            print("Ooh. So close. Your final decision was not a valid answer.")
            end()

def necro3():
    '''final battle sequence part 2'''
    print()
    print("Now that you have landed a hit on Aurelia, she seems angry.")
    print("A sword attack would finish her if the attack made contact but it is very risky.")
    print("You could also run for your life.")
    atk_type2 = raw_input("Do you try to swipe with your 'sword' or 'run' for your life?: ")
    if atk_type2 == 'sword':
        if checkpts[0] == 1:
            print("Checkpoint.")
            necro1()
        else:
            print("The princess dodged the sword attack and killed you.")
            end()
    elif atk_type2 == 'run':
        print("As you run away, the princess closes in on you and you are about to be killed.")
        print("Out of the trees, an arrow comes flying in and kills the princess, saving your life.")
        print("You can't believe it. You were saved by the legendary hunter, LEGO®las.")
        print("LEGO®las helps you up and you have a conversation about your adventures, slowly becoming friends.")
        dark_finale()
    else:
        if checkpts[0] == 1:
            print("Checkpoint.")
            necro1()
        else:
            print("Not a valid answer.")
            end() 

def necro2():
    '''final battle sequence part 1'''
    print("You realize this is the final battle and you have no choice but to fight Princess Aurelia. It's kill or be killed.")
    choice_atk = raw_input("Do you blindly 'rush' in to attack or 'strategize' first?: ")
    if choice_atk == 'rush':
        if checkpts[0] == 1:
            print("Checkpoint.")
            necro1()
        else:
            print("You rushed too fast and tripped on a twig.")
            print("The princess ate you before you could get up. Disappointment to your family.")
            end()
    elif choice_atk == 'strategize':
        print("It seems like the princess is very fast so dodging isn't very safe.")
        print("It also appears the attempting a stab attack is viable but it poses risks of failure.")
        print("A long ranged attack seems like the safest bet.")
        atk_type1 = raw_input("Do you 'dodge', 'stab', or shoot an 'arrow' at the princess?: ")
        if atk_type1 == 'dodge':
            if checkpts[0] == 1:
                print("Checkpoint.")
                necro1()
            else:
                print("You weren't fast enough and the princess caught up to you.")
                end()
        elif atk_type1 == 'stab':
            chance('stab')
            if proceed[0] == 1:
                proceed[0] = 0
                necro3()
        elif atk_type1 == 'arrow':
            print("The bow attack was successful.")
            necro3()
        else:
           if checkpts[0] == 1:
                print("Checkpoint.")
                necro1()
           else:
                print("Not a valid answer.")
                end() 
    else:
       if checkpts[0] == 1:
            print("Checkpoint.")
            necro1()
       else:
            print("Not a valid answer.")
            end() 
def necro1():
    '''the final battle indroduction and ally killing'''
    print()
    print("As you leave the cemetery, you spot a tree grove with an ominous glow escaping through the leaves.")
    print("Thinking it may be a clue to finding the necromancer, you head into the tree grove.")
    print("When you arrive at the  grove, you see Carnax dead and what appears to be a zombie Aurelia.")
    print("The princess looks at you and charges.")
    if help[0] == 1:
        print("The princess jumps past you and kills your ally.")
        necro2()
    else:
        print("The princess goes in front of you and stops.")
        necro2()

def cemetery():
    '''skeletal knight fight with battle sequence'''
    print()
    print("You bypass the split in the road and you see that it all converged into one path again.")
    print("As you continue walking on this path, you find an old cemetery.")
    print("Here you are confronted by a skeletal knight whom you recgonize.")
    print("This knight is Sir Reginald, the knight who taught you strategy and combat skills.")
    print("You remember the lesson he taught you about striking your opponent from the side.")
    print("You also remember that he taught you how to sucessfully defend from those attacks.")
    if dark_a[0] == 1:
        print("You realize that contemplating what to do is a waste of time.")
        print("The mage uses an invisibility potion and you quietly walk past the knight, evading the battle.")
        necro1()
    else:
        atk_direc1 = raw_input("Do you want to attack from the 'side' or attack 'straight' on?: ")
        if atk_direc1 == 'side':
            if checkpts[0] == 1:
                print("Checkpoint.")
                pathways()
            else:
                print("Sir Reginald expected your attack and countered it. You didn't react fast enough and died.")
                end()
        elif atk_direc1 == 'straight':
            print("You chose to attack from straight on and landed a successful hit on Sir Reginald.")
            if dark_a[0] == 2:
                print("The blacksmith followed up your attack and turned the skeletal knight into bone dust.")
                necro1()
            else:
                print("Your attack stunned the knight and you now have a chance to follow up your attack.")
                print("You don't think the same thing will work twice so you contemplate how to attack this time.")
                atk_direc2 = raw_input("Do you follow up with a 'side' attack or attack 'straight' on?: ")
                if atk_direc2 == 'straight':
                    if checkpts[0] == 1:
                        print("Checkpoint.")
                        pathways()
                    else:
                        print("You were right. The same attack wouldn't work twice.")
                        print("You missed your attack and the knight killed you while you were in your lunge.")
                        end()
                elif atk_direc2 == 'side':
                    print("The knight didn't expect a side attack this time and you successfully hit him, reducing him to bone dust.")
                    necro1()
                else:
                    if checkpts[0] == 1:
                        print("Checkpoint.")
                        pathways()
                    else:
                        print("Not a valid answer.")
                        end() 
        else:
            if checkpts[0] == 1:
                print("Checkpoint.")
                pathways()
            else:
                print("Not a valid answer.")
                end() 
    
def pathways():
    '''Pathway choice 1, 2, or 3: with pathway occurences and decisions''' 
    print()
    print("The first obstacle you come across in your journey us a three way split in your path.")
    print("The first path is a muddy road.")
    print("The second path is an old wooden bridge.")
    print("The third path is blocked by a baby dragon.")   
    path_choice = raw_input("Do you want to pick path '1', '2', or '3'?: ")
    if path_choice == '1':
        print("As you are walking in the muddy path, you fall into quicksand." )
        if dark_a[0] == 1:
            print("The mage uses a potion to help you escape from the quicksand.")
            cemetery()
        else:
            if checkpts[0] == 1:
                    print("Checkpoint.")
                    dark_ally()
            else:
                print("You sink in the quicksand and die.")
                end()
    elif path_choice == '2':
        print("As you are walking on the bridge, the bridge breaks and you are hanging off of the edge.")
        if help[0] == 1:
            print("You can only get up on your own, but you don't want to drop your friend.")
            friend_drop = raw_input("Do you want to 'drop' your friend or 'hold' onto your friend?: ")
            if friend_drop == 'hold':
                if checkpts[0] == 1:
                    print("Checkpoint.")
                    dark_ally()
                else:
                    print("You held onto your friend, but because you both were too heavy, you both fell.")
                    end()
            elif friend_drop == 'drop':
                print("You let go of your friend go and get up onto the ledge alone.")
                cemetery()
            else:
                if checkpts[0] == 1:
                    print("Checkpoint.")
                    dark_ally()
                else:
                    print("Not a valid answer.")
                    end() 
        else:
            print("You climb back up onto the ledge thinking that the falling bridge was a very close call.")
    elif path_choice == '3':
        print("You decide to fight the baby dinosaur blocking your path.")
        if dark_a[0] == 2:
            print("With the blacksmith at your side, you flawlessly defeat the baby dinosaur in front of you.")
            cemetery()
        else:
            print("As you confront the dinosaur, you realize that you only have one chance to attack before the dinosaur eats you.")
            atk_type = raw_input("Do you attack with your 'sword' or with your 'spear'?: ")
            if atk_type == 'sword':
                chance('sword')
                if proceed[0] == 1:
                    proceed[0] = 0
                    cemetery()
            elif atk_type == 'spear':
                chance('spear')
                if proceed[0] == 1:
                    proceed[0] = 0
                    cemetery()
            else:
                if checkpts[0] == 1:
                    print("Checkpoint.")
                    dark_ally()
                else:
                    print("Not a valid answer.")
                    end() 
    else:
        if checkpts[0] == 1:
            print("Checkpoint.")
            dark_ally()
        else:
            print("Not a valid answer.")
            end() 

def dark_ally():
    '''ally choice (blacksmith / mage) or no ally'''
    print()
    assist = raw_input("Do you want to go on the quest 'alone' or get an 'ally' in the town?: ")
    if assist == 'alone':
        print("You decided to go on your journey alone.")
        pathways()
    elif assist == 'ally':
        help[0] = 1
        d_ally = raw_input("Do you want the 'blacksmith' or 'mage' aid to assist you on your journey?: ")
        if d_ally == 'mage':
            dark_a[0] = 1
            print("You chose the mage.")
            pathways()
        elif d_ally == 'blacksmith':
            dark_a[0] = 2
            print("You chose the blacksmith.")
            pathways()
        else:
            if checkpts[0] == 1:
                print("Checkpoint.")
                dark_ally()
            else:
                print("Not a valid answer.")
                end() 
    else:
        print("Not a valid answer.")
        end()

def initiate_dark_story():
    '''dark story code start'''
    print()
    print("You are the former knight of the kingdom of Kellain.")
    print("You were banished from the kingdom for being falsely accused for the murder of a fellow knight.")
    print("The king summons you back to the kingdom for a dangerous task with the reward of reentry into the kingdom.")
    print("The king says: 'The dark necromancer, Carnax, has decided to attack the kingdom and has kidnapped my daughter, Aurelia.'")
    print("'I have sent countless knights to go rescue her, but they have all either died or simply disappeared.'")
    print("'If you return with my beloved princess, I will repeal your banishment and allow you back into the royal army.'")
    print("With this information in mind, you set out on your perilous journey with an exorbitant desire to return to the kingdom and your family within it.")
    dark_ally() 
    
def start():
    '''start function: make with an open parentheses'''
    print('Answer the questions you get with correctly spelled answers.')
    print('The valid answers will be in single quotes.')
    savepts = raw_input("This is a 'yes' or 'no' question. Would you like to activate checkpoints?: ")
    if savepts == 'yes':
        checkpts[0] = 1    
        story = raw_input("Would you like the 'fairy' tale or the 'dark' story? ")
        if story == 'fairy':
            print()
            print("You chose the fairy tale.")
            print("Let's begin.")
            initiate_fairy_tale()
        
        elif story == 'dark':
            print()
            print("You chose the dark story.")
            print("Let's begin.")
            initiate_dark_story()
        
        else: 
            print('Not a valid answer.')
            end()
    elif savepts == 'no':
        checkpts[0] = 0
        story = raw_input("Would you like the 'fairy' tale or the 'dark' story? ")
        if story == 'fairy':
            print()
            print("You chose the fairy tale.")
            print("Let's begin.")
            initiate_fairy_tale()
        
        elif story == 'dark':
            print()
            print("You chose the dark story.")
            print("Let's begin.")
            initiate_dark_story()
        
        else: 
            print('Not a valid answer.')
            end()
    else:
        print("Not a valid answer.")
        end()
