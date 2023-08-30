# from kivy.core.window import Window
from win32api import GetSystemMetrics
from enum import Enum
import toml

class Axis (Enum):
    X = 0
    Y = 1

class Window:
    X = GetSystemMetrics(0)
    Y = GetSystemMetrics(1)

    @classmethod
    def get(cls, axis: Axis) -> int:
        return cls.X if axis == Axis.X else cls.Y

def cell(value, axis: Axis) -> int:
    return int(value * (Window.get(axis) // 100))

def cells(x, y) -> (int, int):
    return cell(x, Axis.X), cell(y, Axis.Y)

class Settings:
    _READ = toml.load("../config.toml")
    _SETS = _READ["settings"]
    LANG  = _SETS["language"]

    @classmethod
    def write_settings(cls, key, value=None):
        langs  = ["English", "Polish"]
        config = cls._READ

        match key:
            case Settings.LANG:
                lim = langs.index(cls.LANG)
                if lim+1 != len(langs): config["settings"]["language"] = langs[lim+1]
                else:                   config["settings"]["language"] = langs[0]

        with open("../config.toml", "w") as file: toml.dump(config, file)

def langstr(key):
    return str(toml.load(f"lang/{Settings.LANG}.toml")[key])