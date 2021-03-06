from nltk.tokenize import word_tokenize
from gensim.models.doc2vec import TaggedDocument

from ReadTextFile import readTextFile
from RemoveStopWords import removeStopWords
from TestModel import testModel

def bookingMain(fileLocation,phrase):
    # Modify the file locations to dataset and trained model
    dataFileLocation = fileLocation + 'data/booking.txt'
    modelFileLocation = fileLocation + 'd2v.model'

    # Check the phrase with current trained model
    similarPhrase,similarPhraseValue = testModel(dataFileLocation,modelFileLocation,phrase)

    return similarPhrase,similarPhraseValue
    