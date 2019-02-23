from spellchecker import SpellChecker
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

"""
TODO:
name/surname check; fraction/number control
"""

pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'

# ? image to string
dirtyString = pytesseract.image_to_string(Image.open('test20.jpg'))

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
