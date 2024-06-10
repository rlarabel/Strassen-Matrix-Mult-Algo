#####################################
# Title: Strassen Matrix Multiplication
# Author: Ramses Larabel
# Class: Design and Analysis of Algorithms
# Description: This algorithm finds the result of two matrices being multiplied together. 
#	This solution uses the strassen matrix multiplication formula and recursive function calls to minimize time complexity.
# Inputs: Let X be a 2D list representing the first matrix, let Y be a 2D list representing the second matrix, and
#	let n be the # rows and columns in both matrices.
# Outputs: Let result be a 2D list representing the final matrix after being multiplied.
# Time Complexity: O(n^2.8074)
#######################################


def main():
	X = [[1,1,2,1],[2,0,3,2],[3,4,2,3],[1,3,4,2]]
	Y = [[2,1,2,1],[0,1,0,3],[4,3,2,3],[3,2,4,2]]
	n = 4
	print("X:")
	printMatrix(X)
	print("Y:")
	printMatrix(Y)  
	result = strassenMM(X,Y,n)
	

def strassenMM(X,Y,n):
	if n == 1:
		print("Base Case 1x1 Matrix:")
		print("A * B = ", X[0][0] * Y[0][0])
		print()
		return [[X[0][0] * Y[0][0]]]
	else:
		t = int(n / 2)
		A, B, C, D = splitMatrix(X, t)
		E, F, G, H = splitMatrix(Y, t)

		S1 = strassenMM(A, matrixSub(F, H, t), t)
		S2 = strassenMM(matrixAdd(A, B, t), H, t) 
		S3 = strassenMM(matrixAdd(C, D, t), E, t) 
		S4 = strassenMM(D, matrixSub(G, E, t), t) 
		S5 = strassenMM(matrixAdd(A, D, t), matrixAdd(E, H, t), t) 
		S6 = strassenMM(matrixSub(B, D, t), matrixAdd(G, H, t), t) 
		S7 = strassenMM(matrixSub(A, C, t), matrixAdd(E, F, t), t)

		I = matrixSub(matrixAdd(matrixAdd(S5, S6, t), S4, t), S2, t)
		J = matrixAdd(S1, S2, t)
		K = matrixAdd(S3, S4, t)
		L = matrixAdd(matrixSub(matrixSub(S1, S7, t), S3, t), S5, t)

		result = [[ 0 for _ in range(n)] for _ in range(n)]
		for i in range(t):
			for j in range(t):
				result[i][j] = I[i][j]
				result[i][j+t] = J[i][j]
				result[i+t][j] = K[i][j]
				result[i+t][j+t] = L[i][j] 
		if (n != 4):
			print("Intermediate Results:")
		else:
			print("Final Results:")
		printMatrix(result)
		print()
		return result

def splitMatrix(A, n):
	W = [row[:n] for row in A[:n]]
	X = [row[n:] for row in A[:n]]
	Y = [row[:n] for row in A[n:]]
	Z = [row[n:] for row in A[n:]]

	return W, X, Y, Z

def matrixAdd(A , B, n):
	addM = [[ 0 for _ in range(n)] for _ in range(n)]
	for i in range(n):
		for j in range(n):
			addM[i][j] = A[i][j] + B[i][j]
	return addM

def matrixSub(A, B, n):
	subM = [[ 0 for _ in range(n)] for _ in range(n)]
	for i in range(n):
		for j in range(n):
			subM[i][j] = A[i][j] - B[i][j]
	return subM

def printMatrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))

if __name__ == "__main__":
	main()