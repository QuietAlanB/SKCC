import re
import os
from Tokenizer import Tokenizer

class Compiler:
        # NOTE:
        # file name is recommended to be full path (C:\Users\...)
        def __init__(self, filename):
                file = open(filename, "r", -1, "utf-8")
                code = file.read()
                file.close()

                extensions = re.findall("@extension \".*\"", code)
                includes = re.findall("@include \".*\"", code)

                for include in includes:
                        includeName = re.sub("@include |[\"]", "", include)
                        path = os.path.dirname(filename)
                        
                        includeContent = open(f"{path}/{includeName}").read()
                        
                        code = re.sub(include, includeContent, code)

                self.code = code


        def compile(self):
                pass


c = Compiler("D:/program/py/SKCC/src/testfile.skt")