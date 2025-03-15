# Arithmetic Formatter

## Description
The Arithmetic Formatter is a Python function that arranges arithmetic problems vertically for easier readability, similar to how they are arranged in primary school. This formatter takes arithmetic problems written horizontally and converts them to a visually appealing vertical format.

## Function

```python
arithmetic_arranger(problems, show_answers=False)
```

### Parameters
- `problems`: A list of strings representing arithmetic problems (e.g., `["32 + 698", "3801 - 2"]`)
- `show_answers`: A boolean indicating whether to display the answers to the problems (default is `False`)

### Return Value
- A string with the arithmetic problems arranged vertically and side-by-side

## Features

- Supports addition and subtraction operations
- Right-aligns numbers for proper vertical arithmetic
- Provides clear error messages for invalid inputs
- Optionally displays the calculated answers
- Handles multiple problems side by side with appropriate spacing

## Formatting Rules

- Numbers are right-aligned
- There is a single space between the operator and the longest operand
- The operator is on the same line as the second operand
- There are four spaces between each problem
- Dashes run the entire length of each problem

## Error Handling

The function will return error messages in the following cases:
- If there are more than five problems: `"Error: Too many problems."`
- If operators other than `+` or `-` are used: `"Error: Operator must be '+' or '-'."`
- If operands contain non-digit characters: `"Error: Numbers must only contain digits."`
- If operands have more than four digits: `"Error: Numbers cannot be more than four digits."`

## Examples

### Example 1: Basic Formatting
```python
arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])
```

Output:
```
   32      3801      45      123
+ 698    -    2    + 43    +  49
-----    ------    ----    -----
```

### Example 2: With Answers Displayed
```python
arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49", "988 + 40"], True)
```

Output:
```
   32         1      45      123      988
- 698    - 3801    + 43    +  49    +  40
-----    ------    ----    -----    -----
 -666     -3800      88      172     1028
```

## Usage

1. Import the function into your project:
   ```python
   from arithmetic_formatter import arithmetic_arranger
   ```

2. Call the function with your list of problems:
   ```python
   print(arithmetic_arranger(["32 + 698", "3801 - 2"]))
   ```

3. To display answers, set the second parameter to `True`:
   ```python
   print(arithmetic_arranger(["32 + 698", "3801 - 2"], True))
   ```

## Running Tests

A test suite is included to verify that the function works correctly. Run the tests by executing the script directly:

```
python arithmetic_formatter.py
```

