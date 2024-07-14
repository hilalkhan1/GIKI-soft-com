def find_chosen_one(p):
    step = 0 # Step counter
    index = 0 # Initialize the starting index
    people = list(range(1, p + 1)) # Create a list of people from 1 to p

    while len(people) > 1: # Loop until only one person is left
        index = (index + step) % len(people) # Calculate the next index using the current step 
        del people[index] # Remove the person at the calculated index
        step += 1 # increment the step counter

    return people[0] # return the last remaining person


t_cases = int(input()) # number of test cases
for i in range(t_cases): # loop through each test case
    num_of_people = int(input()) # No. of people current test case
    print(find_chosen_one(num_of_people))
