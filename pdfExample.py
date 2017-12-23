# -*- coding: utf-8 -*-
"""
experimental script to read a pdf file and
extract credit card information

"""

base_path = "/users/jguszr/AnacondaProjects/gusOnfinance/db/"

my_file = os.path.join(base_path + "/" + "Abr_16.pdf")
log_file = os.path.join(base_path + "/" + "pdf_log.txt")

password = ""
extracted_text = ""

import PyPDF2
import re
file = open(my_file, 'rb')

 fileReader = PyPDF2.PdfFileReader(file)
 
print( fileReader.numPages)
page = fileReader.getPage(1)
lines = page.extractText().splitlines()
len(lines)
for l in lines:
    print(l)

txt = page.extractText()

#getting started on the rgex
re.findall("[(\d\d)\.(\d\d)].", txt)
re.findall("\d\d\.\d\d[(\w)]*", txt)
re.findall("\d\d\.\d\d[(\w) \b [(\w)|(\d)]]*[(US$)|(BR$)]", txt)

#better and it is very good first clean up
for l in  re.split("\d{2}\.\d{2}", txt):
    print(re.split("\$", l))



