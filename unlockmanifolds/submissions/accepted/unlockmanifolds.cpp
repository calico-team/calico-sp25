#include <iostream>
#include <vector>

using namespace std;

int solve(int N, int M, vector<vector<int>> &G) {
    vector<int> row(N * M + 1), col(N * M + 1);
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            row[G[i][j]] = j;
            col[G[i][j]] = i;
        }
    }
    
    int actions = 0;
    for (int i = 1; i <= N * M; i++) {
        // vertical move actions
        actions += min((row[i] - row[i - 1] + N) % N, (row[i - 1] - row[i] + N) % N);
        // horizontal move actions
        actions += min((col[i] - col[i - 1] + M) % M, (col[i - 1] - col[i] + M) % M);
        // note: % in C++ can return a negative value, so we need to add N or M to normalize it
        
        // click actions
        actions += 1;
    }
    
    return actions;
}

int main()
{
    int T;
    cin >> T;
    for (int i = 0; i < T; i++) {
        int N, M;
        cin >> N >> M;
        vector<vector<int>> G(N, vector<int>(M));
        for (int j = 0; j < N; j++) {
            for (int k = 0; k < M; k++) {
                cin >> G[j][k];
            }
        }
        cout << solve(N, M, G) << '\n';
    }
}
