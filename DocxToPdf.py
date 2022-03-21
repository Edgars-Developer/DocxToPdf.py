from docx2pdf import convert
import glob  # check things in current directory

for docx_file in glob.glob("*.docx"):
    cv = convert(docx_file)
