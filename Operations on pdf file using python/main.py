# Working with PDF files in python and how to extract text from pdf using python.......


import PyPDF2
a = PyPDF2.PdfReader('process.pdf')
str= ""
for i in range(1, 11):
    str += a.getPage(i).extractText()

with open("text.txt", "w", encoding='utf-8')as f:
    f.write(str)


# OR

import PyPDF2
pdf_file = open('process.pdf', 'rb')
read_pdf = PyPDF2.PdfReader(pdf_file)
page = read_pdf.getPage(0)
page_content = page.extractText()
print (page_content.encode('utf-8'))