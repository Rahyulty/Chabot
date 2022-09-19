# not really ai just avoiding clogging up main.py with tables / functions
import random as rnd
 
 # no i totally did not type all of these out indiviually 
User_Possible_Greeting = [
    "Hi",
    "Hello",
    "hi",
    "hello",
    "wassup",
    "Wassup",
    "yo",
    "Yo"
]

User_Possible_Question_Feeling = [
    "how r u",
    "how r u?",
    "How are you",
    "How are you?",
    "how are you",
    "how are you?",
    "how are you doing",
    "how are you doing?"
    "how was your day",
    "how was your day?",
    "wsg",
    "whats good",
    "Im good how about you?",
    "Im good how about you",
    "im good how about you",
    "im good how abt u",
    "im good how abt u?",
    
]
Greeting_1 = [
    "Hey!",
    "Hello!",
    "Hi there!",
    "Hey there!",
    "Hey! How’s it going?",

]

Greeting_2 = [
    "Im doing great!",
    "Im a computer I cant feel!",
    "Im doing well",
    # "The person who made me looked up responses for this questions on google!"
    "Horrible"
]


What = [
    "What?",
    "I Didnt understand that. Say that again",
    "I was not programmed to respond to that",
    "Huh?",
]

Questions = [
    "How old are you??",
    "Where are you right now?",
    "What grade are you in?",
    "why are you here right now",
    "How are you?",
    "What is your name",
]

# Generate a randomly generated response from greeting_1 array
def GenerateResponse(response):
    if IsInInput(response, User_Possible_Greeting) == True:
        num = GenerateRandomIndex(Greeting_1)
        return Greeting_1[num]
    elif IsInInput(response, User_Possible_Question_Feeling) == True:
        num = GenerateRandomIndex(Greeting_2)
        return Greeting_2[num]
        return "Response"
    elif response == "code 202":
        exit("code granted, exited")
    elif response == "C2C" or response == "c2c":
        return "Hey you must be the person looking over this. I did some of this school and used my basic knowldge of python modules to create this. This involved a bunch of table maniplulation and random seeding :) (code 202 to exit)"
    else:
        num = GenerateRandomIndex(What)
        return What[num]

# return our possible greetings user can show
def GetPossibleGreetings():
    return User_Possible_Greeting 

def GetPossibleFeelingQuestion():
    return User_Possible_Question_Feeling

# We see if one of their responses are in the possible greetings
# if they are return TRUE / FALSE
def IsInInput(var,array):
    if type(var) == type("string"):
        # print(var in array)
        return var in array


# input handling
def GetUserInput():
    var = input("You: ")
    return var

def DisplayBotResponse(name, response):
    print(name + ": " + response)

def GenerateRandomIndex(array):
    return rnd.randint(0, len(array) - 1)

def AskQuestion():
    var = GenerateRandomIndex(Questions)
    return var