import time
import random

colors = ["pink", "black", "white", "red", "green"]
animals = ["bear", "giant goat", "wolf", "snake"]
high_score = []
counter = 0
i = 0
choice_number = ""

# Pause execution, print a message, and wait for a brief moment.
def pause(paused_words):
    time.sleep(0.2)
    print(paused_words)
    time.sleep(0.2)

# Display the number of coins found and return the count.
def player_score(number_of_coins):
    pause(f"You found {number_of_coins} coins.")
    return number_of_coins

# Prompt the player to try again and handle their choice.
def try_again():
    global i
    invalid_input = True
    while invalid_input:
        choice = input("Try again (yes/no): ")
        if choice.lower() == "yes":
            invalid_input = False
        elif choice.lower() == "no":
            i += 1
            invalid_input = False
        else:
            invalid_input = True

# Announce the win, update the high score, and prompt to try again.
def win():
    global counter
    global high_score
    pause("The rain stopped.")
    pause("You returned to your home.")
    pause(f"You win!! Your score is {counter} coins.")
    high_score.append(counter)
    try_again()

# Provide choices to the player and return their selection.
def the_choice(choice_one, choice_two):
    repeater = True
    while repeater:
        pause(f"(Press 1 to choose {choice_one})")
        pause(f"(Press 2 to choose {choice_two})")
        choice_number = input()
        if choice_number in ["1", "2"]:
            repeater = False
            return choice_number
        else:
            repeater = True

# Handle the lose scenario and prompt the player to try again.
def lose():
    pause("You died.")
    pause(f"You lose. Your score is {counter} coins.")
    try_again()

# Describe the first time the player chooses the Fire Lord spell.
def fire_lord1(target):
    pause("You choose the fire lord spell and start to say the words:")
    pause("From the darkest place in the world, I summon the Fire Lord.")
    pause("Come forth and light everything, burning all the feeble souls!")
    pause("After saying those words, smoke started to come from different places")
    pause("It gathered at one point then a knight made of fire came out of that smoke")
    pause(f"Running to the {target}")
    pause(f"The knight put his sword in the throat of {target}")
    pause("Made it burn till death")

# Describe the second time the player chooses the Fire Lord spell.
def fire_lord2(target):
    pause("You said the words of the spell")
    pause("That time the knight was running burning everything in his way")
    pause("The flames of the knight were black at that time")
    pause(f"The {target} starts to burn till it changes to ash")

# Alternate version of Fire Lord but leads to the death of player 
def fire_lord3(the_killed_character, place):
    pause("You said the words of the spell")
    pause(f"You didn't see the knight but the {the_killed_character}'s throat was cut")
    pause(f"The whole {the_killed_character} starts to burn")
    pause(f"You saw a blue light come from outside the {place}")
    pause("You went outside and found blue flames everywhere.")
    pause("The knight was standing in front of you, staring at you.")
    pause("Finally, he burnt you to feel the same as the other souls.")

# Describe the first time the player chooses the Spirit Snatcher spell.
def spirit_snatcher1(target, place, voice):
    pause("You start to say the spelled words:")
    pause("'From the shadows I call, with darkness as my guide.")
    pause("I summon the lost spirits, their whispers near.")
    pause("With a flick of my hand, I snatch what is thine,")
    pause("binding your essence to my will. By the power of night,")
    pause("let the spirits come forth!'")
    pause("After saying those words, a white tall man appeared")
    pause("He wasn't wearing anything except wide trousers-style fabric")
    pause(f"He started to walk toward the {target} but he disappeared")
    pause(f"Then shows up {place}")
    pause(f"Whispering in his ear then the soul of the {target} comes out through him")
    pause(f"A {target} tattoo appears on his body.")
    pause("He comes then towards you walking, he goes through your body")
    pause(f"The tattoo drawn on your body and voice of {voice} started in your ear")
    pause("Then saw the man look at you he pointed at you")
    pause("Moved his hand telling you that you are the next.")

