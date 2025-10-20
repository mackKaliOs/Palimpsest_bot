from palimpsest.scripts.registry import get_script

def transliterate(s: str, script_name: str) -> str:
    script = get_script(script_name)
    if not script:
        raise ValueError(f"Unknown script: {script_name}")
    out = []
    for ch in s.lower():
        out.append(script.get(ch, ch))
    return "".join(out)
