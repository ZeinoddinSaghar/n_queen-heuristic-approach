import random

Row = int(input("Enter the number of rows:"))
Column = Row

# Initialize matrix
matrix = []
#print("Enter the entries rowwise:")

# For user input
for i in range(Row):  # A for loop for row entries
    a = []
    for j in range(Column):  # A for loop for column entries
        a.append(int(0))
    matrix.append(a)

for i in range(Row):
    rand = random.randint(0, Row-1)
    matrix[i][rand]= 1

threat = []
for i in range(Row):
    threat.append(0)

#For printing the matrix
print("board before change:")
for i in range(Row):
    for j in range(Column):
        print(matrix[i][j], end=" ")
    print()

#threat function

def threat_queen ():

    for i in range (Row):

         for j in range (Row):
                 matrix[i][j] = 0

         for j in range(Row):

                 for i_prime in range (Row):
                     if matrix[i_prime][j]== 1:
                         threat[j]= threat[j]+1

                 for i_prime in range (Row):
                     for j_prime in range(Row):
                         if abs(i-i_prime) == abs(j-j_prime):
                             if matrix[i_prime][j_prime]==1:
                                 threat[j] = threat[j]+1

         minimum = min(threat)

         for j in range (Row):
            if threat[j] == minimum:
                matrix[i][j] = 1
                break

         for i in range(Row):
             threat[i] = 0




threat_queen()

print("board after change: ")
for i in range(Row):
    for j in range(Row):
        print(matrix[i][j] , end = " ")
    print()