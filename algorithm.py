import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--sequence", required=True, type=str, help="Enter your RNA sequence here!")
# parser.add_argument("--output_dir", required=True, help="Where to put output files")

a = parser.parse_args()

seq = a.sequence




seqlist = [x for x in seq]

m = len(seq)

minloop = 2                # minimal loop length


# initialise matrix

def init(m):
    matrix = list(list(0 for x in range(m)) for x in range(m))
    return (matrix)


# show matrix

def show(matrix, m):
    for i in range(m):
        for j in range(m):
            print("{:4d}".format(matrix[i][j]), end='')
        print()


# scoring matrix

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


# filling

def fill(matrix, m, pairs):
    for n in range(2, m):
        for j in range(n, m):
            i = j -n
            matrix[i][j] = max(matrix[i][j-1],              # unpaired
                               matrix[i+1][j],              # unpaired
                               matrix[i+1][j-1] + pairs[seq[i], seq[j]],     # paired
                               max(
                                   [(matrix[i][k] + matrix[k+1][j] * pairs[seq[k], seq[j]]) for k in range(i, j)]     # bifurkation
                               )
            )
    return(matrix)


# traceback


dotbracket = ['.' for x in range(m)]   # creating dotbracket annotation


def traceback(i, j):
    if i + minloop < j:            # opportunity to set minimal loop length by adding this to 'i'
        if matrix[i][j] == matrix[i+1][j]:                  # unpaired
            return traceback(i+1, j)
        elif matrix[i][j] == matrix[i][j-1]:  # unpaired
            return traceback(i, j-1)
        elif matrix[i][j] == (matrix[i + 1][j - 1] + pairs[seq[i], seq[j]]):  # paired
            dotbracket[i] = '('
            dotbracket[j] = ')'
            return traceback(i + 1, j - 1)
        else:                                               # bifurkation
            for k in range(i+1, j-1):
                if matrix[i][j] == matrix[i][k] + matrix[k+1][j]:
                    return traceback(i, k), traceback(k+1, j)
    return dotbracket


# calculate binding energy of the structure

def calculateenergy(dotbracket):
    AU = 0
    GC = 0
    x = 0
    Energy_AU = -1.9
    Energy_GC = -2.9
    for charackter in dotbracket:
        if charackter == '(':
            y = dotbracket.index(charackter, x)
            if seqlist[y] == 'A' or 'U':
                AU = AU + 1
            else:
                GC = GC + 1
            x = dotbracket.index(charackter, x ) + 1
        else:
             pass
    Energy = (AU*Energy_AU)+(GC*Energy_GC)
    print("The binding energy of this structure is about", Energy, "kcal/mol.")
    return Energy


matrix = init(m)
score = fill(matrix, m, pairs)
show(matrix, m)

traceback(0, m-1)
dotbracketstring = ''.join(str(i) for i in dotbracket)

print("Dot-Bracket-Annotation:", dotbracketstring)
calculateenergy(dotbracket)
