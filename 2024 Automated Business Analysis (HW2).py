# 2. Write a python function to find the average of odd numbers till a given number.
# For example:
# 	Given number:8
# 	List:[1,3,5,7]
# 	Average:4

def average_of_odd_numbers(n):
    odd_numbers = [num for num in range(1, n+1) if num % 2 != 0]
    if len(odd_numbers) == 0:
        return "No odd numbers found"
    else:
        return sum(odd_numbers) / len(odd_numbers)

# Example
given_number = 8
average = average_of_odd_numbers(given_number)
print(f"Given number: {given_number}")
print(f"List: {list(range(1, given_number+1, 2))}")
print(f"Average: {average}")
