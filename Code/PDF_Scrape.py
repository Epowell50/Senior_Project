import pdftotext
import re

# Opens the PDF and reads in all the text data
with open("Test.pdf", "rb") as f:
    pdf = pdftotext.PDF(f)

# This section joins the data into a single string and begins paring it
# into a useful form through regex and splits
output = "".join(pdf)
info_list = output.split("\n")
info_list = [s.strip() for s in info_list]
for i in range(len(info_list)):
    string = info_list[i]
    string = re.sub("\s+", " ", string)
    info_list[i] = string
#info_list = [s.split(" ") for s in info_list]
#info_list = [s.replace(" ", "") for s in info_list]
print(info_list)