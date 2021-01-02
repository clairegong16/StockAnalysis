import random #for importing the code to generate random numbers 
import matplotlib.pyplot as plt #for importing the plotting a graph

#sum of t from t = 1 to n
#it should be n(n+1)/2
def sumoft(n):
    sum = 0
    for t in range(0,n):
        sum = t + 1 + sum
    if sum != n*(n+1)/2:
        print("sumoft error")
    return sum

#sum of t squared 
def sumoft2(n):
    sum = 0
    for t in range(0,n):
        sum = (t + 1)**2 + sum
    return sum 

#sum of elements in the y list
def sumofyt (ylist):
    sum = 0
    for i in ylist:
        sum = sum + i
    return sum

#sum of elements in the y list multiplied by t
def sumoft_ylist (ylist):
    sum = 0
    for i in range(0, len(ylist)):
        sum = sum + (i + 1) * ylist[i]
    return sum

print(sumoft(100)) #testing sumoft
for i in range (0,5): #testing sumoft2
    print(sumoft2(i+1)) 
print(sumofyt([1,3,-3,-1])) #testing sumofyt
print(sumoft_ylist([3,2,1])) #testing sumoft)ylist 

#calulating m
def calcm(ylist):
    mnum = sumoft_ylist(ylist) - (1/(len(ylist))*sumofyt(ylist)*sumoft(len(ylist))) #mnum = m numerator
    mden = sumoft2(len(ylist)) - (1/len(ylist))*(sumoft(len(ylist)))**2
    m = mnum/mden
    return m
#calculating b 
def calcb(ylist):
    b = -(calcm(ylist)/len(ylist))*sumoft(len(ylist)) + 1/(len(ylist))*sumofyt(ylist)
    return b
#returns m and b
def calcm_and_b(ylist, name):
    m = calcm(ylist)
    b = calcb(ylist)
    '''plt.plot(ylist, color ='blue', label= name)
    plt.show()'''
    return m,b


if __name__ == "__main__": #doesn't run below code if you run from a different file 
#generation of testing data
    m = 0.1
    b = 5
    n = 100
    yhatlist = []
    ylist = []
    for i in range(0,n):
        noise = random.uniform(-1,1)
        y = m*(i+1)+b
        yhat = y + noise
        yhatlist.append(yhat)
        ylist.append(y)

    plt.plot(yhatlist, color ='blue', label= "yhat")
    plt.plot(ylist, color ='red', label = "y")
    plt.xlabel('time')
    plt.ylabel('adj close price')
    plt.legend()
    plt.show()
    print("calc m:", calcm(yhatlist))
    print("calc b:", calcb(yhatlist))

