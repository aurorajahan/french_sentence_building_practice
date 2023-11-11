from random import choice
import keyboard

subject_list = ['I', 'you (informal)', 'he', 'she', 'one', 'we', 'you (formal)', 'they (masculine)', 'they (feminine)']

verb_list = ['admire', 'help', 'love', 'like', 'add', 'bring', 'arrive', 'burn', 'sing', 'count', 'cut', 'cost', 'dance',
             'have lunch', 'ask', 'remain', 'stay', 'dine', 'have dinner', 'ring', 'call', 'give', 'listen to', 'enter',
             'study', 'close', 'live in', 'play', 'climb', 'go up', 'show', 'speak', 'think', 'cry', 'weep', 'carry', 'wear',
             'fall', 'work', 'find', 'begin', 'accomplish', 'build', 'choose', 'obey', 'punish', 'fill', 'succeed', 'wait',
             'defend', 'forbid', 'go down', 'exit a vehicle', 'hear', 'lose', 'give back', 'answer', 'stretch']

negative_list = ['affirmative', 'negative']

question_list = ['declarative', 'interrogative']

imperative_list = ['not imperative', 'imperative']

def make_choice(subject_list, verb_list, negative_list, question_list, imperative_list):
    subject = choice(subject_list)
    verb = choice(verb_list)
    negative = choice(negative_list)
    question = choice(question_list)
    if question == 'declarative':
        if subject == 'you (informal)' or subject == 'you (formal)' or subject == 'we':
            imperative = choice(imperative_list)
        else:
            imperative = 'not imperative'
    else:
        imperative = 'not imperative'
        
    return subject, verb, negative, question, imperative

def print_choice(subject, verb, negative, question, imperative):
    if negative == 'affirmative':
        if imperative == 'imperative':
            print(f'Make an {negative}, {question}, {imperative} sentence with {subject} and {verb}.')
        else:
            print(f'Make an {negative}, {question} sentence with {subject} and {verb}.')
    else:
        if imperative == 'imperative':
            print(f'Make a {negative}, {question}, {imperative} sentence with {subject} and {verb}.')
        else:
            print(f'Make a {negative}, {question} sentence with {subject} and {verb}.')

while True:
    current_event = keyboard.read_event()
    
    if current_event.event_type == 'up':
        continue
    elif current_event.name == 'space':
        subject, verb, negative, question, imperative = make_choice(subject_list, verb_list, negative_list, question_list, imperative_list)
        print_choice(subject, verb, negative, question, imperative)
    elif current_event.name == 'esc':
        break
    else: 
        continue
