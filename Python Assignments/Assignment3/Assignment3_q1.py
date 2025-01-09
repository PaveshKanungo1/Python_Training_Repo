def multiply_numbers(*args):
    product = 1
    for arg in args:
        try:
            number = float(arg)
            product *= number
        except ValueError:
            raise ValueError(f"Non-numeric input detected")
    return product

try:
    result = multiply_numbers(2, 3, '4', 5)
    print(result)
except ValueError as e:
    print(e)
