import PyPDF2
a = PyPDF2.PdfFileReader("f.pdf")
# print(a.documentInfo)
# print(a.getNumPages())
# print(a.getPage(4).extractText())
t=a.getPage(4).extractText()
with open("new.txt","w") as f:
    f.write(t)