# Alternate version of Spirit Snatcher but leads to the death of player 
def spirit_snatcher2(target, voice):
    pause("After saying spell words, a white tall man appeared")
    pause(f"He started to whisper in {target}'s ear then his soul came out of him")
    pause(f"A tattoo of {target} appeared on his body")
    pause("He comes then towards you walking, then he goes through your body")
    pause("The tattoo drawn on your body")
    pause(f"Sound of {voice} screaming in your ear")
    pause("Then the man looks at you and then disappears.")
    pause("You hear the sound of whispering in your ear")
    pause("'Your soul shall drift... forever in the haunting echoes of the abyss.'")

# Describe the Midnight Pilfer spell's effect on the stolen object and your object.
def midnight_pilfer(stolen_object, your_object):
    pause("You start to say the spelled words:")
    pause("'From the shadows I call, with darkness as my guide.")
    pause("I summon the lost spirits, their whispers near.")
    pause("With a flick of my hand, I snatch what is thine,")
    pause("binding your essence to my will. By the power of night,")
    pause("let the spirits come forth!'")
    pause("After saying those words, a dark creature comes out of the book")
    pause("It disappears for a second")
    pause(f"Then the creature appeared in front of you with a {stolen_object}")
    pause("He threw it to your feet")
    pause(f"And your {your_object} was in his hand.")

# Alternate version of Midnight Pilfer but leads to the death of player 
def midnight_pilfer2(stolen_object, your_object):
    pause("After saying spell words, a dark creature comes out of the book")
    pause("It disappears for a second")
    pause(f"Then the creature appeared in front of you with a {stolen_object}")
    pause("He threw it to your feet")
    pause(f"And your {your_object} was in his hand.")


