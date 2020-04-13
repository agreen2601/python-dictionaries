"""
Create a dictionary with key value pairs to
represent words (key) and its definition (value)
"""
word_definitions = dict()

"""
Add several more words and their definitions
   Example: word_definitions["Awesome"] = "The feeling of students when they are learning Python"
"""

word_definitions["Quarantine"] = "Not awesome"
word_definitions["Power Tower 2500"] = "My saving grace during quarantine"
word_definitions["Backyard"] = "Something I am grateful for during quarantine"
word_definitions["Grocery Store"] = "A place I need to go but don't want to die from weeks later"


"""
Use square bracket lookup to get the definition of two
words and output them to the console with `print()`
"""

print(word_definitions["Quarantine"])
print(f'The Grocery store is {word_definitions["Grocery Store"]}')


"""
Loop over the dictionary to get the following output:
    The definition of [WORD] is [DEFINITION]
    The definition of [WORD] is [DEFINITION]
    The definition of [WORD] is [DEFINITION]
"""

for (word, definition) in word_definitions.items():
    print(f'The definition of {word} is {definition}')