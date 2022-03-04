from posixpath import split
import pdftotext
import re

# Opens the PDF and reads in all the text data
with open("Test.pdf", "rb") as f:
    pdf = pdftotext.PDF(f)

# Creates a single string of all text
output = "".join(pdf)

# Splits the string into a tuple
info_list = output.split("\n")

# Removes trailing and leading whitespace
info_list = [s.strip() for s in info_list]

# Replaces all "spaced" sections with "-", preserving
# single spaced pieces
for i in range(len(info_list)):
    a = info_list[i]
    a = re.sub("\s\s+", "_", a)
    info_list[i] = a

# Creates an empty list to store the new data
data = []
for i in range(len(info_list)):
    a = info_list[i]
    print(a)

#print(data)