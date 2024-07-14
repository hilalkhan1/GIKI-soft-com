def equity(arr, k):
    e_array = [] # Initialzie and epmty list ot store the k smallest elements
    for i in range(k):
        minmum = min(arr) # Find the minimum element in the array
        e_array.append(minmum) # Append the minimum element to e_array
        arr.remove(minmum) #reomve minimum element from original array

    return max(e_array) - min(e_array) # return the diff





def main():
    test_cases = int(input()) # No. of test cases
    for i in range(test_cases):
        arr = []
        len_of_arr = int(input()) # length of array
        k = int(input()) # Number of smallest elements to consider
        for i in range(len_of_arr): # Loop to read the elements of array
            num = int(input()) # Read the each element
            arr.append(num) # append the element to array
        print(equity(arr, k))

main()
