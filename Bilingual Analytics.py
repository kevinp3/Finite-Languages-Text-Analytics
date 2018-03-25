###Very important to identify differences between corrected texts and uncorrected texts
###Some analytics (like lexical diversity) should only be performed on sections of
####text that were correct initially (writers shouldn't get Lexical Diversity credit for
####things they didn't write or things they wrote incorrectly)  This isn't yet implemented
####in the code but should be.  Think about using "import difflib" and "SequenceMatcher".
####Reference https://docs.python.org/2/library/difflib.html

import re

contractions = {
"ain’t": "am not / are not",
"aren’t": "are not / am not",
"can’t": "cannot",
"can’t’ve": "cannot have",
"‘cause": "because",
"could’ve": "could have",
"couldn’t": "could not",
"couldn’t’ve": "could not have",
"didn’t": "did not",
"doesn’t": "does not",
"don’t": "do not",
"hadn’t": "had not",
"hadn’t’ve": "had not have",
"hasn’t": "has not",
"haven’t": "have not",
"he’d": "he had / he would",
"he’d’ve": "he would have",
"he’ll": "he shall / he will",
"he’ll’ve": "he shall have / he will have",
"he’s": "he has / he is",
"how’d": "how did",
"how’d’y": "how do you",
"how’ll": "how will",
"how’s": "how has / how is",
"i’d": "I had / I would",
"i’d’ve": "I would have",
"i’ll": "I shall / I will",
"i’ll’ve": "I shall have / I will have",
"i’m": "I am",
"i’ve": "I have",
"isn’t": "is not",
"it’d": "it had / it would",
"it’d’ve": "it would have",
"it’ll": "it shall / it will",
"it’ll’ve": "it shall have / it will have",
"it’s": "it has / it is",
"let’s": "let us",
"ma’am": "madam",
"mayn’t": "may not",
"might’ve": "might have",
"mightn’t": "might not",
"mightn’t’ve": "might not have",
"must’ve": "must have",
"mustn’t": "must not",
"mustn’t’ve": "must not have",
"needn’t": "need not",
"needn’t’ve": "need not have",
"o’clock": "of the clock",
"oughtn’t": "ought not",
"oughtn’t’ve": "ought not have",
"shan’t": "shall not",
"sha’n’t": "shall not",
"shan’t’ve": "shall not have",
"she’d": "she had / she would",
"she’d’ve": "she would have",
"she’ll": "she shall / she will",
"she’ll’ve": "she shall have / she will have",
"she’s": "she has / she is",
"should’ve": "should have",
"shouldn’t": "should not",
"shouldn’t’ve": "should not have",
"so’ve": "so have",
"so’s": "so as / so is",
"that’d": "that would / that had",
"that’d’ve": "that would have",
"that’s": "that has / that is",
"there’d": "there had / there would",
"there’d’ve": "there would have",
"there’s": "there has / there is",
"they’d": "they had / they would",
"they’d’ve": "they would have",
"they’ll": "they shall / they will",
"they’ll’ve": "they shall have / they will have",
"they’re": "they are",
"they’ve": "they have",
"to’ve": "to have",
"wasn’t": "was not",
"we’d": "we had / we would",
"we’d’ve": "we would have",
"we’ll": "we will",
"we’ll’ve": "we will have",
"we’re": "we are",
"we’ve": "we have",
"weren’t": "were not",
"what’ll": "what shall / what will",
"what’ll’ve": "what shall have / what will have",
"what’re": "what are",
"what’s": "what has / what is",
"what’ve": "what have",
"when’s": "when has / when is",
"when’ve": "when have",
"where’d": "where did",
"where’s": "where has / where is",
"where’ve": "where have",
"who’ll": "who shall / who will",
"who’ll’ve": "who shall have / who will have",
"who’s": "who has / who is",
"who’ve": "who have",
"why’s": "why has / why is",
"why’ve": "why have",
"will’ve": "will have",
"won’t": "will not",
"won’t’ve": "will not have",
"would’ve": "would have",
"wouldn’t": "would not",
"wouldn’t’ve": "would not have",
"y’all": "you all",
"y’all’d": "you all would",
"y’all’d’ve": "you all would have",
"y’all’re": "you all are",
"y’all’ve": "you all have",
"you’d": "you had / you would",
"you’d’ve": "you would have",
"you’ll": "you shall / you will",
"you’ll’ve": "you shall have / you will have",
"you’re": "you are",
"you’ve": "you have"
}

"""END SANDBOX"""
#Import nltk for all text work

