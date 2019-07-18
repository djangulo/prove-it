Proof: by induction

Let $P(n)$ be proposition that $\sum \limits_{i=1}^n i = \frac{n(n+1)}{2}$

Check base case $P(0)$

$P(0)=\sum \limits_{i=1}^0 i = \frac{(0)((0)+1)}{2} = 0$

Inductive step:

For $n\geq 0$, show $P(n)\implies P(n+1)$ is true.

Assume $P(n)$ is true for purposes of induction (i.e. assume $1+2+\ldots+n=\frac{n(n+1)}{2}$)

Need to show $1+2+\ldots+(n+1)=\frac{(n+1)(n+2)}{2}$

$1+2+\ldots + n + (n+1)$

$\frac{n(n+1)}{2}+n+1=\frac{n^2+3n+2}{2}=\frac{(n+1)(n+2)}{2}$

Therefore, $\forall n \geq 0; P(n) \implies P(n+1)$

### Theorem: For all natural numbers $n$, $3$ divides $n^3-n$. $\Big(\forall n \in \N (3 \mid (n^3-n))\Big)$

e.g. $n=5$; $3\mid (125-5)$

Proof by induction:

Let $P(n)$ be $3\mid (n^3-n)$

Base case: $P(0)$; $3\mid 0-0\qquad\checkmark$

Inductive step: For $n\geq 0$, show $P(n)\implies P(n+1)$ is true

Assume $P(n)$ is true, i.e. $3\mid (n^3-n)$

Show that $3\mid \Big[(n+1)^3-(n+1)\Big]$

$3\mid \Big[(n+1)^3-(n+1)\Big]=n^3+3n^2+3n+1-(n+1)$

$n^3+3n^2+2n$

$n^3 - n+3n^2+3n$

Then

$3\mid 3n^2$

$3\mid 3n$

$3\mid (n^3-n)$ (by the inductive hypothesis)

Therefore

$3\mid (n+1)^3 - (n+1)$ Q.E.D.

Base case: $P(b)$ is true (not $P(0)$)

Ind. step: $\forall n \geq b;\quad P(n)\implies P(n+1)$

Conclude $\forall n \geq b; \quad P(n)$

# False proof through induction

Theorem (not!) All horses are the same color.

Proof: by induction

$P(n)$, In any set of $n$ horses, $n\geq 1$, the horses are all the same color.

Base case: $n=1$, $P(1)$ is true, since it's just one horse.

Inductive step: Assume $P(n)$ is true, to show $P(n+1)$ is true.

Consider a set of $n+1$ horses, $h_1,h_2,\ldots ,h_{n+1}$

Then $h_1,h_2,\ldots ,h_n$ are all the same color

$h_2,h_3,\ldots ,h_{n+1}$ are all the same color

Since $color(h_1)=color(h_2,\ldots , h_n)=color(h_{n+1})$

$\implies$ all $n+1$ are the same color ($\implies P(n+1)$)

The universe of discourse will be the set $H$ of all horses. For any horse $h$, let $C_h$ be the color of that horse, and $S(C_{h_1}, C_{h_2})$ be "$h_1$ and $h_2$ have the same color", then:

$\forall h\in H\{\forall t \in H (S(h,t))\}$

# Courtyard problem

Theorem: $\forall n, \exist$ way to tile a $2^n\times 2^n$ region with a center square missing (for Bill's statue).

Proof: by induction

$P(n)$ theorem

Base case: $P(0)$, it's just one square, which is Bill's $\qquad \checkmark$

Inductive step: For $n\geq 0$, assume $P(n)$ to verify I.H.

Show $P(n+1)$ is true

Consider a $2^{n+1}\times2^{n+1}$
