from numpy import *

print("Matrix1 is m*n. m is row and n is column.\nEnter m,n down.\nMatrix1:\n")

m = int(input("Enter m:"))

n = int(input("Enter n:"))

matrix1 = zeros((m,n))

print(matrix1,"\n")

print("Matrix2 is p*q. p is row and q is column.\nEnter p,q down.\nMatrix2:\n")

p = int(input("Enter p:"))

q = int(input("Enter q:"))

matrix2 = zeros((p,q))

print(matrix2,"\n")

print("\nYou must add",m*n,"numbers to matrix1.\nYou must add",p*q,"numbers to matrix2.\n")

print("Matrix1:")

count1 = 0

count2 = 0

list_m1 = []

list_n1 = []

list_m2 = []

list_n2 = []

for i in range(m):
    for j in range(n):
        print("A number is replace in",i,"*",j,".")
        
        num = int(input("Enter number:"))

        print("\n")
        
        matrix1[i][j] = num
        
        if num != 0:
            count1 += 1

            list_m1.append(i)
            list_n1.append(j)

print("Matrix2:")

for i in range(p):
    for j in range(q):
        print("A number is replace in",i,"*",j,".")

        num1 = int(input("Enter number:"))

        print("\n")

        matrix2[i][j] = num1

        if num1 != 0:
            count2 += 1

            list_m2.append(i)
            list_n2.append(j)
        
sparse1 = zeros((count1,3))

sparse2 = zeros((count2,3))

if count1 < (m*n) / 2:
    a = 0
    c = 0
    d = 0
    
    for i in range(len(list_m1)):
        sparse1[a,0] = list_m1[c]
        sparse1[a,1] = list_n1[d]
        sparse1[a,2] = matrix1[list_m1[c],list_n1[d]]
        c += 1
        d += 1
        a += 1

if count2 < (p*q) / 2:
    e = 0
    f = 0
    g = 0

    for i in range(len(list_m2)):
        sparse2[e,0] = list_m2[f]
        sparse2[e,1] = list_n2[g]
        sparse2[e,2] = matrix2[list_m2[f],list_n2[f]]
        e += 1
        f += 1
        g += 1

count3 = 0

h = 0
k = 0
    
for i in range(count1):
    k = 0
    if sparse1[h,k] == sparse2[h,k]:
        if sparse1[h,k+1] == sparse2[h,k+1]:
            count3 += 1
            
        else:
            count3 +=2

    h += 1

sparse3 = zeros((m,n))

if m == p and n == q:
    for i in range(m):
        for j in range(n):
            sparse3[i,j] = matrix1[i,j] + matrix2[i,j]

else:
    print("Error!We cant sm these matrixs.")
    exit()
    
sparse4 = zeros((count3,3))

l = 0
o = 0
r = 0

for i in range(m*n):
    if sparse3[l,o] != 0:
        sparse4[r,0] = l
        sparse4[r,1] = o
        sparse4[r,2] = sparse3[l,o]
        r += 1
        
    o += 1
    if o == n:
        o = 0
        l += 1

if n == p:
    sparse5 = zeros((m,q))
else:
    print("Error! We can multiply these matrix.")
    exit()

s = 0
t = 0
u = 0
count4 = 0
count5 = 0

for i in range(m*m*q):
    count4 += matrix1[s,t]*matrix2[t,u]
    t += 1

    if t == q:
        sparse5[s,u] = count4
        if count4 != 0:
            count5 += 1
            
        t = 0
        u += 1
        count4 = 0

    if u == q:
        u = 0
        s += 1

sparse6 = zeros((count5,3))

v = 0
w = 0
x = 0

for i in range(m*q):
    if sparse5[v,w] != 0:
        sparse6[x,0] = v
        sparse6[x,1] = w
        sparse6[x,2] = sparse5[v,w]
        x += 1
        
    w += 1
    if w == q:
        w = 0
        v += 1
        
print("The Matrix1 is sparse:\n",sparse1,"\n")

print("The Matrix2 is sparse:\n",sparse2,"\n")

print("Sum of this 2 sparse matrix is:\n",sparse4,"\n")

print("Multiply of this 2 sparse matrix is:\n",sparse6,"\n")

quit = input("Please Enter to Exit.")
