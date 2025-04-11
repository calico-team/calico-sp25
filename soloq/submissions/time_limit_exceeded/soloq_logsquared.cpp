#include <bits/stdc++.h>
using namespace std;
 
using ll = long long;
using db = long double; // or double if tight TL
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
#define eb emplace_back

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
	return a < b ? a = b, 1 : 0;
} // set a = max(a,b)

/**
 * Description: modular arithmetic operations 
 * Source: 
	* KACTL
	* https://codeforces.com/blog/entry/63903
	* https://codeforces.com/contest/1261/submission/65632855 (tourist)
	* https://codeforces.com/contest/1264/submission/66344993 (ksun)
	* also see https://github.com/ecnerwala/cp-book/blob/master/src/modnum.hpp (ecnerwal)
 * Verification: 
	* https://open.kattis.com/problems/modulararithmetic
 */

template<int MOD, int RT> struct mint {
	static const int mod = MOD;
	static constexpr mint rt() { return RT; } // primitive root for FFT
	int v; explicit operator int() const { return v; } // explicit -> don't silently convert to int
	mint():v(0) {}
	mint(ll _v) { v = int((-MOD < _v && _v < MOD) ? _v : _v % MOD);
		if (v < 0) v += MOD; }
	bool operator==(const mint& o) const {
		return v == o.v; }
	friend bool operator!=(const mint& a, const mint& b) { 
		return !(a == b); }
	friend bool operator<(const mint& a, const mint& b) { 
		return a.v < b.v; }

	mint& operator+=(const mint& o) { 
		if ((v += o.v) >= MOD) v -= MOD; 
		return *this; }
	mint& operator-=(const mint& o) { 
		if ((v -= o.v) < 0) v += MOD; 
		return *this; }
	mint& operator*=(const mint& o) { 
		v = int((ll)v*o.v%MOD); return *this; }
	mint& operator/=(const mint& o) { return (*this) *= inv(o); }
	friend mint pow(mint a, ll p) {
		mint ans = 1; assert(p >= 0);
		for (; p; p /= 2, a *= a) if (p&1) ans *= a;
		return ans; }
	friend mint inv(const mint& a) { assert(a.v != 0); 
		return pow(a,MOD-2); }
		
	mint operator-() const { return mint(-v); }
	mint& operator++() { return *this += 1; }
	mint& operator--() { return *this -= 1; }
	friend mint operator+(mint a, const mint& b) { return a += b; }
	friend mint operator-(mint a, const mint& b) { return a -= b; }
	friend mint operator*(mint a, const mint& b) { return a *= b; }
	friend mint operator/(mint a, const mint& b) { return a /= b; }
};

template<int MOD, int RT> inline ostream& operator << (ostream& o, mint<MOD, RT> const& x) {
	return o << x.v;
}

using mi = mint<MOD,5>; // 5 is primitive root for both common mods
using vmi = V<mi>;
using pmi = pair<mi,mi>;
using vpmi = V<pmi>;

V<vmi> scmb; // small combinations
void genComb(int SZ) {
	scmb.assign(SZ,vmi(SZ)); scmb[0][0] = 1;
	FOR(i,1,SZ) F0R(j,i+1) 
		scmb[i][j] = scmb[i-1][j]+(j?scmb[i-1][j-1]:0);
}

/**
 * Description: 2D matrix operations.
 * Source: KACTL
 * Verification: https://dmoj.ca/problem/si17c1p5, SPOJ MIFF
 */

using T = mi;
using Mat = V<V<T>>; // use array instead if tight TL

Mat makeMat(int r, int c) { return Mat(r,V<T>(c)); }
Mat makeId(int n) { 
	Mat m = makeMat(n,n); F0R(i,n) m[i][i] = 1;
	return m;
}
Mat& operator+=(Mat& a, const Mat& b) {
	assert(sz(a) == sz(b) && sz(a[0]) == sz(b[0]));
	F0R(i,sz(a)) F0R(j,sz(a[0])) a[i][j] += b[i][j];
	return a;
}
Mat& operator-=(Mat& a, const Mat& b) {
	assert(sz(a) == sz(b) && sz(a[0]) == sz(b[0]));
	F0R(i,sz(a)) F0R(j,sz(a[0])) a[i][j] -= b[i][j];
	return a;
}
Mat operator+(Mat a, const Mat& b) { return a += b; }
Mat operator-(Mat a, const Mat& b) { return a -= b; }
V<T> operator*(const Mat& l, const V<T>& r) {
	assert(sz(l[0]) == sz(r));
	V<T> ret(sz(l));
	F0R(i,sz(l)) F0R(j,sz(l[0])) ret[i] += l[i][j]*r[j];
	return ret;
}
Mat operator*(const Mat& a, const Mat& b) {
	int x = sz(a), y = sz(a[0]), z = sz(b[0]); 
	assert(y == sz(b)); Mat c = makeMat(x,z);
	F0R(i,x) F0R(j,y) F0R(k,z) c[i][k] += a[i][j]*b[j][k];
	return c;
}
Mat& operator*=(Mat& a, const Mat& b) { return a = a*b; }
Mat pow(Mat m, ll p) {
	int n = sz(m); assert(n == sz(m[0]) && p >= 0);
	Mat res = makeId(n);
	for (; p; p /= 2, m *= m) if (p&1) res *= m;
	return res;
}
// Computes \sum_{i = 0}^{n}{A^i}
Mat geometricSum(Mat m, ll n) {
    if (n == 0) return makeId(sz(m));
    if (n & 1) return (makeId(sz(m)) + pow(m, n / 2 + 1)) * geometricSum(m, n / 2);
    else return pow(m, n) + geometricSum(m, n - 1);
}

