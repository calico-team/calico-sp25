#include <iostream>
#include <vector>
using namespace std;

long long int MOD = 1000000007;

/**
 * Return the LP gain mode 10^9 + 7.
 * 
 * N: Number of games
 * K: Number of special streaks
 * X: LP won per win
 * Y: LP lost per loss
 * W1 / W2: Chance to win in the Winners Queue
 * L1 / L2: Chance to win in the Losers Queue
 * S: List containing the K special streaks
 */
int solve(long long N, int K, int X, int Y, int W1, int W2, int L1, int L2, vector<string>& S) {
    // YOUR CODE HERE
    return -1;
}

int main() {
    int T;
    cin >> T;
    for (int i = 0; i < T; i++) {
        long long N;
        int K, X, Y, W1, W2, L1, L2;
        cin >> N >> K;
        cin >> X >> Y >> W1 >> W2 >> L1 >> L2;
        vector<string> S(K);
        for (int j = 0; j < K; ++j) {
            cin >> S[j];
        }
        cout << solve(N, K, X, Y, W1, W2, L1, L2, S) << '\n';
    }
}
