from enum import Enum

class Color(Enum):
    RED = "r"
    BLACK = "b"
    GREEN = "g"
    OTHER = ""
    
class Parity(Enum):
    ODD = "o"
    EVEN = "e"
    ERR = ""
    
class Range(Enum):
    HIGH = "h"
    LOW = "l"  
    ERR = ""
    