from app import make_greeting


def test_greeting_with_name():
    assert make_greeting("An") == "Xin chào, An!"


def test_greeting_with_spaces():
    assert make_greeting("  An  ") == "Xin chào, An!"


def test_greeting_with_empty_name():
    assert make_greeting("") == "Xin chào, bạn!"


def test_greeting_with_only_spaces():
    assert make_greeting("   ") == "Xin chào, bạn!"


def test_greeting_with_vietnamese_name():
    assert make_greeting("Nguyễn Văn A") == "Xin chào, Nguyễn Văn A!"

