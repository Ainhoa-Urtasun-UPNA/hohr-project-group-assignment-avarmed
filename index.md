#                                                                               AVARMED

If the images do not work, please visit: https://docs.google.com/presentation/d/1tQ6YnvLIhR6890R4hFa8KOZzscMGlRhlKx-XU9JUlDY/edit?usp=sharing

![Image](https://github.com/Ainhoa-Urtasun-UPNA/hohr-project-group-assignment-avarmed/blob/facdb207991ae752f47783edab4a7d79892f35f5/Logo%20slogan%20naics%20avarmed.jpg)

## About us:
![Image](https://github.com/Ainhoa-Urtasun-UPNA/hohr-project-group-assignment-avarmed/blob/gh-pages/Primary%20and%20support%20activities.jpg)
![Image](https://github.com/Ainhoa-Urtasun-UPNA/hohr-project-group-assignment-avarmed/blob/gh-pages/Cognitive%20Routine%20Esquema.jpg)


### Recruitment Process:

1) **Job posting**

2) **Sorting and screening out job candidates happens**

3) **Hiring process:**

   -Resume and credentials

   -Psychotechnical exam 

   -Interview

   -Practical part

4) **Onboarding**

### Work with us!:  
![Image](https://github.com/Ainhoa-Urtasun-UPNA/hohr-project-group-assignment-avarmed/blob/3b317b99ecb666632c88b2d6b26b76d456ac4d22/Job%20Postings.png)


### Our team and our future
![Image](predictionworkers.PNG)


```markdown


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