"""Importing Packages"""
#Importing NLTK for text analytics, random, FreqDist, PlaintextCorpusReader
import nltk
import random
import string
import os

#Imports necessary for lex D function
from httplib2 import Http
from urllib.parse import urlencode
from xml.etree.ElementTree import fromstring

#FreqDist will allow us to count the useage of each word in a text.
from nltk import FreqDist

#The PlaintextCorpusReader allows us to work with out own imported .txt files
from nltk.corpus import PlaintextCorpusReader

"""Finished Importing Packages"""

"""Defining Functions to be Used"""

#Lex D function that is an alternative to MTLD and HDD and may not be used if
#  MTLD and/ or HDD are found to be accurate.
error_codes = ["'", 'E', 'T', 'D', 'Z']
http = Http()

def find_lex_d(text):
    data = {'input': text}
    response, content = http.request("http://lex-d.herokuapp.com", "POST", urlencode(data))
    if response['status'] != 200:
        if str(content)[2] in error_codes:
            print(content)                    # print error message if error
        else:
            print(float(str(content).split("'")[1]))  # print Lexical diversity score
    else:
        print('Error 200 thrown from server')

# Global trandform for removing punctuation from words
remove_punctuation = str.maketrans('', '', string.punctuation)

#Normal TTR method of lexical diversity.  This will only be used as a checker
#  check the accuracy of MTLD and HDD lexical diversity calculations.
def lexical_diversity(text):
	word_count = len(text)
	vocab_size = len(set(text))
	diversity_score = vocab_size / word_count
	return diversity_score

# MTLD internal implementation to be used in MTLD final function.
def mtld_calc(word_array, ttr_threshold):
    current_ttr = 1.0
    token_count = 0
    type_count = 0
    types = set()
    factors = 0.0
    
    for token in word_array:
        token = token.translate(remove_punctuation).lower() # trim punctuation, make lowercase
        token_count += 1
        if token not in types:
            type_count +=1
            types.add(token)
        current_ttr = type_count / token_count
        if current_ttr <= ttr_threshold:
            factors += 1
            token_count = 0
            type_count = 0
            types = set()
            current_ttr = 1.0
    
    excess = 1.0 - current_ttr
    excess_val = 1.0 - ttr_threshold
    factors += excess / excess_val
    if factors != 0:
        return len(word_array) / factors
    return -1

# MTLD implementation
def mtld(word_array, ttr_threshold=0.72):
    if isinstance(word_array, str):
        raise ValueError("Input should be a list of strings, rather than a string. Try using string.split()")
    if len(word_array) < 50:
        raise ValueError("Input word list should be at least 50 in length")
    return (mtld_calc(word_array, ttr_threshold) + mtld_calc(word_array[::-1], ttr_threshold)) / 2


# HD-D internals

# x! = x(x-1)(x-2)...(1)
def factorial(x):
    if x <= 1:
        return 1
    else:
        return x * factorial(x - 1)

# n choose r = n(n-1)(n-2)...(n-r+1)/(r!)
def combination(n, r):
    r_fact = factorial(r)
    numerator = 1.0
    num = n-r+1.0
    while num < n+1.0:
        numerator *= num
        num += 1.0
    return numerator / r_fact

# hypergeometric probability: the probability that an n-trial hypergeometric experiment results 
#  in exactly x successes, when the population consists of N items, k of which are classified as successes.
#  (here, population = N, population_successes = k, sample = n, sample_successes = x)
#  h(x; N, n, k) = [ kCx ] * [ N-kCn-x ] / [ NCn ]
def hypergeometric(population, population_successes, sample, sample_successes):
    return (combination(population_successes, sample_successes) *\
            combination(population - population_successes, sample - sample_successes)) /\
            combination(population, sample)
    
# HD-D implementation
def hdd(word_array, sample_size=42.0):
    if isinstance(word_array, str):
        raise ValueError("Input should be a list of strings, rather than a string. Try using string.split()")
    if len(word_array) < 50:
        raise ValueError("Input word list should be at least 50 in length")

    # Create a dictionary of counts for each type
    type_counts = {}
    for token in word_array:
        token = token.translate(remove_punctuation).lower() # trim punctuation, make lowercase
        if token in type_counts:
            type_counts[token] += 1.0
        else:
            type_counts[token] = 1.0
    # Sum the contribution of each token - "If the sample size is 42, the mean contribution of any given
    #  type is 1/42 multiplied by the percentage of combinations in which the type would be found." (McCarthy & Jarvis 2010)
    hdd_value = 0.0
    for token_type in type_counts.keys():
        contribution = (1.0 - hypergeometric(len(word_array), sample_size, type_counts[token_type], 0.0)) / sample_size
        hdd_value += contribution

    return hdd_value

