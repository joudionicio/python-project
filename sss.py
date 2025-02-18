#! python3
# merge PDF files based on a /numeric/string/ code in file name
# example1 r01_cz14_028_city_text1.PDF
# example1 r01_cz14_028_city_text2.PDF
import os
from pypdf import PdfWriter
from pathlib import Path

def mergeFiles(folder):
    
    folder = os.path.abspath(folder)   # make sure folder is absolute path

    # make a lists
    fileList1 = Path(folder).glob('*text1.pdf')


    outputName = ''
    outputFolderPath = folder + '\\somefolder'
    p = Path(outputFolderPath)
    if not p.exists():
            os.makedirs(outputFolderPath)
    n = 0
    folderLenght = len(folder)+1
    fileNameArea = folderLenght+12
    print(f'Adding files in {outputFolderPath}...')


    for filename1 in fileList1:
        n += 1
        fileList2 = Path(folder).glob('*text2.pdf') #Move fileList2 inside first loop
        # match test                   = SECOND LOOP
        for filename2 in fileList2:
            string1 = str(filename1)[folderLenght:fileNameArea].lower()
            string2 = str(filename2)[folderLenght:fileNameArea].lower()

            # Add choosen files in this folder to the PDF file by string.    
            if string1 == string2:
                outputName = 'D' + \
                str(filename1)[folderLenght + 4: folderLenght + 6].upper() + \
                '_' + str(filename1)[folderLenght + 9: folderLenght + 12] + \
                '_text3.pdf'

                outputName = outputFolderPath + '\\' + outputName
                file1Out = str(filename1)
                file2Out = str(filename2)
                pdfMerge([file1Out, file2Out], outputName)  #  function, works fine
                
                break
            
        print (f'{n}. {os.path.basename(outputName)}')
    
    print('Done.')

mergeFiles('X:\\MergeTest')
