from win32api import GetSystemMetrics
from enum import Enum

class Axis (Enum):
    X = 0
    Y = 1

class WinRes:
    X = GetSystemMetrics(0)
    Y = GetSystemMetrics(1)

    @classmethod
    def get(cls, axis: Axis) -> int:
        return cls.X if axis == Axis.X else cls.Y

def cell(value, axis: Axis) -> int:
    return int(value * (WinRes.get(axis) // 100))

def cells(x, y) -> (int, int):
    return cell(x, Axis.X), cell(y, Axis.Y)