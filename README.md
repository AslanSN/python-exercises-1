
## Python Exercises
#### Importing
```Python
import math
import random
```
#### & due to lists
```Python
names = ['Jeferson', 'Matilda', 'R@fael', '1van', 'Pep3', 'Loquesea', 'Fel1berto', 'Pepit@', 'D@M']
surnames = ['10', '10', 'juan', '@12', 'null', 'antonioPerezDelCarmen', 'abcdefghtioiasoisdjads', 'Manolo', 'Perez', 'Soledad']
excuses = ['OMG?', 'Whats going on?', 'How much is it?', 'undefined', 'undefined']
```

###  1.  Create a function that generates a random excuse with this lists
**My Code:**

Simple function with three vars to save the random item taken of each array with a print including the concatenation of the three vars.

```Python
def excuse_generator (names_list, surnames_list, excuses_list):

    name =  names_list[random.randint( 0, len(names_list) - 1)]
    surname = surnames_list[random.randint ( 0, len(surnames_list) - 1)]
    excuse = excuses_list[random.randint ( 0, len(excuses_list) - 1)]

    print(f"My excuse is that {name} {surname}, {excuse}");

excuse_generator(names, surnames, excuses)
```
**Output ex.:**
```Terminal
My excuse is that D@M 10, OMG?
```

###  2. Create another function that counts the number of repetitions of letters in each array.
**My Code:**

I used a function that has a new dictionary where all the letters and each countered repetition is saved.

I first do a loop to find the items and after that I seek each letter of the item. In this last loop is where I inject the letters counting. 

Using letter_iterations[letter.upper()] I determinate the key of the items coverting the letters into UPPERCASE for having a standard and a good counting of letters (if not low and upper cases are differenciated).

Then I match itself with a `.get` to retrieve the letters in upper case from the item id = 0, when `.get` finds that the letter it exists already it just sums 1 to it.
```Python
def number_of_letters (list):

    letter_iterations = {}

    for item in list:
        for letter in item:
            letter_iterations[letter.upper()] = letter_iterations.get(letter.upper(), 0) + 1

    print(f"Dictionary of number of letters: {dict(sorted(letter_iterations.items()))}")

```
**Output ex.:**
```Terminal
Dictionary of number of letters: {'1': 3, '3': 1, '@': 3, 'A': 6, 'B': 1, 'D': 2, 'E': 9, 'F': 3, 'I': 2, 'J': 1, 'L': 4, 'M': 2, 'N': 3, 'O': 3, 'P': 4, 'Q': 1, 'R': 3, 'S': 2, 'T': 3, 'U': 1, 'V': 2}
```

### 3. Delete repetitions in an array and return the array without the repetition

**My Code:**

For the sake of optimization I used the native `.set` method in a `lambda` function which converts any list received to a `Set` type eliminating all duplicates.
>_It should be noted that the `Set` comes out unordered._

```Python
no_more_repetitions = lambda list : set(list)
```
**Output ex.:**
```Terminal
List without repetitions: {'Loquesea', 'Pepit@', '1van', 'Fel1berto', 'D@M', 'R@fael', 'Jeferson', 'Matilda', 'Pep3'}
```

### 4. Function that inverts all the values in the array
**My Code:**

As the previous exercise I considered to use a `lambda` function due to the very little code needed. 
I used a `Python` shortcut to iterate it backwards. `list[::-1]` understands that you are asking him to iterate the array like this `list[0:list.len():-1]`. 
- The first number sets the item id departure.
	-It interprets that should be the first item of the array.
- The middle one indicates up to which item it should go.  
	-It understands that is the whole list what you want to loop.
- The last number sets up of wich items the iteration must jump, on this one is each item so is one at a time. So how you want to loop it.
	-In this case we are telling him to iterate it in reverse!
```Python
inverted_list = lambda list: list[::-1]
```
**Output ex.:**
```Terminal
Inverted list: ['undefined', 'undefined', 'How much is it?', 'Whats going on?', 'OMG?']
```

------------
## How to run it
Just type `python3 app.py` into the terminal to run it! 

------------
> _Thank you for reading,
>Aslan_
