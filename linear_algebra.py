import numpy as np

arr = np.matrix('[5,2,-1; 3,-4,1; 8,-2,6]')

# fuction prints matrix transpose 
def transpose(array):

	print("transpose of matrix arr: \n\n", array.transpose())  
	
# function returns inverse of given matrix
def matrix_inverse(array):
	
	inverse_matrix = np.linalg.inv(array)
	print("inverse of matrix arr: \n\n", inverse_matrix)

# function returns sum of diagonal elements	
def diagonal_sum(array):
	
	sum_of_diagonal_elements = np.trace(array)
	print("diagonal sum of matrix arr: ", sum_of_diagonal_elements)	
	
# function returns identity matrix by eye() function's parameter
def identity_matrix():
	
	ar = np.eye(4)
	print("indentity matrix: \n\n", ar)
	
		
	
if __name__ == "__main__":
	transpose(arr)
	print("\n")
	matrix_inverse(arr)
	print("\n")
	diagonal_sum(arr)
	print("\n")
	identity_matrix()
