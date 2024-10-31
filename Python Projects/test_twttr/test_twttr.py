from twttr import shorten

def test_letter():
    assert shorten("Hello") == "Hll"
    assert shorten("My PeT iS bArKiNg") == "My PT S brKNg"
    assert shorten("Hello!") == "Hll!"
    assert shorten("Hello123") == "Hll123"
