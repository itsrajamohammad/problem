#import urllib for process url func
from urllib import request as ur
#install PyPDf2 lib to access pdf files
import PyPDF2.PdfFileReader as pdfr
url=input("enter url")
file=ur.urlopen(url)
if lower(url[-3:])=="pdf":
    file=pdfr(url)
for line in file:
    #decode the file to read the data
    output=line.decode('utf-8').strip()
    print(output)