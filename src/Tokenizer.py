import re

class Tokenizer:
        def __init__(self):
                self.specialChars = "!@#$%^&*(){}[]<>,.;:-=+\"' "
                self.numbers = "0123456789"

        def tokenize(self, code):
                tokens = []
                buffer = ""

                code = re.sub("[\n]", "", code)

                code = list(code)
                code.append(self.specialChars[0]) # allows tokenization for last expression

                for char in code:
                        if (char in self.specialChars):
                                if (buffer.strip(" ") == ""):
                                        tokens.append(char)
                                        continue

                                tokens.append(buffer)
                                tokens.append(char)
                                buffer = ""

                        else:
                                buffer += char

                lastItem = tokens[len(tokens) - 1]
                tokens.remove(lastItem)

                while (" " in tokens):
                        tokens.remove(" ")

                return tokens


t = Tokenizer()
tok = t.tokenize(open("src/testfile.skt", "r").read())
for to in tok:
        print(f" |{to}| ", end="")