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

ll solve(int n, string str) {
    int curw = -1, nxtw[n], sufo[n], sufu[n];
    sufo[n - 1] = sufu[n - 1] = 0;
    for (int i = n - 1; i >= 0; i--) {
        if (i != n - 1) {
            sufo[i] = sufo[i + 1];
            sufu[i] = sufu[i + 1];
        }
        if (str[i] == 'w') curw = i;
        if (str[i] == 'o') sufo[i]++;
        if (str[i] == 'u') sufu[i]++;
        nxtw[i] = curw;
    }
    ll ans = 0;
    for (int i = 0; i < n; i++) {
        if (str[i] == 'o') {
            if (nxtw[i] != -1) ans += sufo[nxtw[i]];
        }
        if (str[i] == 'u') {
            if (nxtw[i] != -1) ans += sufu[nxtw[i]];
        }
    }
    return ans;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int t;
    cin >> t;
    while (t--) {
        int n;
        string str;
        cin >> n >> str;
        cout << solve(n, str) << endl;
    }
}