while i < 1:

        if high_score != []:
            print(f"Highest score: {int(max(high_score))}")

        pause("while you were walking through the woods when") 
        pause("the sky started to rain.")
        pause("you found a little hut and a cave that could protect you from the rain.")
        choice_number = the_choice("the cave","the hut")

        if (choice_number == "1"):
            pause(f"You entered the cave, but you found a {random.choice(animals)}")
            pause("which attacked and killed you.")
            try_again()
            
        elif(choice_number == "2"):
            pause("You got into the hut and found an old man.")
            pause("You asked him to stay until the rain stopped")
            pause("but he told you that if you wanted to stay")
            pause("you had to play a game with him.")
            pause("the old man choose a card form bunch of cards.")
            pause("he flipped the card which had a wizard image.")
            pause("he told you that you two missions.")
            pause("first to colect golden coins,second to kill the dragon.")
            choice_number = the_choice("refuse and go to the cave","accept")

            if(choice_number == "1"):
                pause("you left the hut and went to the cave.")     
                pause(f"you found a {random.choice(animals)} that killed you.")  
                lose()
                
            elif(choice_number == "2"):
                pause("the old man give you a wand and spell book")  
                pause(f"also he gave you bottle of {random.choice(colors)} liquid to return back.") 
                pause("he transfered you to strange forest.") 
                pause("you saw a strange man and you saw a map with him.")
                choice_number = the_choice("kill him and take the map","give him your horse for map")

                if(choice_number == "1"):
                    pause("you show your wand and open spell book.")  
                    choice_number = the_choice("Fire Lord","Spirit Snatcher")

                    if (choice_number == "1"):
                        fire_lord1("strange man")
                        pause("you took the map and found some burnt areas")   
                        counter += player_score(50)
                        pause("while you was travelling you found commerical carts.")  
                        pause("for sure there a lot of coins there.")
                        choice_number = the_choice("steal the gold","ignore them")

                        if (choice_number == "1"):
                            pause("you show your wand and open spell book.") 
                            pause("a new spell appeared in the book.. the Midnight Pilfer")
                            choice_number = the_choice("Midnight Pilfer","between Fire Lord and Spirit Snatcher")

                            if (choice_number == "1"):
                                midnight_pilfer("golden coins","spell book")
                                counter += player_score(100)
                                pause("after walking for a half day.") 
                                pause("you reached the dragon den and you hide behind a rock.")                                
                                pause("now you had to attak him with one of your spell.")
                                choice_number = the_choice("Fire Lord","Midnight Pilfer")

                                if (choice_number == "1"):
                                    fire_lord2("dragon body")
                                    pause("you go to collect the coins") 
                                    pause("but found them melted due to the heat")
                                    pause(f"you drink the {random.choice(colors)} liquid.")                                  
                                    pause("you returned to the hut.")                                
                                    pause("the old man told you to give him the coins.")                               
                                    choice_number = the_choice("give the coins","attack him")

                                    if (choice_number == "1"):
                                        pause(f"you give him {counter} coins")                               
                                        counter = 0
                                        win()

                                    elif (choice_number == "2" ):
                                        pause("you show your wand and open spell book.")
                                        choice_number = the_choice("Fire Lord","Midnight Pilfer")

                                        if (choice_number == "1"):
                                            fire_lord3("old man","hut")
                                            lose()
                                            
                                        elif (choice_number == "2"):
                                            midnight_pilfer2("old man heart","half golden coins")
                                            counter = counter/2
                                            win()

                                elif(choice_number == "2"):
                                    midnight_pilfer("dragon heart","wand")
                                    pause(f"you drink the {random.choice(colors)} liquid.")
                                    pause("you returned to the hut.")
                                    pause("the old man told you to give him the coins.")                               
                                    choice_number = the_choice("give the coins","attack him")

                                    if (choice_number == "1"):
                                        pause(f"you give him {counter} coins.")                                                                   
                                        counter = 0
                                        win()

                                    elif (choice_number == "2" ):
                                        pause("you don't have your hand so you attack him with hand.")
                                        pause(f"he throw a {random.choice(colors)} bottle on you turned you to frog then he took the coins")
                                        lose() 

                            elif(choice_number == "2"):
                                choice_number = the_choice("Fire Lord","Spirit Snatcher")

                                if (choice_number == "1"):
                                    fire_lord2("people")
                                    pause("you go to collect the coins") 
                                    pause("but found them melted due to the heat")
                                    pause("you continued your travel to the den")
                                    pause("you reached the den then you hide behind rock")
                                    pause("you had to attack the dragon")
                                    choice_number = the_choice("Midnight Pilfer","between the Fire Lord and Spirit Snatcher")

                                    if (choice_number == "1"):
                                        midnight_pilfer("dragon heart","wand")
                                        pause(f"you drink the {random.choice(colors)} liquid.")
                                        pause("you returned to the hut.")
                                        pause("the old man told you to give him the coins.")                               
                                        choice_number = the_choice("give the coins","attack him")

                                        if (choice_number == "1"):
                                            pause(f"you give him {counter} coins.")                               
                                            counter = 0
                                            win()

                                        elif (choice_number == "2" ):
                                            pause("you don't have your hand so you attack him with hand.")
                                            pause(f"he throw a {random.choice(colors)} bottle on you turned you to frog then he took the coins")
                                            lose()

                                    elif ( choice_number == "2"):
                                        choice_number = the_choice("Fire Lord","Spirit Snatcher")

                                        if(choice_number == "1"):
                                            fire_lord3("dragon","near to the dragon nick")
                                            lose()

                                        elif(choice_number == "2"):
                                            spirit_snatcher1("dragon","dragon nick","fire")
                                            counter += player_score(200)
                                            pause(f"you drink the {random.choice(colors)} liquid.")
                                            pause("you returned to the hut.")
                                            pause("the old man told you to give him the coins.")                               
                                            choice_number = the_choice("give the coins","attack him")

                                            if (choice_number == "1"):
                                                pause(f"you give him {counter} coins")                               
                                                counter = 0
                                                win()

                                            elif(choice_number == "2"):
                                                choice_number = the_choice("midnight Pilfer","between Fire Lord and Spirit Snatcher")

                                                if(choice_number =="1"):
                                                    midnight_pilfer2("old man heart","half golden coins")
                                                    counter = counter/2
                                                    win()

                                                elif (choice_number == "2"):
                                                    choice_number = the_choice("Fire Lord","Spirit Snatcher")

                                                    if (choice_number == "1"):
                                                       fire_lord3("old man")
                                                       lose() 

                                                    elif(choice_number == "2"):
                                                        spirit_snatcher2("old man","screaming")
                                                        lose()

                                elif(choice_number == "2"):
                                    spirit_snatcher1("people","near to there ears","screaming of hundreds")
                                    pause("you go to collect the coins")
                                    counter += player_score(100)
                                    pause("you continued your travel to the den")
                                    pause("you reached the den then you hide behind rock")
                                    pause("you had to attack the dragon")
                                    choice_number = the_choice("Midnight Pilfer","between the Fire Lord and Spirit Snatcher")

                                    if (choice_number == "1"):
                                        midnight_pilfer("dragon heart","wand")
                                        pause(f"you drink the {random.choice(colors)} liquid.")
                                        pause("you returned to the hut.")
                                        pause("the old man told you to give him the coins.")                               
                                        choice_number = the_choice("give the coins","attack him")

                                        if (choice_number == "1"):
                                            pause(f"you give him {counter} coins.")                               
                                            counter = 0
                                            win()

                                        elif (choice_number == "2" ):
                                            pause("you don't have your wand so you attack him with hand.")
                                            pause(f"he throw a {random.choice(colors)} bottle on you turned you to frog then he took the coins")
                                            lose()

                                    elif ( choice_number == "2"):
                                        choice_number = the_choice("Fire Lord","Spirit Snatcher")

                                        if(choice_number == "1"):
                                            fire_lord2("dragon")
                                            pause("you go to collect the coins") 
                                            pause("but found them melted due to the heat")
                                            pause(f"you drink the {random.choice(colors)} liquid.")
                                            pause("you returned to the hut.")
                                            pause("the old man told you to give him the coins.")                               
                                            choice_number = the_choice("give the coins","attack him")
                                            
                                            if (choice_number == "1"):
                                                pause(f"you give him {counter} coins")                               
                                                counter = 0
                                                win()

                                            elif (choice_number == "2" ):
                                                pause("you show your wand and open spell book.")
                                                choice_number = the_choice("Fire Lord","Spirit Snatcher")

                                                if (choice_number == "1"):
                                                    fire_lord3("old man","hut")
                                                    lose()

                                                elif (choice_number == "2"):
                                                    spirit_snatcher2("old man","screaming")
                                                    lose()

                                        elif(choice_number == "2"):
                                            spirit_snatcher2("dragon","fire")
                                            lose()

                        elif (choice_number == "2"):
                            pause("you continued your journey")
                            pause("you reached the dragon den and hide behind a rock")
                            pause("you had to attack him")
                            choice_number = the_choice("Fire Lord","Spirit Snatcher")

                            if (choice_number == " 1"):
                                fire_lord2("dragon")
                                pause("you go to collect the coins") 
                                pause("but found them melted due to the heat")
                                pause(f"you drink the {random.choice(colors)} liquid.")
                                pause("you returned to the hut.")
                                pause("the old man told you to give him the coins.")                               
                                choice_number = the_choice("give the coins","attack him")
                                
                                if (choice_number == "1"):
                                    pause(f"you give him {counter} coins")                               
                                    counter = 0
                                    win()

                                elif (choice_number == "2" ):
                                    pause("you show your wand and open spell book.")
                                    choice_number = the_choice("Fire Lord","Spirit Snatcher")

                                    if (choice_number == "1"):
                                        fire_lord3("old man","hut")
                                        lose()

                                    elif (choice_number == "2"):
                                        spirit_snatcher1("old man","near to the old man","screaming")
                                        win()
                                        
                            elif ( choice_number == "2"):
                                spirit_snatcher1("dragon","on the dragon nick","fire")
                                counter += player_score(200)
                                pause(f"you drink the {random.choice(colors)} liquid.")
                                pause("you returned to the hut.")
                                pause("the old man told you to give him the coins.")                               
                                choice_number = the_choice("give the coins","attack him")

                                if (choice_number == "1"):
                                    pause(f"you give him {counter} coins")                               
                                    counter = 0
                                    win()

                                elif (choice_number == "2" ):
                                    pause("you show your wand and open spell book.")
                                    choice_number = the_choice("Fire Lord","Spirit Snatcher")

                                    if (choice_number == "1"):
                                        fire_lord2("old man")
                                        win()

                                    elif (choice_number == "2"):
                                        spirit_snatcher2("old man","screamng")
                                        lose()

                    elif( choice_number == "2"):
                        pause("you took the map and find a place called the market")
                        choice_number = the_choice("fo to market","go to the den")   

                        if (choice_number == "1"):
                            pause("you reach the marke after two days of travelling")
                            pause("for sure ther are a lot of coins there")
                            choice_number = the_choice("steal them","leave them and go to the den")

                            if (choice_number == "1"):
                                pause("you show your wand and open spell book.")
                                pause("a new spell appeared in the book.. the Midnight Pilfer")
                                choice_number = the_choice("Midnight Pilfer","between Fire Lord and Spirit Snatcher")

                                if(choice_number == "1"):
                                    midnight_pilfer("golden coins","spell book")
                                    counter += player_score(300)
                                    pause("after walking for a three day.")
                                    pause("you reached the dragon den and you hide behind a rock.")
                                    pause("now you had to attak him with one of your spell.")
                                    choice_number = the_choice("Spirit Snathcer","Midnight Pilfer")

                                    if (choice_number == "1"):
                                        spirit_snatcher2("dragon","fire")
                                        lose()

                                    elif (choice_number == "2"):
                                        midnight_pilfer2("dragon heart","wand")
                                        counter += player_score(200)
                                        pause(f"you drink the {random.choice(colors)} liquid.")
                                        pause("you returned to the hut.")
                                        pause("the old man told you to give him the coins.")                               
                                        choice_number = the_choice("give the coins","attack him")

                                        if (choice_number == "1"):
                                            pause(f"you give him {counter} coins.")                               
                                            counter = 0
                                            win()

                                        elif (choice_number == "2" ):
                                            pause("you don't have your hand so you attack him with hand.")
                                            pause(f"he throw a {random.choice(colors)} bottle on you turned you to frog then he took the coins")
                                            lose()

                                elif(choice_number == "2"):
                                    choice_number = the_choice("Fire Lord","Spirit Snatcher")
                                    if(choice_number == "1"):
                                        fire_lord1("people")
                                        pause("you go to collect the coins") 
                                        counter += player_score(100)
                                        pause("after travelling for three days")
                                        pause("you reached the dragon den and hide behind a rock")
                                        pause("you had to attack hime")
                                        choice_number = the_choice("Midnight Pilfer","between Spirit Snatcher and Fire Lord")

                                        if(choice_number == "1"):
                                            midnight_pilfer2("dragon heart","wand")
                                            counter += player_score(200)
                                            pause(f"you drink the {random.choice(colors)} liquid.")
                                            pause("you returned to the hut.")
                                            pause("the old man told you to give him the coins.")                               
                                            choice_number = the_choice("give the coins","attack him")

                                            if (choice_number == "1"):
                                                pause(f"you give him {counter} coins.")
                                                counter = 0
                                                win()

                                            elif (choice_number == "2" ):
                                                pause("you don't have your hand so you attack him with hand.")
                                                pause(f"he throw a {random.choice(colors)} bottle on you turned you to frog then he took the coins")
                                                lose()

                                        elif(choice_number == "2"):
                                                choice_number = the_choice("Fire Lord","Spirit Snatcher")
                                            
                                                if (choice_number == "1"):
                                                    fire_lord2("dragon")
                                                    pause("you go to collect the coins") 
                                                    pause("but found them melted due to the heat")
                                                    pause(f"you drink the {random.choice(colors)} liquid.")
                                                    pause("you returned to the hut.")
                                                    pause("the old man told you to give him the coins.")                               
                                                    choice_number = the_choice("give the coins","attack him")

                                                    if (choice_number == "1"):
                                                        pause(f"you give him {counter} coins")                               
                                                        counter = 0
                                                        win()

                                                    elif (choice_number == "2" ):
                                                        pause("you show your wand and open spell book.")
                                                        choice_number = the_choice("Fire Lord","Spirit Snatcher")

                                                        if (choice_number == "1"):
                                                            fire_lord3("old man","hut")
                                                            lose()

                                                        elif (choice_number == "2"):
                                                            spirit_snatcher1("old man","near to the old man","screaming")
                                                            win()

                                                elif(choice_number == "2"):
                                                    spirit_snatcher1("dragon","dragon nick","fire")
                                                    counter += player_score(200)
                                                    pause(f"you drink the {random.choice(colors)} liquid.")
                                                    pause("you returned to the hut.")
                                                    pause("the old man told you to give him the coins.")                               
                                                    choice_number = the_choice("give the coins","attack him")

                                                    if (choice_number == "1"):
                                                        pause(f"you give him {counter} coins")                               
                                                        counter = 0
                                                        win()

                                                    elif(choice_number == "2"):
                                                        choice_number = the_choice("midnight Pilfer","between Fire Lord and Spirit Snatcher")

                                                        if(choice_number =="1"):
                                                            midnight_pilfer2("old man heart","half golden coins")
                                                            counter = counter/2
                                                            win()

                                                        elif (choice_number == "2"):
                                                            choice_number = the_choice("Fire Lord","Spirit Snatcher")

                                                            if (choice_number == "1"):
                                                                fire_lord3("old man","hut")
                                                                lose() 

                                                            elif(choice_number == "2"):
                                                                spirit_snatcher2("old man","screaming")
                                                                lose()

                                    elif(choice_number == "2"):
                                        spirit_snatcher1("people","near to there ears","screaming of hundreds")
                                        counter += player_score(300)
                                        pause("after walking for a three days.")
                                        pause("you reached the draon den and you hide behind a rock.")
                                        pause("now you had to attak him with one of your spell.")
                                        choice_number = the_choice("Spirit Snathcer","Midnight Pilfer")

                                        if (choice_number == "1"):
                                            spirit_snatcher2("dragon","fire")
                                            lose()

                                        elif (choice_number == "2"):
                                            midnight_pilfer2("dragon heart","wand")
                                            counter += player_score(200)
                                            pause(f"you drink the {random.choice(colors)} liquid.")
                                            pause("you returned to the hut.")
                                            pause("the old man told you to give him the coins.")                               
                                            choice_number = the_choice("give the coins","attack him")

                                            if (choice_number == "1"):
                                                pause(f"you give him {counter} coins.")                               
                                                counter = 0
                                                win()

                                            elif (choice_number == "2" ):
                                                pause("you don't have your hand so you attack him with hand.")
                                                pause(f"he throw a {random.choice(colors)} bottle on you turned you to frog then he took the coins") 
                                                lose()
            
                        elif (choice_number == "2"):
                            pause("you continued your journey") 
                            pause("you reached the dragon den and hide behind a rock")
                            pause("you had to attack hime")
                            choice_number = the_choice("Fire Lord","Spirit Snatcher")

                            if (choice_number == " 1"):
                                fire_lord2("dragon")
                                pause("you go to collect the coins") 
                                pause("but found them melted due to the heat")
                                pause(f"you drink the {random.choice(colors)} liquid.")
                                pause("you returned to the hut.")
                                pause("the old man told you to give him the coins.")                               
                                choice_number = the_choice("give the coins","attack him")

                                if (choice_number == "1"):
                                    pause(f"you give him {counter} coins")                               
                                    counter = 0
                                    win()

                                elif (choice_number == "2" ):
                                    pause("you show your wand and open spell book.")
                                    choice_number = the_choice("Fire Lord","Spirit Snatcher")

                                    if (choice_number == "1"):
                                        fire_lord3("old man","hut")
                                        lose()

                                    elif (choice_number == "2"):
                                        spirit_snatcher1("old man","near to the old man","screaming")
                                        win()

                            elif ( choice_number == "2"):
                                spirit_snatcher2("dragon","fire")
                                lose()         
                                         
                elif( choice_number == "2"):
                    pause("you took the map and find a place called the market")
                    choice_number = the_choice("go to market","go to the den")  

                    if (choice_number == "1"):
                        pause("you reach the market after two days of travelling")
                        pause("for sure ther are a lot of coins there")
                        choice_number = the_choice("steal them","leave them and go to the den")

                        if (choice_number == "1"):
                            pause("you show your wand and open spell book.")
                            pause("a new spell appeared in the book.. the Midnight Pilfer")
                            choice_number = the_choice("Midnight Pilfer","between Fire Lord and Spirit Snatcher")

                            if(choice_number == "1"):
                                midnight_pilfer("golden coins","spell book")
                                counter += player_score(300)
                                pause("after walking for a three day.")
                                pause("you reached the dragon den and you hide behind a rock.")
                                pause("now you had to attak him with one of your spell.")
                                choice_number = the_choice("Spirit Snathcer","Midnight Pilfer")

                                if (choice_number == "1"):
                                        spirit_snatcher1("dragon","dragon nick","fire")
                                        counter += player_score(200)
                                        pause(f"you drink the {random.choice(colors)} liquid.")
                                        pause("you returned to the hut.")
                                        pause("the old man told you to give him the coins.")                               
                                        choice_number = the_choice("give the coins","attack him")

                                        if (choice_number == "1"):
                                            pause(f"you give him {counter} coins")                               
                                            counter = 0
                                            win()

                                        elif(choice_number == "2"):
                                            choice_number = the_choice("midnight Pilfer","Spirit Snatcher")

                                            if(choice_number =="1"):
                                                midnight_pilfer2("old man heart","half golden coins")
                                                counter = counter/2
                                                win()

                                            elif (choice_number == "2"):
                                                spirit_snatcher2("old man","screaming")
                                                lose()

                                elif (choice_number == "2"):
                                    midnight_pilfer2("dragon heart","wand")
                                    counter += player_score(200)
                                    pause(f"you drink the {random.choice(colors)} liquid.")
                                    pause("you returned to the hut.")
                                    pause("the old man told you to give him the coins.")                               
                                    choice_number = the_choice("give the coins","attack him")

                                    if (choice_number == "1"):
                                        pause(f"you give him {counter} coins.")                               
                                        counter = 0
                                        win()

                                    elif (choice_number == "2" ):
                                        pause("you don't have your hand so you attack him with hand.")
                                        pause(f"he throw a {random.choice(colors)} bottle on you turned you to frog then he took the coins")
                                        lose()

                            elif(choice_number == "2"):
                                choice_number = the_choice("Fire Lord","Spirit Snatcher")

                                if(choice_number == "1"):
                                    fire_lord1("people")
                                    pause("you go to collect the coins") 
                                    counter += player_score(100)
                                    pause("after travelling for three days")                        
                                    pause("you reached the dragon den and hide behind a rock")
                                    pause("you had to attack hime")
                                    choice_number = the_choice("Midnight Pilfer","between Spirit Snatcher and Fire Lord")

                                    if(choice_number == "1"):
                                        midnight_pilfer2("dragon heart","wand")
                                        counter += player_score(200)
                                        pause(f"you drink the {random.choice(colors)} liquid.")
                                        pause("you returned to the hut.")
                                        pause("the old man told you to give him the coins.")                               
                                        choice_number = the_choice("give the coins","attack him")

                                        if (choice_number == "1"):
                                            pause(f"you give him {counter} coins.")                               
                                            counter = 0
                                            win()

                                        elif (choice_number == "2" ):
                                            pause("you don't have your hand so you attack him with hand.")
                                            pause(f"he throw a {random.choice(colors)} bottle on you turned you to frog then he took the coins")
                                            lose()

                                    elif(choice_number == "2"):
                                        choice_number = the_choice("Fire Lord","Spirit Snatcher")
                                    
                                        if (choice_number == "1"):
                                            fire_lord2("dragon")
                                            pause("you go to collect the coins") 
                                            pause("but found them melted due to the heat")
                                            pause(f"you drink the {random.choice(colors)} liquid.")
                                            pause("you returned to the hut.")
                                            pause("the old man told you to give him the coins.")                               
                                            choice_number = the_choice("give the coins","attack him")

                                            if (choice_number == "1"):
                                                pause(f"you give him {counter} coins")                               
                                                counter = 0
                                                win()

                                            elif (choice_number == "2" ):
                                                pause("you show your wand and open spell book.")
                                                choice_number = the_choice("Fire Lord","Spirit Snatcher")

                                                if (choice_number == "1"):
                                                    fire_lord3("old man","hut")
                                                    lose()

                                                elif (choice_number == "2"):
                                                    spirit_snatcher1("old man","near to the old man","screaming")
                                                    win()

                                        elif(choice_number == "2"):
                                            spirit_snatcher1("dragon","dragon nick","fire")
                                            counter += player_score(200)
                                            pause(f"you drink the {random.choice(colors)} liquid.")
                                            pause("you returned to the hut.")
                                            pause("the old man told you to give him the coins.")                               
                                            choice_number = the_choice("give the coins","attack him")

                                            if (choice_number == "1"):
                                                pause(f"you give him {counter} coins")                               
                                                counter = 0
                                                win()

                                            elif(choice_number == "2"):
                                                choice_number = the_choice("midnight Pilfer","between Fire Lord and Spirit Snatcher")

                                                if(choice_number =="1"):
                                                    midnight_pilfer2("old man heart","half golden coins")
                                                    counter = counter/2
                                                    win()

                                                elif (choice_number == "2"):
                                                    choice_number = the_choice("Fire Lord","Spirit Snatcher")

                                                    if (choice_number == "1"):
                                                        fire_lord3("old man","hut")
                                                        lose() 

                                                    elif(choice_number == "2"):
                                                        spirit_snatcher2("old man","screaming")
                                                        lose()

                                elif(choice_number == "2"):
                                    spirit_snatcher1("people","near to there ears","screaming of hundreds")
                                    counter += player_score(300)
                                    pause("after walking for a three days.")
                                    pause("you reached the draon den and you hide behind a rock.")
                                    pause("now you had to attak him with one of your spell.")
                                    choice_number = the_choice("Spirit Snathcer","Midnight Pilfer")

                                    if (choice_number == "1"):
                                        spirit_snatcher2("dragon","fire")
                                        lose()

                                    elif (choice_number == "2"):
                                        midnight_pilfer2("dragon heart","wand")
                                        counter += player_score(200)
                                        pause(f"you drink the {random.choice(colors)} liquid.")
                                        pause("you returned to the hut.")
                                        pause("the old man told you to give him the coins.")                               
                                        choice_number = the_choice("give the coins","attack him")

                                        if (choice_number == "1"):
                                            pause(f"you give him {counter} coins.")                               
                                            counter = 0
                                            win()

                                        elif (choice_number == "2" ):
                                            pause("you don't have your hand so you attack him with hand.")
                                            pause(f"he throw a {random.choice(colors)} bottle on you turned you to frog then he took the coins")
                                            lose()
        
                    elif (choice_number == "2"):
                        pause("you continued your journey")
                        pause("you reached the dragon den and hide behind a rock")
                        pause("you had to attack hime")
                        choice_number = the_choice("Fire Lord","Spirit Snatcher")

                        if (choice_number == " 1"):
                            fire_lord2("dragon")
                            pause("you go to collect the coins") 
                            pause("but found them melted due to the heat")
                            pause(f"you drink the {random.choice(colors)} liquid.")
                            pause("you returned to the hut.")
                            pause("the old man told you to give him the coins.")                               
                            choice_number = the_choice("give the coins","attack him")

                            if (choice_number == "1"):
                                pause(f"you give him {counter} coins")                               
                                counter = 0
                                win()

                            elif (choice_number == "2" ):
                                pause("you show your wand and open spell book.")
                                choice_number = the_choice("Fire Lord","Spirit Snatcher")

                                if (choice_number == "1"):
                                    fire_lord3("old man","hut")
                                    lose()

                                elif (choice_number == "2"):
                                    spirit_snatcher1("old man","near to the old man","screaming")
                                    win()

                        elif ( choice_number == "2"):
                            spirit_snatcher2("dragon","fire")
                            lose()