from palimpsest.transliterate import transliterate
def test_roundtrip_basic():
    s = "abc"
    out = transliterate(s, "theban")
    assert len(out) == 3
