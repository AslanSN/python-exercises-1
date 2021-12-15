import random

surnames = ['10', '10', 'juan', '@12', 'null', 'antonioPerezDelCarmen', 'abcdefghtioiasoisdjads', 'Manolo', 'Perez', 'Soledad']
excuses = ['OMG?', 'Whats going on?', 'How much is it?', 'undefined', 'undefined']
names = ['Jeferson', 'Matilda', 'R@fael', '1van', '1van', 'Pep3', 'Loquesea', 'Fel1berto', 'Pepit@', 'D@M']

# 1 - crear una funcion que genere una excusa aleatoria con esos datos 
def excuse_generator (names, surnames, excuses):

    name =  names[random.randint( 0, len(names) - 1)]
    surname = surnames[random.randint ( 0, len(surnames) - 1)]
    excuse = excuses[random.randint ( 0, len(excuses) - 1)]

    print(f"My excuse is that {name} {surname}, {excuse}");

excuse_generator(names, surnames, excuses)

# 2 - creeis otra funcion que cuente el numero de repeticiones de letras en cada array
def number_of_letters (list):

    letter_iterations = {}

    for item in list:
        for letter in item:
            if letter.lower() in letter_iterations:
                letter_iterations[letter.lower()] += 1
            else :
                letter_iterations[letter.lower()] = 1

    print(f"Dictionary of number of letters: {letter_iterations}")

number_of_letters(names)
number_of_letters(surnames)
number_of_letters(excuses)


# 3 - suprimir repeticiones en un array y devolver el array sin la repeticion
def no_repetitions (list):

    print(f'List without repetitions {set(list)}')

no_repetitions(names)
no_repetitions(surnames)
no_repetitions(excuses)

# 4 - function que invierta todos los valores de el array

def inverted_list (list):

    print(f'Inverted list: {(list[::-1])}')

inverted_list(names)
inverted_list(surnames)
inverted_list(excuses)

