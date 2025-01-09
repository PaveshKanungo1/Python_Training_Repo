import numpy as np

class MathOperations:
    def add(a, b):
        return a + b
    
    def subtract(a, b):
        return a - b
    
    def multiply_matrices(matrix1, matrix2):
        try:
            result = np.dot(matrix1, matrix2)
            return result
        except ValueError as e:
            print(f"Error in matrix multiplication: {e}")
            return None