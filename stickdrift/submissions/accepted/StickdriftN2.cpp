#include <bits/stdc++.h>
using namespace std;


int main() {
    int tc; cin >> tc;
    while (tc--) {
        int n, m;
        cin >> n >> m;
        string s;
        cin >> s;
        map<int, pair<int, int>> d;
        for (int i = 0; i < n; ++i)
            for (int j = 0; j < m; ++j) {
                int x; cin >> x;
                d[x] = {i,j};
            }
        int curx = 0, cury = 0;

        long long ans = 0;
        int idx = 0;

        for (auto& z : d) {
            auto [x, y] = z.second;
            #define dist() (min(abs(curx-x), min(abs(curx-x-n),abs(curx-x+n))) + min(abs(cury-y),min(abs(cury-y-m), abs(cury-y+m))))
            int aux = 0;
            while (dist() > aux) {
                if (s[idx] == 'U') curx = (curx + n - 1) % n;
                else if (s[idx] == 'D') curx = (curx + 1) % n;
                else if (s[idx] == 'L') cury = (cury + m - 1) % m;
                else if (s[idx] == 'R') cury = (cury + 1) % m;
                idx = (idx + 1) % int(size(s));
                ++aux;
            }
            ans += aux;
            curx = x;
            cury = y;
        }
        cout << ans << '\n';
    }
    return 0;
}