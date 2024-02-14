def printStats(t):
      """ Print statistics: count, average, maximum for a list of numbers read from a file.
      
      Parameters:
      t (str): Text file containing lines of numbers 
      """
      # open file 't' for reading
      with open(t, 'r') as file: 
        # read in lines from the file and store in a list
        lines = file.readlines() 
        for line in file:
            #call the decorator function for each line
            read_num(line)

def print_decorator(func):
    def wrapper(nums):
        # call the original function to get the numbers
        results = func(nums)
        # calculate the stats
        count = len(results) # length of the list is the number of numbers
        total = sum(results) # get the sum to calculate the average
        avg = total / count # sum divided by number of elements
        max = max(results)

        # print the stats
        print("Numbers: ", results)
        print("Count: ", count)
        print("Average: ", avg) 
        print("Maximum: ", max) 
        # return the result of the original function after the extra 
        # functionality from the decorator is executed
        return results 
    return wrapper

@print_decorator
def read_num(line):
    # convert the line of numbers into a list integers
    # strip() to remove extra white space at beginning and end of line
    # split() to split string into substring using whitespace delimiter
    # map() so that int() is applied to each element from line.strip().split()
    # int() to convert from string to integer
    # list() to convert the output from map(an iterable)into a list
    return list(map(int, line.strip().split()))