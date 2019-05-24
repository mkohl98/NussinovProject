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

def traceback(matrix,m):
    dotbracket = ['.' for x in range(m)]
    trace = [(0,m-1)]
    while trace is not []:
        if i >= j:
            pass
        elif matrix[i+1][j] == matrix[i][j]:
            trace.append(matrix[i+1][j])
        elif matrix[i][j-1] == matrix[i][j]:
            trace.append(matrix[i][j])
        elif (matrix[i+1][j-1] + pairs[seq[i],pairs[j]]) == matrix[i][j]:
            trace.append(matrix[i+1][j-1])
            dotbracket[i] = '('
            dotbracket[j] = ')'
        else:
            for k in range(i+1,j-1):
                if (matrix[i][k] + matrix[k+1][j]) == matrix[i][j]:
                    trace.append(matrix[k+1][j])
                    trace.append(matrix[i][k])
                else:
                    break
    return(dotbracket)





def calculateenergy():
    pass





matrix = init(m)
score = fill(matrix,m,pairs)
show(matrix, m)

print(score[0][m-1])

traceback(matrix,m)
print(dotbracket)