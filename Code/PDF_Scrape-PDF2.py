from PyPDF2 import PdfFileReader

with open("Test.pdf", 'rb') as f:
    pdf = PdfFileReader(f)
    text = pdf.getFormTextFields()

    print(text)
    print("---------------")
    print(text["ClassLevel"])