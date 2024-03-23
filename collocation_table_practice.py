#TO DO: add spaCy and PyPDF2 to this instance or open this in the NLP instance
import spacy, PyPDF2
nlp = spacy.load("en_core_web_sm")

def find_distance(file_name_between_quotes): #finds the distance between each word in doc (a string), w/o stop words or punctuation
    with open(file_name_between_quotes, "rb") as file
        #converts a PDF file to an NLP string.
        doc_string = PyPDF2.PdfFileReader(file).extractText()
        doc_nlp = nlp(doc_string)
        #removes stops and puts all non-stop, non-punctuation tokens in a regular list object
        doc = []
        for token in doc_nlp:
            if token.is_stop = False:
                doc.append(token)
        #creates dict object to return
        collocation = {}
        for i in doc:
            for j in doc:
                if i != j:
                    #TO DO: find how to measure distance between i and j
                    collocation[i][j] = #distance value here
                    # The line above should format it as
                    #             {word1 : {"dist_word2" : number, "dist_word3" : number, ...},
                    #              word2 : {"dist_word1" : number, "dist_word3" : number, ...},
                    #              ... }
    return collocation


def make_table(dist)
    #TO DO: find how you make a table from a dict object
    #TO DO: map the distance values onto a colour gradient for some extra wow effect



#executes the program
distances = find_distance("") #insert PDF file name from the right directory between quotes
make_table(distances)



#Further ideas for variations on that code: looking at POS instead of wordspython
