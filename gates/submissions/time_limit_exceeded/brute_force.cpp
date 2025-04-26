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

int calc(int a, int op, int b) {
    if (op == 0) return a & b;
    else if (op == 1) return a | b;
    else return a ^ b;
}

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
        int pw[n];
        pw[0] = 1;
        for (int i = 1; i < n; i++) {
            pw[i] = pw[i - 1] * 3;
        }
        int ans = 0, op[n - 1];
        for (int i = 0; i < pw[n - 1]; i++) {
            int x = i;
            for (int j = n - 2; j >= 0; j--) {
                op[j] = x / pw[j];
                x %= pw[j];
            }
            for (int p1 = 0; p1 <= n - 1; p1++) {
                for (int p2 = p1; p2 <= n - 1; p2++) {
                    int vp = arr[p1];
                    for (int k = p1; k + 1 <= p2; k++) {
                        vp = calc(vp, op[k], arr[k + 1]);
                    }
                    int v;
                    if (p1 != 0) {
                        v = arr[0];
                        for (int k = 0; k + 1 < p1; k++) {
                            v = calc(v, op[k], arr[k + 1]);
                        }
                        v = calc(v, op[p1 - 1], vp);
                    }
                    else v = vp;
                    for (int k = p2; k + 1 <= n - 1; k++) {
                        v = calc(v, op[k], arr[k + 1]);
                    }
                    if (v) ans++;
                    ans = ans % MOD;
                }
            }
        }
        cout << ans << endl;
    }
}