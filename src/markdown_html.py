class FromMarkdownToHTML():
    
    def convertion(self, text: str):
         return self.multiple_lines(text)
    
    def h1(self, text: str) -> str:
        if text[0] == "#":
                return "<h1>" + text[1:] + "</h1>"
        
    def multiple_lines(self, text: str) -> str:
        splitted_markdown = text.split("\n")
        splitted_html = []

        for string in splitted_markdown:
            splitted_html.append(self.h1(string))
        
        final_text = r'\n'.join(splitted_html)

        return final_text
              
              
              
              
              
        
    
    

