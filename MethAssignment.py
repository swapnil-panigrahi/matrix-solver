def take_first(x):
    return x[0]

def leading_one(x):
    for i in range(len(x)):
        if x[i]!=0:    
            y=i
            break
    else:
        return [0 for i in range(len(x))] 
    leading_coeff=x[y]
    
    for i in range(len(x)):
        x[i]=x[i]/leading_coeff
        
    return x

def check_echelon(x):
    for i in range(len(x)-1):
        if x[i]!=[0 for z in range(len(x[0]))] and x[i+1]!=[0 for z in range(len(x[0]))]:
            j=x[i].index(1)
            k=x[i+1].index(1)
        
            if j>=k:
                return False
    else:
        return True

def row_to_reduce(x):
    for i in range(len(x)-1):
        j=x[i].index(1)
        k=x[i+1].index(1)
        
        if j==k:
            return i+1
    else:
        return False

i,j=map(int,input("Enter the dimensions of the matrix: ").strip().split())

matrix=[]
for x in range(i):
    row=list(map(float,input("Enter Row: ").strip().split()[:j]))+[0]
    matrix.append(row)
    
'''
1 2 3 0
4 5 6 0
7 8 9 0

1 0 -1 0
0 1  2 0
0 0  0 0 
''' 

for x in range(i):
        matrix[x]=leading_one(matrix[x])
        
while check_echelon(matrix)==False:
    matrix.sort(reverse=True)
    
    y=row_to_reduce(matrix)
    if y!=0:
        leading_index=matrix[y].index(1)
            
        for x in range(leading_index,len(matrix[y])):
            matrix[y][x]=matrix[y][x]-matrix[y-1][x]
    else:
        break
                
    for x in range(i):
        matrix[x]=leading_one(matrix[x])
        
    for x in matrix:
        for y in range(len(x)):
            x[y]=round(x[y],5)

print(matrix)