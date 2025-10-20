from palimpsest.scripts.theban import MAPPING as THEBAN
from palimpsest.scripts.celestial import MAPPING as CELESTIAL

_REG = {
    "theban": THEBAN,
    "celestial": CELESTIAL,
}

def get_script(name: str):
    return _REG.get(name)
