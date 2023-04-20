# main.py
from functionPackage.function import *

myLetters = sentence_analyzer("Eagles will dominate the Chiefs in the Super Bowl")
print(myLetters)
# what key in the dictionary occurs the most times
maxValue = -10000
letter = ""
for key in myLetters.keys():
    if maxValue < myLetters[key]:
        maxValue = myLetters[key]
        letter = key
print(letter, "appears", maxValue, "times.")

import matplotlib.pyplot as plt

# generate a histogram of letters and frequencies ie a histogram of the dictionary
# use matplotlib

plt.bar(list(myLetters.keys()), myLetters.values(), color='r')
plt.show()
