**\*1.** (a) Factor $2^{15}-1=32,767$ into a product of two smaller positive integers.

$$n = 15\qquad  a, b = 3, 5 $$

Let
$$x=2^b-1 = 2^{5}-1 = 32 - 1 = 31$$
and
$$y = 1 + 2^b + 2^{2b} +\ldots +2^{(a-1)b} = 1 + 2^5 + 2^{10} = 1057$$

$$ xy = 32,767 = 2^n - 1$$

(b) Find an integer $x$ such that $1 < x < 2^{32767} − 1$ and $2^{32767} − 1$ is divisible by $x$.

$n=15$ is not prime, therefore $2^n-1=32,767$ is not prime; therefore $2^{32,767} -1$ will not be prime either. $x$ exists!

$$xy = z = 2^n-1 = 2^{32,767} - 1$$

We take factors $a=1057$ and $b=31$ from part (a), then

$$x = 2^b - 1 = 2^{31} - 1 = 2,147,483,647 $$

**2.** Make some conjectures about the values of $n$ for which $3^n − 1$ is prime or the values of $n$ for which $3^n − 2^n$ is prime. (You might start by making a table similar to Figure 1.)

| n   | Is n prime           | $3^n - 1$ | Is $3^n - 1$ prime          | $3^n - 2^n$ | Is $3^n - 2^n$ prime        |
| --- | -------------------- | --------- | --------------------------- | ----------- | --------------------------- |
| 2   | yes                  | 8         | no: $8= 2 \times 4$         | 5           | yes                         |
| 3   | yes                  | 26        | no: $26= 2 \times 13$       | 19          | yes                         |
| 4   | no: $4= 2 \times 2$  | 80        | no: $80= 2 \times 40$       | 65          | no: $65= 5 \times 13$       |
| 5   | yes                  | 242       | no: $242= 2 \times 121$     | 211         | yes                         |
| 6   | no: $6= 2 \times 3$  | 728       | no: $728= 2 \times 364$     | 665         | no: $665= 5 \times 133$     |
| 7   | yes                  | 2186      | no: $2186= 2 \times 1093$   | 2059        | no: $2059= 29 \times 71$    |
| 8   | no: $8= 2 \times 4$  | 6560      | no: $6560= 2 \times 3280$   | 6305        | no: $6305= 5 \times 1261$   |
| 9   | no: $9= 3 \times 3$  | 19682     | no: $19682= 2 \times 9841$  | 19171       | no: $19171= 19 \times 1009$ |
| 10  | no: $10= 2 \times 5$ | 59048     | no: $59048= 2 \times 29524$ | 58025       | no: $58025= 5 \times 11605$ |

**Conjecture 1.** _Suppose $n$ is an integer larger than 1. Then $3^n -1$ will not be prime._

**\*3.** The proof of Theorem 3 gives a method for finding a prime number different
from any in a given list of prime numbers.

(a) Use this method to find a prime different from 2, 3, 5, and 7.

Let
$$m = p_1p_2\ldots p_n+1=2\times3\times5\times7 + 1 = 211$$

$m>1$, therefore $m=211$ is either prime or a product of primes

$m=211$ is in fact, prime, as its not divisible by any number preceding it.

(b) Use this method to find a prime different from 2, 5, and 11.

$$m = p_1p_2\ldots p_n+1=2\times5\times11+ 1 = 111$$

$m>1$, but $m=111$ is not prime, since $111/3=37$, here $q=3$ which is prime and is not in the original list.

**4.** Find five consecutive integers that are not prime.

Poorly optimized algorithm with $O(n^2)$ growth.

```python
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
```

```python
>>> find_5_non_primes(0,100)
 91 92 93 94 95
```

**5.** Use the table in Figure 1 and the discussion on p. 5 to find two more perfect
numbers.

Using Euclid's proof: If $2^n - 1$ is prime, then $2^{n-1}(2^n-1)$ is perfect.

Excluding $6=2^1(2^2-1)$ and $28=2^2(2^3-1)$ which are already given.

Inserting $n$ for the next primes 5 and 7 leaves us with

$$2^4(2^5-1)=496\qquad and \qquad 2^6(2^7-1)=8128$$
