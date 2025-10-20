import random, regex as re

def archaize(text: str, style_name: str, opts: dict) -> str:
    rnd = random.Random(opts.get("seed", 1337))
    if style_name == "early_modern_en":
        text = _early_modern_en(text, rnd, opts)
    # add more styles here
    return text

THOU_MAP = {
    r"\byou\b": "thou",
    r"\byour\b": "thy",
    r"\byours\b": "thine",
    r"\bare\b": "art",
    r"\bhave\b": "hast",
    r"\bdo\b": "dost",
}

def _early_modern_en(s: str, rnd, opts):
    # light pronoun/verb swaps
    if opts.get("archaic_pronouns", True):
        for pat, rep in THOU_MAP.items():
            s = re.sub(pat, rep, s, flags=re.I)

    # sprinkle “-eth/-est”
    s = re.sub(r"\b(is)\b", "is", s)
    s = re.sub(r"\b(has)\b", "hath", s, flags=re.I)
    s = re.sub(r"\b(does)\b", "doth", s, flags=re.I)

    # syntactic inversion sometimes
    if rnd.random() < opts.get("invert_clauses", 0.2):
        s = _invert_once(s)

    # lexis seasoning
    s = s.replace("perhaps", "peradventure").replace("before", "ere")
    return s

def _invert_once(s: str) -> str:
    # very naive inversion of main clause commas/semicolons
    parts = re.split(r"([;,:])", s, 1)
    if len(parts) == 3:
        return parts[2].strip().capitalize() + parts[1] + " " + parts[0].strip().lower()
    return s
