# PyChat 2K17

import random

def start():
    print(" _____   _   _    ___    _____  ______   _____   _____ \n/  __ \ | | | |  / _ \  |_   _| | ___ \ |  _  | |_   _|\n| /  \/ | |_| | / /_\ \   | |   | |_/ / | | | |   | |  \n| |     |  _  | |  _  |   | |   | ___ \ | | | |   | |  \n| \__/\ | | | | | | | |   | |   | |_/ / \ \_/ /   | |  \n \____/ \_| |_/ \_| |_/   \_/   \____/   \___/    \_/  ")
    print()

def end():
    pass

def confirm(question):
    while True:
        answer = input(question + " (y/n)")
        answer = answer.lower()

        if answer in ["y" , "yes", "yup"]:
            return True
        elif answer in ["n", "no", "nope"]:
            return False
   
def has_keyword(statement, keywords):
    statement = " " + statement
    for word in keywords:
        word = " " + word
        if word in statement:
            return True

    return False

def get_question_response():
    responses = ["¯\_(ツ)_/¯",
                 "I dunno.",
                 "Ask again later."]

    return random.choice(responses)
    
def get_random_response():
    responses = ["Uh, huh.",
                 "Oh, that's interesting",
                 "Do you really think so?",
                 "Could we talk about something different?",
                 "That's cool, I guess."]

    return random.choice(responses)

def get_response(statement):
    statement = statement.lower()

    thanks_words = ["thanks", "thank you"]
    lenny_words = ["lenny", "( ͡° ͜ʖ ͡°)", "meme"]
    family_words = [" mother", "father", "brother", "sister"]
    teacher_words = ["cooper"]
    stop_words = ["stop", "quit", "go away", "shut up", "close", "end", "leave"]
    calculator_words = ["calculator"]
    name_change_words = ["change"]

    if len(statement) == 0:
        response = "Say something to me."
    elif has_keyword(statement, name_change_words):
        response = "If you want to change your name, say \"Change name\". If you want to change my name, say \"Change bot name\"."
    elif has_keyword(statement, stop_words):
        response = "If you want to stop talking, say 'Goodbye'."
    elif statement[-1] == "?":
        response = get_question_response()
    elif has_keyword(statement, thanks_words):
        response = "You're welcome! (°͜ʖ°)"
    elif has_keyword(statement, family_words):
        response = "Tell me more about your family."
    elif has_keyword(statement, teacher_words):
        response = "I hear Mr. Cooper's class is really fun."
    elif has_keyword(statement, lenny_words):
        response = "( ͡° ͜ʖ ͡°)"
    elif has_keyword(statement, calculator_words):
        response = "I heard a hundred dollar bill pops out of the computer if you hold the calc button for five minutes. You should really try it."
    else:
        response = get_random_response()

    return response

def play():
    talking = True

    print("Chatbot: Hello, uh... what was your name again?")
    print()
    name = input("Your name: ")
    print()
    print("Chatbot: Ah, I remember now! What I don't remember is my own name.")
    print()
    bot_name = input("Chatbot's name: ")
    print()
    print(bot_name + ": Ah, thanks. I tend to forget things often. In fact, I'll probably forget this conversation before the next time we talk. Anyways, say something to me!")
    print()

    while talking:
        statement = input(name + ": ")

        if statement == "Goodbye":
            talking = False
            
        elif statement == "Change name":
            print("So you want to change your name?")
            print()
            name = input("Your name: ")
            print()
            print("From now on, I will call you " + name + ". Say something to me!")
            print()
            
        elif statement == "Change bot name":
            print("So you want to change my name?")
            print()
            bot_name = input("Chatbot's name: ")
            print()
            print("Alright, my new name is " + bot_name + ". Say something to me!")
            print()
            
        else:
            response = get_response(statement)
            print(bot_name + ": " + response)
            print()

    print(bot_name + ": Goodbye. It was nice talking to you.")

start()

playing = True

while playing:
    play()
    playing = confirm("Would you like to chat again?")

end()
