# I added a hidden path that can only be discovered by typing a secret word, and one scenario has more than two options. The secret word is Abracadabra

print("You wake up in a mysterious cave. You see three exits: a DOOR, a LADDER, and a TUNNEL.")
choice1 = input("Which one do you choose? ").lower()

if choice1 == "door":
    print("You open the door and find yourself in a library filled with floating books. A voice asks: 'READ a book or SEARCH the room?'")
    choice2 = input("What do you do? ").lower()
    
    if choice2 == "read":
        print("The book tells the story of someone just like you... and the last page is blank. You feel sleepy. Do you WRITE your own ending or CLOSE the book?")
        choice3 = input("Your choice: ").lower()
        
        if choice3 == "write":
            print("You write your name... and vanish into the story forever.")
        elif choice3 == "close":
            print("You close the book and everything fades. You wake up at home. Was it all a dream?")
        else:
            print("That choice doesn't make sense. The book vanishes in a puff of smoke.")

    elif choice2 == "search":
        print("You find a hidden switch. Press it or leave it alone? PRESS or LEAVE?")
        choice3 = input("What do you do? ").lower()
        
        if choice3 == "press":
            print("A secret door opens to a garden of light. You're free!")
        elif choice3 == "leave":
            print("You walk away and the library begins to crumble. You barely escape.")
        else:
            print("You hesitate too long. The room disappears around you.")

    else:
        print("You can't do that. The books swirl angrily and vanish.")

elif choice1 == "ladder":
    print("You climb the ladder into a dense jungle. You see a PARROT, a PATH, and a POND.")
    choice2 = input("Which do you explore? ").lower()

    if choice2 == "parrot":
        print("The parrot speaks: 'Solve my riddle or stay forever. What has keys but can't open doors?'")
        answer = input("Your answer: ").lower()
        
        if answer == "piano":
            print("The parrot nods. A door appears and you walk free!")
        else:
            print("Wrong! The jungle grows thicker, trapping you.")

    elif choice2 == "path":
        print("The path splits into two: LEFT or RIGHT?")
        choice3 = input("Which direction? ").lower()
        
        if choice3 == "left":
            print("You find a hut with friendly villagers who help you home.")
        elif choice3 == "right":
            print("You get lost but discover a hidden treasure chest.")
        else:
            print("You stand frozen, unsure where to go, until night falls.")

    elif choice2 == "pond":
        print("You look into the pond and see your reflection change. Do you TOUCH it or STEP back?")
        choice3 = input("What do you do? ").lower()

        if choice3 == "touch":
            print("You are pulled into another world—your adventure continues!")
        elif choice3 == "step":
            print("You back away and find a map on the ground.")
        else:
            print("The water ripples... then stills.")

    else:
        print("Confused, you wander until the jungle swallows you whole.")

elif choice1 == "tunnel":
    print("You crawl through the tunnel and find a glowing crystal. You can GRAB it, LEAVE it, or SAY a secret word.")
    choice2 = input("Your action? ").lower()

    if choice2 == "grab":
        print("The crystal pulses, and you gain strange powers... but you're trapped in the tunnel forever.")
    elif choice2 == "leave":
        print("You crawl past it and emerge into daylight. Freedom!")
    elif choice2 == "abracadabra":
        print("The crystal shatters and a portal opens. You step into a land of wonder.")
    else:
        print("Nothing happens. The tunnel begins to shake... you'd better run.")

else:
    print("That path doesn't exist. You remain in the cave, undecided... forever.")

