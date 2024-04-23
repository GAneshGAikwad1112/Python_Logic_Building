def matrix(m, n):
    o = []
    for i in range(m):
        row =[]
        for j in range (n):
            inp = int(input(f"Enter o[{i}, {j}]"))
            row.append(inp)
        o.append(row)
    return o

def sum(A, B):
    output = []
    for i in range (len(A)):   #number of rows
        row = []
        for j in range(len(A[0])):  #number of columns
            row.append(A[i] + B[j]) 


m = int(input("En{ter the value of m: "))
n = int(input("Enter the value of n: "))

print("Enter Matrix A")
A = matrix(m, n)
print("Enter Matrix B")
B = matrix(m, n)