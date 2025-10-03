# PRIESTESS PROBLEM SET

This repository contains solutions for a given problem set in CSALGCM

## Table of Contents

- [POWAH! UNLIMITED POWAH!](#powah-unlimited-powah)
- [It's Like I Have ESPN Or Something](#its-like-i-have-espn-or-something)

## POWAH! UNLIMITED POWAH! 

Emperor Palpatine has the vicious ability to shoot force lightning out of his fingers. The way this works is actually quite predictable through some mathematical computation. Depending on how much Palpatine has exerted himself that day, he has a certain amount of energy $E$ stored. Once he starts shooting lightning, the power $P$ of his lightning is equal to $1$. After each millisecond, $P$ increases by a factor of $E$, that is to say, we multiply $P$ by $E$ to get the new $P$.

Given Palpatine's initial energy $E$ and the number of milliseconds $T$ he has been shooting lightning out of his fingers, compute the power $P$ of his lightning. Since this may be very large, output $P$ modulo $10^7$.

### Input Format

Input consists of a single test case containing a line with two integers $E$ and $T$ separated by a space indicating the energy and the time elapsed in milliseconds.

### Constraints

$$1 \leq E \leq 10^{12}$$
$$0 \leq T \leq 10^{12}$$

### Output Format

Output consists of one line containing Palpatine's power $P$ after $T$ milliseconds modulo $10^7$.


### Sample Input 0
`2 4`

### Sample Output 0
`16`

### Sample Input 1
`10 4`

### Sample Output 1
`10000`

## It's Like I Have ESPN Or Something

Karen Smith is one of those gifted teens with the power of ESPN. For us normal people, this skill is also known as telepathy. She can read the minds of people around her, which helps her out because she loves gossip. She frequently just sits in crowded areas around North Shore High School and uses her ESPN to read the minds of the people around her. After picking up gossip, she goes to her friends Cady, Regina, and Gretchen to tell them all these "fetch" stories.

The range of her ESPN is limited. Before she starts collecting gossip, she must prepare a certain amount of ESPN energy $E$ before starting to read people's minds. If she accumulates $E$ energy, she can read the minds of the people who are at most $E$ units away from her.

Distance between two points $(x_1, y_1)$ and $(x_2, y_2)$ is defined as the **Manhattan distance**:
$$D = |x_1 - x_2| + |y_1 - y_2|$$

Karen goes to the cafeteria to start collecting gossip. She positions herself at the coordinates $(K_x, K_y)$ and prepares $E$ energy. Given the positions of the $N$ people in the cafeteria, how many people can Karen collect gossip from?

### Input Format

Input consists of one test case beginning with three space-separated integers $N$, $K_x$, and $K_y$, which are the number of people in the cafeteria, and Karen's location respectively.

$N$ lines follow, the $i^{th}$ of which containing two space-separated integers $X_i$ and $Y_i$ denoting the coordinates of the $i^{th}$ person.

The next line contains a single integer $Q$. You must answer $Q$ queries.

The next $Q$ lines contain an integer $E$, which is the energy of Karen for that query.

### Constraints

$$0 \leq N \leq 10^5$$
$$0 \leq |K_x|, |K_y|, |X_i|, |Y_i| \leq 10^8$$
$$0 \leq E \leq 4 \cdot 10^8$$
$$1 \leq Q \leq 10^5$$

### Output Format

For each query, output one line containing a single integer which denotes the number of people within range of Karen's ESPN.

### Sample Input 0

3 6 7
-10 10
-6 0
8 7
3
30
6
1


### Sample Output 0

3
1
0


### Explanation 0

The distances of the 3 people from Karen at $(6, 7)$ are calculated as follows:

| Person Location $(X_i, Y_i)$ | Manhattan Distance ($D$) from $(6, 7)$ |
| :--- | :--- |
| $(-10, 10)$ | $|-10 - 6| + |10 - 7| = 16 + 3 = 19$ |
| $(-6, 0)$ | $|-6 - 6| + |0 - 7| = 12 + 7 = 19$ |
| $(8, 7)$ | $|8 - 6| + |7 - 7| = 2 + 0 = 2$ |

The distances of the 3 people are **19, 19, and 2**.

* With $E = 30$: Karen can reach people with distance $\leq 30$. This includes all 3 people. **Output: 3**
* With $E = 6$: Karen can reach people with distance $\leq 6$. This only includes the person 2 units away. **Output: 1**
* With $E = 1$: Karen can reach people with distance $\leq 1$. This includes none of the people. **Output: 0**
