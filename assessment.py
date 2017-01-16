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
    phrase = phrase.split()

    for word in phrase:
        word_count[word] = word_count.get(word, 0) + 1

    return word_count


def get_melon_price(melon_name):
    """Given a melon name, return the price of the melon.

    Here are a list of melon names and prices:
    Watermelon 2.95
    Cantaloupe 2.50
    Musk 3.25
    Christmas 14.25
    (it was a bad year for Christmas melons -- supply is low!)

    If melon name does not exist, return 'No price found'.

        >>> get_melon_price('Watermelon')
        2.95

        >>> get_melon_price('Musk')
        3.25

        >>> get_melon_price('Tomato')
        'No price found'
    """
    melon_prices_dict = {"Watermelon": 2.95, "Cantaloupe": 2.50, "Musk": 3.25, "Christmas": 14.25}

    melon_price = melon_prices_dict.get(melon_name, "No price found")
    
    return melon_price


def word_length_sorted(words):
    """Return list of word-lengths and words.

    Given a list of words, return a list of tuples, ordered by
    word-length. Each tuple should have two items --- a number that
    is a word-length, and the list of words of that word length.

    In addition to ordering the list by word length, order each
    sub-list of words alphabetically.

    For example::

        >>> word_length_sorted(["ok", "an", "apple", "a", "day"])
        [(1, ['a']), (2, ['an', 'ok']), (3, ['day']), (5, ['apple'])]

        >>> word_length_sorted(["porcupine", "ok"])
        [(2, ['ok']), (9, ['porcupine'])]
    """
    word_length_dict = {}

    for word in words:
        same_length_words = word_length_dict.get(len(word), [word])

        if word_length_dict.get(len(word)) is not None:
            same_length_words.append(word)
            word_length_dict[len(word)] = sorted(same_length_words)
        else:
            word_length_dict[len(word)] = same_length_words

    word_length_list = sorted(word_length_dict.items())

    return word_length_list


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

    eng_pirate_dict = {'sir': 'matey', 'hotel': 'fleabag inn', 'student': 'swabbie', 'man': 'matey',
                        'professor': 'foul blaggart', 'restaurant': 'galley', 'your': 'yer',
                        'excuse': 'arr', 'students': 'swabbies', 'are': 'be', 'restroom': 'head',
                        'my': 'me', 'is': 'be'}

    translated_phrase = []
    phrase = phrase.split()

    for word in phrase:
        new_word = eng_pirate_dict.get(word, word)
        translated_phrase.append(new_word)

    return ' '.join(translated_phrase)


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

    # names = names.split()
    print_list = [names[0]]
    game_dict = {}


    # builds list of possible word pairs
    def add_words_to_dict(key_word, remaining_words):
        value_word_list = []
        remaining_words = remaining_words[1:]

        for word in remaining_words:  
            if key_word[-1] is word[0]:
                value_word_list.append(word)

        return value_word_list

    # build initial dictionary
    for word in names:
        game_dict[word] = add_words_to_dict(word, names)

    # checks potential next word against current list to prevent duplicates
    def check_for_duplicate(possible_words, current_list):
        i = 0
        next_word = possible_words[0]

        while next_word in current_list:
                next_word = possible_words[i + 1]
                i += 1

        return next_word


    # builds output list
    def add_words_to_end_list(end_list):

        possible_word_values = game_dict.get(end_list[-1])
        
        # tried a while loop here but kept encountering an IndexError at line 228
        if possible_word_values != []:

            word_added = check_for_duplicate(possible_word_values, end_list)
            print_list.append(word_added)
            possible_word_values = game_dict.get(end_list[-1])
            

        return print_list

    # was having a hard time looping this to produce a continuous list (not a list within a list)
    # without an index error that was occurring in line 228 with the check_for_duplicate function
    # no errors, but not quite working correctly.
    add_words_to_end_list(print_list)
    
    return print_list

#####################################################################
# You can ignore everything below this.

def print_dict(d):
    # This method is used to print dictionaries in key-alphabetical
    # order, and is only for our doctests. You can ignore it.
    if isinstance(d, dict):
        print "{" + ", ".join(
            "%r: %r" % (k, d[k]) for k in sorted(d)) + "}"
    else:
        print d


if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"
    print
