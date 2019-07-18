6.042/18.062J Mathematics for Computer Science

Tom Leighton and Marten van Dijk

# Problem Set 1.

## Problem 1. [24points]

Translate the following sentences from English to predicate logic. The domain that you are working over is $X$,the set of people. You may use the functions $S(x)$, meaning that "$x$ has been a student of 6.042", $A(x)$, meaning that "$x$ has gotten an 'A' in 6.042", $T(x)$, meaning that "$x$ is a TA of 6.042", and $E(x,y)$, meaning that "$x$ and $y$ are the same person".

- (a) [6pts] There are people who have taken 6.042 and have gotten A's in 6.042

  $\exist x \Big(S(x)\land A(x)\Big)$

- (b) [6pts] All people who are 6.042 TA's and have taken 6.042 got A's in 6.042

  $\forall x\Big(T(x) \land S(x)\implies A(x)\Big)$

- (c) [6pts] There are no people who are 6.042 TA's who did not get A's in 6.042.

  $\neg\exist x\Big(S(x) \implies T(x)\land \neg A(x)\Big)$

- (d) [6pts] There are at least three people who are TA's in 6.042 and have not taken 6.042.

  $\exist x \exist y \exist z\Big(\neg E(x,y) \land \neg E(x, z) \land \neg E(y,z) \land \neg A(x)\land \neg A(y) \land \neg A(z)\Big)$

  But we can do better!

  For all people $x \in X$, let $A_x$ represent the set of all people who have taken 6.042, and $T_x$ represent the set of all people who are TA's of 6.042, then

  $\cup_{x \in X}(T_x \setminus A_x)$

  will be the set of all people who are TA's of 6.042, but have not taken 6.042 themselves.

  Rewriting it in long form:

  $\cup_{x \in X}(T_x \setminus A_x)=\{x \mid x \in X(t\in T_x \setminus A_x)\}=\Bigg\{\exist x \in X\Big(T(x) \land \neg A(x)\Big)\Bigg\}$

## Problem2. [24points]

Use a truth table to prove or disprove the following statements:

- (a) [12pts]

$$\neg\Big(P\lor(Q\land R)\Big)=(\neg P)\land(\neg Q \lor \neg R)$$

| $P$ | $Q$ | $R$ | $\neg\Big(P\lor(Q\land R)\Big)$ | $(\neg P)\land(\neg Q \lor \neg R)$ |
| :-: | :-: | :-: | :-----------------------------: | :---------------------------------: |
|  F  |  F  |  F  |                T                |                  T                  |
|  F  |  F  |  T  |                T                |                  T                  |
|  F  |  T  |  F  |                T                |                  T                  |
|  F  |  T  |  T  |                F                |                  F                  |
|  T  |  F  |  F  |                F                |                  F                  |
|  T  |  F  |  T  |                F                |                  F                  |
|  T  |  T  |  F  |                F                |                  F                  |
|  T  |  T  |  T  |                F                |                  F                  |

They're equivalence is also stated by DeMorgan's law, which when applied to the term on the left becomes the term on the right.

$$\neg(P\lor Q)\equiv \neg P \land \neg Q$$

$$\neg(P\land Q)\equiv \neg P \lor \neg Q$$

- (b) [12pts]

  $$\neg\Big(P\land (Q\lor R)\Big)=\neg P \lor (\neg Q \lor \neg R)$$

| $P$ | $Q$ | $R$ | $\neg\Big(P\land (Q\lor R)\Big)$ | $\neg P \lor (\neg Q \lor \neg R)$ |
| :-: | :-: | :-: | :------------------------------: | :--------------------------------: |
|  F  |  F  |  F  |                T                 |                 T                  |
|  F  |  F  |  T  |                T                 |                 T                  |
|  F  |  T  |  F  |                T                 |                 T                  |
|  F  |  T  |  T  |                T                 |                 T                  |
|  T  |  F  |  F  |                T                 |                 T                  |
|  T  |  F  |  T  |                F                 |                 T                  |
|  T  |  T  |  F  |                F                 |                 T                  |
|  T  |  T  |  T  |                F                 |                 F                  |

Rows 6 and 7 disprove the expression the falsehood.

## Problem3. [24points]

The binary logical connectives $\land$ (and), $\lor$ (or), and $\implies$ (implies) appear often in not only computer programs, but also everyday speech. In computer chip designs, however, it is considerably easier to construct these out of another operation, _nand_, which is simpler to represent in a circuit. Here is the truth table for nand:

