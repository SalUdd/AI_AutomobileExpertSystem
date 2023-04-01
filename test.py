# Import the regex library for pattern matching
import re

# This dictionary contains the rules for the expert system
rules = {
  '1': {
       'question': '\nDoes the engine start?',
       'options': {
           'a': 'Yes',
           'b': 'No'
       },
       'next': {
           'a': '2',
           'b': '4'
       }
  },
  '2': {
       'question': '\nDoes the engine make any unusual noises?',
       'options': {
           'a': 'Yes',
           'b': 'No'
       },
       'next': {
           'a': '3',
           'b': '8'
       }
   },
   '3': {
       'question': '\nWhat kind of noise is the engine making?',
       'options': {
           'a': 'Rattling',
           'b': 'Knocking',
           'c': 'Squeaking'
       },
       'next': {
           'a': '14',
           'b': '15',
           'c': '16'
       }
   },
   '4': {
       'question': '\nDo you see the instrument panel or dashboard lights turn on?',
       'options': {
           'a': 'Yes',
           'b': 'No'
       },
       'next': {
           'a': '5',
           'b': '13'
       }
   },
   '5': {
       'question': '\nPick one for the condition of the battery terminal:',
       'options': {
           'a': 'Corroded/ Dirty',
           'b': 'Loose',
           'c': 'Neither'
       },
       'next': {
           'a': '11',
           'b': '12',
           'c': '6'
       }
   },
   '6': {
       'question': '\nDoes the electrical component like the dome light or other interior lights start bright and then go dim?',
       'options': {
           'a': 'Yes',
           'b': 'No'
       },
       'next': {
           'a': '10',
           'b': '7'
       }
   },
   '7': {
       'question': '\nIs the car in park or neutral?',
       'options': {
           'a': 'Yes',
           'b': 'No'
       },
       'next': {
           'a': '8',
           'b': '9'
       }
   },
   '8': {
       'answer': '\n\033[1mPossible Problem: No issue detected: \033[0m There may be no issues with the engine or other areas of the car. Take the car to the mechanic if the vehicle has issues.\n\n'
   },
   '9': {
       'answer': '\n\033[1mPossible Problem: Put car in Park/ Neutral: \033[0mPut the car in park or neutral and start the car.\n\n'
   },
   '10': {
       'answer': '\n\033[1mPossible Problem: Bad Alternator: \033[0mReplace alternator as soon as possible.\n\n'
   },
   '11': {
       'answer': '\n\033[1mPossible Problem: Corroded or Dirty Battery Terminal: \033[0mTake the car to a mechanic to fix the corrosion/ dirt on battery terminal.\n\n'
   },
   '12': {
       'answer': '\n\033[1mPossible Problem: Battery Terminal is loose: \033[0mTurn off the car. Then twist and turn the cables at the battery terminal.\n\n'
   },
   '13': {
       'answer': '\n\033[1mPossible Problem: Dead Battery: \033[0mYou may have a weak battery and will need to charge or replace the battery.\n\n'
   },
   '14': {
       'answer': '\n\033[1mPossible Problem: Loose or damaged engine part: \033[0m The engine may have a loose or damaged part. Visit a mechanic to fix the issue.\n\n'
   },
   '15': {
       'answer': '\n\033[1mPossible Problem: Bearing Problem: \033[0m The engine may have a bearing problem. Replace bearings.\n\n'
   },
   '16': {
       'answer': '\n\033[1mPossible Problem: Belts or Pulleys problem: \033[0m The engine may have a problem with the belts or pulleys. Replace belts or pulleys.\n\n'
   }
}


# This function is responsible for displaying the question and available options,
# as well as receiving the user's answer and validating it.
def ask_question(question, options):
    # Print the question and options
    print(question)
    
    for option, value in options.items():
        print(option.upper(), value)
    answer = input('\nEnter your choice: ')

    # Get user input and validate it
    while not re.match('[a-zA-Z]+', answer) or answer.lower() not in options:
        if answer.lower() == 'q':
            return 'exit'
        print('Invalid input. Please try again. \n')
        answer = input('Enter your choice: ')
    # Return the user's valid answer
    return answer.lower()

# This function runs the expert system using the provided rules
def run_expert_system(rules):
    # Print the welcome message
    print("\n\033[1mAutomobile Expert System\033[0m")
    print("--------------------------------")
    print("\033[1mChoose options by choosing letters a,b,c,etc\033[0m")

    # Initialize the current question/answer id
    current = '1'

    # Main loop for running the expert system
    while True:
        # Print a message to allow the user to exit the program
        print("\n\033[1mTo exit the program enter option q\033[0m")

        # If the current item is a question, display it and get the user's answer
        if 'question' in rules[current]:
            answer = ask_question(rules[current]['question'], rules[current]['options'])
            if answer == 'exit':
                break

            # Update the current id based on the user's answer
            current = rules[current]['next'][answer]

        # If the current item is an answer, display it and ask the user if they want to run the expert system again
        elif 'answer' in rules[current]:
            print(rules[current]['answer'])
            answer = ask_question('\nDo you want to run the expert system again?', {'a': 'Yes', 'b': 'No'})

            # If the user wants to run the expert system again, reset the current id to '1'

            if answer == 'b':
                break
            current = '1'

            
# Run the expert system
run_expert_system(rules)


