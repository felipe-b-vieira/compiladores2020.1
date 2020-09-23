# ------------------------------------------------------------
# Processing a log file
# ------------------------------------------------------------
import ply.lex as lex

# List of token names.   This is always required
tokens = [
    'TIMESTAMP',
    'PROC',
    'MESSAGE'
] 

def t_TIMESTAMP(t):
    r'[0-9]+:[0-9]+:[0-9]+.[0-9]+\s-[0-9]+'
    return t

def t_PROC(t):
    r'\t[a-zA-Z][a-zA-Z0-9]*\t'
    t.value = t.value[1:len(t.value) - 1]
    return t

def t_MESSAGE(t):
    r'.+\n+'
    t.value = t.value[0:len(t.value) - 1]
    return t

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


class LogProcLexer:
    data = None
    lexer = None
    def __init__(self):
        fh = open("log", 'r')
        self.data = fh.read()
        fh.close()
        self.lexer = lex.lex()
        self.lexer.input(self.data)

    def collect_messages(self):
        tokens = []
        while True:
            tok = self.lexer.token()
            if not tok:
                break      # No more input
            if(tok.type == "PROC" and tok.value=="kernel"):
                tok=self.lexer.token()
                #print(tok)
                tokens.append(tok)
        return tokens
        
if __name__ == '__main__':
    print(LogProcLexer().collect_messages())
    
