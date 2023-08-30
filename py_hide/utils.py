from kivy.core.window import Window
import toml

class GH:
    X = 0
    Y = 1

def cell(value, axis) -> int:
    return int(value * (Window.size[axis] // 100))

def cells(x, y) -> (int, int):
    return cell(x, GH.X), cell(y, GH.Y)

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