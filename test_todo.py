from todo import greet

def test_greet():
    # Intentional failure
    assert greet("Sam") == "Hi, Sam"   # but greet() returns "Hello, Sam"