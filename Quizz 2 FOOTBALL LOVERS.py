def some_Game(start,name,numb):
    '''Author: Raymond
    Game: FOOTBALL LOVERS
    Version: 1.0
    © 2021 RAYMOND. All rights reserved.

    This is a program for the demo of a multiple-choice Quiz,
    which will be presented at an event. The aim is to make is
    to make it interactive and user-friendly.'''
        
    # setting the condition for starting the game
    if start == 'play' and (numb == 3 or numb == 7 or numb == 10):
        Copyright="© 2021 RAYMOND, {0}. All rights reserved.";
        Game_name="FOOTBALL LOVERS";
        Message="""\nWelcome, welcome to {0}, {1}. {0} is a multiple-choice quiz that is fully interactive.
        To beat the game, you'll have to answer a series of questions correctly.
        So your aim should be to score as many points as possible.
        There's no timer, so take your time answering the questions.
        The rules of {0} are simple:
        Once a question is posed, you'll be given three options: a, b and c.
        Use your judgement to select the correct answer. That means you can only choose a, b or c.
        When entering your answer, ensure that you use a lowercase letter.
        Take the following example:
        Q1. Which team has been crowned European champions in 2021?
        a. Manchester City (0)
        b. Barcelona FC (0)
        c. Chelsea FC (10)
        If you feel a is the correct answer, when prompted, enter simply the letter a."""
        print(Copyright.format(Game_name))
        print(Message.format(Game_name, name))
        user_input=input('\nAre you happy to play the game with those rules? ');

        # We either start the game or stop it depending on user input
        if user_input == "y":
            listQuestions=["\n\nQ. Which team has been crowned English Premier league champions in 2021?",
                           "\n\nQ. Which team has been crowned European champions in 2021?",
                           "\n\nQ. Which team was the winner of the Carabao Cup in 2021?",
                           "\n\nQ. Which team was the winner of the 2021 FA Cup?",
                           "\n\nQ. Who is the English Premier League best goal scorer 2020/2021?",
                           "\n\nQ. Who is the top scorer in Europa league in 2021?",
                           "\n\nQ. Who was elected man of the match in Europa league final in 2021?",
                           "\n\nQ. Who is the French League best goal scorer 2020/2021?",
                           "\n\nQ. Which team was the winner of the 2021 French League?",
                           "\n\nQ. Who won the Europa league in 2021?"];   
            listChoices=["\na. Liverpool FC  \nb. Manchester City \nc. Manchester United",
                         "\na. Manchester City \nb. Barcelona \nc. Chelsea FC",
                         "\na. Manchester City \nb. Tottenham Hotspurs \nc. Leicester City",
                         "\na. Leicester City \nb. Chelsea FC \nc. Arsenal",
                         "\na. Harry Kane \nb. Mohamed Salah \nc. Bruno Hernandez",
                         "\na. Edin Dzeko \nb. Munas Dabur \nc. Edinson Cavani",
                         "\na. Étienne René Capou \nb. Killian Mbape \nc. Leo Messi", 
                         "\na. Memphis Depay \nb. Killian Mbape \nc. Wissam Ben Yedder",
                         "\na. Paris Saint Germain \nb. Marseille \nc. Lille LOSC",
                         "\na. Real Madrid \nb. Villareal CF \nc. Manchester United"];
            correct_answers=["b","c","a","a","a","c","a","b","c","b"];
            # make a new list of questions wih answers:
            newList=[listQuestions[0]+listChoices[0],listQuestions[1]+listChoices[1]],
            [listQuestions[2]+listChoices[2],listQuestions[3]+listChoices[3]],
            [listQuestions[4]+listChoices[4],listQuestions[5]+listChoices[5]],
            [listQuestions[6]+listChoices[6],listQuestions[7]+listChoices[7]],
            [listQuestions[8]+listChoices[8],listQuestions[9]+listChoices[9]];
                        # computer chooses a question at random:
            import random
            AI_question=random.choice(newList);
            print(AI_question)
            answer_input=input('\nEnter your answer:')
            pos_AI_ques=int(newList.index(AI_question))
                        
            if user_input == "n":
                print('\nSad to see you go {0}. Till you next time!!'.format(name))
            else:
                while user_input != "n" or user_input != "y":
                    print('\nYou can only enter lowercase letters as your answer: n, to quit game or y,\n to play game.')
                    new_input=input('\nAre you happy to play the game with those rules? ');     
                    if new_input == "y":
                        print('o')
                        break
                    elif new_input == "n":
                        print('\nSad to see you go {0}. Till you next time!!'.format(name))
                    break
    # catching some errors: 
    elif start != "play":
        print('You must enter the word "play" into the function to continue', end='.')
    elif type(numb) != int or numb <= 0:
        print('\nYou must enter into the function an integer,\ni.e., whole numbers positive or negative, that is postive.\nDo not enter decimals, e.g., 1.0.')
    elif numb != int(3) or numb != int(5):
        print('\nYou can only choose a 3 or 7 or 10 question round.\nPlease enter 3 or 7 or 10 into the function.')
