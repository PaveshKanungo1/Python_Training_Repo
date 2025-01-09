import numpy as np
from math_operations import MathOperations

def get_matrix_input(str):
    try:
        rows = int(input(f"Enter the number of rows: "))
        cols = int(input(f"Enter the number of cols: "))
        print(f"Enter the row-wise elements: ")
        elements = list(map(float, input().split()))
        if len(elements) != rows * cols:
            print("The number of elements are not equal")
            return None
        matrix = np.array(elements).reshape(rows, cols)
        return matrix
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return None


def main():
    print("::Math Operations Program::")
    while True:
        print("\nSelect an operation")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Matrix Multiplication")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == 1 or choice == 2:
            try:
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
                if choice == 1:
                    result = MathOperations.add(num1, num2)
                else:
                    result = MathOperations.substract(num1, num2)
                print(f"Result: {result}")
            except ValueError:
                print("Invalid Input.")

        elif choice == 3:
            matrix1 = get_matrix_input("Matrix 1")
            if matrix1 is None:
                continue
            matrix2 = get_matrix_input("Matrix 2")
            if matrix2 is None:
                continue
            result = MathOperations.multiply_matrices(matrix1, matrix2)
            if result is not None:
                print("The result of matrix multiplication is:")
                print(result)
        elif choice == '4':
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
