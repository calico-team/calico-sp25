#include <iostream>
#include <vector>
using namespace std;

long long int MOD = 1000000007;

/**
 * Return the sum of A and B.
 * 
 * A: a non-negative integer
 * B: another non-negative integer
 */
int solve(int N, int K, int W1, int W2, int L1, int L2, vector<string>& S) {
    // YOUR CODE HERE
    return -1;
}

int main() {
    int T;
    cin >> T;
    for (int i = 0; i < T; i++) {
        int N, K, W1, W2, L1, L2;
        cin >> N >> K >> W1 >> W2 >> L1 >> L2;
        vector<string> S(K);
        for (int j = 0; j < K; ++j) {
            cin >> S[j];
        }
        cout << solve(N, K, W1, W2, L1, L2, S) << '\n';
    }
}
