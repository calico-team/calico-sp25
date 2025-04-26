#include <iostream>
#include <vector>

using namespace std;

/**
 * Return the minimum number of actions
 *
 * N: a non-negative integer representing the number of rows
 * M: another non-negative integer representing the number of columns
 * S: A string representing a sequence of drift inputs
 * G: N x M array representing a grid
 */
int solve(int N, int M, string s, vector<vector<int>> &G) {
    // YOUR CODE HERE
    return -1;
}

int main()
{
    int T;
    cin >> T;
    for (int i = 0; i < T; i++) {
        int N, M;
        cin >> N >> M;
        string S;
        cin >> S;
        vector<vector<int>> G(N, vector<int>(M));
        for (int j = 0; j < N; j++) {
            for (int k = 0; k < M; k++) {
                cin >> G[j][k];
            }
        }
        cout << solve(N, M, S, G) << '\n';
    }
}