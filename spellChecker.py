from spellchecker import SpellChecker

"""
TODO:
name/surname check; fraction/number control
"""


dirtyString = """
The Property of CaptatN JOHN AYLWARD

‘A SourH ARABIAN ALABASTER FUNERARY MALE HEAD with sunken eyes, flat behind,
3iin. (9.6em.) 15t Century B.C./1st Century A.D.

(See ILLustRation)

A SoUTH ARABIAN ALABASTER BEARDED MALE FUNERARY HEAD, with stylised
features, with sunken eyes, straight recessed eyebrows and small mouth, che crown
of the head flattened and flat behind, 53in. (14cm), c. 1st Century B.C.|1st Century
AD.

Various Properties
‘A SOUTH ARABIAN ALABASTER BEARDED MALE FUNERARY Heap of stylised form,

with large recessed eyes and grooved eyebrows, 7in. (17.8cm.), Ist Century B.C.|1st
Century A.D.

(See Intustration)

A South Arabian alabaster male Funerary Head of highly stylised form, the pupils of
the eyes depressed, flat behind, Gin, (15.20m.), 1st Century B.C./18t Century AD.
"""

# ? string to list (by single spaces)
dirtyList = dirtyString.split()

# ? removing string with numbers/special characters
def withNum(s):
    'returns True if string contains any number'
    return any(i.isdigit() for i in s)

noNumList = []
[noNumList.append(word) for word in dirtyList if not withNum(word)]
dirtyList = noNumList

# ? check for misspelled words
spell = SpellChecker()
misspelled = spell.unknown(dirtyList)

misspelledDict = {k:spell.correction(k) for k in misspelled}

missDict = {word:correctWord for word, correctWord in misspelledDict.items()
            if (word[:-1] != correctWord and word[1:] != correctWord
                and word != correctWord)}

lowDirtyList = [word.lower() for word in dirtyList]

for key, value in missDict.items():
    if key in lowDirtyList:
        i = lowDirtyList.index(key)
        dirtyList[i] = value

cleanString = " ".join(dirtyList)

print(cleanString)