#Define plot to be used for Frequency Distribution
def plot_freqdist_freq(fd, max_num=None, cumulative=False, title='Frequency plot', linewidth=2):
        tmp = fd.copy()
        norm = fd.N()
        for key in tmp.keys():
                tmp[key] = float(fd[key]) / norm * 100

        if max_num:
                tmp.plot(max_num, cumulative=cumulative,
                        title=title, linewidth=linewidth)
        else:
                tmp.plot(cumulative=cumulative, 
                        title=title, 
                        linewidth=linewidth)

        return

"""Defining Working Directory"""

#corpus_root will be the file directory where the .txt files for analysis are stored.
corpus_root = '/Users/Bryce/Desktop/Corpora/Texts'
# temporary user input bypass above^^^ input('Input file location of text files for analysis: ')
wordlists = PlaintextCorpusReader(corpus_root, '.*')

"""Combing .txt Files and Loading to List"""

#Load .txt files into list that has .txt file name in odd indexes and separated
#  texts of those .txt files in even indexes.
all_texts = list()
for file in wordlists.fileids():
	if file[-3:] == "txt":
		all_texts.append(file)
		all_texts.append(wordlists.words(file))
test = list()
with open('/Users/Bryce/Desktop/Corpora/Texts/en Ely Bakouche info@elybakouche.com.txt', 'r+', encoding="utf-8") as f:
	alist = [line.rstrip('\n') for line in f]
	for s in alist:
		test.append(str(s))
		
#NOTE THIS EXPANDS CONTRACTIONS BUT IS NOT YET IMPLEMENTED ANYWHERE.  SHOULD BE MADE INTO A FUNCTION
i = 0
j = 0
count = 0
lister = list()

while count < len(test):
    for string in test:
        i = 0
        for word in string.split():
            if word.lower() in contractions:
                if i == 0:
                    hat = string.replace(word, contractions[word.lower()])
                    lister.append(hat)
                    count += 1
                    i += 1
                elif i >= 1:
                    hat = lister[count - 1]
                    hat = hat.replace(word, contractions[word.lower()])
                    lister[count - 1] = hat
        if i == j:
            lister.append(string)
            count += 1
        i = 0
        j = 0
            

"""Lexical Diversity and Frequency Distribution for each Entry in List"""

#Initialize list of .txt file names
text_file_names = list()
        

#Initializing counter i to 0
i = 0

#Initializing list to temporary hold each Frequency Distribution (FreqDist)
#  before it's loaded to a joined list.
freqdist = list()
filtered_texts = list()
import string
#Step through each index of the list with all file names and texts to output
#  corresponding lexical diversity and load a FreqDist list.
while (i*2 < (len(all_texts))):
        #Load filtered_texts wil string list to be worked on
        filtered_texts = all_texts[i *2 + 1]
        #Remove all punctuation from filtered_texts
        filtered_texts = [''.join(c for c in s if c not in string.punctuation) for s in filtered_texts]
        #Remove all empty strings left over from removing punctuation
        filtered_texts = [s for s in filtered_texts if s]
        #Calculate and store FreqDist of each text in an index of freqdist
        #Lowercase all words so capital and lowercase are counted together
        freqdist.append(FreqDist([x.lower() for x in filtered_texts]))
        #Write to new list to be shuffled
        randomized_text = filtered_texts
        #Counter set for next while loop
        j = 0
        #List to hold MTLD values that will be averaged for final score
        random_mtlds = list()
        #Calculate MTLD score more times for shorter texts to get a more
        #  consistent average.  Calculate minumum of 25 times.

        
        if (100000 / (len(randomized_text)) < 25):
                while j < 25:
                        #Shuffle list
                        random.shuffle(randomized_text)
                        #Loading random_mtlds list of length 'j' with mtld values
                        random_mtlds.append(mtld(randomized_text))
                        j += 1
        else:
                while j < (100000 / (len(randomized_text))):
                        #Shuffle list
                        random.shuffle(randomized_text)
                        #Loading random_mtlds list of length 'j' with mtld values
                        random_mtlds.append(mtld(randomized_text))
                        j += 1
                        
        #MTLD Lexical Diversity of list without punctuation and shuffled
        #MTLD shuffle ensures texts represent average writing lexical diversity
        print(all_texts[i * 2], ' MTLD Shuffled Score:', (sum(random_mtlds) / j))
        plot_freqdist_freq(freqdist[i], max_num=15, cumulative=True, title='Frequency plot', linewidth=2)
        i += 1
