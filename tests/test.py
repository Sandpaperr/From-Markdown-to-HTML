import unittest
from src.markdown_html import FromMarkdownToHTML


# setup a class to test the conversion function
class TestSummation(unittest.TestCase):
    converter = FromMarkdownToHTML()
    def test_h1(self):
        

        self.assertEqual(self.converter.convertion("#Hello World"), "<h1>Hello World</h1>")

    
    def test_multiple_lines(self):
        
        
        markdown = """#Hello\n#Bye"""

        expected_result = r"<h1>Hello</h1>\n<h1>Bye</h1>"
        self.assertEqual(self.converter.convertion(markdown), expected_result)

    
    def test_h2(self):

        markdown = "##Hello"
        expected_result = "<h2>Hello</h2>"
        self.assertEqual(self.converter.convertion(markdown), expected_result)

    def test_h3(self):

        markdown = "###Hello"
        expected_result = "<h3>Hello</h3>"
        self.assertEqual(self.converter.convertion(markdown), expected_result)


    def test_h4(self):

        markdown = "####Hello"
        expected_result = "<h4>Hello</h4>"
        self.assertEqual(self.converter.convertion(markdown), expected_result)


    def test_h5(self):

        markdown = "#####Hello"
        expected_result = "<h5>Hello</h5>"
        self.assertEqual(self.converter.convertion(markdown), expected_result)


    def test_h6(self):

        markdown = "######Hello"
        expected_result = "<h6>Hello</h6>"
        self.assertEqual(self.converter.convertion(markdown), expected_result)


    def test_h7(self):

        markdown = "#######Hello"
        expected_result = "#######Hello"
        self.assertEqual(self.converter.convertion(markdown), expected_result)

    def test_hash_whitespace(self):

        markdown = "##### Hello"
        expected_result = "##### Hello"
        self.assertEqual(self.converter.convertion(markdown), expected_result)

    def test_bold(self):

        markdown = "**Amber**"
        expected_result = "<strong>Amber</strong>"
        self.assertEqual(self.converter.convertion(markdown), expected_result)

    #TODO: what if we got something like a**abbab**
    #TODO: what if the sentence is today **I went** to school. Where does the rest of the sentence go?
    
