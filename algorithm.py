# sub = input("Enter your sequence or fasta file.")
#
# if sub == *.fasta:
#     parser(sub)
# else:
#     sub = seq

#create valid sequence from .fasta
def parser(x):
    pass
    return(seq)


#testsequence
seq = "ACUGUUACCGUAAGC"

m = len(seq)

minloop = 4 #minimal loop lenght
def init(m):
    matrix = list(list(0 for x in range(m)) for x in range(m))
    return(matrix)


def show(matrix, m):
    for i in range(m):
        for j in range(m):
            print("{:4d}".format(matrix[i][j]), end='')
        print()


#initialise matrix

matrix = init(m)


#fill matrix

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

#scoring


for n in range(2,m):
    for j in range(n,m):
        i = j -n
        matrix[i][j] = max(matrix[i][j-1],              #unpaired
                           matrix[i+1][j],              #unpaired
                           matrix[i+1][j-1] + pairs[seq[i],seq[j]],     #paired
                           max(
                               [(matrix[i][k] + matrix[k+1][j] * pairs[seq[k],seq[j]]) for x in i <= k < (j-1)]     #bifurkation
                           )
        )








show(matrix, m)