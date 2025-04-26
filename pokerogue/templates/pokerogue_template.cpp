#include <iostream>
#include <vector>
#include <iomanip>

using namespace std;

/**
 * Return the best score you can achieve in the Daily Run.
 * 
 * N: number of stages
 * K: number of turns each lure lasts
 * A: list containing the health points of the first Pokemon in each stage
 * B: list containing the turns it takes to beat each stage if it were a singles battle
 * C: list containing the health points of the additional Pokemon in each stage
 * D: list containing the turns it takes to beat each stage if it were a doubles battle
 */
double solve(int N, int K, vector<int> A, vector<int> B, vector<int> C, vector<int> D) {
    // YOUR CODE HERE
    return 0.0;
}

int main() {
    int T;
    cin >> T;
    for (int i = 0; i < T; i++) {
        int N, K;
        cin >> N >> K;
        vector<int> A(N), B(N), C(N), D(N);
        for (int& a : A) cin >> a;
        for (int& b : B) cin >> b;
        for (int& c : C) cin >> c;
        for (int& d : D) cin >> d;
        cout << fixed << setprecision(5) << solve(N, K, A, B, C, D) << '\n';
    }
}
