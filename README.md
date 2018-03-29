# Finite-Languages-Text-Analytics

The basic setup:

Non-native authors write texts in their non-native language.  A native speaker then corrects this text and several metrics are analyzed (explained below).  All data is saved in a MySQL database with columns as follows: Name, Target Language, Target Text Uncorrected, Target Text Corrected, Native French Text, Native English Text, Native German Text, Native Italian Text.  The code will have to pull all necessary information from these columns if triggered by a row being updated in the 'Target Text Corrected' column.  This will always be the last information added to the database.
    
Several example files are included in the repository for testing (at this time they do not follow this format above, will fix)

The Finite Languages code is used to compare native author writing style to that of non-natives on five key metrics:
    1.    Correction Differences
    2.    Lexical Diversity
    3.    Average Word Length
    4.    Average Sentence Length
    5.    Word Frequency Distribution Comparison
    
Correction Differences:  This will need to be determined for most of the following metrics.  For the text being analyzed, four outputs will be generated having to do with the corrected vs. non-corrected text.
    1.    Text string of all text that was not corrected (written correctly by the non-native author)
    2.    Text string of all sentences that were not corrected (sentences where no corrections were present)
    3.    Percentage changed (percentage of words that underwent corrections)
(1) and (2) will be used to determine other metrics later on but (3) will be one of the five metrics used in the final grade.

Lexical Diversity:  Lexical diversity is essentially the ration of unique words to the total amount of words.  However, Finite Languages uses a mix of MTLD and HD-D to determine the Lexical Diversity score.  This score is usually above 100 and is meaningless without comparing it to the native text.  Therefore, the output is always the percentage of the non-native lexical diversity divided by the native text lexical diversity.  A perfect score is 100% with anything above or below being 'less native sounding' (ex.  105% lexical diversity compared to native speakers is actually a bad thing... we are aiming for 100% exactly).  Lexical diversity is found in the following steps:
    1.    Use only (1) from Correction Differences (text string of all text that was not corrected).  Authors should not get credit for words written incorrectly to their lexical diversity score.
    2.    Removing punctuation of writing (punctuation should not count as a word)
    3.    Expanding all contractions (expanding all contractions in each language so each word is counted accurately)
    4.    Randomizing words (the way lexical diversity is calculated, word order matters.  The way to get the most accurate results is to have the words randomized.
    5.    Solve for lexical diversity.
    6.    Perform steps (4) and (5) multiple times (more times for shorter texts since shorter texts will have the greatest variance between trials) and take an average of the results to get the Lexical Diversity score.  It is necessary to do this multiple times because you will get a slightly different lexical diversity score on each pass, depending on the order of randomized words.
    
Average Word Length:  This is the average word length of the non-native's text.  As with the lexical diversity score, the author's average word length should not be above OR below the result of the average word length for a native speaker (100% is perfect, < or > results in a lower grade).  Use only (1) from Correction Differences (text string of all text that was not corrected).  Authors should not get credit for words written incorrectly to their average word length.

Average Sentence Length:  This is the average sentence of the non-native's text.  As with the lexical diversity score, the author's average word length should not be above OR below the result of the average word length for a native speaker (100% is perfect, < or > results in a lower grade).  Use only (2) from Correction Differences (text string of all sentences that were not corrected).  Authors should not get credit for sentences written incorrectly to their average word length.

Word Frequency Distribution Comparison:  ***Definition still in progress

Final Student Score

Along with the results and charts from the above metrics, students will get a singular score.  This will be weighted as such
    32% Percentage Corrected
    30% Lexical Diversity
    18% Average Word Length
    13% Average Sentence Length
    7%  Word Frequency Distribution Comparison
