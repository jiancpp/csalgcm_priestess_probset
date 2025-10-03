# PRIESTESS PROBLEM SET

This repository contains solutions for a given problem set in CSALGCM

## Table of Contents

- [POWAH! UNLIMITED POWAH!](#powah-unlimited-powah)
- [It's Like I Have ESPN Or Something](#its-like-i-have-espn-or-something)
- [Shattering the Towers of Algorythmos](#shattering-the-towers-of-algorythmos)
- [Let's Plant Rice](#lets-plant-rice)
- [Tbe Monkey's Paw](#the-monkeys-paw)
- [Laughter is The Best Medicine](#laughter-is-the-best-medicine)

---

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
```text
2 4
```

### Sample Output 0
```text
16
```

### Sample Input 1
```text
10 4
```

### Sample Output 1
```text
10000
```

---

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

```text
3 6 7
-10 10
-6 0
8 7
3
30
6
1
```


### Sample Output 0

```text
3
1
0
```


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

---

## Shattering the Towers of Algorythmos

The devious Telophoroi have now launched their master plan: they have placed towers throughout the land, launching signals into the minds of the unwitting citizens. These signals brainwash civilians, convincing them to worship the Algorythmos Empire unconditionally.

You have gathered the Scions of the School of Turing, a secret organization dedicated to maintaining order throughout the land, to infiltrate these towers and crumble them to dust, hopefully releasing their grip on the minds of the innocent people.

Once inside the core of one of the towers, the leader of the group of Scions infiltrating the specific tower unleashes several **area of effect attacks** on the $N$ pillars holding up the tower. Upon the destruction of these $N$ pillars, the tower crumbles, and that region is now free from the influence of the Algorythmos Empire.

Your party leader has $K$ attacks. The $i^{th}$ attack deals $D_i$ damage to all the $N$ pillars. The $j^{th}$ pillar crumbles if the $S_j$ value is reduced to 0 or less. After the $K^{th}$ attack, the party leader simply returns to their first attack. Essentially, they repeat all their attacks iteratively until the tower crumbles.

The scholar of your team, Krile Turing, is diagnosing the tower's integrity. If you get swarmed, and the tower is nowhere near crumbling, she would trigger an emergency retreat. Can you help her diagnose the integrity of the tower's supports throughout your operation?

### Input Format

Input begins with a line containing two space-separated integers $N$ and $K$, indicating the **number of pillars** holding up the tower and the **number of attacks** your team leader has.

$K$ lines follow, each containing a single integer $D_i$, the damage dealt to all the pillars by your party leader's $i^{th}$ attack.

$N$ lines follow, each containing a single integer $S_j$, indicating the **strength** of the $j^{th}$ pillar.

### Constraints

$$1 \leq N, K, D_i, S_j \leq 10^5 \text{, for all } 0 \leq i \leq K \text{ and } 0 \leq j \leq N$$

### Output Format

For each attack executed before the collapse of a tower, print a line containing a single integer indicating how many of the $N$ pillars are still standing. Once all pillars are destroyed, print **0** to indicate that no pillars are standing. This is the last line of the output.

### Sample Input 0

```text
5 1
8
3
7
11
5
39
```


### Sample Output 0

```text
2
1
1
1
0
```


### Sample Input 1

```text
6 1
23
21
56
51
51
56
92
```


### Sample Output 1

```text
5
5
1
0
```


### Sample Input 2

```text
7 1
54
60
55
57
367
42
57
19
```


### Sample Output 2

```text
5
1
1
1
1
1
0
```

---

## Let's Plant Rice

To simulate rice paddy maintenance, a game company decided to use the following function to calculate the evaporation rate of water:

$$\text{rate} = 1 - \left(\frac{1}{1 + e^{-k(x - 0.5)}}\right)^a + d$$

**Where:**

* $x$ - how full the rice paddy is at the start of the day, the value of which ranges from $0.0$ ($0\%$ water level) to $1.0$ ($100\%$ water level).
* $d$, $k$, and $a$ - variables that control the rate of evaporation.

When a rice paddy is filled with water, the evaporation rate is set for that day, and water would slowly evaporate following this rate.

Upon releasing the game, players discovered that if a **sweet spot evaporation rate $s$**, with an error margin of $0.1$ is used, the water level would be perfect every time and would result in the best quality crop. However, because players were not yet aware of factors $d$, $k$, and $a$, they were unable to figure out how to properly set their starting water level to exploit this sweet spot.

After data mining through the game, however, you managed to uncover factors $d$, $k$, and $a$, and you found out that these three factors were arbitrarily set at the start of each day. Moreover, there are indeed days where, no matter what you set your starting water level to, the sweet spot cannot be reached (darn those cheeky game developers!). Your task is to write a program that, given the values of $d$, $k$, and $a$, would determine the starting water level $x$ that would result in an evaporation rate of $s$ for that particular day. On days where $s$ cannot be reached, indicate that **"Sweet spot cannot be reached! Those cheeky developers!"** (without the quotation marks).

### Input Format

The first line of the input contains an integer $N$, indicating the number of days you would need to figure out the starting water level for.

$N$ lines follow, each containing four space-separated real numbers that correspond to the value of **$s$, $d$, $k$, and $a$**. $s$ is the sweet spot evaporation rate. $d$, $k$, and $a$ are described in the problem statement.

### Constraints

$$0 \leq N \leq 5 \cdot 10^3$$
$$0 \leq s \leq 1$$
$$-0.5 \leq d \leq 0.5$$
$$0 \leq a, k \leq 5$$

### Output Format

There will be $N$ lines of outputs, each line being the **lowest starting water level** that would get to within the acceptable margins for the sweet spot evaporation rate $s$. **Absolute or relative error must not exceed $10^{-6}$**. Print **"Sweet spot cannot be reached! Those cheeky developers!"** (without the quotation marks) if the sweet spot is impossible to be reached.

### Sample Input 0

```text
5
0.7119 -0.1206 2.9930 4.0577
0.9219 0.1963 2.7140 4.3201
0.2692 -0.0695 2.9132 1.6116
0.3601 -0.1771 0.6213 1.1870
0.3492 -0.3865 3.8889 2.5649
```


### Sample Output 0

```text
0.697784503037
0.887908531876
0.921929270250
0.645118392190
0.599166042326
```


### Explanation 0

On the first day, a starting water level of $0.6977845$, with $d = -0.1206$, $k = 2.9930$, and $a = 4.0577$ will result in an evaporation rate within $10^{-6}$ absolute error of $0.7119$. The same is true for the other days.

### Sample Input 1

```text
7
0.2772 0.2253 4.2550 1.9385
0.2807 -0.2682 1.5963 1.6372
0.9055 0.0522 2.5857 2.2600
0.3196 -0.2520 2.7628 0.9047
0.6853 -0.2366 3.6572 2.5567
0.7148 -0.1846 0.9737 4.1721
0.9411 -0.1370 2.0860 2.6794
```


### Sample Output 1

```text
Sweet spot cannot be reached! Those cheeky developers!
0.793247141838
0.387402764833
0.340837109300
0.353158012405
0.817511673620
Sweet spot cannot be reached! Those cheeky developers!
```


### Explanation 1

On the first day, it is impossible to reach an evaporation rate within $10^{-6}$ of $0.2772$ given $d=0.2253, k=4.2550$, and $a=1.9385$.

---

## The Monkey's Paw

Richie likes to watch movies at the local cineplex. His only complaint with the universe right now seems to be that there simply aren't enough hours in a day watch, like, $10^7$ movies in one day for example. That all changed the day Richie found the Monkey's Paw.

The Monkey's Paw spoke in a low voice and offered him three wishes. Richie wished for more wishes, wasting his first wish. With his second wish, he wished for the day to be long enough to show a lot of movies, which The Paw defined as $N$ movies. For his final wish, Richie wished to be able to stay awake to watch all of them, which The Paw granted.

The next day, Richie went to the cineplex. He had only $A$ pesos and ticket prices were $K$ pesos per ticket. To save time, Richie rips out a range of movies. He then keeps watching the **longest film** he hasn't seen yet, spending $K$ pesos per ticket, until his $A$ pesos are insufficient to buy another ticket. You can assume that The Monkey's Paw made it so that all the movies showing have not been watched by Richie before.

Richie proceeds to do this until he's out of money, only picking movies from the range he ripped out to save time.

Basically, given $N$ films each with their runtimes, you must answer $Q$ queries. For each query, please print the runtime of the last film Richie is able to see.

### Input Format

Input starts with a line containing a single integer $N$ denoting the **number of movies** showing in the theater.

$N$ lines follow, the $i^{th}$ of which contains two space-separated integers $R_i$ and $C_i$. $R_i$ is the **runtime** of the film. $C_i$ is the length of the **credits**. Richie always leaves before the credits, so you can subtract the credits from the runtime when computing for the answer.

This is followed by a line containing a single integer $Q$ denoting the **number of queries**.

$Q$ lines follow, each containing 4 space-separated integers $S$, $E$, $A$, and $K$. $S$ and $E$ denote the **start index** and **end index** of the movie range, respectively. Indices are 0-based. $A$ is Richie's **budget**. $K$ is the **cost of a single ticket**.

### Constraints

$$1 \leq N \leq 10^6$$
$$1 \leq C_i \leq R_i \leq 10^9$$
$$1 \leq Q \leq 4000$$
$$0 \leq S \leq E < N$$
$$0 \leq E - S < 10^4$$
$$1 \leq A, K \leq 10^9$$

### Output Format

For each query, output one line containing the length of the **last movie Richie watches, without the credits**. The length should be based on the strategy described in the problem statement. If Richie can't watch any movie, output **-1**.

### Sample Input 0
```text
8
148 116
157 100
169 15
188 98
91 68
165 70
145 2
11 6
3
2 6 52 12
2 6 13 7
0 4 2 3
```


### Sample Output 0

```text
90
154
-1
```

---

## Laughter is The Best Medicine

Let us define the **Laughter sequence** as a sequence of strings only containing either the character "H" or "A". This sequence is defined recursively as:

* $L_0 = H$
* $L_1 = A$
* $L_i = L_{i-2} \cdot L_{i-1}$, for $i > 1$

($S_1 \cdot S_2$ means concatenate $S_1$ and $S_2$). The first few strings in the Laughter sequence are $H, A, HA, AHA, HAAHA, A H A H A A H A$.

Given $i$ and $k$, determine whether the $k^{th}$ character in $L_i$ is an $H$ or an $A$.

### Input Format

Input consists of one test case. Each test case consists of one line with two space separated integers $i$ and $k$, denoting the **index of the string** in the Laughter sequence, and the **index of the character** to be checked. $k$ is a 0-based index.

### Constraints

$$0 \leq i \leq 10^5$$
$$0 \leq k < \min(10^{18}, |L_i|)$$

### Output Format

Output consists of one line containing "H" (without the quotes), if the $k^{th}$ character in $L_i$ is an $H$. Output "A" (also without quotes), if the $k^{th}$ character in $L_i$ is an $A$.

### Sample Input 0
```text
3 1
```

### Sample Output 0

```text
H
```


### Sample Input 1

```text
4 3
```

### Sample Output 1

```text
H
```

### Sample Input 2

```text
10 4
```


### Sample Output 2

```text
A
```

