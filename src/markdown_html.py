class FromMarkdownToHTML():
    
    def convertion(self, text: str):
         return self.multiple_lines(text)
    
    def convert_header(self, text: str) -> str:
        header_count = 0
        copy_of_text = text

        while copy_of_text[0] == "#":
                header_count += 1
                copy_of_text = copy_of_text[1:]
        
        # for this exercise I assume that #Hello is valid and # Hello is not
        if header_count > 0 and not copy_of_text[0].isspace():
            if header_count <= 6:
                return "<h"+str(header_count)+">" + copy_of_text + "</h"+str(header_count)+">"
            else:
                return text
        else:
            return text
            
        
    def multiple_lines(self, text: str) -> str:
        splitted_markdown = text.split("\n")
        splitted_html = []

        for string in splitted_markdown:
            work_in_progress_text = self.convert_header(string)
            work_in_progress_text = self.convert_bold(work_in_progress_text)
            splitted_html.append(work_in_progress_text)
        
        final_text = r'\n'.join(splitted_html)

        return final_text
    
    #TODO: check if asterisks are consecutive and bold the content
    def convert_bold(self, text: str) -> str:
         instances_of_asterisk = [i for i, c in enumerate(text) if c == "*"]

         if len(instances_of_asterisk) > 3:
              list_of_pair_of_asterisks = []
              
              for i in range(len(instances_of_asterisk) - 1):
                   #if asterisk is next to another asterisk, save the position as a tuple
                   if instances_of_asterisk[i + 1] - instances_of_asterisk[i] == 1:
                        list_of_pair_of_asterisks.append((instances_of_asterisk[i], instances_of_asterisk[i + 1]))
                        #TODO: what happens if 3 or more asterisk are one after the other?

              if len(list_of_pair_of_asterisks) > 1:
                   for i in range (len(list_of_pair_of_asterisks)):
                        index_end_of_first_pair_of_asterisks = list_of_pair_of_asterisks[i][1]
                        index_start_of_second_pair_of_asterisks = list_of_pair_of_asterisks[i + 1][0]
                        #If 2 pairs of asterisks are next to each other or there are 3 asterisks it shouldn't create the bold (****, ***)
                        if index_start_of_second_pair_of_asterisks - index_end_of_first_pair_of_asterisks <= 1:
                             return text 
                        else:
                             #TODO: what if we got something like a**abbab**
                             #TODO: what if the sentence is today **I went** to school. Where does the rest of the sentence go?
                             return "<strong>" + text[index_end_of_first_pair_of_asterisks + 1: index_start_of_second_pair_of_asterisks] + "</strong>"
              else:
                   return text + "no pair"
                
                         
              
         else:
              return text

         
              
              
              
              
              
        
    
    