|  $P$  |  $Q$  | $P\text{ nand } Q$ |
| :---: | :---: | :----------------: |
| true  | true  |       false        |
| true  | false |        true        |
| false | true  |        true        |
| false | false |        true        |

- (a) [12 pts] For each of the following expressions, find an equivalent expression using only $nand$ and $\neg$ (not), as well as grouping parentheses to specify the order in which the operations apply. You may use $A$, $B$, and the operators any number of times.

  - (i) $A\land B$
    | $P$ | $Q$ | $P\text{ nand } Q$ | $P\land Q$ |
    | :---: | :---: | :----------------: | :--------: |
    | true | true | false | true |
    | true | false | true | false |
    | false | true | true | false |
    | false | false | true | false |

    By extending the truth table for $nand$ with $P\land Q$, it's easy to see that it's the opposite of $\land$ (and). The hint even lies in the name, as $nand$ is an abbreviation for $\mathbf{n}ot\text{ }\mathbf{and}$. Therefore

    $$P\text{ nand } Q\equiv \neg(P\land Q)$$

    Then $A\land B\equiv \neg(A\text{ nand }B)$

  - (ii) $A \lor B$

    $\lor$ (or) is trickier, but we can make use of DeMorgan's law to convert the $\lor$ to a $\land$ with equivalent truth value, then it's a simple matter of negating the $\land$ expression.

    $A\lor B \equiv \neg(\neg A \land \neg B)$

    By using the equivalence found in (i), and negating both sides

    $\neg(A\land B)\equiv \neg\neg(A\text{ nand }B)$

    $\neg(A\land B)\equiv A\text{ nand }B$

    Then

    $\neg(\neg A \land \neg B) \equiv \neg A \text{ nand }\neg B$

    We confirm it via the truth table

    |  $A$  |  $B$  | $A\lor B$ | $\neg A\text{ nand } \neg B$ |
    | :---: | :---: | :-------: | :--------------------------: |
    | true  | true  |   true    |             true             |
    | true  | false |   true    |             true             |
    | false | true  |   true    |             true             |
    | false | false |   false   |            false             |

  - (iii) $A \implies B$

    $A \implies B \equiv \neg A \lor B$ (Conditinal law)

    $\neg A \lor B\equiv \neg(\neg A)\text{ nand } \neg B$

    $A \implies B \equiv A \text{ nand } \neg B$

    Confirm via truth table

    |  $A$  |  $B$  | $A\implies B$ | $A \text{ nand } \neg B$ |
    | :---: | :---: | :-----------: | :----------------------: |
    | true  | true  |     true      |           true           |
    | true  | false |     false     |          false           |
    | false | true  |     true      |           true           |
    | false | false |     true      |           true           |

- (b) [4pts] It is actually possible to express each of the above using only $nand$, without needing to use $\neg$. Find an equivalent expression for $(\neg A)$ using only $nand$ and grouping parentheses.

  |  $A$  | $\neg A$ | $A \text{ nand } A$ |
  | :---: | :------: | :-----------------: |
  | true  |  false   |        false        |
  | false |   true   |        true         |

  - (i) $A\land B\equiv \neg(A\text{ nand }B)\equiv (A\text{ nand }B) \text{ nand }(A\text{ nand }B)$
  - (ii) $A\lor B\equiv \neg A \text{ nand }\neg B\equiv (A \text{ nand } A) \text{ nand } (B \text{ nand } B)$
  - (iii) $A\implies B \equiv A \text{ nand } \neg B \equiv A \text{ nand } (B \text{ nand } B)$

- (c) [8pts] The constants $true$ and $false$ themselves may be expressed using only $nand$. Construct an expression using an arbitrary statement $A$ and $nand$ that evaluates to $true$ re­gardless of whether $A$ is $true$ or $false$. Construct a second expression that always evaluates to false. Do not use the constants $true$ and $false$ themselves in your statements.

  |  $A$  | $A \text{ nand } A$ | $A\text{ nand } (A\text{ nand } A)$ | $\Big[A\text{ nand } (A\text{ nand } A)\Big]\text{ nand }\Big[A\text{ nand } (A\text{ nand } A)\Big]$ |
  | :---: | :-----------------: | :---------------------------------: | :---------------------------------------------------------------------------------------------------: |
  | true  |        false        |                true                 |                                                 false                                                 |
  | false |        true         |                true                 |                                                 false                                                 |

