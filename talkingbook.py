import pyttsx3
import PyPDF2
book = open('number4.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print("Total page of your book have : ", pages)
Friend = pyttsx3.init()

page = pdfReader.getPage(int(input("Which page you want to read : ")))
text = page.extractText()
Friend.say(text)
Friend.runAndWait()
