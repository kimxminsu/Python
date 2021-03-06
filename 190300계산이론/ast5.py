# -----------------------------------------------------------------------------
# Evaluator of Abstract Syntax Trees
# Sequence of statements with  ";"
# -----------------------------------------------------------------------------


#######################  Test Code  #############################
ast1 = ('+', ('N', 10), ('N', 20))  # 10 + 20

# x = 10 + 20
ast2 = ('=', 'x',
        ('+', ('N', 10), ('N', 20))
        )

# x = 10 + 20 ; x + x
ast3 = (';', ('=', 'x', ('+', ('N', 10), ('N', 20))),
        ('+', ('NAME', 'x'), ('NAME', 'x'))
        )
#################################################################

# x * x + x
ast5 = ('+',
        ('NAME', 'x'),
        ('*', ('NAME', 'x'), ('NAME', 'x')))

ast = ast5

print(ast)

# dictionary of names
names = {'x' : 10}


def eval(tree):
    if not tree:          return 0  # tree == None
    opr = tree[0]
    if opr == '+':
        return eval(tree[1]) + eval(tree[2])
    elif opr == '-':
        return eval(tree[1]) - eval(tree[2])
    elif opr == '*':
        return eval(tree[1]) * eval(tree[2])
    elif opr == '/':
        return eval(tree[1]) / eval(tree[2])
    elif opr == 'UMINUS':
        return - eval(tree[1])
    elif opr == 'N':
        return tree[1]
    elif opr == 'NAME':
        return names[tree[1]]
    elif opr == ';':
        eval(tree[1]); return eval(tree[2])
    elif opr == '=':
        names[tree[1]] = eval(tree[2])
    else:
        print("unexpeced case : ", tree)


print(eval(ast))
