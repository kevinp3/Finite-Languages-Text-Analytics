#Contraction expanding function

#Takes a list of contractions and their corresponding expansions and a list of strings
def contraction_expand(contraction_list, list_strings):
    i = 0
    j = 0
    count = 0
    holding_list = list()

    #Do the following for each of the strings in list_strings
    while count < len(list_strings):
        for string in list_strings:
            #This counter tracks how many contractions have been expanded for the current text string
            i = 0
            for word in string.split():
                if word.lower() in contraction_list:
                    if i == 0:
                        #Load the corresponding contraction expansion to the replacement_holder
                        replacement_holder = string.replace(word, contraction_list[word.lower()])
                        #Append the expanded text in the holder above to the holding list
                        holding_list.append(replacement_holder)
                        #This counter keeps track of how many contractions have been expanded total
                        count += 1
                        #Incremented to show there was an expansion for this string.  This is incremented every time there is an expansion for the current string.
                        i += 1
                    #If there has already been one or more contraction expansions, do the following
                    elif i >= 1:
                        replacement_holder = holding_list[count - 1]
                        replacement_holder = replacement_holder.replace(word, contraction_list[word.lower()])
                        holding_list[count - 1] = replacement_holder
            if i == j:
                holding_list.append(string)
                count += 1
            i = 0
            j = 0
