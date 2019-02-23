from spellchecker import SpellChecker
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'

class spellImprove:
    def __init__(self, dirtyString):
        self.dirtyList = dirtyString.split()

    def numbDelete(self):
        def withNum(s):
            'returns True if string contains any number'
            return any(i.isdigit() for i in s)

        noNumList = []
        [noNumList.append(word) for word in self.dirtyList if not withNum(word)]
        self.dirtyList = noNumList

    def missCheck(self):
        self.numbDelete()

        # ? initialise spellchecker object
        spell = SpellChecker()

        # ? look for unknown words
        misspelled = spell.unknown(self.dirtyList)

        # ? create dict of misspelled word with correction as values
        misspelledDict = {k:spell.correction(k) for k in misspelled}

        # ? delete mistakes
        missDict = {word:correctWord for word, correctWord in misspelledDict.items()
                    if (word[:-1] != correctWord and word[1:] != correctWord
                        and word != correctWord)}

        # ? replace misspelled words in dirtyList
        lowDirtyList = [word.lower() for word in self.dirtyList]
        for key, value in missDict.items():
            if key in lowDirtyList:
                i = lowDirtyList.index(key)
                self.dirtyList[i] = value

    def cleanString(self):
        self.missCheck()

        # ? concatenate list into clean string
        cleanString = " ".join(self.dirtyList)

        print(cleanString)


# ? image to string
dirtyString = pytesseract.image_to_string(Image.open('test20.jpg'))

# ? initialise object
stringToClean = spellImprove(dirtyString)
stringToClean.cleanString()
