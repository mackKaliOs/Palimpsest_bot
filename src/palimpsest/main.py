import json, hashlib, time, yaml, click
from palimpsest.normalizer import normalize
from palimpsest.style_transfer import archaize
from palimpsest.classical_gen import to_classical
from palimpsest.transliterate import transliterate
from palimpsest.provenance import add_provenance_footer

def hash_text(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()[:12]

@click.command()
@click.option("--input", "inp", required=True, help="Source text to process.")
@click.option("--style", type=str, default=None, help="Style adapter (e.g., early_modern_en).")
@click.option("--target_lang", type=str, default=None, help="Classical language target: la, grc.")
@click.option("--script", type=str, default=None, help="Transliteration script: theban, celestial.")
@click.option("--config", type=click.Path(exists=True), default=None, help="YAML pipeline config.")
@click.option("--out", type=click.Path(), default="out/output.txt", help="Output file.")
def cli(inp, style, target_lang, script, config, out):
    cfg = {}
    if config:
        with open(config, "r", encoding="utf-8") as f:
            cfg = yaml.safe_load(f) or {}
    text = normalize(inp)

    if style or cfg.get("style", {}).get("name"):
        style_name = style or cfg["style"]["name"]
        text = archaize(text, style_name, cfg.get("style", {}))

    if (target_lang and target_lang != "auto") or cfg.get("classical", {}).get("enable", False):
        lang = target_lang or cfg.get("classical", {}).get("target_lang", "la")
        if lang == "auto": lang = "la"
        text = to_classical(text, lang)

    if script or cfg.get("transliteration", {}).get("script"):
        script_name = script or cfg["transliteration"]["script"]
        text = transliterate(text, script_name)

    prov = {
        "source_hash": hash_text(inp),
        "time_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "style": style or cfg.get("style", {}).get("name"),
        "target_lang": target_lang or cfg.get("classical", {}).get("target_lang"),
        "script": script or cfg.get("transliteration", {}).get("script"),
        "config_used": bool(config),
        "version": "0.1.0"
    }
    text = add_provenance_footer(text, prov, cfg.get("provenance", {}))

    os.makedirs("out", exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(text)
    click.echo(f"Wrote {out}")

if __name__ == "__main__":
    import os
    cli()
