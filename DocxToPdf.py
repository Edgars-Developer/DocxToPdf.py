from docx2pdf import convert
import glob


for docx_file in glob.glob("*.docx"):
    cv = convert(docx_file)


