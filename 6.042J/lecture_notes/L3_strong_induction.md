# Lecture 3: Strong Induction

## Good proofs are:

- correct
- complete
- clear
- brief
- "elegant" (nice to have) - crisp, clever, short, to the point
- well organized (use lemmas)
- in order

---

## Invariant<a name="invariant"></a>

In order to show that your system can never reach a particular state, it is sufficient to show that some property, called the _invariant_, that holds at the initial state, and it's preserved by every legal move, and it does not hold in that special state.

---

## Word puzzle<a name="word-puzzle"></a>

Legal move: slide a letter into adjacent blank square

Thm: There is no sequence of legal moves to invert $G$ & $H$ and return all other letters to their original position.

|     |     |     |
| :-: | :-: | :-: |
|  A  |  B  |  C  |
|  D  |  E  |  F  |
|  H  |  G  |     |

What happens during a move?

**Row move**

|     |     |     |                   |     |     |     |
| :-: | :-: | :-: | ----------------- | :-: | :-: | :-: |
|  A  |  B  |  C  |                   |  A  |  B  |  C  |
|  D  |  G  |     | $\longrightarrow$ |  D  |     |  G  |
|  E  |  F  |  H  |                   |  E  |  F  |  H  |

Natural order:

|     |     |     |
| :-: | :-: | :-: |
|  1  |  2  |  3  |
|  4  |  5  |  6  |
|  7  |  8  |  9  |

**Lemma 1**: A row move does not change the order of the items.

**Proof**: In a row move, we move an item from some cell $i$ into an adjacent cell $i-1$ or $i+1$, nothing else moves. Hence, the order of the items is preserved.

**Column move**

|     |     |     |                   |     |     |     |
| :-: | :-: | :-: | ----------------- | :-: | :-: | :-: |
|  A  |  B  |  C  |                   |  A  |  B  |  C  |
|  D  |  F  |     | $\longrightarrow$ |  D  |  F  |  G  |
|  H  |  E  |  G  |                   |  H  |  E  |     |

<br>

|     |     |     |                   |     |     |     |
| :-: | :-: | :-: | ----------------- | :-: | :-: | :-: |
|  A  |  B  |  C  |                   |  A  |     |  C  |
|  D  |     |  G  | $\longrightarrow$ |  D  |  B  |  G  |
|  H  |  E  |  F  |                   |  H  |  E  |  F  |

**Lemma 2**:

A column move changes the relative order of precisely 2 pairs of items.

**Proof**: In a column move, we move an item in cell $i$ to a blank spot in cell $i-3$ or $i + 3$. When an item moves 3 positions, it changes relative order with 2 other items ($i-1$, $i-2$, or $i+1$, $i+2$)

**Def**. A pair of letters $L_1$ & $L_2$ is an inversion (a.k.a. an _inverted pair_) if $L_1$ precedes $L_2$ in alphabet, but $L_1$ is after $L_2$ in the puzzle.

**Lemma 3** During a move, the # of inversions can only increase by 2, decrease by 2, or stay the same.

**Proof**:

Row move: no changes (by **Lemma 1**)

Column move: 2 pairs change order (**Lemma 2**)

- a. both pairs were in order $\longrightarrow$ # of inversions $\uparrow2$
- b. both pairs were inverted $\longrightarrow$ # of inversions $\downarrow2$
- c. one pair is inverted, the other is not $\longrightarrow$ # of inversions stays the same

**Corollary 1**: During a move, the parity (even/odd) of the number of inversions, does not change.

**Proof**: adding or substracting 2, does not change the parity. $\square$

**Lemma 4**: In every state reachable from the start state

|     |     |     |
| :-: | :-: | :-: |
|  A  |  B  |  C  |
|  D  |  E  |  F  |
|  H  |  G  |     |

The parity of the # of inversions, is odd

**Proof**: by induction (Invariant proofs are always by induction)

$P(n)$: After any sequence of $n$ moves from the start state, the parity of the number of inversions is odd.

**Base case**: $n=0$. # of inversions is 1, therefore parity is odd $\checkmark$

**Inductive step**: For $n\geq 0$, show $P(n)\implies P(n+1)$

Consider any sequence of $n+1$ moves, $m_1, m_2, \ldots, m_{n+1}$

By I.H. (or by $P(n)$), we know that the parity after moves $m_1, \ldots, m_n$ is odd.

By Corollary 1, we know that the parity of the # of inversions does not change during $m_{n+1}$, this implies that the parity after $m_1,m_2,\ldots,m_n,m_{n+1}$ is odd, $\implies P(n+1)$

**Proof of Theorem**: The parity of the number of inversions, in desired state is even ($0$). By **Lemma 4**, the desired state cannot be reached from the start state, using legal moves.

---

## Strong induction axiom<a name="strong-induction"></a>

Let $P(n)$ be any predicate. If $P(0)$ is true and $\forall n \Big(P(0) \land P(1) \land \ldots \land P(n)\Big)\implies P(n+1)$ is true, then $\forall n P(n)$ is true.

---

## Unstacking game<a name="unstacking-game"></a>

**Theorem**: All strategies for the $n$-block game, produce the same score $S(n)$.

Ex. $S(8)=28$

Proof by strong induction

**Predicate:** All strategies $P(n)$ for the $n$-block game, produce the same score.

**Base case**: $n=1\qquad S(1)=0$

**Inductive step**: Assume $P(1)$, $P(2)$, $\ldots$, $P(n)$ to prove $P(n+1)$

Look at $n+1$ blocks, $1 \leq k \leq n$

$\qquad \qquad n+1$

$\qquad \quad$/$\qquad\qquad$\

$\qquad k\qquad \qquad n+1-k$

$\text{score}_{S(n+1)}=k(n+1-k) + P(k) + P(n+1-k)$

**Stronger predicate**: All strategies for the $n$-block game, produce the same score $S(n)=\frac{n(n-1)}{2}$.

Then

$\text{score}_{S(n+1)}=k(n+1-k) + \frac{k(k-1)}{2} + \frac{(n+1-k)(n-k)}{2}$

$=\frac{2kn + 2k - 2k^2 + k^2 - k + (n+1)n -kn -k -kn + k^2}{2}=\frac{(n+1)n}{2}=S(n+1)$
