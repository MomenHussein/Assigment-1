
import numpy as np

def dotmultiplication(mat1=[[]],mat2=[[]]):
    
    dimensions1 = np.shape(mat1)
    R1, C1 = dimensions1
    dimensions2 = np.shape(mat2)
    R2, C2 = dimensions2
    if C1 == R2:
        res = [[0 for x in range(R1)] for y in range(C2)] 
     
    # explicit for loops
        for i in range(0, R1):
            for j in range(0, C2):
                for k in range(0, R2):
                    res[i][j] += mat1[i][k] * mat2[k][j]
        return res
    else:
        return "Sorry Invalid Dimensions"
    
        

def inverse(a=[]):

    return np.linalg.inv(a)

def transpose(arr=[]):
    return (list(map(list, zip(*arr))))
    
def NormalEquation(a=[],b=[]):
    return (dotmultiplication(inverse(dotmultiplication(transpose(a),a))),dotmultiplication(transpose(a),b))

# Another way of linear Equation
def NormalEquation2(a=[],b=[]):
    a_tran = transpose(a)
    mult = dotmultiplication(a_tran,a)
    mult_inv = inverse(mult)
    mult2 = dotmultiplication(a_tran,b)
    x_n = dotmultiplication(mult_inv,mult2)
    return x_n