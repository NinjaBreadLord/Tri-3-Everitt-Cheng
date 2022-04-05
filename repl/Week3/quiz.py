def start():
    print('Only respond with y/n')
    answer = input('Are you ready for the quiz?')
    score = 0
    total_questions = 4

    if answer.lower() == 'y':
        answer = input('Is this program written in Javascript?')
        if answer.lower() == 'n':
            score += 1
            print('Correct')
        else:
            print('Wrong, it is written in python')


        answer = input('Is Mortensens class the only CSP class during period 3 this trimester?')
        if answer.lower() == 'y':
            score += 1
            print('Correct')
        else:
            print('Wrong, it is')


        answer = input('Is spicy a real flavor')
        if answer.lower() == 'n':
            score += 1
            print('Correct')
        else:
            print('Wrong, spiciness is not a real flavor, it is just pain')


        answer=input('Respond with a whole number and no units; If Bob runs at 3x^2 + 6x - 2 meters per minute how far would he have ran after 10 minutes?')
        if answer.lower()=='1280':
            score += 1
            print('Correct')
        else:
            print('Wrong, Bob would have ran 1280 meters after 10 minutes')
    else:
        print('Try again when you are ready')
        exit()
    mark = (score/total_questions)*100
    print('You scored:',mark, 'percent')
    print('See you next time')

def starter():
    start()