#include <iostream>
#include <vector>
#include <cmath>
#include <set>
#include <map>
#include <algorithm>
using namespace std;
typedef pair <int, int> pii;
typedef long long ll;
#define pb push_back
#define mp make_pair
#define f first
#define s second

const int MOD = 1e9 + 7;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        int arr[n];
        for (int i = 0; i < n; i++) {
            cin >> arr[i];
        }
        // 2nd term is current state
        // 0: haven't entered paranthesis
        // 1: in paranthesis, was 0 before paranthesis
        // 2: in paranthesis, was 1 before paranthesis
        // 3: finished paranthesis
        ll dp[n][4][2];
        memset(dp, 0, sizeof(dp));
        dp[0][0][arr[0]] = 1;
        for (int i = 0; i < n - 1; i++) {
            if (arr[i + 1] == 1) {
                for (int j = 0; j < 4; j++) {
                    dp[i + 1][j][0] += dp[i][j][0] + dp[i][j][1];
                    dp[i + 1][j][1] += 2 * (dp[i][j][0] + dp[i][j][1]);
                }
                dp[i + 1][1][1] += dp[i][0][0];
                dp[i + 1][2][1] += dp[i][0][1];
            }
            else {
                for (int j = 0; j < 4; j++) {
                    dp[i + 1][j][0] += 3 * dp[i][j][0] + dp[i][j][1];
                    dp[i + 1][j][1] += 2 * dp[i][j][1];
                }
                dp[i + 1][1][0] += dp[i][0][0];
                dp[i + 1][2][0] += dp[i][0][1];
            }
            dp[i + 1][3][0] += 3 * dp[i + 1][1][0] + dp[i + 1][1][1] + dp[i + 1][2][0] + dp[i + 1][2][1];
            dp[i + 1][3][1] += 2 * dp[i + 1][1][1] + 2 * dp[i + 1][2][0] + 2 * dp[i + 1][2][1];
            for (int j = 0; j < 4; j++) {
                for (int k = 0; k < 2; k++) {
                    dp[i + 1][j][k] %= MOD;
                }
            }
        }
        ll num0 = 0, num1 = 0;
        num0 += dp[n - 1][3][0];
        num1 += dp[n - 1][3][1];
        num0 += n * dp[n - 1][0][0];
        num1 += n * dp[n - 1][0][1];
        num0 %= MOD;
        num1 %= MOD;
        cout << num1 << endl;
    }
}