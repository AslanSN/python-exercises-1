import random

surnames = ['10', '10', 'juan', '@12', 'null', 'antonioPerezDelCarmen', 'abcdefghtioiasoisdjads', 'Manolo', 'Perez', 'Soledad']
excuses = ['OMG?', 'Whats going on?', 'How much is it?', 'undefined', 'undefined']
names = ['Jeferson', 'Matilda', 'R@fael', '1van', '1van', 'Pep3', 'Loquesea', 'Fel1berto', 'Pepit@', 'D@M']


def excuse_generator (names_list, surnames_list, excuses_list):

    name =  names_list[random.randint( 0, len(names_list) - 1)]
    surname = surnames_list[random.randint ( 0, len(surnames_list) - 1)]
    excuse = excuses_list[random.randint ( 0, len(excuses_list) - 1)]

    print(f"My excuse is that {name} {surname}, {excuse}");

excuse_generator(names, surnames, excuses)


'''
!Counter of chars
@param {list} list
returns printed {dictionary} 'letter_iterations'
'''
def number_of_letters (list):

    letter_iterations = {}

    for item in list:
        for letter in item:
            letter_iterations[letter.upper()] = letter_iterations.get(letter.upper(), 0) + 1

    print(f"Dictionary of number of letters: {dict(sorted(letter_iterations.items()))}")

number_of_letters(names)
number_of_letters(surnames)
number_of_letters(excuses)


''' 
!Convertor
@params {list}
returns setted list
'''
no_more_repetitions = lambda list : set(list)

print(f"List without repetitions: {no_more_repetitions(names)}")
print(f"List without repetitions: {no_more_repetitions(surnames)}")
print(f"List without repetitions: {no_more_repetitions(excuses)}")


'''

!Inverter
@params {list}
returns {list} inverted by Items
'''
def inverted_list (list):

    print(f'Inverted list: {(list[::-1])}')

inverted_list(names)
inverted_list(surnames)
inverted_list(excuses)

