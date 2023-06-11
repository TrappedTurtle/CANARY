def start_game():
    print("You are CANARY, a Knight cursed to never speak again.")
    print("After making a deal with a WITCH to save her village, you find yourself roaming the kingdoms to find a cure.")
    print("Canary rides her horse through the forest when robed men wearing the king's seal surround her.")
    print("One of them hands her a parchment.")

    choice = input("Do you crumple up the note or start your journey? (Crumple/Start): ")
    if choice.lower() == "crumple":
        print("Your cowardice has helped cast the realm into MADNESS. You are no Knight.")
        start_game()
    elif choice.lower() == "start":
        print("For three days and three nights, you travel to meet the king.")
        print("You find a sea of tents, the same red color as your very own armor.")
        print("Smoke billows from the tents as the siege and war party is in full swing.")
        print("You enter the king's tent. He lets out a chuckle and calls you forward.")
        print("You tower over every man in the tent. The king speaks, with each word a bit of food falls out of his mouth into his lap.")

        choice = input("Do you nod to the king or shake your head? (Nod/Shake): ")
        if choice.lower() == "nod":
            print("I knew you were sensible. Meet with my War Warden and his dogs to strategize on our final advance.")
            print("We've been craving at them for weeks, and victory is at our feet.")
            meet_warden()
        elif choice.lower() == "shake":
            print("You feel a sharp pain and then BLACK.")
            print("You wake up tied to a post with dents in your armor.")
            print("Rocks and fruit are being thrown at you.")
            print("A man with a scroll reads off the name of your loved ones: GARTH, HANNAH, FELNIR.")
            print("As he continues, a soldier walks up to you and forces your helmet off your head.")
            print("Your eyes are bleeding. Your mouth is SEWN shut.")
            print("As you attempt to scream, a bit of light creeps in between the stitches on your mouth.")
            print("They throw more rocks at you.")
            print("A person from the crowd screams, 'THIS IS BLACK SORCERY! THIS IS!'")
            print("One of the people picks up a stone the size of your head, gets within heaving distance, and THROWS.")
            print("GAME OVER.")
            start_game()

def meet_warden():
    print("You meet with the War Warden and enter a giant armory.")
    print("Soldiers are grabbing swords off racks and preparing for battle.")
    print("A grizzled veteran wearing a honey badger red crest stands around a map with other soldiers.")
    print("He notices you and calls you over.")

    choice = input("Will you put your hands on the map or stand motionless? (Hands/Stand): ")
    if choice.lower() == "hands":
        print("As the sun rises, the Crimson King's army and the MAD KING's mercenaries line up on the battlefield.")
        print("A sea of red and a sea of blue. The trebuchets that were tossing diseased corpses are now filled with flaming rocks.")
        print("Horns blow, and you are the TIP OF THE SPEAR. Both sides charge at each other.")
        print("With one swing of your two-handed sword, you slice through three men.")
        print("The battle is a blur. The sun moves across the sky.")
        print("Blood is congealing on your blade, wiped and then replaced with each soul taken.")
        print("When all is said and done, there's a sea of limbs, dead horses, discarded weapons, and red and blue.")
        print("The red men stand in victory, screaming! A hole in the castle wall allows entrance. You and the men enter.")
    elif choice.lower() == "stand":
        print("You sit out the battle, watching from a distance.")
        print("The battle is hard fought and barely won.")
        print("You wait until darkness and sneak over the castle wall where the Crimson King's men already work on fighting their way towards the actual castle.")
    else:
        meet_warden()

    enter_pub()

def enter_pub():
    print("You enter the pub, and there seems to be a robed man in the corner.")
    print("You feel a power coming from him.")
    print("You notice CRIMSON MEN are sitting with THE MAD KING'S men inside this pub, not drinking or even staring at their drinks.")
    print("This is a fake peace.")
    print("The robed man motions for you to come closer.")
    choice = input("Do you participate in the battle or kill the robed man? (Participate/Kill): ")
    if choice.lower() == "participate":
        print("You participate in the battle and enter the castle walls.")
        print("The citizens are scared of your dented armor, claymore, and congealed blood.")
        print("You enter the Royal pub to quench your thirst.")
        print("Inside is empty except for a robed man in the corner. He motions for you.")
        sit_or_kill()
    elif choice.lower() == "kill":
        print("You take your dagger out from his neck and clean it on your cape. You sheath it and leave the pub.")
        castle_gates()
    else:
        enter_pub()

