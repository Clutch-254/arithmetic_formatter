def arithmetic_arranger(problems, show_answers=False):
    # Check if there are too many problems
    if len(problems) > 5:
        return "Error: Too many problems."
    
    # Initialize lists to store each line of the arranged problems
    first1_line = []
    second2_line = []
    dash_line = []
    result_line = []
    
    
    for problem in problems:
        # This splits the problem into components
        components = problem.split()
        
        # Checks if the format is correct (should have 3 components: first operand, operator, second operand)
        if len(components) != 3:
            return "Error: Each problem should be in the format 'number operator number'."
        
        first_operand, operator, second_operand = components
        
        # Checkss if the operator is valid
        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."
        
        # Checks if the operands contain only digits
        if not (first_operand.isdigit() and second_operand.isdigit()):
            return "Error: Numbers must only contain digits."
        
        # Checks if the operands have more than 4 digits
        if len(first_operand) > 4 or len(second_operand) > 4:
            return "Error: Numbers cannot be more than four digits."
        
        # for calculate the width needed for alignment (max of both operands + 2 for operator and space)
        width = max(len(first_operand), len(second_operand)) + 2
        
        # For formating each line
        first1_line.append(first_operand.rjust(width))
        second2_line.append(operator + second_operand.rjust(width - 1))
        dash_line.append('-' * width)
        
        # Calculate the result if needed
        if show_answers:
            if operator == '+':
                result = int(first_operand) + int(second_operand)
            else:  
                result = int(first_operand) - int(second_operand)
            result_line.append(str(result).rjust(width))
    
    # For combining all problems 
    arranged_problems = '    '.join(first1_line) + '\n' + '    '.join(second2_line) + '\n' + '    '.join(dash_line)
    
    # For adding the results line if its needed
    if show_answers:
        arranged_problems += '\n' + '    '.join(result_line)
    
    return arranged_problems


# Test cases to test if the arithmetic formater works
def run_tests():
    # Test 1
    print("Test case 1:")
    result = arithmetic_arranger(["3801 - 2", "123 + 49"])
    expected = "  3801      123\n-    2    +  49\n------    -----"
    print(f"Result: {result}")
    print(f"Expected: {expected}")
    print(f"Test passed: {result == expected}\n")

    # Test 2
    print("Test case 2:")
    result = arithmetic_arranger(["1 + 2", "1 - 9380"])
    expected = "  1         1\n+ 2    - 9380\n---    ------"
    print(f"Result: {result}")
    print(f"Expected: {expected}")
    print(f"Test passed: {result == expected}\n")

    # Test 3
    print("Test case 3:")
    result = arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"])
    expected = "    3      3801      45      123\n+ 855    -    2    + 43    +  49\n-----    ------    ----    -----"
    print(f"Result: {result}")
    print(f"Expected: {expected}")
    print(f"Test passed: {result == expected}\n")

    # Test 4
    print("Test case 4:")
    result = arithmetic_arranger(["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"])
    expected = "  11      3801      1      123         1\n+  4    - 2999    + 2    +  49    - 9380\n----    ------    ---    -----    ------"
    print(f"Result: {result}")
    print(f"Expected: {expected}")
    print(f"Test passed: {result == expected}\n")

    # Test  5
    print("Test case 5:")
    result = arithmetic_arranger(["44 + 815", "909 - 2", "45 + 43", "123 + 49", "888 + 40", "653 + 87"])
    expected = "Error: Too many problems."
    print(f"Result: {result}")
    print(f"Expected: {expected}")
    print(f"Test passed: {result == expected}\n")

    # Test  6
    print("Test case 6:")
    result = arithmetic_arranger(["3 / 855", "3801 - 2", "45 + 43", "123 + 49"])
    expected = "Error: Operator must be '+' or '-'."
    print(f"Result: {result}")
    print(f"Expected: {expected}")
    print(f"Test passed: {result == expected}\n")

    # Test  7
    print("Test case 7:")
    result = arithmetic_arranger(["24 + 85215", "3801 - 2", "45 + 43", "123 + 49"])
    expected = "Error: Numbers cannot be more than four digits."
    print(f"Result: {result}")
    print(f"Expected: {expected}")
    print(f"Test passed: {result == expected}\n")

    # Test  8
    print("Test case 8:")
    result = arithmetic_arranger(["98 + 3g5", "3801 - 2", "45 + 43", "123 + 49"])
    expected = "Error: Numbers must only contain digits."
    print(f"Result: {result}")
    print(f"Expected: {expected}")
    print(f"Test passed: {result == expected}\n")

    # Test 9
    print("Test case 9:")
    result = arithmetic_arranger(["3 + 855", "988 + 40"], True)
    expected = "    3      988\n+ 855    +  40\n-----    -----\n  858     1028"
    print(f"Result: {result}")
    print(f"Expected: {expected}")
    print(f"Test passed: {result == expected}\n")

    # Test 10
    print("Test case 10:")
    result = arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49", "988 + 40"], True)
    expected = "   32         1      45      123      988\n- 698    - 3801    + 43    +  49    +  40\n-----    ------    ----    -----    -----\n -666     -3800      88      172     1028"
    print(f"Result: {result}")
    print(f"Expected: {expected}")
    print(f"Test passed: {result == expected}\n")


# Run the tests when the file is executed
if __name__ == "__main__":
    run_tests()