import matplotlib.pyplot as plt # Import Matplotlib library for creating plots
import numpy as np # Import NumPy library for numerical operations and array handling

def graphSnowfall(t):
    """ Create a bar plot to visualize the distribution of snowfall ranges.
    
    Parameters:
    t (str) - text file containing snowfall data; 
              each line represents a snowfall measurement 

    """
    # Initialize dictionary to hold counts for each snowfall range
    counts = {'a': 0, 'b':0, 'c':0, 'd':0, 'e':0} 

    # Open the file 't' 
    with open(t, 'r') as file: 
        lines = file.readlines() # read all the lines from the file

    # Iterate through each line in the file     
    for line in lines:
        value = int(line.strip()) # Convert the text line to integer
        # Update the count for the corresponding snowfall range
        if value >= 0  and value <= 10:
            counts['a'] += 1
        elif value >= 11 and value <= 20:
            counts['b'] += 1
        elif value >= 21 and value <= 30:
            counts['c'] += 1
        elif value >= 31 and value <= 40:
            counts['d'] += 1
        elif value >= 41 and value <= 50:
            counts['e'] += 1

    # Define the x-axis labels for snowfall ranges
    x = np.array(["0-10", "11-20", "21-30", "31-40", "41-50"])

    # Define the y-axis for the occurrences of snowfall in each range
    y = np.array([counts['a'], counts['b'], counts['c'], counts['d'], counts['e']]) 

    # Dreate a bar plot
    plt.bar(x,y)

    # Add axis labels and title to the plot
    plt.xlabel('Snowfall Range')
    plt.ylabel('Occurrences')
    plt.title('Snowfall Distribution')

    # Display the plot
    plt.show()