# Initial code taken from
# https://www.tutorialspoint.com/extract-hyperlinks-from-pdf-in-python

# Import necessary packages
import PyPDF2
import re

# Open The File in the Command
file = open("Toward_Causal_Representation_Learning.pdf", 'rb')
readPDF = PyPDF2.PdfFileReader(file)
def find_urls(string):
   #Find all the String that matches with the pattern
   # string = remove_control_chars(string)
   regex = r"(https?://\S+)"
   urls = re.findall(regex,string)
   return urls
# Iterating over all the pages of File
for page_no in range(readPDF.numPages):
   page=readPDF.getPage(page_no)
   #Extract the text from the page
   text = page.extractText()

   # Print all URL
   urls = find_urls(text)
   for u in urls:
       # the reference include the "[reference-no]" at the end of the url
       # create a substring up to the [ char to deal with this
       pos = u.find("[")
       if pos != -1:
           u = u[:pos]
       print("[{}][{}]".format(page_no, u))

# CLost the file
file.close()
