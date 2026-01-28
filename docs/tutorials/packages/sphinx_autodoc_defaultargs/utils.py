"""Utility functions demonstrating sphinx-autodoc-defaultargs."""


def greet(name: str, greeting: str = "Hello", punctuation: str = "!") -> str:
    """
    Generate a greeting message.

    :param name: Name to greet
    :param greeting: Greeting word
    :param punctuation: Punctuation to end with
    :return: Formatted greeting
    """
    return f"{greeting} {name}{punctuation}"
