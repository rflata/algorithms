import itertools as it

perms = list(it.product('ABCDE','ABCDE'))
perms = sorted(perms)
for k in perms:
    print(''.join(k))


