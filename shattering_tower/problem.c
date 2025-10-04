#include <bits/stdc++.h>

#define MAX_N 100000

using namespace std;

int n, k, d_i[MAX_N], s_i[MAX_N];
int answers[MAX_N]; // SAVE ANSWERS HERE
int answer_line_count; // SAVE NUMBER OF ANSWERS TO PRINT HERE

/*
Takes in the key input values and saves all answers in the 'answers' array. 
Save the number of answers to print in the 'answer_line_count' variable.
*/
void solve() {
    // TODO

    return;
}

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