class Result:
    def __init__(self, value, pos):
        self.value = value
        self.pos = pos
    
    def __repr__(self):
        return 'Result(%s, %d)'%(self.value, self.pos)

class Parser:
    def __call__(self, tokens, pos):
        return None
    
    def __add__(self, other):
        return Concat(self, other)

    def __mul__(self, other):
        return Exp(self, other)

    def __or__(self, other):
        return Alternate(self, other)

    def __xor__(self, other):
        return Process(self, function)