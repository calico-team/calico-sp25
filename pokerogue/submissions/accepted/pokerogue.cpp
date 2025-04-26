#include <bits/stdc++.h>
using namespace std;
 
using ll = long long;
using db = double; // or double if tight TL
using str = string;

using pi = pair<int,int>;
#define mp make_pair
#define f first
#define s second

#define tcT template<class T
tcT> using V = vector<T>; 
tcT, size_t SZ> using AR = array<T,SZ>;
using vi = V<int>;
using vb = V<bool>;
using vpi = V<pi>;

#define sz(x) int((x).size())
#define all(x) begin(x), end(x)
#define sor(x) sort(all(x))
#define rsz resize
#define pb push_back
#define ft front()
#define bk back()

#define FOR(i,a,b) for (int i = (a); i < (b); ++i)
#define F0R(i,a) FOR(i,0,a)
#define ROF(i,a,b) for (int i = (b)-1; i >= (a); --i)
#define R0F(i,a) ROF(i,0,a)
#define rep(a) F0R(_,a)
#define each(a,x) for (auto& a: x)

const int MOD = 1e9+7;
const db PI = acos((db)-1);
mt19937 rng(0); // or mt19937_64

tcT> bool ckmin(T& a, const T& b) {
	return b < a ? a = b, 1 : 0; } // set a = min(a,b)
tcT> bool ckmax(T& a, const T& b) {
	return a < b ? a = b, 1 : 0; } // set a = max(a,b)

/**
 * Description: Segment Tree with lazy updates. Segments are [l,r)
 * Source: Nyaan's Library
 * Verification:
    * https://vjudge.net/problem/Yosupo-range_affine_range_sum
 * Time: O(\log N) per query
 */

template<typename T, typename E, T (*f)(T, T), T (*g)(T, E), E (*h)(E, E), T(*ti)(), E (*ei)()>
struct LazySegTree {
    int n, log, s;
    V<T> val; V<E> laz;
    LazySegTree() {}
    LazySegTree(V<T> const& v) { init(v); }
    void init(V<T> const& v) {
        n = 1, log = 0, s = sz(v);
        while (n < s) n <<= 1, ++log;
        val.rsz(2 * n, ti());
        laz.rsz(n, ei());
        F0R(i, s) val[i+n] = v[i];
        ROF(i,1,n) _update(i);
    }
    void update(int l, int r, E const& x) {
        if (l >= r) return; // [l, r)
        l += n, r += n;
        ROF(i,1,log+1) {
            if (((l>>i)<<i) != l) _push(l>>i);
            if (((r>>i)<<i) != r) _push((r-1)>>i);
        }
        int l2 = l, r2 = r;
        while (l < r) {
            if (l & 1) _apply(l++,x);
            if (r & 1) _apply(--r,x);
            l >>= 1, r >>= 1;
        }
        l = l2, r = r2;
        FOR(i,1,log+1) {
            if (((l>>i)<<i) != l) _update(l>>i);
            if (((r>>i)<<i) != r) _update((r-1)>>i);
        }
    }
    T query(int l, int r) {
        if (l >= r) return ti(); // [l,r)
        l += n, r +=n;
        T L = ti(), R = ti();
        ROF(i,1,log+1) {
            if (((l>>i)<<i) != l) _push(l>>i);
            if (((r>>i)<<i) != r) _push((r-1)>>i);
        }
        while (l < r) {
            if (l & 1) L = f(L,val[l++]);
            if (r & 1) R = f(val[--r], R);
            l >>= 1, r >>= 1;
        }
        return f(L, R);
    }
    void set_val(int k, T const& x) {
        k += n;
        ROF(i,1,log+1)
            if (((k>>i)<<i) != k or (((k+1)>>i)<<i) != (k+1))
                _push(k>>i);
        val[k] = x;
        FOR(i,1,log+1)
            if (((k>>i)<<i) != k or (((k+1)>>i)<<i) != (k+1))
                _update(k>>i);
    }
private:
    void _push(int i) {
        if (laz[i] != ei()) {
            F0R(j,2) val[2*i+j] = g(val[2*i+j],laz[i]);
            if (2*i<n) F0R(j,2) compose(laz[2*i+j], laz[i]);
        }
        laz[i] = ei();
    }
    inline void _update(int i) { val[i] = f(val[2*i],val[2*i+1]); }
    inline void _apply(int i, E const& x) {
        if (x != ei()) {
            val[i] = g(val[i], x);
            if (i < n) compose(laz[i], x);
        }
    }
    inline void compose(E& a, E const& b) { a = a == ei() ? b : h(a, b); }
};

using T = db;
using E = db;
T f(T a, T b) { return max(a, b); }
T g(T a, E b) { return a + b; }
E h(E a, E b) { return a + b; }
T ti() { return -1e12; }
E ei() { return 0; }

using SegTree = LazySegTree<T, E, f, g, h, ti, ei>;

using vd = vector<db>;


db solve(int N, int K, vector<int> A, vector<int> B, vector<int> C, vector<int> D) {
    vd a(N), b(N), c(N), d(N);
    for (int i = 0; i < N; ++i) {
        a[i] = A[i];
        b[i] = B[i];
        c[i] = C[i];
        d[i] = D[i];
    }
    db l = 0, r = 2e6;
    while (r - l > 1e-6) {
        db x = (r + l) / db(2);
        // Check if it's possible that ans >= x
        vd v(N + 1);
        SegTree st(v);
        vd dp(N + 1);
        for (int i = N - 1; i >= 0; --i) {
            dp[i] = a[i] - x * b[i] + max(dp[i + 1], st.query(min(N, i + K + 1), N + 1));
            st.update(i, i + 1, dp[i]);
            st.update(i + 1, N + 1, a[i] + c[i] - x * d[i]);
        }
        // Possible iff dp[0] >= x
        if (dp[0] >= 0) l = x;
        else r = x;
    }
    return l;
}

int main() {
    int T;
    cin >> T;
    for (int i = 0; i < T; i++) {
        int N, K;
        cin >> N >> K;
        vector<int> A(N), B(N), C(N), D(N);
        for (int& a : A) cin >> a;
        for (int& b : B) cin >> b;
        for (int& c : C) cin >> c;
        for (int& d : D) cin >> d;
        cout << fixed << setprecision(7) << solve(N, K, A, B, C, D) << '\n';
    }
}