def sit_or_kill():
    print("You have two options:")
    print("1. Plunge a dagger into his neck, killing him instantly. The battle never finished for you, and you can't take any chances.")
    print("2. Sit down across from him and wait for him to speak.")
    choice = input("What will you do? (Kill/Sit): ")
    if choice.lower() == "kill":
        print("You plunge a dagger into his neck, killing him instantly.")
        print("The battle never finished for you, and you can't take any chances.")
        print("You sheath your dagger and leave the pub.")
        castle_gates()
    elif choice.lower() == "sit":
        print("Listen closely. Meeting you was not by chance. The fate of the realm is at stake.")
        print("The mad king's sorceress has been incubating a weapon that fell from the heavens sometime ago.")
        print("It is the source of the madness that has been infecting this land as of late.")
        print("I am aware that the Crimson King wants you to bring it back to him after you murder his brother.")
        print("I would appreciate it if you were to 'misplace' it and I could take it to be hidden away forever.")
        print("Do not fear for your family as I have put things into motion to keep them safe.")
        print("Do not worry about gold as I can conjure as much as you can carry.")
        print("You do not need to make a decision now. When the time comes, do the right thing.")
        print("Candles flicker, and the robed man is gone.")
        print("All of a sudden, all the men inside the pub leave their relaxed state and begin fighting each other.")
        print("You leave the pub and make your way towards the castle.")
        castle_gates()
    else:
        sit_or_kill()

def castle_gates():
    print("You have finally made it to the Castle gates where your target lives and breathes.")
    print("Some Crimson men knock on the gates taunting for them to open.")
    print("You remember the map that the War Warden was looking at.")
    print("There were X's strewn about the map.")
    print("What will you do?")
    print("1. Wait for the door knocker to be brought up.")
    print("2. Go in through the sewage tunnel.")
    print("3. Go back to the pub for a drink.")
    choice = input("Enter your choice (1/2/3): ")
    if choice == "1":
        print("A line of men holding a wooden siege device slam the gate.")
        print("The wood splinters and then finally breaks, revealing the Castle Courtyard filled with undead.")
        print("They lumber towards the now open gate facing you and the Crimson's men.")
    elif choice == "2":
        print("You decide to go in through the sewage tunnel.")
        print("You maneuver through the dark and foul-smelling tunnel, avoiding traps and hazards.")
        print("Finally, you emerge inside the castle.")
    elif choice == "3":
        print("You turn back and go to the pub for a drink.")
        print("Unfortunately, the pub is now in chaos due to the fighting between the Crimson men and the Mad King's men.")
        print("You realize it's not a safe place to stay.")
        print("You leave the pub and make your way towards the castle.")
    else:
        castle_gates()

# Start the game
print("You are CANARY, a Knight cursed to never speak again.")
print("After making a deal with a WITCH to save her village, she finds herself roaming the kingdoms to find a cure.")
print("Canary rides her horse through the forest when robed men wearing the king's seal surround her.")
print("One of them hands her a parchment.")
print("It reads: 'THE CRIMSON KING REQUESTS YOU TO JOIN HIM OUTSIDE BULLWICH CASTLE.'")
print("What will you do?")
print("1. Crumple up the note.")
print("2. Start your journey.")
choice = input("Enter your choice (1/2): ")
if choice == "1":
    print("Your cowardice has helped cast the realm into madness. You are no Knight.")
    exit_game()
elif choice == "2":
    print("For three days and three nights, you travel to meet the king.")
    print("You find a sea of tents the same red color as your very own armor.")
    print("Smoke billows from the tents, and on the outskirts of the town, men with medieval quarantine suits load bodies into trebuchets and launch them a great distance over castle walls.")
    print("The siege and war party is in full swing.")
    print("You enter the king's tent. He lets out a chuckle and calls you forward.")
    print("You tower over every man in the tent. The king speaks, and with each word, a bit of food falls out of his mouth into his lap.")
    print('"My brother has gone mad, CANARY," he says, using the name you received after making the deal with the witch.')
    print('"His mad sorceress from faraway lands has done this."')
    print('"She made him mad, cursed him with an ailment to his mind."')
    print('"I need you to kill him," the king finishes.')
    print("The King's words echo in your mind.")
    print("Will you nod or shake your head?")
    print("1. Nod to the king.")
    print("2. Shake your head.")
    choice = input("Enter your choice (1/2): ")
    if choice == "1":
        print("I knew you were sensible. Meet with my War Warden and his dogs to strategize on our final advance.")
        print("We've been craving at them for weeks, and victory is at our feet.")
        meet_warden()
    elif choice == "2":
        print("You feel a sharp pain and then BLACK.")
        print("You wake up tied to a post with dents in your armor.")
        print("Rocks and fruit are being thrown at you.")
        print("A man with a scroll reads off the name of your loved ones: GARTH, HANNAH, FELNIR.")
        print("As he continues, a soldier walks up to you and forces your helmet off your head.")
        print("Your eyes are bleeding. Your mouth is sewn shut.")
        print("As you attempt to scream, a bit of light creeps in between the stitches on your mouth.")
        print("They throw more rocks at you.")
        print("A person from the crowd screams, 'THIS IS BLACK SORCERY! THIS IS!'")
        print("One of the people picks up a stone the size of your head, gets within heaving distance, and THROWS.")
        print("GAME OVER.")
        exit_game()
else:
    exit_game()
