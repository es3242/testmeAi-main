import os
from tokenize import String
from konlpy.tag import Okt
from pdftotext_pdfminer import mining

Okt = Okt()

def nounExtractor(path,pageOrLine):
    try:    
        if pageOrLine == 0:
            writeLine = mining(path,0).copy()
            nounsLine = []
            nouns = []
            pages = len(writeLine)
            for i in range (pages):
                line = writeLine[i]# 한 페이지 씩 읽어 옴
                if not line: break # 파일 끝 까지 반복
                nouns = Okt.nouns(line) #한 페이지에 있는 명사들 모두 nouns에 저장 (리스트)

                if len(nouns) == 0 : 
                    nounsLine.append(' ')
                    continue #명사 없을 경우 ' ' 저장 후 pass
                line= ' '.join(map(str, nouns))
                nounsLine.append(line)

            print('nounExtractor 정상작동 ',pages,'페이지 확인')
            return(nounsLine)

        if pageOrLine == 1:
              
            writeLine = mining(path,1).copy()
            pages = len(writeLine)
            # nouns = [[0 for i in range(len(list))] for j in range (len(pages))]
            # nounsLine = [[0 for i in range(len(list))] for j in range (len(pages))]
            # for i in range (pages):
            #     linelen = len(writeLine[i])
            #     for j in range (linelen):
            #         line = writeLine[i][j]# 한줄 씩 읽어 옴
            #         if not line: break # 파일 끝 까지 반복

            #         if not len(Okt.nouns(line)) == 0:
            #             nouns[i][j] = Okt.nouns(line) #한 줄에 있는 명사들 모두 nouns에 저장 (리스트)
            #         #if len(nouns[i][j]) == 0 : 
            #             #nounsLine.append(' ')
            #             #continue #명사 없을 경우 ' ' 저장 후 pass
            #         #line= ' '.join(map(str, nouns))
            #         #nounsLine.append(line)

            print('nounExtractor 정상작동 ',pages,'페이지 확인')

            return(writeLine)

    except:
        print('error')

print(nounExtractor("./test3.pdf",1))

