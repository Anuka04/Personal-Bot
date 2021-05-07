#pip install PyPDF2

import pyttsx3
import pyaudio
import PyPDF2

#rb = read in form of binary
book = open('sample.pdf','rb')
Reader = PyPDF2.PdfFileReader(book)
pages = Reader.numPages
print(pages)

speaker = pyttsx3.init()
print("Playing...")
page = Reader.getPage(0)
#page numbers start from 0
#nth page is stored as n-1th page
text = page.extractText()
speaker.say(text)
speaker.runAndWait()
