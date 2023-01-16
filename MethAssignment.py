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
        if abs(x[i])>=0.000001:
            x[i]=x[i]/leading_coeff
        else:
            x[i]=0
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
    
for x in range(i):
        matrix[x]=leading_one(matrix[x])

matrix.sort(reverse=True)
    
while check_echelon(matrix)==False:
    
    y=row_to_reduce(matrix)
    if y!=0:
        leading_index=matrix[y].index(1)
            
        for x in range(leading_index,len(matrix[y])):
            matrix[y][x]=matrix[y][x]-matrix[y-1][x]
    else:
        break
    
    # for x in matrix:
    #     for y in range(len(x)):
    #         x[y]=round(x[y],2)
                
    for x in range(i):
        matrix[x]=leading_one(matrix[x])
        
    matrix.sort(reverse=True)
    
for i in matrix:
    print(i)