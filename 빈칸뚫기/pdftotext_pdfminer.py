from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import HTMLConverter, XMLConverter, TextConverter
from pdfminer.pdfdocument import PDFDocument
from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextContainer
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser
from io import StringIO
from tokenize import String
from konlpy.tag import Okt

Okt = Okt()

path = "test3.pdf"

def mining(path,pageOrLine):
    fp = open(path, 'rb') # 읽어올거
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    #print(type(retstr))
    codec = 'utf-8'
    laparams = LAParams()

    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    interpreter = PDFPageInterpreter(rsrcmgr, device)

    pdf_bypage = []
    page_no = 0

    for pageNumber, page in enumerate(PDFPage.get_pages(fp)):
        if pageNumber == page_no:
            interpreter.process_page(page)
            data = retstr.getvalue()
            #print(data)
            
            pdf_bypage.append(data)

            # 페이지 단위로 파일 나눠서 기록할때 쓰면됨
            # f = open('./out%d.txt' % page_no, 'wb') # 출력할거
            # f.write(data.encode("utf-8"))
            # f.close()

            data = ''
            retstr.truncate(0)
            retstr.seek(0)

            page_no += 1

    if pageOrLine == 0:
        for i in range(0, len(pdf_bypage)):
            pdf_bypage[i] = pdf_bypage[i].replace("\n", "")
            return pdf_bypage
    if pageOrLine == 1:
        for i in range(0, len(pdf_bypage)):
            list = pdf_bypage[i].splitlines()    
            pdf_byline =[[0 for k in range(len(list))] for l in range (len(pdf_bypage))]

            for j in range(len(list)):  
                pdf_byline[i][j] = list[j]
        return pdf_byline
    

    fp.close()
        
    print('pdfminer 정상작동')
    
# 내용 보면서 디버깅할때 쓰면됨
f = open("txtoutput3.txt","w",encoding = 'utf-8')
docs = mining(path,0).copy()

size = len(docs)
for i in range(0, size):
     f.write(docs[i])
f.close()

# print(docs[1])



