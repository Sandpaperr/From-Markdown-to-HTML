import unittest
from src.markdown_html import FromMarkdownToHTML


# setup a class to test the summation function
class TestSummation(unittest.TestCase):
    def test_h1(self):
        converter = FromMarkdownToHTML()

        self.assertEqual(converter.convertion("#Hello World"), "<h1>Hello World</h1>")
    
    def test_multiple_lines(self):
        converter = FromMarkdownToHTML()
        
        markdown = """#Hello\n#Bye"""

        expected_result = r"<h1>Hello</h1>\n<h1>Bye</h1>"
        self.assertEqual(converter.convertion(markdown), expected_result)
    
    def test_h2(self):
        converter = FromMarkdownToHTML()
        self.assertEqual()