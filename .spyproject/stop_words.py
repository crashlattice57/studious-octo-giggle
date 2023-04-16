# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 13:20:05 2023

@author: damia
"""

import nltk
nltk.download("stopwords")
from nltk.corpus import stopwords
stop_words = stopwords.words("english")
additional_words = ["Believed", "work", "Also", "known"]

for word in additional_words:
    stop_words.append(word)
