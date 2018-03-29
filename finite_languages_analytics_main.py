###Very important to identify differences between corrected texts and uncorrected texts
###Some analytics (like lexical diversity) should only be performed on sections of
####text that were correct initially (writers shouldn't get Lexical Diversity credit for
####things they didn't write or things they wrote incorrectly)  This isn't yet implemented
####in the code but should be.  Think about using "import difflib" and "SequenceMatcher".
####Reference https://docs.python.org/2/library/difflib.html


"""IMPORTING PACKAGES AND FUNCTIONS"""

#Importing packages to be used for text analysis, calculations, and directories
import nltk
import random
import string
import os
import re
import sys

#FreqDist will allow us to count the useage of each word in a text.
from nltk import FreqDist

#The PlaintextCorpusReader allows us to work with out own imported .txt files
from nltk.corpus import PlaintextCorpusReader

"""SET THE DIRECTORY LOCATION WHERE THE FUNCTION MODULES ARE KEPT"""
#module_root = input('Input directory location of modules where functions are kept: ')
#sys.path.insert(0, module_root)

"""IMPORTING USER DEFINED FUNCTIONS FROM FILES"""

#Lists of contractions that are referenced for contraction expansion with the contraction_expand function
from italian_list_of_contractions import *
from english_list_of_contractions import *

#Expands the contractions into their full form
#contraction_expand(contraction_list, list_strings)
from contraction_expand import *

#Plots the frequency distribution of words
#plot_freqdist_freq(fd, max_num=None, cumulative=False, title='Frequency plot', linewidth=2)
from FreqDist_plot import *

#This file holds both MTLD and HDD functions
#hdd(word_array, sample_size=42.0)
#mtld(word_array, ttr_threshold=0.72)
from all_lexical_diversity_functions import *

"""Defining Directory Location of Texts"""

#corpus_root will be the file directory where the .txt files for analysis are stored.
corpus_root = input('Input file location of text files for analysis: ')
wordlists = PlaintextCorpusReader(corpus_root, '.*')

"""Combing .txt Files and Loading to List"""

#Load .txt files into list that has .txt file name in odd indexes and separated
#  texts of those .txt files in even indexes.
all_texts = list()
for file in wordlists.fileids():
	if file[-3:] == "txt":
		all_texts.append(file)
		all_texts.append(wordlists.words(file))

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
