import numpy

A = numpy.matrix([[1,2,3,-2,-1],[3,5,5,-3,-9],[2,3,2,0,-8],[2,6,7,-5,1],[1,2,6,-4,-10]])
B = numpy.matrix([[6],[2],[-5],[17],[12]])
A_inverse = numpy.linalg.inv(A) #oblicz odwrotnosc macierzy
X = A_inverse * B
print(X)