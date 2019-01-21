"""Dictionaries Assessment

**IMPORTANT:** These problems are meant to be solved using
dictionaries and sets.
"""

def count_words(phrase):
    """Count unique words in a string.

    This function should take a single string and return a dictionary
    that has all of the distinct words as keys and the number of
    times that word appears in the string as values.

    For example::

        >>> print_dict(count_words("each word appears once"))
        {'appears': 1, 'each': 1, 'once': 1, 'word': 1}

    Words that appear more than once should be counted each time::

        >>> print_dict(count_words("rose is a rose is a rose"))
        {'a': 2, 'is': 2, 'rose': 3}

    It's fine to consider punctuation part of a word (e.g., a comma
    at the end of a word can be counted as part of that word) and
    to consider differently-capitalized words as different::

        >>> print_dict(count_words("Porcupine see, porcupine do."))
        {'Porcupine': 1, 'do.': 1, 'porcupine': 1, 'see,': 1}
    """


    word_count = {}


    words = phrase.split()
    

    for word in words:
        if word in word_count:
        #word.endswith(".", ","):
            word_count[word] += 1

        else:
            word_count[word] = 1
    return word_count

#test:
# new_dict_1 = count_words("Porcupine see, porcupine do.")
# print(new_dict_1)
# new_dict_2 = count_words("each word appears once")
# print(new_dict_2)
# new_dict_3 = count_words("rose is a rose is a rose")
# print(new_dict_3)








def print_melon_at_price(price):
    """Given a price, print all melons available at that price, in alphabetical order.

    Here are a list of melon names and prices:

    Honeydew 2.50
    Cantaloupe 2.50
    Watermelon 2.95
    Musk 3.25
    Crenshaw 3.25
    Christmas 14.25
    (it was a bad year for Christmas melons -- supply is low!)

    If there are no melons at that price print "None found"

        >>> print_melon_at_price(2.50)
        Cantaloupe
        Honeydew

        >>> print_melon_at_price(2.95)
        Watermelon

        >>> print_melon_at_price(5.50)
        None found
    """

    # melon_dict = {"Honeydew": 2.50, "Cantaloupe": 2.50, "Watermelon": 2.95, "Musk": 3.25, "Crenshaw": 3.25, "Christmas": 14.25}

    # melon_at_price = []

    # for key, value in melon_dict.items():
    #     if price == value:
    #         melon_at_price.append(key)
#"none found" got printed out so many times??
    #     else:
    #     print("None found")
    # for melon in sorted(melon_at_price):
    #     print(melon)

       

    # #test:
#print_melon_at_price(2.50)


def translate_to_pirate_talk(phrase):
    """Translate phrase to pirate talk.

    Given a phrase, translate each word to the Pirate-speak
    equivalent. Words that cannot be translated into Pirate-speak
    should pass through unchanged. Return the resulting sentence.

    Here's a table of English to Pirate translations:

    ----------  ----------------
    English     Pirate
    ----------  ----------------
    sir         matey
    hotel       fleabag inn
    student     swabbie
    man         matey
    professor   foul blaggart
    restaurant  galley
    your        yer
    excuse      arr
    students    swabbies
    are         be
    restroom    head
    my          me
    is          be
    ----------  ----------------

    For example::

        >>> translate_to_pirate_talk("my student is not a man")
        'me swabbie be not a matey'

    You should treat words with punctuation as if they were different
    words::

        >>> translate_to_pirate_talk("my student is not a man!")
        'me swabbie be not a man!'
    """


    english_to_pirate_dict = {
        'hotel': 'fleabag inn',
        'student': 'swabbie',
        'man': 'matey',
        'professor': 'foul blaggart',
        'restaurant': 'galley',
        'your': 'yer',
        'excuse': 'arr',
        'students': 'swabbies',
        'are': 'be',
        'restroom': 'head',
        'my': 'me',
        'is': 'be'    
        }

    words = phrase.split()

    new_phrase = " "
    for word in words:
        if word in english_to_pirate_dict.keys():
            new_phrase += " " + english_to_pirate_dict[word]
        else:
            new_phrase += " " + word
    return new_phrase
        
#test:
# sentence_1= translate_to_pirate_talk("my student is not a man")
# print(sentence_1)
# sentence_2 = translate_to_pirate_talk("my student is not a man!")
# print(sentence_2)

    


def kids_game(names):
    """Play a kids' word chain game.

    Given a list of names, like::

      bagon baltoy yamask starly nosepass kalob nicky

    Do the following:

    1. Always start with the first word ("bagon", in this example).

    2. Add it to the results.

    3. Use the last letter of that word to look for the next word.
       Since "bagon" ends with n, find the *first* word starting
       with "n" in our list --- in this case, "nosepass".

    4. Add "nosepass" to the results, and continue. Once a word has
       been used, it can't be used again --- so we'll never get to
       use "bagon" or "nosepass" a second time.

    5. When you can't find an unused word to use, you're done!
       Return the list of output words.

    For example::

        >>> kids_game(["bagon", "baltoy", "yamask", "starly",
        ...            "nosepass", "kalob", "nicky", "booger"])
        ['bagon', 'nosepass', 'starly', 'yamask', 'kalob', 'baltoy']

    (After "baltoy", there are no more y-words, so we end, even
    though "nicky" and "booger" weren't used.)

    Two more examples:

        >>> kids_game(["apple", "berry", "cherry"])
        ['apple']

        >>> kids_game(["noon", "naan", "nun"])
        ['noon', 'naan', 'nun']

    This is a tricky problem. In particular, think about how using
    a dictionary (with the super-fast lookup they provide) can help;
    good solutions here will definitely require a dictionary.
    """


    # results = []
    # #add first word in names to an empty list
    # results.append(names[0])

    # #loop over each word in names
    # i = 0
    # for name in names:
    # #find next word whose first letter is the last letter of the previous word added to the list

    #     for letter in name:
    #         if name.startswith(letter) == results[i][-1]:
    #             results.append(name)
    #             i += 1
    # #only one item added to the list??
    # return (results)

#test:
# given_words = ["bagon", "baltoy", "yamask", "starly",
#                "nosepass", "kalob", "nicky", "booger"]
# output_words = kids_game(given_words)
# print(output_words)




