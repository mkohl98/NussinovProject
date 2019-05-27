# submission = input("Enter your sequence.")


#testsequence

seq = "ACGAGGAAUCGUA"


m = len(seq)

minloop = 2                #minimal loop lenght



# initialise matrix

def init(m):
    matrix = list(list(0 for x in range(m)) for x in range(m))
    return(matrix)


#show matrix

def show(matrix, m):
    for i in range(m):
        for j in range(m):
            print("{:4d}".format(matrix[i][j]), end='')
        print()


#scoring matrix

pairs = {
    ('A', 'A'): 0,
    ('U', 'U'): 0,
    ('G', 'G'): 0,
    ('C', 'C'): 0,
    ('A', 'U'): 1,
    ('U', 'A'): 1,
    ('G', 'C'): 1,
    ('C', 'G'): 1,
    ('A', 'C'): 0,
    ('C', 'A'): 0,
    ('A', 'G'): 0,
    ('G', 'A'): 0,
    ('U', 'C'): 0,
    ('C', 'U'): 0,
    ('U', 'G'): 0,
    ('G', 'U'): 0,
}


#filling

def fill(matrix,m,pairs):
    for n in range(2,m):
        for j in range(n,m):
            i = j -n
            matrix[i][j] = max(matrix[i][j-1],              #unpaired
                               matrix[i+1][j],              #unpaired
                               matrix[i+1][j-1] + pairs[seq[i],seq[j]],     #paired
                               max(
                                   [(matrix[i][k] + matrix[k+1][j] * pairs[seq[k],seq[j]]) for k in range(i,j)]     #bifurkation
                               )
            )
    return(matrix)


#traceback


dotbracket = ['.' for x in range(m)]   #creating dotbracket annotation


def traceback(i,j):
    if i < j:
        if matrix[i][j] == matrix[i+1][j]:                  #unpaired
            print("1")
            return traceback(i+1,j)
        elif matrix[i][j] == matrix[i][j-1]:  #unpaired
            print("2")
            return traceback(i,j-1)
        elif matrix[i][j] == (matrix[i + 1][j - 1] + pairs[seq[i], seq[j]]):  # paired
            print("3")
            dotbracket[i] = '('
            dotbracket[j] = ')'
            return traceback(i + 1, j - 1)
        else:                                               #bifurkation
            print("4")
            for k in range(i+1,j-1):
                if matrix[i][j] == matrix[i][k] + matrix[k+1][j]:
                    return traceback(i,k), traceback(k+1,j)
    return dotbracket



def calculateenergy(dotbracket):
    pass


print("start")

matrix = init(m)
score = fill(matrix,m,pairs)
show(matrix, m)

print(score[0][m-1])

traceback(0,m-1)
print(dotbracket)

print("end")