/**
 * Description: Aho-Corasick for fixed alphabet. For each prefix, 
 	* stores link to max length suffix which is also a prefix.
	* solve() returns a list with all appearances of the words of v in s
 * Time: O(N\sum)
 * Source: https://vjudge.net/solution/47771157
	* https://codeforces.com/contest/710/problem/F
	* https://codeforces.com/contest/1207/problem/G
 * Verification:
 	* https://vjudge.net/problem/Kattis-stringmultimatching
	* https://vjudge.net/problem/CodeForces-963D
 */

template<size_t ASZ> struct ACfixed {
	struct Node { AR<int, ASZ> to; int link; vpi endsHere; bool end; int terminal; };
	V<Node> d{{}};
	vi bfs;
	ACfixed(vector<str> v) { // Initialize with patterns
		F0R(i, sz(v)) ins(v[i], i);
		pushLinks();
	}
	void ins(str& s, int i) {
		int v = 0;
		each(C,s) {
			// int c = C-A;
            int c = C == 'L';
			if (!d[v].to[c]) d[v].to[c] = sz(d), d.eb();
			v = d[v].to[c];
		}
		d[v].end = true;
		d[v].endsHere.eb(i, sz(s));
	}
	void pushLinks() {
		d[0].link = -1;
		queue<int> q; q.push(0);
		while (sz(q)) {
			int v = q.ft; q.pop(); bfs.pb(v);
			d[v].terminal = d[v].link == -1 ? 0 : d[d[v].link].end ? d[v].link : d[d[v].link].terminal;
			each(x, d[d[v].terminal].endsHere) d[v].endsHere.pb(x); 
			F0R(c,ASZ) {
				int u = d[v].to[c]; if (!u) continue;
				d[u].link = d[v].link == -1 ? 0 : d[d[v].link].to[c];
				q.push(u);
			}
			if (v) F0R(c,ASZ) if (!d[v].to[c])
				d[v].to[c] = d[d[v].link].to[c];
		}
	}
	V<vi> solve(str s, int n) {
		V<vi> ans(n);
		int cur = 0;
		F0R(i, sz(s)) {
			cur = d[cur].to[s[i] == 'L'];
			each(p, d[cur].endsHere) ans[p.f].pb(i - p.s + 1);
		}
		return ans;
	}
};


/**
 * Return the LP gain mod 10^9 + 7.
 * 
 * N: Number of games
 * K: Number of special streaks
 * X: LP won per win
 * Y: LP lost per loss
 * W1 / W2: Chance to win in the Winners Queue
 * L1 / L2: Chance to win in the Losers Queue
 * S: List containing the K special streaks
 */
int solve(long long N, int K, int X, int Y, int W1, int W2, int L1, int L2, vector<string>& S) {
    // Calculate probabilities
    mi w = mi(W1) / mi(W2);
    mi l = mi(L1) / mi(L2);
    // Generate graph using AhoCorasick
    ACfixed<2> AC(S);
    int n_states = sz(AC.d);
    V<vmi> A(2 * n_states, vmi(2 * n_states, 0));
    for (int i = 0; i < n_states; ++i) {
        int u = AC.d[i].to[0], v = AC.d[i].to[1];
        bool swap_u = sz(AC.d[u].endsHere) & 1;
        if (swap_u) {
            A[i][u + n_states] = w;
            A[i + n_states][u] = l;
        } else {
            A[i][u] = w;
            A[i + n_states][u + n_states] = l;
        }
        bool swap_v = sz(AC.d[v].endsHere) & 1;
        if (swap_v) {
            A[i][v + n_states] = 1 - w;
            A[i + n_states][v] = 1 - l;
        } else {
            A[i][v] = 1 - w;
            A[i + n_states][v + n_states] = 1 - l;
        }
    }
    // Compute mu
    V<vmi> mu(2 * n_states, vmi(1));
    F0R(i, n_states) {
        mu[i][0] = X * w - Y * (1 - w);
        mu[i + n_states][0] = X * l - Y * (1 - l);
    }

    // Compute d0
    V<vmi> d0(1, vmi(2 * n_states));
    d0[0][0] = 1;

    Mat ans = d0 * geometricSum(A, N - 1) * mu;

    return ans[0][0].v;

}


int main() {
    int T;
    cin >> T;
    for (int i = 0; i < T; i++) {
        long long N;
        int K, X, Y, W1, W2, L1, L2;
        cin >> N >> K;
        cin >> X >> Y >> W1 >> W2 >> L1 >> L2;
        vector<string> S(K);
        for (int j = 0; j < K; ++j) {
            cin >> S[j];
        }
        cout << solve(N, K, X, Y, W1, W2, L1, L2, S) << '\n';
    }
}
