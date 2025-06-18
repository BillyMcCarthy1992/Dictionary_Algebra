import re


def closed(dictionary, stopwords=None):
    if stopwords is None:
        stopwords = set()  # No stopwords by default

    keys = set(word.lower() for word in dictionary)
    words_in_defs = set()

    for definition in dictionary.values():
        # Extract words ignoring punctuation using regex
        words = re.findall(r'\b\w+\b', definition.lower())
        words_in_defs.update(words)

    words_to_check = words_in_defs - stopwords
    undefined_words = words_to_check - keys

    is_closed = len(undefined_words) == 0

    print("Dictionary is closed:" if is_closed else "Dictionary is NOT closed.")
    print(f"Number of undefined words: {len(undefined_words)}")

    if not is_closed:
        with open("undefined_words.txt", "w") as f:
            for word in sorted(undefined_words):
                f.write(word + "\n")
        print("Undefined words saved to 'undefined_words.txt'.")

    return is_closed


def useful(dictionary):
    keys = set(word.lower() for word in dictionary)
    words_in_defs = set()

    for definition in dictionary.values():
        words = re.findall(r'\b\w+\b', definition.lower())
        words_in_defs.update(words)

    useless_keys = keys - words_in_defs
    is_useful = len(useless_keys) == 0

    print("Dictionary is useful:" if is_useful else "Dictionary is NOT useful.")
    print(f"Number of useless (unused) entries: {len(useless_keys)}")

    if not is_useful:
        with open("useless_keys.txt", "w") as f:
            for word in sorted(useless_keys):
                f.write(word + "\n")
        print("Useless keys saved to 'useless_keys.txt'.")

    return is_useful


def gen_book(dictionary, word):
    if word not in dictionary:
        return set()

    expanded = set([word])
    while True:
        new_expanded = set(expanded)
        for w in expanded:
            if w in dictionary:
                definition = dictionary[w].lower()
                words = set(re.findall(r'\b\w+\b', definition))
                new_expanded.update(words)
        if new_expanded == expanded:
            break
        expanded = new_expanded   
    return expanded

# Minimally closed: is closed and has no non-empty closed sub-dictionaries #
# I have a theorem showing that this is equivalent to the condition that for all x in D, the book of x is identical to D #
def minimally_closed(dictionary):
    x = set()
    y = set(dictionary.keys())
    
    for key in dictionary:
        x.add(frozenset(gen_book(dictionary, key)))
        
    if all(book == y for book in x):
        print("The dictionary is minimally closed.")
        return True
    else:
        print("The dictionary is not minimally closed.")
        return False
        
    return all(book == y for book in x)






# Kerneled: has a non-empty minimally closed sub-deictionary #
# I have a theorem showing that a dictionary contains a non-empty minimally closed sub-dictionary just in case ... #
# ... it has an entry x, whose book B(x), is the same as the book of every word in B(x) #
def kerneled(dictionary):
    kernels = []
    
    for key in dictionary:
        book = gen_book(dictionary, key)
        if book and all(gen_book(dictionary, word) == book for word in book):
            kernels.append(book)
    
    if kernels:
        print("This dictionary is kerneled.")
        print("Minimally closed subdictionaries found:")
        for kernel in kernels:
            print(kernel)
        return True
    else:
        print("This dictionary is not kerneled.")
        return False
    



import nltk
from nltk.corpus import wordnet as wn
from collections import defaultdict

# Download WordNet if not already available
nltk.download('wordnet')

# Use defaultdict to concatenate definitions
english_dict = defaultdict(str)

for synset in wn.all_synsets():
    definition = synset.definition().lower()
    for lemma in synset.lemmas():
        word = lemma.name().lower()
        english_dict[word] += ' ' + definition

# Optional: Clean up leading/trailing whitespace
english_dict = {word: defs.strip() for word, defs in english_dict.items()}


gen_book(english_dict, 'love')
