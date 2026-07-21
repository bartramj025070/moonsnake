##########################################################################################################
#      |\      _,,,---,,_
#ZZZzz /,`.-'`'    -.  ;-;;,_
#     |,4-  ) )-,_. ,\ (  `'-'
#     '---''(_/--'  `-'\_)
##########################################################################################################

##########################################################################################################
## @name: Lexer.py
## @desc: highkey lowk lexes luau :)
## @author: bartramj025070 <- that's me! =]
## @created: 20/07/26
## @last-edited: 20/07/26
##########################################################################################################

from enum import Enum

## ENUMS
class Type(Enum):
    EOF = 0,
    
    Char_END = 256,
    
    Equal = 257,
    LessEqual = 258,
    GreaterEqual = 259,
    NotEqual = 260,
    Dot2 = 261,
    Dot3 = 262,
    SkinnyArrow = 263,
    DoubleColon = 264,
    FloorDiv = 265,
    
    InterpStringBegin = 266,
    InterpStringMid = 267,
    InterpStringEnd = 268,
    # An interpolated string with no expressions (like `x`)
    InterpStringSimple = 269,

    AddAssign = 270,
    SubAssign = 271,
    MulAssign = 272,
    DivAssign = 273,
    FloorDivAssign = 274,
    ModAssign = 275,
    PowAssign = 276,
    ConcatAssign = 277,

    RawString = 278,
    QuotedString = 279,
    Number = 280,
    Name = 281,

    Comment = 282,
    BlockComment = 283,

    Attribute = 284,
    AttributeOpen = 285,

    BrokenString = 286,
    BrokenComment = 287,
    BrokenUnicode = 288,
    BrokenInterpDoubleBrace = 289,
    Error = 290,

    Reserved_BEGIN = 291,
    ReservedAnd = Reserved_BEGIN,
    ReservedBreak = 292,
    ReservedDo = 293,
    ReservedElse = 294,
    ReservedElseif = 295,
    ReservedEnd = 296,
    ReservedFalse = 297,
    ReservedFor = 298,
    ReservedFunction = 299,
    ReservedIf = 300,
    ReservedIn = 301,
    ReservedLocal = 302,
    ReservedNil = 303,
    ReservedNot = 304,
    ReservedOr = 305,
    ReservedRepeat = 306,
    ReservedReturn = 307,
    ReservedThen = 308,
    ReservedTrue = 309,
    ReservedUntil = 310,
    ReservedWhile = 311,
    Reserved_END = 312
    
class QuoteStyle(Enum):
    Single = 1,
    Double = 2

## CLASSES
class Position:
    def __init__(self, line, column):
        self.line = line
        self.column = column
        
    @staticmethod
    def missing():
        return Position(sys.maxint, sys.maxint)
        
    def isEqual(self, rhs):
        return self.line == rhs.line and self.column == rhs.column
        
    def isNotEqual(self, rhs):
        return self.line != rhs.line or self.column != rhs.column
        
    def lessThan(self, rhs):
        if self.line == rhs.line:
            return self.column < rhs.column
        else:
            return self.line < rhs.line
            
    def greaterThan(self, rhs):
        if self.line == rhs.line:
            return self.column > rhs.column
        else:
            return self.line > rhs.line
            
    def lessThanOrEqual(self, rhs):
        return self.isEqual(rhs) or self.lessThan(rhs)
        
    def greaterThanOrEqual(self, rhs):
        return self.isEqual(rhs) or self.greaterThan(rhs)
        
    def hasValue(self):
        self.line != self.maxint and self.column != self.maxint

class Location:
    def __init__(self, begin=None, end=None, length: int=None):
        if end == None and length != None:
            if isinstance(begin, Position) and isinstance(length, int):
                self.begin = begin
                self.end = Position(begin.line, begin.column + length)
        elif begin != None and end != None:
            if isinstance(begin, Position) and isinstance(end, Position):
                self.begin = begin
                self.end = end
            elif isinstance(begin, Location) and isinstance(end, Location):
                self.begin = Position(begin.begin)
                self.end = Position(end.end)
    
    def isEqual(self, rhs):
        return self.begin.isEqual(self.rhs.begin) and self.end.isEqual(self.rhs.end)
        
    def isNotEqual(self, rhs):
        return not self.isEqual(rhs)

class Lexeme:
    def __init__(self, location: Location, pType=None, character=None, name=None, data=None, size=None):
        # (data, name, codepoint), length, type, location
        return True
        
    def getLength(self):
        return True
        
    def getBlockDepth(self):
        return True
        
    def getQuoteStyle(self):
        return True
        
    def toString(self):
        return True
        
def isSpace(char):
    return char == ' ' or char == '\t' or char == '\r' or char == '\n' or char == '\v' or char == '\f'