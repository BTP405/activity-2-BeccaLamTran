def wordCount(t):
     """ Count the occurences of each word in a text file and track
     the line numbers where each word appears.
     
     Parameters:
     t (str): A text file to be read/analyzed.

     Returns:
     dict: A dictionary containing words as keys and a list of line numbers as values.
     """
     # initialize an empty dictionary struct to store words
     word_dict = {} 
      # open file 't' for reading
     with open(t, 'r') as file:
        # read in the lines from the file and store in a list
        lines = file.readlines() 
         # use enumerate to iterate over lines along 
         # with its line number (index); start at 1 bc
         # counting line numbers (default is 0)
        for line_num, line in enumerate(lines, start=1):
            # split the lines into words, delimiter is whitespace by default
            words = line.split()
            #iterate over each word in the line
            for word in words:
                word = word.strip() #remove extra whitespace

                # check if the word isnt already in the dictionary
                if word not in word_dict:
                    word_dict[word] = [line_num]
                # also check if the line number is not already included in the list for that word
                # (e.g. same word multiple times in 1 line)
                elif line_num not in word_dict[word]:
                    word_dict[word].append(line_num) #line number not in the list, so append it
   
        # return the dictionary with the words and list of line numbers where the words are found 
        return word_dict