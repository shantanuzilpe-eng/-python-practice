# Lab Assignment - 1

# Input: series of integers
nums = tuple(map(int, input("Enter integers separated by space: ").split()))

# a) Total number of items
print("Total number of items in the tuple:", len(nums))

# b) Print last item
if len(nums) > 0:
    print("Last item in the tuple:", nums[-1])
else:
    print("Tuple is empty")

# c) Print elements in reverse order
print("Tuple in reverse order:", nums[::-1])

# d) Check if tuple contains integer 5
if 5 in nums:
    print("Yes, tuple contains 5")
else:
    print("No, tuple does not contain 5")

# e) Remove first and last items, sort remaining items
if len(nums) > 2:
    remaining = nums[1:-1]
    sorted_tuple = tuple(sorted(remaining))
    print("Sorted tuple after removing first and last items:", sorted_tuple)
else:
    print("Not enough elements to remove first and last")
