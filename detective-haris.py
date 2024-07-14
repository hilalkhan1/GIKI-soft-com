def detective(string):
    
    # Create a dictionary to store the frequency of each character
    frequency = {}
    for s in string:
        if s in frequency.keys():
            # Increment the count if the char is already in the dict.
            frequency[s] += 1
        else:
            # Initialize the count to 1 if the char is not in the dict.
            frequency[s] = 1

    
    # Initialzie max and min frequency values    
    max_freq_value = float('-inf')
    min_freq_value = float('inf')

    # Counter for the maximum frequency
    max_freq_counter = 0

    # Iterate over the frequency dict to find the max and min frequency
    for key in frequency:
        if frequency[key] == max_freq_value:
            # Increment the max frequency if the current frequency is equal to max frequency
            max_freq_counter += 1
        
        if frequency[key] > max_freq_value:
            # Update the max frequency value and reset the max frequency counter
            max_freq_value = frequency[key]
            max_freq_counter = 1

        if frequency[key] < min_freq_value:
            # Update the min frquency value
            min_freq_value = frequency[key]

    # Check if all frquencies are the same
    if (max_freq_value - min_freq_value) == 0:
        return "YES"


    # Check if the differnece between max and min frequencies is 1 
    elif (max_freq_value - min_freq_value) == 1:
        if max_freq_counter == 1:
            # If there is only one character with the max frequency, it's valid
            return "YES"
        else:
            # if there is more than one charcter with max frequency, it's not valid
            return "NO"
        
    else:
        # if the diff b/w max and min frequency is more than 1, it's not valid
        return "NO"



n = int(input()) # number of test cases
for i in range(n):
    string = input("") # read each string
    print(detective(string))