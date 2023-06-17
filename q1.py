
'''
    Write a function called calculate_statistics that takes a list of numbers as a parameter.
    
    This function should calculate and print the following statistics about the numbers:
    
    The minimum value
    The maximum value
    The total sum of numbers
    The average of the numbers (you can calculate this as the sum divided by the number of elements)
    
'''
def calculate_statistics(numbers):
    min_val = min(numbers)
    max_val = max(numbers)
    total_sum = sum(numbers)
    average = total_sum / len(numbers)
    
    print("Minimum: ", min_val)
    print("Maximum: ", max_val)
    print("Sum: ", total_sum)
    print("Average: ", average)

calculate_statistics([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
