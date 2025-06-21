# Modules & The Score Of The User
import time
import random

# ----------------------------- FUNCTIONS ----------------------------- #

# checks if the user's input is valid


def valid_inputs(word):

    user_input = input("").lower()  # The User Must Type The Valid Word

    while word != user_input:
        print("Please Type " + word)
        user_input = input("").lower()

        if word == user_input:  # The Kew Word Is "attack"
            break


# delaying time after each output & PT --> Pause Time


def PT(Text_input):
    Text_input
    if len(Text_input) >= 45:
        print(Text_input)
        time.sleep(5.5)
    elif len(Text_input) < 45:
        print(Text_input)
        time.sleep(4)
    elif len(Text_input) < 20:
        time.sleep(1)


# --------------------------

# Checks If The User Entered Numeric Value Of 1 Or 2
# & The Code For Takes The User's Inputs Directly Is:
# print(check_letters("USER'S-INPUT"))


def check_letters(text):
    text = input("(Please enter 1 or 2)\n")

    if text not in ["1", "2"]:
        while text not in ["1", "2"]:
            text = str(input("please choose only 1 or 2\n"))
        return text
    else:
        return text


# --------------------------

# calculating The IQ SCORE


def Calc_Score(num, IQ_SCORE):
    IQ_SCORE += num

    print("The Change In IQ SCORE:", num, "\ntotal IQ =", IQ_SCORE)
    time.sleep(3)
    return IQ_SCORE


# --------------------------

# Checks If The User Wanna Play Another Game


def another_game():
    another_loop = input("").lower()

    while another_loop not in ["yes", "no"]:
        print("Please choose 'yes' or 'no'")
        another_loop = input("").lower()
    return another_loop


# --------------------------

# The Beginning Of The Story & The User Name Of The Player


def Starting_Scenario(USER_NAME):

    PT("You are now a new member of an organization investigating mysteries \
and crimes around the world,")

    PT("Your goal is to solve *THE PALACE OF THE DEAD MISSION* to \
increase your IQ points after the mission.")

    PT("And now, what would you like people to call you?")

    user_name = input("(please enter the name)\n")  # Takes The User Name

    while user_name.isalpha() == False:
        print("Your name should only contain alphabetic characters.")
        user_name = input("(please enter the name)\n")

        if user_name.isalpha() == True:
            break

    print("Alright", user_name, "Lets start investigating")
    time.sleep(2)
    PT(
        "Loading the mission... (your normal IQ score is *100* to win \
the mission you need to increase it)")
    time.sleep(6.5)
    return user_name


# --------------------------

# The First Choice From The User


def Front_Door():
    PT("Before you went to open the door,")
    PT("you felt someone was watching,")
    PT("and when you glanced at the upper window,")

    PT("you started imagining as if there was a shadow there, \
but its features weren't clear.")

    PT("You decided to open the front door, and trying to avoid what you saw")
    PT("upon entering, it was pitch dark.")


def Back_Door():
    PT("While walking to the backyard garden,")

    PT("the atmosphere seemed calm until suddenly \
there were sounds behind the trees,")

    PT("but they might have been just the wind,")
    PT("so you ignored them and continued toward the back door.")
    PT("Upon entering quietly,")
    PT("the room was empty except for one wardrobe,")
    PT("which had some blood on it.")
    PT("When you opened it, you found head of a corpse")

    PT("and at that moment, you felt a sense of urgency \
and hurried inside the palace.")
    PT("upon entering, it was pitch dark.")


# --------------------------

# clarify who is the killer in the story


def The_Killer_Is():
    print("Interpretation: According to the evidence in front of you,")
    time.sleep(1)

    PT("before entering, the weather was rainy, and certainly the killer was \
someone who came from outside to invade the palace.")

    PT("Before entering the room, there was broken glass on the floor,")

    PT("and perhaps the man in the suit was trying to defend himself \
by breaking something over the intruder's head.")

    PT("This explains the reason for the injury to the wet man,")
    PT("and clarifies the reason for his wet clothes.")


# --------------------------

# The Main Story


