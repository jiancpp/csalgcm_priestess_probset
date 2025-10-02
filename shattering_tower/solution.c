#include <bits/stdc++.h>

#define MAX_N 100000

using namespace std;

int n, k, d_i[MAX_N], s_i[MAX_N];
int answers[MAX_N]; // SAVE ANSWERS HERE
int answer_line_count; // SAVE NUMBER OF ANSWERS TO PRINT HERE

int damagePillar(int damage, int low, int high);

/*
Takes in the key input values and saves all answers in the 'answers' array. 
Save the number of answers to print in the 'answer_line_count' variable.
*/
void solve() {
    // TODO
    answer_line_count = 0;
    int standing_towers = n;

    while (standing_towers > 0) {
        // damage pillar by d_i and iterate over k
        standing_towers = damagePillar(d_i[answer_line_count % k], 0, n - 1);
        
        // save answers
        answers[answer_line_count] = standing_towers;
        answer_line_count++;
    }
    return;
}

int damagePillar(int damage, int low, int high) {
    int mid = low + (high - low) / 2; // divide and conquer

    if (high <= low) {
        s_i[mid] -= damage;
        return s_i[mid] > 0;
    }
    
    // Count towers with health more than 0
    return damagePillar(damage, low, mid) + damagePillar(damage, mid + 1, high);    
}

/**
    0 1 2 3 4 // d(d, 0, 2)  and d (3, 4)
    0 1 2   3 4 // d(d, 0, 1) d(d, 2, 2)    and   d(d, 3, 3) d(d, 4, 4)
    0 1  2  3  4 // d
    0  1  2  3  4
**/

int main() {
    scanf("%d%d",&n,&k);
    for(int i = 0; i < k; i++){
        scanf("%d",&d_i[i]);
    }
    for(int i = 0; i < n; i++) {
        scanf("%d",&s_i[i]);
    }

    solve();

    for(int i = 0; i < answer_line_count; i++) {
        printf("%d\n",answers[i]);
    }
}