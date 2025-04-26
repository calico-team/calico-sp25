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

ll solve(string str) {
    int n = str.length();
    int curw = -1, nxtw[n], suf[n];
    suf[n - 1] = 0;
    for (int i = n - 1; i >= 0; i--) {
        if (i != n - 1) {
            suf[i] = suf[i + 1];
        }
        if (str[i] == 'w') curw = i;
        if (str[i] == 'u') suf[i]++;
        nxtw[i] = curw;
    }
    ll ans = 0;
    for (int i = 0; i < n; i++) {
        if (str[i] == 'u') {
            if (nxtw[i] != -1) ans += suf[nxtw[i]];
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
        string str;
        cin >> str;
        cout << solve(str) << endl;
    }
}