def Main_Scenario(IQ_SCORE):
    PT(
        "Do you want to use the "
        + light
        + " or try to find a switch to turn on the light?"
    )
    PT("(Note that the " + light + " could run out after you enter deeply.)")
    PT("(1) " + light)
    PT("(2) Search for the room switch")
    user_input = check_letters("USER'S-INPUT")

    if user_input == "1":  # FlashLight Or Candle
        PT("When you entered, you felt water on the ground as you walked,")
        PT("and when you aimed the " + light + " downwards,")
        if light == "flashlight":
            PT("you found that the battery had died.")
        elif light == "candle":
            PT("you found that the candle has went out")

        IQ_SCORE = Calc_Score(-10, IQ_SCORE)

        PT("Fortunately, when you tried to return to the palace \
door While you were holding onto the wall,")

        PT("you found light switches then turned it on.")

    elif user_input == "2":  # Room Switch

        PT("When you entered, you were holding onto the wall \
searching for the room switches,")

        PT("and you felt as if there was water on the ground.")
        PT("When you found the switches, you turned them on.")

        IQ_SCORE = Calc_Score(10, IQ_SCORE)

    PT("...")

    PT("Suddenly, fear and shock appeared on your face as the \
first thing you saw was a room filled with blood,")

    PT("with a message written on the wall in this blood.")
    PT("When you went to read the words,")
    PT("it said, " + messages)

    PT("After grasping these words, you confirmed that \
whoever is with you in this house is not a normal person,")

    PT("and just a few seconds later,")

    PT("your thoughts were interrupted by a scream coming \
from the second floor.")

    PT("Now, what will you do?")
    PT("(1) Check the source of the scream")
    PT("(2) Ignore it and explore the palace")

    user_input = check_letters("USER'S-INPUT")

    if user_input == "1":  # Source Of The Scream

        IQ_SCORE = Calc_Score(10, IQ_SCORE)

        PT("The first thing you did was to make sure you was carrying \
your weapon and head towards the source of the scream.")

        PT("Upon reaching there,")
        PT("you found a closed door with broken glass on the ground.")
        PT("When you tried to open the door,")
        PT("it was locked from the inside")
        PT("Quickly, break down the door.")
        PT("(Type \"Attack\" to break down the door)")

        valid_inputs("attack")

    elif user_input == "2":  # Ignore The Scream

        IQ_SCORE = Calc_Score(-15, IQ_SCORE)

        PT("(It is not in the investigator's style to leave a \
problem and ignore it)")

        PT("You decided to ignore the sound and continued \
exploring the rest of the rooms.")

        PT("However, you came across a room with a long, deep corridor.")
        PT("Upon entering,")
        PT("it was dimly lit but you paid no mind.")
        PT("Shortly after, you stumbled and fell to the ground.")
        PT("As you tried to regain your composure,")
        PT(" you found " + num_of_corpses + " on the floor.")
        PT("While attempting to discern any features of the deceased,")
        PT("*you found none,*")
        PT("as the face had been completely wiped clean.")
        PT("At that moment, you quickly retreated back inside,")
        PT("Upon reaching to the second floor,")
        PT("you found a closed door with broken glass on the ground.")
        PT("When you tried to open the door,")
        PT("it was locked from the inside.")
        PT("(Type \"Attack\" to break down the door)")

        valid_inputs("attack")

    PT("You succeeded. You broke the door.")
    PT("Upon entering the room, you found two individual.")

    PT("The first person was wearing a suit and appeared \
to be injured in his left leg.")

    PT("The second person was dressed in wet clothes and \
also had a head injury,")

    PT("causing blood to trickle down his body.")
    PT(
        "When the two men saw you, the "
        + gun_type
        + " was aimed at them, and an attempt was made to investigate them."
    )
    PT("Each one justified their situation")

    PT("where the man in the suit said, \"HELP this wet man was \
trying to kill me and escape.\"")

    PT("while the wet man injured his head said, \"I was defending myself \
because this person entered my palace and killed my friends.\"")

    PT("Now, who do you think is lying?")
    PT("(1) The man in the suit")
    PT("(2) the wet person")
    user_input = check_letters("USER'S-INPUT")

    if user_input == "1":  # The man in the suit

        IQ_SCORE = Calc_Score(-5, IQ_SCORE)

        The_Killer_Is()

    elif user_input == "2":  # wet person

        IQ_SCORE = Calc_Score(25, IQ_SCORE)
        PT("Nice Choice!")

        The_Killer_Is()

    PT("Alright, first you should take these two to the \
investigation center to investigate further into their case.")

    PT("As you were trying to tell them to come with you, lifting the "
        + gun_type
        + " as a precaution,")

    PT("the man in wet clothing appeared nervous.")
    PT("However, both agreed to come with you,")
    PT("and just before they left the room, someone turned off the lights")
    PT("You quickly moved and took some distance,")
    PT("and upon hearing fast approaching footsteps towards you,")
    PT("you had only a few seconds to act.")

    PT("Do you want to randomly fire the gun or attempt \
a temporary escape to the first floor?")

    PT("(1) use " + gun_type)
    PT("(2) run to the first floor")
    user_input = check_letters("USER'S-INPUT")

    if user_input == "1":  # Fire Gun
        PT("You raised your weapon towards the sound,")

        PT("but the lights were off so you couldn't \
see anything, thus missing the target.")

        PT("Then the assailant attacked you, injuring your \
shoulder with a sharp tool.")

        PT("Fortunately, the assailant attempted to flee. Quickly,")

        IQ_SCORE = Calc_Score(-10, IQ_SCORE)

        PT("tie the wound without removing the sharp tool, \
to prevent more blood from coming out.")

        PT("(Type \"tie\" to prevent blood from coming out)")

        valid_inputs("tie")

        PT("WELL DONE, you tied the wound")
        PT("but you heard the sound of a jump outside the palace,")
        PT("then you realized that the killer was trying to escape the palace")

    elif user_input == "2":  # Run To The First Floor

        PT("You took the man in the suit with you and hurried \
up to the stairs to reach the first floor,")

        PT("but the killer didn't catch up with you.")

        IQ_SCORE = Calc_Score(10, IQ_SCORE)

        PT("Then you heard the sound of a jump outside the palace,")
        PT("and then you realized that the killer was escaping \
through the window.")

    PT("You rushed out and saw the killer trying to jump \
over the Palace wall.")

    PT("you must use the " + gun_type + " again to stop him")
    PT("How do you want to use the gun?")
    PT("(1) Headshot")
    PT("(2) Foot shot")
    user_input = check_letters("USER'S-INPUT")

    if user_input == "1":  # HeadShot
        PT("You hit the target and killed him")
        PT("Well done " + USER_NAME + ",")
        PT("you managed to protect the owner of the palace.")

        PT("However, it would have been better not to kill \
this person for further investigation.")

        IQ_SCORE = Calc_Score(-15, IQ_SCORE)

    elif user_input == "2":  # Foot Shot
        PT("You hit the target and he fell to the ground.")
        PT("You rushed to catch him as he tried to escape,")
        PT("but you managed to tie his hands.")
        PT("Well done " + USER_NAME + ",")
        PT("you protected the owner of the palace and caught the killer.")
        IQ_SCORE = Calc_Score(15, IQ_SCORE)

    # --------------------------

    # Checks If The Player Won or Loss According To The Score

    if IQ_SCORE > 100:
        PT("Your IQ SCORE Is More Than 100, Great Jop \
You Succeeded In This Mission")

    else:
        PT("Your IQ SCORE Is Less Than 100, You Didn't Passed In The Mission,")
        PT("But Dont Worry, You Can Imporve Yourself Next Time")


