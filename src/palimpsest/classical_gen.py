# lightweight “classicalization”: placeholder patterns + CLTK hooks if installed
from cltk.alphabet.lat import normalize as lat_norm

def to_classical(s: str, lang: str) -> str:
    if lang == "la":
        # naive latinization: replace of=de, to=ad, by=per (for *very* rough flavor)
        s2 = s.replace(" of ", " de ").replace(" to ", " ad ").replace(" by ", " per ")
        try:
            s2 = lat_norm(s2)
        except Exception:
            pass
        return f"[LATIN-FLAVORED] {s2}"
    elif lang == "grc":
        # koine/attic “feel” via loanwords (purely decorative)
        greekisms = {"wisdom":"σοφία", "word":"λόγος", "law":"νόμος", "life":"ζωή"}
        for en, gr in greekisms.items():
            s = s.replace(en, gr)
        return f"[GRC-FLAVORED] {s}"
    else:
        return s
