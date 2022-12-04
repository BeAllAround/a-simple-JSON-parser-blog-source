class EndLine(Exception):
    pass

class Token_stream:

    def __init__(self, source, c = 0):
        self.c = c # counter for our token stream
        self.source = source

    @property
    def current(self):
        if not self.c < len(self.source):
            raise EndLine("EndLine Error!")
        return self.source[self.c]

    def next_char(self):
        if self.c > len(self.source):
            raise EndLine("EndLine Error!")
        self.c += 1

    def __eq__(self, toMatch):
        if self.is_over():
            return False # return False when there is nothing to match
        if type(toMatch) != str:
            raise Exception("Can't match non-str")
        return self.current == toMatch

    def is_over(self):
        return not self.c < len(self.source)

    def set_ts(self, token_stream):
        self.source = token_stream.source
        self.c = token_stream.c

# reuse Token_stream to extend Parser - adding new methods in the future, and vice versa
class Parser(Token_stream): 
    pass