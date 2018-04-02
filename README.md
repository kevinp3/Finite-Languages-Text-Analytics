# Finite-Languages-Text-Analytics

## The basic setup:

Non-native authors write texts in their non-native language.  A native speaker then corrects this text and several metrics are analyzed (explained below).  All data is saved in a MySQL database.  The code will have to pull all necessary information from these columns if triggered by a row being updated in the column where corrected text is stored.  This will always be the last information added to the database and is needed for all of the following calculations.
    
*Several example files are included in the repository for testing (at this time they do not follow this format above, will fix)

The Finite Languages code is used to compare native author writing style to that of non-natives on five key metrics:

1. Correction Differences
2. Lexical Diversity
3. Average Word Length
4. Average Sentence Length
5. Word Frequency Distribution Comparison
    
##### Correction Differences
Each submission is corrected by a native speaker.  The corrected and uncorrected versions of the text are compared and the resulting strings below are stored.

1. Text string of all text that was not corrected (written correctly by the non-native author)
2. Text string of all sentences that were not corrected (sentences where no corrections were present)
3. Percentage changed (percentage of words that were corrected)

*NOTE: (1) and (2) will be used to determine other metrics later on but (3) will be one of the five metrics used in the final grade.

##### Lexical Diversity
Lexical diversity is essentially the ratio of unique words to the total amount of words.  However, Finite Languages uses MTLD to determine the Lexical Diversity score.  This score is usually above 100 and is meaningless without comparing it to the native text.  Therefore, the output is always the percentage of the non-native lexical diversity divided by the average native text lexical diversity (pull and perform lexical diversity test on native text from database for compare).  A perfect score is 100% with anything above or below being 'less native sounding' (ex.  105% lexical diversity compared to native speakers is actually a bad thing)

OUTPUTS
> 100% - 'percent difference' = lexical diversity percentage

*Lexical diversity is found in the following steps:

1. Use only (1) from Correction Differences (text string of all text that was not corrected).  Authors should not get credit for words written incorrectly to their lexical diversity score.
2. Removing punctuation of writing (punctuation should not count as a word)
3. Expanding all contractions (expanding all contractions in each language so each word is counted accurately)
4. Randomizing words (the way lexical diversity is calculated, word order matters.  The way to get the most accurate results is to have the words randomized.
5. Solve for lexical diversity.
6. Perform steps (4) and (5) multiple times (more times for shorter texts since shorter texts will have the greatest variance between trials) and take an average of the results to get the Lexical Diversity score.  *It is necessary to do this multiple times because you will get a slightly different lexical diversity score on each pass, depending on the order of randomized words.*
    
##### Average Word Length
This is the average word length of the non-native's text.  As with the lexical diversity score, the author's average word length should not be above OR below the result of the average word length for a native speaker.  Use only (1) from Correction Differences (text string of all text that was not corrected).  Authors should not get credit for words written incorrectly to their average word length.

OUTPUTS
> Average Word Length Score = 100% - %-Difference
> User Average Word Length
> Native Average Word Length

##### Average Sentence Length
This is the average sentence of the non-native's text.  As with the lexical diversity score, the author's average sentence length should not be above OR below the result of the average sentence length for a native speaker.  Use only (2) from Correction Differences (text string of all sentences that were not corrected).  Authors should not get credit for sentences written incorrectly to their average word length.

OUTPUTS
> Average Sentence Length Score = 100% - %-Difference
> User Average Sentence Length
> Native Average Sentence Length

##### Word Frequency Distribution Comparison
A frequency distribution of the top 20 words used by native speakers will be compared to the top 30 words used by the user.  This frequency distribution will be compared to the total number of words in the text so each word is evaluated as a percent-of-total value.  For example:  A native English writer may see the following frequency distribution {the: 0.08, a: 0.06, an: 0.05...} while a non-native English writer may see the following {the: 0.10, a: 0.04, an: 0.05...}.  The percent difference for each word is calculated.  In the example the corresponding percent differences between the user and the native are {the: 22.22%, a: 40.00%, an: 0.00%}.  Therefore, the final, unweighted score is (average of top 20 words used by the native speaker) 100% - 20.74% = 79.26%.  However, words at the top of the list (most common words) should be weighted higher than words at the bottom of the list that may change more depending on topic.  Therefore, the top 20 %-difference scores will be weighted as follows:

> 1: 14%, 2: 12%, 3: 11%, 4: 10%, 5: 9%, 6: 8%, 7: 7%, 8: 6%, 9: 5%, 10: 5%, 11: 4%, 12: 3%, 13: 3%, 14: 2%, 15: 1%

## Final Student Score

Along with the results and charts from the above metrics, students will get a singular score.  This will be weighted as such:
    
##### 32% Percentage Corrected
Most important because a native knows best how a native should write but is not weighted more because often a user will correct mistakes but not make the text sound like it was written by a native.
    
##### 30% Lexical Diversity
Lexical diversity is a great dipictor of nativeness of writing because it shows both the user's level of vocabulary compared to a native, and writing syle to a degree.

##### 18% Average Word Length
Word length average has shown to be a strong depictor of an author's comfort with a language.  This is a good reinforcement to lexical diversity.  Users who have a below-native word length generally have a lower vocabulary while users who have an above-native average word length write in a way that sounds unnatural to a native speaker (usually).

##### 13% Average Sentence Length
Average sentence length informally reports whether or not a user has issues with run-on sentences or writing that presents a "choppy" feel.  However, this can vary greatly even between native writers which is why it has been weighted lightly.

##### 7%  Word Frequency Distribution Comparison
Word frequency should be considered when comparing writing styles because it gives a great depiction of how balanced the user's composition of short "helping words" are.  However, this is weighted lightly because word frequency distributions can vary greatly based on the text topic even among natives.
