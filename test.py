import re

rules = {
    '1': {
        'question': '\nDoes the engine make any unusual noises?',
        'options': {
            'a': 'Yes',
            'b': 'No'
        },
        'next': {
            'a': '2',
            'b': '3'
        }
    },
    '2': {
        'question': '\nWhat kind of noise is the engine making?',
        'options': {
            'a': 'Rattling',
            'b': 'Knocking',
            'c': 'Squeaking'
        },
        'next': {
            'a': '4',
            'b': '5',
            'c': '6'
        }
    },
    '3': {
        'answer': '\n\033[1mPossible Problem\033[0m There may be no issues with the engine.\n\n'
    },
    '4': {
        'answer': '\n\033[1mPossible Problem:\033[0m The engine may have a loose or damaged part.\n\n'
    },
    '5': {
        'answer': '\n\033[1mPossible Problem:\033[0m The engine may have a bearing problem.\n\n'
    },
    '6': {
        'answer': '\n\033[1mPossible Problem:\033[0m The engine may have a problem with the belts or pulleys.\n\n'
    }
}

def ask_question(question, options):
    print(question)
    for option, value in options.items():
        print(option.upper(), value)
    answer = input('\nEnter your choice: ')
    while not re.match('[a-zA-Z]+', answer) or answer.lower() not in options:
        if answer.lower() == 'q':
            return 'exit'
        print('Invalid input. Please try again. \n')
        answer = input('Enter your choice: ')
    return answer.lower()

def run_expert_system(rules):
    print("\n\033[1mAutomobile Expert System\033[0m")
    print("--------------------------------")
    print("\033[1mChoose options by choosing letters a,b,c,etc\033[0m")
    current = '1'
    while True:
        
        print("\n\033[1mTo exit the program enter option q\033[0m")
        if 'question' in rules[current]:
            answer = ask_question(rules[current]['question'], rules[current]['options'])
            if answer == 'exit':
                break
            current = rules[current]['next'][answer]
        elif 'answer' in rules[current]:
            print(rules[current]['answer'])
            answer = ask_question('\nDo you want to run the expert system again?', {'a': 'Yes', 'b': 'No'})
            if answer == 'b':
                break
            current = '1'

run_expert_system(rules)
