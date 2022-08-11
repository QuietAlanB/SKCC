class Node:
        def __init__(self, token, children = []):
                self.name = token.data
                self.type = token.type
                self.children = children

class Parser:
        def __init__(self):
                pass