## Problem 4. [10 points]

You have $12$ coins and a balance scale, one of which is fake. All the real coins weigh the same, but the fake coin weighs less than the rest. All the coins visually appear the same, and the difference in weight is imperceptible to your senses. In at most 3 weighings, give a strategy that detects the fake coin. (Note: the scale in this problem is a scale with two dishes, which tips toward the side that is heavier. For clarification, do an image search for "balance scale")

Let $C$ be our set of coins, let's denote a subset of coins as $S^m_n$ where $n$ denotes the number of coins, and $m$ denotes an identifier

1. First, divide the set $C$ into two subsets: $S^a_8$ and $S^b_4$
2. Divide the subset $S^a_8$ into two more equal subsets
3. Weigh $S^{a1}_4$ and $S^{a2}_4$ (1st weigh used up)
   1. If they weigh the same, then the fake coin is in $S^b_4$
      1. Divide $S^b_4$ into two equal subsets $S^{b1}_2$ and $S^{b2}_2$
      2. Weigh $S^{b1}_2$ and $S^{b2}_2$, and let $S^c_2$ be the lighter one (2nd weigh)
      3. Divide $S^c_2$ into two equal subsets $S^{c1}_1$ and $S^{c2}_1$
      4. Weigh $S^{c1}_1$ and $S^{c2}_1$, (3rd weigh), then the fake coin is the lightest of the two
   2. If they have different weights, let $S^c_4$ be the lighter one
      1. Divide $S^c_4$ into two equal subsets $S^{c1}_2$ and $S^{c2}_2$
      2. Weigh $S^{c1}_2$ and $S^{c2}_2$, and let $S^d_2$ be the lighter one (2nd weigh)
      3. Divide $S^d_2$ into two equal subsets $S^{d1}_1$ and $S^{d2}_1$
      4. Weigh $S^{d1}_1$ and $S^{d2}_1$, (3rd weigh), then the fake coin is the lightest of the two

## Problem 5. [6 points]

Prove the following statement by proving its contrapositive: if $r$ is irrational, then $r^{1/5}$ is irrational. (Be sure to state the contrapositive explicitly.)

The original statement has the form $\neg R(x)\implies \neg R(x^{1/5})$, where $R(x)$ means "$x$ is a rational number"

We prove the contrapositive:

$R(x^{1/5}) \implies R(x)$

Suppose $R(x^{1/5})$, that is, $x^{1/5}=\sqrt[5]{x}$ is rational. Then, there exists integers $a$ and $b$ such that

$\sqrt[5]{x}=\frac{a}{b}$

elevating to the power of $5$ both sides, we have

$x=\frac{a^5}{b^5}$

Since $a^5$ and $b^5$ are integers, $x$ is rational. $\square$

## Problem 6. [12 points]

Suppose that $w^2+x^2+y^2=z^2$, where $w$, $x$, $y$, and $z$ always denote positive integers. (Hint: It may be helpful to represent even integers as $2i$ and odd integers as $2j+1$, where $i$ and $j$ are integers).

Prove the proposition: $z$ is even if and only if $w$, $x$, and $y$ are even. Do this by considering all the cases of $w$, $x$, $y$ being odd or even.

Predicate $P(x,y,w,z)$

$E(w) \land E(x) \land E(y) \iff E(z)$, where $E(x)$ means "$x$ is even"

Can also be written as

$\Bigg(E(w) \land E(x) \land E(y) \implies E(z)\Bigg)\land \Bigg(E(z) \implies E(w) \land E(x) \land E(y)\Bigg)$, where $E(x)$ means "$x$ is even"

We prove that $E(w) \land E(x) \land E(y)$ implies $E(z)$ and vice-versa.

Suppose $w$, $x$ and $y$ are even, then, for some integer $i\in \Z$, $w=2i$, $x=2i$, and $y=2i$, then

$(2i)^2+(2i)^2+(2i)^2=4i^2+4i^2+4i^2=2(6i^2)$, since $6i^2$ is an integer, $w^2+x^2+y^2$ are even. Thus, if $w$, $x$ and $y$ are even, then $z$ is even.

Suppose $z$, is even, then for some integer $i\in \Z$, $z=2i$, then

$z^2=(2i)^2=4i^2=2(2i^2)$, since $2i^2$ is an integer, $z^2$ is is even. Thus, if $z$, is even, then $w$, $x$ and $y$ are even.
