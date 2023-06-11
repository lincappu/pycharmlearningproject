import  PyPDF4


file='./test.pdf'

with open(file,'rb') as f:
    pdf=PyPDF4.PdfFileReader(f)
    print(pdf.getNumPages())
    print(pdf.getDocumentInfo())


pdf_w=PyPDF4.PdfFileWriter()
pdf_r=PyPDF4.PdfFileReader(file)
page_1=pdf_r.getPage(1).rotateCounterClockwise(90)
pdf_w.addPage(page_1)

with  open(file,'wb') as f:
    pdf_w.write(f)