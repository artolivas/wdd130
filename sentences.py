import random

def get_determiner(quantity):
    """Return a randomly chosen determiner.
    If quantity is 1, return a singular determiner.
    Otherwise, return a plural determiner.
    """
    if quantity == 1:
        determiners = ["a", "one", "the"]
    else:
        determiners = ["some", "many", "the"]
    return random.choice(determiners)

def get_noun(quantity):
    """Return a randomly chosen noun.
    If quantity is 1, return a singular noun.
    Otherwise, return a plural noun.
    """
    if quantity == 1:
        nouns = ["bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"]
    else:
        nouns = ["birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"]
    return random.choice(nouns)

def get_verb(quantity, tense):
    """Return a randomly chosen verb.
    If tense is "past", return a past tense verb.
    If tense is "present" and quantity is 1, return a singular present tense verb.
    If tense is "present" and quantity is not 1, return a plural present tense verb.
    If tense is "future", return a future tense verb.
    """
    if tense == "past":
        verbs = ["ate", "thought", "ran", "wrote", "saw"]
    elif tense == "present":
        if quantity == 1:
            verbs = ["eats", "thinks", "runs", "writes", "sees"]
        else:
            verbs = ["eat", "think", "run", "write", "see"]
    elif tense == "future":
        verbs = ["will eat", "will think", "will run", "will write", "will see"]
    return random.choice(verbs)

def get_preposition():
    """Return a randomly chosen preposition
    from this list of prepositions:
        "about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"

    Return: a randomly chosen preposition.
    """
    prepositions = ["about", "above", "across", "after", "along", "around", "at", "before", "behind", "below", "beyond", "by", "despite", "except", "for", "from", "in", "into", "near", "of", "off", "on", "onto", "out", "over", "past", "to", "under", "with", "without"]
    return random.choice(prepositions)

def get_prepositional_phrase(quantity):
    """Build and return a prepositional phrase composed
    of three words: a preposition, a determiner, and a
    noun by calling the get_preposition, get_determiner,
    and get_noun functions.

    Parameter
        quantity: an integer that determines if the
            determiner and noun in the prepositional
            phrase returned from this function should
            be single or plural.
    Return: a prepositional phrase.
    """
    preposition = get_preposition()
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    return f"{preposition} {determiner} {noun}"

def make_sentence(quantity, tense):
    """Create and return a sentence composed of a determiner,
    a noun, a verb, and a prepositional phrase."""
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    verb = get_verb(quantity, tense)
    prepositional_phrase = get_prepositional_phrase(quantity)
    sentence = f"{determiner.capitalize()} {noun} {verb} {prepositional_phrase}."
    return sentence

def main():
    # Generate and print six sentences with different quantities and tenses
    print(make_sentence(1, "past"))
    print(make_sentence(1, "present"))
    print(make_sentence(1, "future"))
    print(make_sentence(2, "past"))
    print(make_sentence(2, "present"))
    print(make_sentence(2, "future"))

if __name__ == "__main__":
    main()
