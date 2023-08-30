from win32api import GetSystemMetrics
from enum import Enum

class Axis (Enum):
    X = 0
    Y = 100

class WinRes:
    X = GetSystemMetrics(0)
    Y = GetSystemMetrics(1)

    @classmethod
    def get(cls, axis: Axis) -> int:
        return cls.X if axis == Axis.X else cls.Y

def cell(value, axis: Axis) -> int:
    """Uses reversed system to arcade (Y=0 is top) in <axis.value - ...>"""
    return int((axis.value - value) * (WinRes.get(axis) // 100))

def cells(x, y) -> (int, int):
    return cell(x, Axis.X), cell(y, Axis.Y)