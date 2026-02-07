# PYTHON Course
# Week 03 - Text based Adventure game
# Author Victor Hugo Neumann
# Purpose:
#   The user is presented with the text description of a scene or 'room'.
#   Along the description, the user is offered two or three choices
#   highlighted in UPPERCASE and a prompt waiting for the response.
#   The user must type the choice, either in uppercase, lowercase or mixed
#   and with the exact spelling. Each choice leads to a different scenario
#   where further choices are offered. The program procedes through the user's
#   choices until one out of several final scenes is reached.

"""
The present version of the game is loosely based on several
spy movies that the author watched through the years.
"""

# Room descriptions and messages

room1000 = """
The plane lands in a foreign airport. You are an undercover agent.
As you go through the hall someone calls you by your real name.
Do you say HI to the person or walk AWAY?"""

room1200 = """
    The person is truly a friend of yours. Do you go together
    for LUNCH or shake hands and go look for a CAB?"""

room1210 = """
        After lunch is over you have the option to pay with
        CASH or CREDIT card. Which do you choose?"""
room1211 = """
            It was great to meet your friend
            and talk about vacation plans!"""
room1212 = """
            Your credit card has reached the limit.
            Your face turns red!"""

room1220 = """
        At the pickup zone you see several BEIGE cabs
        and a BLACK one. Which do you choose?"""
room1221 = """
            You have a ride to your embassy
            and hand down confidential papers.
            Mission accomplished!"""
room1222 = """
            At the end of the ride the cab goes
            into an alley and you are surrounded
            by masked men. You are a prisoner!"""

room1300 = """
    At the end of the corridor there is a SHOP
    and also a TOILETTE. Which one do you go into?"""

room1310 = """
        In the shop you see a PUZZLE magazine and
        a street ATLAS. Which one do you buy?"""
room1311 = """
            You solve the puzzle in page 13 and find
            the location of a counterfeiter shop!"""
room1312 = """
            Using the street atlas you find the way
            to the museum and enjoy the day!"""

room1320 = """
        In the toilette you find a CELL phone, some KEYS
        and a GUN. Which one do you pick?"""
room1321 = """
            You type a secret code in the cell phone and
            receive a greeting from the agency's safe house!"""
room1322 = """
            The keys have the address and room number
            of a luxurious hotel!"""
room1323 = """
            Three police officers come into the toilette
            and arrest you for gun possesion!"""

# Variable answer, to hold the choice of the user.
answer = """
------------
Your ANSWER? """

# Error message
wrong_choice = """
    You mistyped the choice :(
    Try again!"""

# room = 100

# Start playing
print() # empty line

print(room1000) # Display Initial Scene
choice = input(answer).strip().lower()  # Ask for a choice

if choice == "hi":  # If choice is HI
    print(room1200)
    choice = input(answer).strip().lower()
    if choice == "lunch":
        print(room1210)
        choice = input(answer).strip().lower()
        if choice == "cash":
            print(room1211)
        elif choice == "credit":
            print(room1212)
        else:
            print(wrong_choice)
            exit()
    elif choice == "cab":   # If choice is CAB
        print(room1220)
        choice = input(answer).strip().lower()
        if choice =="beige":
            print(room1221)
        elif choice == "black":
            print(room1222)
        else:
            print(wrong_choice)
            exit()
    else:
        print(wrong_choice)
        exit()
        
elif choice == "away":
    print(room1300)
    choice = input(answer).strip().lower()
    if choice == "shop":
        print(room1310)
        choice = input(answer).strip().lower()
        if choice == "puzzle":
            print(room1311)
        elif choice == "atlas":
            print(room1312)
        else:
            print(wrong_choice)
            exit()
    elif choice == "toilette":
        print(room1320)
        choice = input(answer).strip().lower()
        if choice =="cell":
            print(room1321)
        elif choice == "keys":
            print(room1322)
        elif choice == "gun":
            print(room1323)
        else:
            print(wrong_choice)
            exit()
    else:
        print(wrong_choice)
        exit()

else:
    print(wrong_choice)
    exit()

# End of the game
print() # empty line
print("you got to the end!")
# print(str(room))
