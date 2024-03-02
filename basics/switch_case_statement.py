# https://www.codingninjas.com/studio/problems/switch-case-statement_8357244?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
from typing import *
import math

def areaSwitchCase(ch: int, a: List[float]):
    if ch == 1:
        return round(math.pi * a[0]**2,5)
    else:
        l=a[0]
        b=a[1]
        result = l* b
        return format(result, ".5f")
        


    