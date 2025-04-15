import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pages.test_page import hello_from_pages
def test_import():
    assert hello_from_pages() == "Hello from pages!"