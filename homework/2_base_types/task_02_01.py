from math import gcd


def task_solution(first, second):
    n1, d1 = map(int, first.split('/'))
    n2, d2 = map(int, second.split('/'))

    if d1 == d2:
        return '{}/{}'.format(n1+n2, d1)
    else:
        cd = int(d1*d2/gcd(d1, d2))
        rn = int(cd/d1*n1+cd/d2*n2)
        g2 = gcd(rn, cd)
        n = int(rn/g2)
        d = int(cd/g2)
    return '{}/{}'.format(n, d) if n != d else n


first = '1/2'
second = '2/3'

print(task_solution(first, second))
