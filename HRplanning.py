import numpy

# Forecasting number of available workers
print("\n", "TASK 3")
D = numpy.array([[15,0,0],[0,20,0],[0,0,50]])
M = numpy.array([[5,2,0],[0,10,0],[5,5,45]])
b = numpy.array([[1],[2],[2]])
a = M@numpy.linalg.inv(D)@b
print("a=", "\n", a, "\n")
#code credits: Ruti:)

# Forecasting number of needed workers
print("\n","TASK 4", "\n")
X = numpy.array([[15,1,0,0],[17,1,0,0],[14,1,0,0],[6,0,1,0],[6,0,1,0],[5,0,1,0],[23,0,0,1],[27,0,0,1],[25,0,0,1]])
Y = numpy.array([[4],[6],[5],[7],[7],[9],[13],[12],[13]])
XTX = numpy.matmul(X.T,X)
print(XTX, "\n")
inverse = numpy.linalg.inv(XTX)
print(inverse, "\n")
XTY = numpy.matmul(X.T,Y)
print(XTY, "\n")
betas = numpy.matmul(inverse,XTY)
print(betas, "\n")
U = numpy.array([[10,1,0,0],[4,0,1,0],[20,0,0,1]])
BU = numpy.matmul(U, betas)
print("\n", "BU=", "\n", BU)
#code credits: Ruti:)
