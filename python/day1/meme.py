# The most cursed Advent of Code solution you've ever seen

# Token functions - because why use strings directly when you can use functions?
def DEF(): return "def"
def RETURN(): return "return"
def FOR(): return "for"
def IN(): return "in"
def IF(): return "if"
def ELIF(): return "elif"
def PRINT(): return "print"
def OPEN(): return "open"
def INT(): return "int"

def COLON(): return ":"
def COMMA(): return ","
def DOT(): return "."
def EQUALS(): return "="
def DOUBLE_EQUALS(): return "=="
def PLUS_EQUALS(): return "+="
def PLUS(): return "+"
def MINUS(): return "-"
def PERCENT(): return "%"
def LPAREN(): return "("
def RPAREN(): return ")"
def LBRACKET(): return "["
def RBRACKET(): return "]"
def QUOTE(): return '"'

def SPACE(): return " "
def NEWLINE(): return "\n"
def INDENT(): return "    "
def INDENT2(): return "        "
def INDENT3(): return "            "

# Variable names as functions - very normal programming
def read_file(): return "read_file"
def part1(): return "part1"
def filename(): return "filename"
def lines(): return "lines"
def pos(): return "pos"
def ans(): return "ans"
def line(): return "line"
def direction(): return "direction"
def to_turn(): return "to_turn"
def readlines(): return "readlines"
def strip(): return "strip"

# Numbers and strings
def ZERO(): return "0"
def ONE(): return "1"
def FIFTY(): return "50"
def HUNDRED(): return "100"
def L(): return "L"
def R(): return "R"
def INPUT_FILE(): return "i.txt"

# BUILD THE PROGRAM AS A BEAUTIFUL CONCATENATION
# Formatted to look like the actual code structure

program = (
    # def read_file(filename):
    DEF() + SPACE() + read_file() + LPAREN() + filename() + RPAREN() + COLON() + NEWLINE() +
    #     return open(filename).readlines()
    INDENT() + RETURN() + SPACE() + OPEN() + LPAREN() + filename() + RPAREN() + DOT() + readlines() + LPAREN() + RPAREN() + NEWLINE() +
    NEWLINE() +

    # def part1(lines):
    DEF() + SPACE() + part1() + LPAREN() + lines() + RPAREN() + COLON() + NEWLINE() +
    #     pos = 50
    INDENT() + pos() + SPACE() + EQUALS() + SPACE() + FIFTY() + NEWLINE() +
    #     ans = 0
    INDENT() + ans() + SPACE() + EQUALS() + SPACE() + ZERO() + NEWLINE() +
    #     for line in lines:
    INDENT() + FOR() + SPACE() + line() + SPACE() + IN() + SPACE() + lines() + COLON() + NEWLINE() +
    #         direction = line[0]
    INDENT2() + direction() + SPACE() + EQUALS() + SPACE() + line() + LBRACKET() + ZERO() + RBRACKET() + NEWLINE() +
    #         to_turn = int(line[1:].strip())
    INDENT2() + to_turn() + SPACE() + EQUALS() + SPACE() + INT() + LPAREN() + line() + LBRACKET() + ONE() + COLON() + RBRACKET() + DOT() + strip() + LPAREN() + RPAREN() + RPAREN() + NEWLINE() +
    #         if direction == "L":
    INDENT2() + IF() + SPACE() + direction() + SPACE() + DOUBLE_EQUALS() + SPACE() + QUOTE() + L() + QUOTE() + COLON() + NEWLINE() +
    #             pos = (pos - to_turn) % 100
    INDENT3() + pos() + SPACE() + EQUALS() + SPACE() + LPAREN() + pos() + SPACE() + MINUS() + SPACE() + to_turn() + RPAREN() + SPACE() + PERCENT() + SPACE() + HUNDRED() + NEWLINE() +
    #         elif direction == "R":
    INDENT2() + ELIF() + SPACE() + direction() + SPACE() + DOUBLE_EQUALS() + SPACE() + QUOTE() + R() + QUOTE() + COLON() + NEWLINE() +
    #             pos = (pos + to_turn) % 100
    INDENT3() + pos() + SPACE() + EQUALS() + SPACE() + LPAREN() + pos() + SPACE() + PLUS() + SPACE() + to_turn() + RPAREN() + SPACE() + PERCENT() + SPACE() + HUNDRED() + NEWLINE() +
    #         if pos == 0:
    INDENT2() + IF() + SPACE() + pos() + SPACE() + DOUBLE_EQUALS() + SPACE() + ZERO() + COLON() + NEWLINE() +
    #             ans += 1
    INDENT3() + ans() + SPACE() + PLUS_EQUALS() + SPACE() + ONE() + NEWLINE() +
    #     return ans
    INDENT() + RETURN() + SPACE() + ans() + NEWLINE() +
    NEWLINE() +

    # print(part1(read_file("i.txt")))
    PRINT() + LPAREN() + part1() + LPAREN() + read_file() + LPAREN() + QUOTE() + INPUT_FILE() + QUOTE() + RPAREN() + RPAREN() + RPAREN()
)

# Witness the horror
exec(program)
