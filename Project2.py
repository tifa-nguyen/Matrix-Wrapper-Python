from matrix_wrapper import MatrixWrapper

def main():
    matrixRow = int(input("Enter the number of matrix rows: "))
    matrixCol = int(input("Enter the number of matrix columns: "))
    myMatrix = MatrixWrapper(matrixRow, matrixCol)
    print(myMatrix)
    while True:
        print("Matrix Menu")
        print("1. Randomize the matrix")
        print("2. Change the rows and columns of the matrix")
        print("3. Change the value of a particular row and column")
        print("4. Display the maximum and minimum value of the matrix")
        print("5. Transpose the matrix")
        print("Please select an option:")
        choice = int(input())
        if choice == 1:
            myMatrix.randomMatrix()
            print(myMatrix)
        elif choice == 2:
            myMatrix.changeMatrix()
            print(myMatrix)
        elif choice == 3:
            myMatrix.changeElement()
            print(myMatrix)
        elif choice == 4:
            myMatrix.matrixMinMax()
            print(myMatrix)
        elif choice == 5:
            myMatrix.transpose()
            print(myMatrix)
        else:
            print("This is not a valid option. Please select again.")

if __name__ == "__main__":
    main()