# -------------------------- END OF THE FUNCTIONS -------------------------- #


USER_NAME = Starting_Scenario("USER_NAME")  # The First Part Of The Text Game


# The Main Loop Of The Game


while True:

    # Randomness

    one = ["pistol", "Revolver"]
    two = ["candle", "flashlight"]

    three = ["1 corpse", "2 corpses"]
    four = ["cellar", "garage"]
    five = [
        "Corpses are nothing but dolls and blood.",
        "Shadows dance in the corridors of memory.",
    ]

    gun_type = random.choice(one)
    light = random.choice(two)

    num_of_corpses = random.choice(three)
    back_door = random.choice(four)
    messages = random.choice(five)

    # --------------------------

    IQ_SCORE = 100

    PT("You've reached the gate of the palace,")
    PT("The atmosphere appears to be nighttime and rainy,")
    PT("but beware! It's said that no one has ever come out of it unscathed.")
    PT(
        "Therefore, you are given a "
        + gun_type
        + " for self-defense with only two shots, Use it wisely."
    )
    PT("After entering the palace, you are faced with two paths.")
    PT("The first is the front door, which appears old and rusty.")

    PT("The second path leads to a "
       + back_door
       + " behind the palace, and there are many windows \
overlooking the palace gate.")

    PT("Which path do you want to explore first?")
    PT("(1) Front door")
    PT("(2) the " + back_door)
    user_input = check_letters("USER'S-INPUT")

    if user_input == "1":  # Front Door
        Front_Door()

    elif user_input == "2":  # Back Door
        Back_Door()

    # --------------------------

    IQ_SCORE = Main_Scenario(IQ_SCORE)  # THE MAIN PART OF THE WHOLE STORY

    # Asks The User For Another Loop

    PT("GAME OVER")
    PT("Would you like to play again? (yes/no)")

    another_loop = another_game()

    if another_loop == "yes":
        continue
    elif another_loop == "no":
        print("Thanks for playing")
        break
