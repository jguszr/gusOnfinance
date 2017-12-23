# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

base_path = "/users/jguszr/AnacondaProjects/gusOnfinance/db/"

my_file = os.path.join(base_path + "/" + "Abr_16.pdf")
log_file = os.path.join(base_path + "/" + "pdf_log.txt")

password = ""
extracted_text = ""

import PyPDF2
file = open(my_file, 'rb')

 fileReader = PyPDF2.PdfFileReader(file)
 
print( fileReader.numPages)