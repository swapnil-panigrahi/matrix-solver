def leading_one(x):
    global zero_row
    
    for i in range(len(x)):
        if abs(x[i])>=0.000001:    
            y=i
            break
    else:
        return zero_row 
    
    leading_coeff=x[y]
    for i in range(len(x)):
        if abs(x[i])>=0.000001:
            x[i]=x[i]/leading_coeff
        else:
            x[i]=0
    return x

def non_zero(x):
    for i in range(len(x)):
        if x[i]!=0:    
            y=i
            break
    else:
        return 0  
    return y

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
zero_row=[0]*(j+1)

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
                
    for x in range(i):
        matrix[x]=leading_one(matrix[x])
        
    matrix.sort(reverse=True)

for row in range(-1,-len(matrix),-1):
    for next_row in range(row,0):                                            #Iterates from the given row to last row
        if matrix[next_row]!=zero_row:
            pivot_pos=matrix[next_row].index(1)
            multiplier=matrix[row-1][pivot_pos]
        
            if pivot_pos!=0:
                for y in range(pivot_pos,j+1):                              #Row subtraction
                    matrix[row-1][y]-=multiplier*matrix[next_row][y]
            else:
                continue
    
print("\nRow Reduced Echelon Form of the Augumented Matrix: ")
for x in matrix:
    for y in range(j):
        x[y]=round(x[y],3)        
    print(x)

free_var=[]
for x in range(len(matrix)-1):
    if matrix[x+1]==zero_row:
        free_var.extend(range(matrix[x].index(1)+2,j+1))
        break
    
    pivot_diff=matrix[x+1].index(1)-matrix[x].index(1)
    if pivot_diff>1:
        free_var.extend(range(matrix[x].index(1)+2,matrix[x+1].index(1)+1))
else:
    free_var.extend(range(matrix[x+1].index(1)+2,j+1))

if len(free_var)!=0:
    parametric=[]
    for x in matrix:
        
        vector=[]
        for y in free_var:
            vector.append(x[y-1])
            
        parametric.append(vector)

    to_print="x = "
    
    for x in range(len(free_var)):
        
        vector=[]
        for y in parametric:
            vector.append(-y[x])
        
        for z in free_var:
            if free_var[x]!=z:
                vector.insert(z-1,0)
        else:
            vector.insert(free_var[x]-1,1)
        
        vector.pop(-1)
            
        to_print+=str(vector)+"x"+str(free_var[x])+"+"

    print("\n"+to_print.rstrip("+"))
else:
    print("\nNo free variables thus, only trivial solutions exist")       