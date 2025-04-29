from app.services.simplification_service import simplify_text

def test_simplify():
    text = "This regulation applies to all residents regardless of income."
    simplified = simplify_text(text)
    assert isinstance(simplified, str)
    assert len(simplified) > 0