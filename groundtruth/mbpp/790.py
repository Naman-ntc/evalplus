"""
Write a python function to check whether every even index contains even numbers of a given list.
"""

def even_position(nums):
	assert isinstance(nums, list), "invalid inputs" # $_CONTRACT_$
	assert all(isinstance(i, int) for i in nums), "invalid inputs" # $_CONTRACT_$
	return all(nums[i]%2==i%2 for i in range(len(nums)))



assert even_position([3,2,1]) == False
assert even_position([1,2,3]) == False
assert even_position([2,1,4]) == True