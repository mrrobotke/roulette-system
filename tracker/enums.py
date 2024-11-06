from enum import Enum

class Color(Enum):
    RED = "r"
    BLACK = "b"
    GREEN = "g"
    OTHER = "00"
    
class Parity(Enum):
    ODD = 1
    EVEN = 2  
    ERR = 3
    
class Range(Enum):
    HIGH = 1
    LOW = 2  
    ERR = 3
    