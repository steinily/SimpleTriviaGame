from numpy import true_divide
import requests
import json
import pandas as pd
import random


# Open trivia database webpage:
# https://opentdb.com/api.php?amount=50

def triviaDataBase():
    try:
        with requests.request('GET', "https://opentdb.com/api.php?amount=50") as webpage:
            data = webpage.json()
            df = pd.DataFrame(data["results"])
            # Need some formating to tweak the readability for questin and answers
            formatting = [
                ("#039;", "'"),
                ("&'", "'"),
                ("&quot;", '"'),
                ("&lt;", "<"),
                ("&gt;", ">"),
                ("&amp;","and" )
            ]
            for i in range(len(formatting)):
                df = df.replace(formatting[i][0],formatting[i][1],regex=True)
            return df
    except:
        print('Connection error  cannot connect to the Trivia Database. Try again later!')


def gameMechanik():
    # In this module from pandas dataframe we collecting a random question , and for the answers.
    #  And we returning this variables to the maingame function
    data = triviaDataBase()
    randomQuestionRow = data.sample()
    question = randomQuestionRow['question'].values[0]
    answers = randomQuestionRow['correct_answer'].values.tolist()
    allanswers = randomQuestionRow['incorrect_answers'].values.tolist()
    allanswers[0].extend(answers)
    random.shuffle(allanswers[0])
    category = randomQuestionRow['category']
    difficulty = randomQuestionRow['difficulty']

    return question, answers, allanswers, category, difficulty


def mainMenu():
    player = input("Hello Player how can i call you?\n ")

    welcome = input(f"Hello {player} do you want to play a game?\n ")

    yeslist = ['Yes', 'YES', 'yes', 'y', 'Y']

    if welcome in yeslist:
        game = True
    else:
        game = False
    print("\n*!Help!* :You need type the full answer\n" )
    while game == True:
        round = input("How many round do you wanna play?\n ")

        print(f"Okay , {player} ! Let's play a game whit {round}'s!\n")

        points = 0

        for i in range(int(round)):
            trivia = gameMechanik()

            print(
                f"\nThis Questin is  : {trivia[4].to_string(index=False)}  in the {trivia[3].to_string(index=False)} category")
            print("Questinon : " + trivia[0] + "\n")

            for i in range(len(trivia[2][0])):

                print(str(i+1) + ". Answers : " + trivia[2][0][i])
            playerasnwer = input(
                f"\nSo {player} what do you think what is the correct answer? \n")
            print(10*'_')
            if playerasnwer.lower() == trivia[1][0].lower():
                points += 1

        print(f"Good game {player}!! \nYou had {points} good answer !!")

        welcome = input("\nDo You wanna play again?\n")
        if welcome in yeslist:
            game = True
        else:
            game = False
    print(f"Thank you for the game good by {player}")


mainMenu()

