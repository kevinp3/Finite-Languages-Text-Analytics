"""Functions necessary to expand contractions.
"""


def contraction_expand(contractions, strings):
    """Replace contractions found in the strings with their expanded form.
        Count the number of possible contractions, and the
        number that we actually contracted.
        That is, given ["You are what you're"], return
        ["You are what you are"], 2 possible contractions, 1 actual

        For extra credit, maintain capitalization.

        It may be necessary for contractions dict to include capitalized forms,
        but for now I asume it doesn't -- I'll add them myself.

    :param contractions: a dict mapping contractions to expansions
    :param strings: list of "sentences" to evaluate
    :return: tuple(revised_strings, n_possible, n_contracted)
    """
    res = []
    n_possible = 0
    n_contracted = 0

    # I'm going to expand the given contractions in several ways, but I don't want to munge the original
    full = contractions.copy()

    # Bryce's contractions use a unicode char for the apostrophe, which might be correct, but...
    # I don't even know how to type it, so I expect lots of contributors will use
    # a single quote instead.  Rather that argue, I'll add the "wrong" form to the dict
    wonky = chr(8217)
    extra = {}
    for cont, expansion in full.items():
        wrong = cont.replace(wonky, "'")
        if wrong != cont:
            extra[wrong] = expansion
    full.update(extra)

    # Add capitalized forms of contractions
    # that way, I won't have to think about caps in my main loop.
    extra = {}
    for cont, expansion in full.items():
        # the capitalized var names break PEP8, but makes it easier to follow, IMHO
        Cont = cont[0].upper() + cont[1:]
        Expansion = expansion[0].upper() + expansion[1:]
        extra[Cont] = Expansion
    full.update(extra)

    # from contractions, build a reverse dict so I can look for un-contracted possibles
    # firsts['you'] = [(2,('you', 'are')),
    #                  (2, ('you', 'will')),
    #                 ]
    firsts = {}
    for cont, expansion in full.items():
        e_words = expansion.split()
        firsts.setdefault(e_words[0], []).append((len(e_words), e_words))

    # Begin
    for ll, line in enumerate(strings):
        line_words = line.split()
        new_words = []
        ww = 0
        while ww < len(line_words):
            word = line_words[ww]

            # by returning () instead of None, the loop below won't do anything,
            # without needed an extra if: block around it
            possible_uncontractions = firsts.get(word, ())

            consumed = False
            for n_words, words in possible_uncontractions:
                test = line_words[ww:ww + n_words]
                if test == words:
                    # I am at the start of a phrase that could've been contracted but wasn't
                    # add these words to the result, increment bookkeeping
                    consumed = True
                    new_words.extend(test)
                    ww += n_words
                    n_possible += 1
                    break

            # If I didn't consume word, maybe it is a contraction
            if not consumed:
                expansion = full.get(word)
                if expansion:
                    # it is a contraction
                    # add the expansion to the result, increment bookkeeping
                    new_words.append(expansion)
                    ww += 1
                    n_possible += 1
                    n_contracted += 1

                else:
                    # not a contraction, keep original
                    new_words.append(word)
                    ww += 1

        new_line = ' '.join(new_words)
        res.append(new_line)

    return res, n_possible, n_contracted


# #Takes a list of contractions and their corresponding expansions and a list of strings
# def contraction_expand(contraction_list, list_strings):
#     i = 0
#     j = 0
#     count = 0
#     holding_list = list()
#
#     #Do the following for each of the strings in list_strings
#     while count < len(list_strings):
#         for string in list_strings:
#             #This counter tracks how many contractions have been expanded for the current text string
#             i = 0
#             for word in string.split():
#                 if word.lower() in contraction_list:
#                     if i == 0:
#                         #Load the corresponding contraction expansion to the replacement_holder
#                         replacement_holder = string.replace(word, contraction_list[word.lower()])
#                         #Append the expanded text in the holder above to the holding list
#                         holding_list.append(replacement_holder)
#                         #This counter keeps track of how many contractions have been expanded total
#                         count += 1
#                         #Incremented to show there was an expansion for this string.  This is incremented every time there is an expansion for the current string.
#                         i += 1
#                     #If there has already been one or more contraction expansions, do the following
#                     elif i >= 1:
#                         replacement_holder = holding_list[count - 1]
#                         replacement_holder = replacement_holder.replace(word, contraction_list[word.lower()])
#                         holding_list[count - 1] = replacement_holder
#             if i == j:
#                 holding_list.append(string)
#                 count += 1
#             i = 0
#             j = 0


def test_me():
    """
    Simple tests.  Usually these would be in unittests, but that's a bridge to far, today.
    """
    import json

    # test english
    fpath = 'config/english/rules.json'
    rules = json.load(open(fpath))
    conts = rules['contractions']
    test_strings = [
        "This is not a test",
        "This ain't a test",
        "You are what you're",
        "It's what it is",
    ]
    expanded, n_possible, n_found = contraction_expand(conts, test_strings)
    for a,b in zip(test_strings, expanded):
        print(repr(a), " => ", repr(b))
    print ("n_possible: ", n_possible, "n_found: ", n_found)

    # try loading french.  It has unicode....
    # I would try some french expansions...but I don't know any french to expand
    fpath = 'config/french/rules.json'
    rules = json.load(open(fpath))


# this little line means that the following will only run if the
# file is invoked from the command line, not via import
if __name__ == '__main__':
    test_me()