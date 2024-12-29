def add_matrices(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def subtract_matrices(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def multiply_matrices(A, B):
    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    return result

def print_matrix(matrix):
    for row in matrix:
        print(row)

def main():
    print("Matrix Calculator")
    print("1. Add Matrices")
    print("2. Subtract Matrices")
    print("3. Multiply Matrices")
    choice = int(input("Choose an operation (1-3): "))

    if choice in [1, 2, 3]:
        rows = int(input("Enter number of rows: "))
        cols = int(input("Enter number of columns: "))
        
        print("Enter first matrix:")
        A = [list(map(int, input("Enter row values separated by space: ").split())) for _ in range(rows)]
        
        print("Enter second matrix:")
        B = [list(map(int, input("Enter row values separated by space: ").split())) for _ in range(rows)]
        
        if choice == 1:
            result = add_matrices(A, B)
            print("Result of Addition:")
        elif choice == 2:
            result = subtract_matrices(A, B)
            print("Result of Subtraction:")
        elif choice == 3:
            result = multiply_matrices(A, B)
            print("Result of Multiplication:")
        
        print_matrix(result)
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
