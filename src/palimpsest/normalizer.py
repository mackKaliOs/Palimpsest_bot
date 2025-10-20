import regex as re
from unidecode import unidecode

def normalize(s: str) -> str:
    s = s.strip()
    s = re.sub(r"\s+", " ", s)
    # preserve diacritics for Greek, etc.; but ensure NFC
    try:
        import unicodedata as ud
        s = ud.normalize("NFC", s)
    except Exception:
        pass
    return s
