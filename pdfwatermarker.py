##CLI scrupt 
##arg1 = pdf to add water mark to
#arg2 = pdf to source water mark from
#arg3 = output pdf filename


import PyPDF2
from sys import argv

# print(f"Printing argv: {argv}")

#Initialize PDFwriter and reader objects

template = PyPDF2.PdfFileReader(open(argv[1], 'rb'))
# print(f"Printing template.pages: {template.numPages}")
watermark = PyPDF2.PdfFileReader(argv[2])
# print(f"Printing watermark.pages: {watermark.numPages}")
output = PyPDF2.PdfFileWriter()

#watermark is on page one
watermark_page = watermark.getPage(0)

for page_num in range(template.numPages):
    page = template.getPage(page_num)
    page.mergePage(watermark_page)
    output.addPage(page)

# print(f"Printing writer.getNumPages(): {writer.getNumPages()}")

with open(argv[3], 'wb') as output_stream:
    writer.write(output_stream)
print(f"File saved as: {argv[3]}")


# for page in template.pages:
#     page.mergePage()




#Add watermark onto each page
