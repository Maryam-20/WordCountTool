import os 
import sys
from docx import Document
import PyPDF2



class Word_count:
    def __init__(self):
        self.filePath =input("Enter file path OR file name")
        self.filePath = self.filePath.strip('"')
        if os.path.isabs(self.filePath):
            self.AbsolutePath = os.path.abspath(self.filePath)
            self.file_name, self.file_extension = os.path.splitext(self.AbsolutePath)
            self.count_word()

        else:
            print("The provided path is not absolute")

            
    def count_word(self):
        if self.file_extension:
            if self.file_extension == ".txt":

                if os.path.exists(self.AbsolutePath):
                    with open (self.filePath) as file:
                        readFile = file.read()
                        split_word = readFile.split()
                        word_num = len(split_word)
                    print("Word count is {}" .format(word_num))
                else:
                    print("File does not exist")
            
            elif self.file_extension == ".docx":
                if os.path.exists(self.AbsolutePath):
                    document = Document(self.AbsolutePath)
                    word_len = 0

                    for paragraph in document.paragraphs:
                        word_split = paragraph.text.split()
                        word_len += len(word_split)
                    print("Word count is {}".format(word_len))
                else:
                    print("File does not exist")
            elif self.file_extension == ".pdf":
                if os.path.exists(self.AbsolutePath):
                    with open (self.AbsolutePath, "rb") as pdfFile:
                        pdf_reader = PyPDF2.PdfReader(pdfFile)
                        num_pages = len(pdf_reader.pages)

                        word_count = 0

                        for pages_num in range(num_pages):
                            page =pdf_reader.pages[pages_num]
                            text_content = page.extract_text()
                            words = text_content.split()
                            word_count += len(words)
                        print("Word count is {}".format(word_count)) 
                else:
                    print("File does not exist")
            else:
                print("File extension not supported. .txt, .docx, .pdf are file extensions supported")


        else:
            print("file does not have an extension")

start = Word_count()
