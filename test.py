# Import the necessary libraries
import re

# Define the rules of the expert system
rules = {
    '1': {
        'question': 'Does the engine make any unusual noises?',
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
        'question': 'What kind of noise is the engine making?',
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
        'answer': 'There may be no issues with the engine.'
    },
    '4': {
        'answer': 'The engine may have a loose or damaged part.'
    },
    '5': {
        'answer': 'The engine may have a bearing problem.'
    },
    '6': {
        'answer': 'The engine may have a problem with the belts or pulleys.'
    }
}

# Define a function to ask questions and get answers
def ask_question(question, options):
    print(question)
    for option, value in options.items():
        print(option.upper(), value)
    answer = input('Enter your choice: ')
    while not re.match('[a-zA-Z]+', answer) or answer.lower() not in options:
        print('Invalid input. Please try again.')
        answer = input('Enter your choice: ')
    return answer.lower()

# Define a function to run the expert system
def run_expert_system(rules):
    current = '1'
    while True:
        if 'question' in rules[current]:
            answer = ask_question(rules[current]['question'], rules[current]['options'])
            current = rules[current]['next'][answer]
        elif 'answer' in rules[current]:
            print(rules[current]['answer'])
            break

# Run the expert system
run_expert_system(rules)
