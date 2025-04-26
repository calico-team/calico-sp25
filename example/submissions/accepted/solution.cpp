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

const int maxn = 1010, maxl = 10010;

int n, m;
pii arr[maxn * maxn];
int len = 0;
int prex[maxl], prey[maxl];

bool check(int v, int cx, int cy, int nx, int ny, int cm) {
    int ov = v;
    if (cm + v >= len) {
        cx += prex[len] - prex[cm];
        cx += prey[len] - prey[cm];
        v -= (len - cm);
        cm = 0;
        int d = v / len;
        cx += d * prex[len];
        cy += d * prey[len];
        v %= len;
        cx = ((cx % n) + n) % n;
        cy = ((cy % m) + m) % m;
    }
    cx += prex[cm + v] - prex[cm];
    cy += prey[cm + v] - prey[cm];
    int dx = abs(cx - nx), dy = abs(cy - ny);
    dx = min(dx, n - dx);
    dy = min(dy, m - dy);
    return dx + dy <= ov;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int t;
    cin >> t;
    while (t--) {
        cin >> n >> m;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                int x;
                cin >> x;
                arr[x - 1] = mp(i, j);
            }
        }
        string str;
        cin >> str;
        len = str.length();
        prex[0] = prey[0] = 0;
        for (int i = 0; i < len; i++) {
            prex[i + 1] = prex[i];
            prey[i + 1] = prey[i];
            if (str[i] == 'U') prey[i + 1]--;
            else if (str[i] == 'D') prey[i + 1]++;
            else if (str[i] == 'L') prex[i + 1]--;
            else if (str[i] == 'R') prex[i + 1]++;
        }
        int cx = 0, cy = 0, cm = 0;
        ll ans = 0;
        for (int i = 0; i < n * m; i++) {
            int nx = arr[i].f, ny = arr[i].s;
            int l = -1, r = n * m;
            while (l + 1 < r) {
                int mid = (l + r) >> 1;
                if (check(mid, cx, cy, nx, ny, cm)) r = mid;
                else l = mid;
                ans += r;
                cm = (cm + r) % len;
            }
        }
        cout << ans << endl;
    }
}