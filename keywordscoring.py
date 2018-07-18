from rake_nltk import Rake

r = Rake()

# importing required modules
import PyPDF2

# creating a pdf file object
pdfFileObj = open('C:/Users/HP/Downloads/JavaBasics-notes.pdf', 'rb') #This is the location of file I have been reading
 
# creating a pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
 
# printing number of pages in pdf file
numb=pdfReader.numPages
print(numb)

# creating a page object
#for i in range (numb):
    #pageObj = pdfReader.getPage(i)
    #extracting text from page
    #print(pageObj.extractText())
    
for k in range (numb):
    pageObj = pdfReader.getPage(k)    
    r.extract_keywords_from_text(pageObj.extractText())
    r.get_ranked_phrases()
    # To get keyword phrases ranked highest to lowest with scores.
    r.get_ranked_phrases_with_scores()
    
pdfFileObj.close()        
