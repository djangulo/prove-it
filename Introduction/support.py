import math

def test_primality_dumb(n):
    for i in range(2,n+1):
        if n!= i and n % i == 0:
            return 'no: $%s= %.0f \\times %.0f$' % (n,i, n/i)
        if n == i:
            return 'yes'



for  i in range(2, 11):
    print("| %(n).0f | %(yn)s | %(n2).0f | %(yn2)s | %(n3).0f | %(yn3)s |" % {
        "n": i,
        "yn": test_primality_dumb(i),
        "n2": math.pow(3, i) - 1,
        "yn2": test_primality_dumb(int(math.pow(3, i) - 1)),
        "n3": math.pow(3, i) - math.pow(2, i),
        "yn3": test_primality_dumb(int(math.pow(3, i) - math.pow(2, i))),
    })

def test_primality(n):
    if n == 1 or n == 2:
        return True
    for i in range(2,n+1):
        if n!= i and n % i == 0:
            return False
        if n == i:
            return True

def find_5_non_primes(start, n):
    ans = ''
    for i in range(start,n,2):
        if test_primality(i):
            continue
        for j in range(1,6):
            if test_primality(i+j):
                ans = ''
                break
            # passed the prime-test wall
            ans += ' ' + str(i+j)
        if len(ans.split(' ')) >= 5:
            print(ans)
            return
    print('no such sequence found in 1 through %s' % n)

def perfect_num(n):
    return math.pow(2,n-1) * (math.pow(2,n)-1)
