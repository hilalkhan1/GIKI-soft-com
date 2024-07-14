
def is_sorted():
    
        length = int(input("")) # read the len of the list
        nums = list(map(int, input().split())) # read the list of integers
        if sorted(nums) == nums: #if list is already sorted
            return ("YES")
        first = nums[:-3] # Extract the lsit excluding last three elements
        last3 = nums[-3:] # extract the last three elements
        for i in range(3):
            
            # Perform a rotation of last three elements 
            last3[0], last3[1], last3[2] = last3[1], last3[2], last3[0]

            # Create a tempprory list by combining the first part and the rotated last three elements
            temp1 = first.copy()
            temp1.extend(last3)

            # Check if the rotated list is sorted
            if temp1 == sorted(nums):
                return "YES"
            
            # Perform another rotation
            last3[0], last3[1], last3[2] = last3[1], last3[2], last3[0]
            # Create another temp list by combing first part and last three elements
            temp2 = first.copy()
            temp2.extend(last3)
            if temp2 == sorted(nums): # check if the list is sorted
                return "YES"
            else:
                return "NO" # if the list is not sorted after these rotations

            

test_cases = int(input("")) # number of test cases
for test_case in range(test_cases): # Loop through each test case
    print(is_sorted())

