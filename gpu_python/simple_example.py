import numpy as np
import time
import sys



def intialize():
	X = np.random.rand(r,3)
	return X

def matrix_add(a,b):
	Z = a + b
	return Z
def matrix_maltil(a,b):
	m = a * b
	return m
def print_arry(X):
	print('Array value :')
	print(X)



r = input("Enter number of Rows: ")
c = input("Enter number of Cols: ")
print(r,c)
#r=3
#c=3
A = np.array((r,c),dtype=np.float32)
B = np.array((r,c),dtype=np.float32)
C = np.array((r,c),dtype=np.float32)

A = intialize()
B = intialize()
start_time = time.time()
add = matrix_add(A,B)
print('serial execution time:',(time.time() - start_time))
#print(time.time() - start_time)
mul = matrix_maltil(A,B)

print_arry(A)
print_arry(B)
print_arry(add)
print_arry(mul)

