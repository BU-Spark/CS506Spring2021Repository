import PyPDF2

def import_pdf(filename, debug):
    row_count = 0
    with open(filename, 'r') as f:
        pdfReader = PyPDF2.PdfFileReader(f)
        print(pdfReader.numPages)
        pageObj = pdfReader.getPage(0)
        print(pageObj.extractText())
        f.close()