import re
import enum

def isNumber(string):
        if (len(string) == 0):
                return False

        dots = 0

        for char in string:
                if (char == '.'): dots += 1
                elif (char == '-'): continue
                elif (not char.isdigit()): return False

        if (dots == 1 or dots == 0): return True
        return False


class TokenType(enum.Enum):
        HASHTAG = 0
        ASTERISK = 1
        LBRACKET = 2
        RBRACKET = 3
        LBRACE = 4
        RBRACE = 5
        LSQRBRACKET = 6
        RSQRBRACKET = 7
        LANGLEBRACKET = 8
        RANGLEBRACKET = 9
        COMMA = 10
        PERIOD = 11
        SEMICOLON = 12
        COLON = 13
        MINUS = 14
        EQUALS = 15
        PLUS = 16
        NUM = 17
        STR = 18
        KWINT = 19
        KWFLOAT = 20
        KWBOOL = 21
        KWSTRING = 22
        KWLOCATION = 23
        KWVECTOR = 24
        LIST = 25
        KWVOID = 26
        KWIF = 27
        KWELSE = 28
        KWFUNCTION = 29
        KWCOMMAND = 30
        KWSTRUCT = 31
        KWGLOBAL = 32
        KWLOCAL = 33
        KWWHILE = 34
        KWFOR = 35
        IDENTIFIER = 36


class Token:
        def __init__(self, data):
                self.data = data
                self.type = None

                if (self.data == "#"): self.type = TokenType.HASHTAG
                elif (self.data == "*"): self.type = TokenType.ASTERISK
                elif (self.data == ","): self.type = TokenType.COMMA
                elif (self.data == "."): self.type = TokenType.PERIOD
                elif (self.data == ";"): self.type = TokenType.SEMICOLON
                elif (self.data == ":"): self.type = TokenType.COLON
                elif (self.data == "-"): self.type = TokenType.MINUS
                elif (self.data == "="): self.type = TokenType.EQUALS
                elif (self.data == "+"): self.type = TokenType.PLUS

                elif (self.data == "("): self.type = TokenType.LBRACKET
                elif (self.data == ")"): self.type = TokenType.RBRACKET
                elif (self.data == "{"): self.type = TokenType.LBRACE
                elif (self.data == "}"): self.type = TokenType.RBRACE
                elif (self.data == "["): self.type = TokenType.LSQRBRACKET
                elif (self.data == "]"): self.type = TokenType.RSQRBRACKET
                elif (self.data == "<"): self.type = TokenType.LANGLEBRACKET
                elif (self.data == ">"): self.type = TokenType.RANGLEBRACKET

                elif (isNumber(self.data)): self.type = TokenType.NUM
                elif (self.data[0] == "\""): self.type = TokenType.STR

                elif (self.data == "int"): self.type = TokenType.KWINT
                elif (self.data == "float"): self.type = TokenType.KWFLOAT
                elif (self.data == "bool"): self.type = TokenType.KWBOOL
                elif (self.data == "string"): self.type = TokenType.KWSTRING
                elif (self.data == "location"): self.type = TokenType.KWLOCATION
                elif (self.data == "vector"): self.type = TokenType.KWVECTOR
                elif (self.data == "list"): self.type = TokenType.LIST

                elif (self.data == "void"): self.type = TokenType.KWVOID

                elif (self.data == "if"): self.type = TokenType.KWIF
                elif (self.data == "else"): self.type = TokenType.KWELSE

                elif (self.data == "function"): self.type = TokenType.KWFUNCTION
                elif (self.data == "command"): self.type = TokenType.KWCOMMAND
                elif (self.data == "struct"): self.type = TokenType.KWSTRUCT
                elif (self.data == "global"): self.type = TokenType.KWGLOBAL
                elif (self.data == "local"): self.type = TokenType.KWLOCAL

                elif (self.data == "while"): self.type = TokenType.KWWHILE
                elif (self.data == "for"): self.type = TokenType.KWFOR

                else: self.type = TokenType.IDENTIFIER


class Tokenizer:
        def __init__(self):
                self.specialChars = "!@#$%^&*(){}[]<>,.;:-=+ "
                self.numbers = "0123456789"

        def tokenize(self, code):
                tokens = []
                buffer = ""

                code = re.sub("[\n]", "", code)

                code = list(code)
                code.append(self.specialChars[0]) # allows tokenization for last expression

                prevChar = ""
                continueAmount = 0

                for i in range(len(code)):
                        char = code[i]

                        if (continueAmount > 0):
                                continueAmount -= 1
                                continue

                        # special case for strings
                        if (char == "\"" and prevChar != "\\"):
                                curCharIndex = 0
                                curChar = code[i + curCharIndex]

                                while (True):
                                        if (curChar == "\"" and curCharIndex != 0):
                                                continueAmount = curCharIndex - 1
                                                break

                                        curChar = code[i + curCharIndex]

                                        buffer += curChar
                                        curCharIndex += 1
                                
                                tokens.append(buffer)
                                buffer = ""
                                

                        # special character case
                        if (char in self.specialChars):
                                # special case for floats
                                if (char == "." and prevChar.isdigit()):
                                        buffer += "."
                                        continue

                                # spaces are not ignored since they help with tokenizing
                                if (buffer.strip(" ") == ""):
                                        tokens.append(char)
                                        continue

                                tokens.append(buffer)
                                tokens.append(char)
                                buffer = ""

                        else:
                                buffer += char

                        prevChar = char

                lastItem = tokens[len(tokens) - 1]
                tokens.remove(lastItem)

                while (" " in tokens): tokens.remove(" ")
                while ("\"" in tokens): tokens.remove("\"")

                # convert tokens to a Token type
                for i in range(len(tokens)):
                        tokens[i] = Token(tokens[i])

                return tokens

t = Tokenizer()
tok = t.tokenize(open("src/testfile.skt").read())

for to in tok:
        print(f" |{to.data}| ", end = "")