"""
Convert a list of language contractions from a dict in a python file to .json

Usage:  convert_contractions_to_json.py

Its hard to pass in a file name to import, and the input file names each have a different name for the
data, which is also hard.

The proper ways of dealing with stuff is harder than a 1-time script warrants, so...
hardcoding, here I come.

Basically no error checking.
"""


import json
import os.path

from config import french_list_of_contractions as fr
from config import german_list_of_contractions as gr  # probably wrong language code, oh-well
from config import italian_list_of_contractions as it
from config import english_list_of_contractions as en


frc = fr.french_contractions
grc = gr.german_contractions
itc = it.italian_contractions
enc = en.english_contractions

for contractions, lang in ((frc, 'french'), (grc, 'german'), (itc, 'italian'), (enc, 'english')):
    res = {}
    res['contractions'] = contractions

    fname = os.path.join('../config/', lang, 'rules.json')
    json.dump(res, open(fname, 'w'), indent=4, sort_keys=True, ensure_ascii=False)
