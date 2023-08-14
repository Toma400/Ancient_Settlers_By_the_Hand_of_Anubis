#[ nim c --app:lib --out:nutils.pyd --threads:on --tlsEmulation:off --passL:-static nutils ]#
import nimpy

type
  Rect = object
    x:  int # begin
    y:  int
    ex: int # end
    ey: int

proc iterateOverPos* (rect: (int, int, int, int), pos: (int, int)): bool {.exportpy.} =
    let R = Rect(x: rect[0], y: rect[1], ex: rect[2], ey: rect[3])
    for x in R.x..R.ex:
      for y in R.y..R.ey:
        if x == pos[0] and y == pos[1]:
          return true
    return false