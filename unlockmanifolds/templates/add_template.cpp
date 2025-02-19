#include <iostream>

using namespace std;

/**
 * Return the sum of A and B.
 *
 * A: a non-negative integer
 * B: another non-negative integer
 */
int solve(int N, int M, int G[][])
{
    // YOUR CODE HERE
    return "";
}

int main()
{
    int T;
    cin >> T;
    for (int i = 0; i < T; i++)
    {
        int N, BM;
        cin >> N >> BM;
        int G[N][M];

        for (int j = 0; j < N; j++)
        {
            for (int k = 0; k < M; k++)
            {
                cin >> G[j][k];
            }
        }
        cout << solve(N, M, G) << '\n';
    }
}
