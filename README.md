# palimpsest-bot
A research-grade bot that rewrites source texts in the style of OLD works and/or renders them into historical or “forgotten” scripts/languages (e.g., Theban alphabet attributed to Agrippa, Celestial alphabet, Classical Latin, Attic/Koine Greek, Coptic). Includes:
- Style adapter for archaic diction and syntactic inversions
- Transliteration engines for historical/occult alphabets
- Optional classical-language generation via open-source NLP
- Provenance + disclaimers baked into output metadata

⚠️ Accuracy note
This project **does not claim philological authenticity**. For real scholarship, keep the provenance blocks and cite original editions. Many “occult” alphabets are *cipher scripts* mapping modern letters, not actual languages.

## Features
- Style transfer: Early-Modern English, Late Latin, Koine Greek-like diction (heuristic)
- Script transliteration: Theban, Celestial; easy plugin interface for new scripts
- Classical language support (where feasible): Latin (CLTK/latindata), Greek (polytonic)
- Prompt/LLM driver or “LLM-free” heuristic mode
- YAML configs for pipelines; CLI + Python API
- Unit tests; reproducible seeds; metadata stamped into every artifact

## Quickstart
```bash
# 1) create & activate env
python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate

# 2) install
pip install -r requirements.txt

# 3) run a simple rewrite (archaic Early-Modern English)
python src/palimpsest/main.py \
  --input "Knowledge is the seed; discipline the rain." \
  --style early_modern_en \
  --out out/seed_earlymodern.txt

# 4) transliterate same line into Theban alphabet (cipher)
python src/palimpsest/main.py \
  --input "Knowledge is the seed; discipline the rain." \
  --script theban \
  --out out/seed_theban.txt

# 5) pipeline: archaic style → Latin attempt → Celestial script
python src/palimpsest/main.py \
  --input "Light seeks the path through shadow." \
  --style early_modern_en \
  --target_lang la \
  --script celestial \
  --out out/light_pipeline.txt \
  --config configs/pipeline.default.ymll

Examples
	•	style: early_modern_en → “Knowledge is the seed; and discipline the rain, whereby the mind bringeth forth increase.”
	•	script: theban → same sentence rendered in Theban glyphs (see docs/samples/).

Architecture
	•	normalizer → cleans input (unicode, punctuation, casing)
	•	style_transfer → rule-based archaizer + optional LLM helper
	•	classical_gen → Latin/Greek helpers via CLTK or templates
	•	transliterate → pluggable script mappers (Theban, Celestial, user-defined)
	•	provenance → inserts a JSON block (source hash, time, config, model)

Add a new script

Create src/palimpsest/scripts/my_script.py exporting:
NAME = "my_script"
MAPPING = {"a": "…", "b": "…", ...}

Then register it in registry.py.

Ethics & Licensing
	•	Public-domain texts only for full reproduction; otherwise quote sparingly and cite.
	•	Outputs include a Provenance footer by default.
	•	License: MIT (see LICENSE).

Roadmap
	•	Better Latin morphology with lemmas & inflection templates
	•	Coptic transliteration + rendering
	•	Fine-tuned archaic-English n-gram model (LLM-free mode)

# requirements.txt
```txt
regex>=2024.5.10
unidecode>=1.3.8
PyYAML>=6.0.2
click>=8.1.7
rapidfuzz>=3.9.7
cltk>=1.2.0    # classical languages toolkit (Latin/Greek utilities)
# requirements.txt
```txt
regex>=2024.5.10
unidecode>=1.3.8
PyYAML>=6.0.2
click>=8.1.7
rapidfuzz>=3.9.7
cltk>=1.2.0    # classical languages toolkit (Latin/Greek utilities)
