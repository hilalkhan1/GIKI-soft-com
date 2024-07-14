def is_power_of_two(n):
	# by bit manipulation
	# power of two digits has only one, 1 at starting in binary
	return "YES" if n > 1 and bin(n).count("1") == 1 else "NO"

test_cases = int(input())
for i in range(test_cases):	
	num = int(input())
	print(is_power_of_two(num))
