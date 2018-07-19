from rake_nltk import Rake

r = Rake()

# importing required modules, here PyPDF2 as we want to read a PDF file
import PyPDF2
 
# creating a pdf file object
pdfFileObj = open('C:/Users/HP/Downloads/JavaBasics-notes.pdf', 'rb')
 
# creating a pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
 
# storing the number of pages available in that file in a variable called numb
numb=pdfReader.numPages


for i in range (numb):
    pageObj = pdfReader.getPage(i)# creating a page object, which will create a list of page objects for each page
    print(pageObj.extractText())# extracting text from page, from each page one after the another
    r.extract_keywords_from_text(pageObj.extractText())# Extracting keywords from the documents
    phrases=r.get_ranked_phrases()#It will give all the keyworded phrases from the document
    print(phrases)
    phrases_scores=r.get_ranked_phrases_with_scores()#It will give the phrases with scores
    print(phrases_scores)
