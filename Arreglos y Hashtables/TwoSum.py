#Naive Solution
def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []


#Solución ordenar y Two Pointer
def twoSum(nums, target):
    # Create a list of tuples, where each tuple contains the original index and the element
    indexed_nums = [(i, num) for i, num in enumerate(nums)]
    
    # Sort the list of tuples by the elements
    indexed_nums.sort(key=lambda x: x[1])
    
    # Initialize two pointers, one at the beginning of the list and one at the end
    left = 0
    right = len(indexed_nums) - 1
    
    # Keep looping until the pointers meet
    while left < right:
        # Calculate the sum of the elements at the pointers
        sum = indexed_nums[left][1] + indexed_nums[right][1]
        
        # If the sum is equal to the target, return the indices
        if sum == target:
            return [indexed_nums[left][0], indexed_nums[right][0]]
        
        # If the sum is less than the target, move the left pointer to the right
        elif sum < target:
            left += 1
        
        # If the sum is greater than the target, move the right pointer to the left
        else:
            right -= 1
    
    # If the target is not found, return an empty list
    return []
  
#Solución optima:
def twoSum(nums, target):
    # Create an empty dictionary to store the indices of the elements
    indices = {}
    # Iterate through the list of numbers
    for i, num in enumerate(nums):
        # Check if the target minus the current number is in the dictionary
        if target - num in indices:
            # If it is, return the indices of the pair
            return [indices[target - num], i]
        # Otherwise, add the current number and its index to the dictionary
        indices[num] = i
    # If no pair was found, return an empty list
    return []
