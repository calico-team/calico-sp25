#include <bits/stdc++.h>
using namespace std;

const int MOD = 1000000007;

using ll = long long;

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

using mi = mint<MOD, 5>;

using Mat = vector<vector<mi>>;

Mat makeMat(int r, int c) { return Mat(r, vector<mi>(c)); }
Mat makeId(int n) {
    Mat m = makeMat(n, n);
    for (int i = 0; i < n; ++i)
        m[i][i] = 1;
    return m;
}
Mat& operator+=(Mat& a, Mat const& b) {
    assert(size(a) == size(b) && size(a[0]) == size(b[0]));
    for (int i = 0; i < size(a); ++i)
        for (int j = 0; j < size(a[0]); ++j)
            a[i][j] += b[i][j];
    return a;
}
Mat operator+(Mat a, Mat const& b) { return a += b; }

Mat operator*(Mat const& a, Mat const& b) {
    int x = size(a), y = size(a[0]), z = size(b[0]);
    assert(y == size(b));
    Mat c = makeMat(x, z);
    for (int i = 0; i < x; ++i)
        for (int j = 0; j < y; ++j)
            for (int k = 0; k < z; ++k)
                c[i][k] += a[i][j] * b[j][k];
    return c;
}
Mat& operator*=(Mat& a, Mat const& b) { return a = a * b; }
Mat pow(Mat m, long long p) {
    int n = size(m);
    assert(n == size(m[0]) && p >= 0);
    Mat res = makeId(n);
    for (; p; p /= 2, m *= m) if (p & 1) res *= m;
    return res;
}
Mat geometricSum(Mat const& m, long long n) {
    if (n == 0) return makeId(size(m));
    // case 2k
    if (n % 2 == 0) return pow(m, n) + geometricSum(m, n - 1);
    // case 2k - 1 with n / 2 = k - 1 
    return (makeId(size(m)) + pow(m, n / 2)) * geometricSum(m, n / 2);
}

struct AhoCorasick {
    struct Node {
        int link;
        vector<int> to = {0,0};
        int ends_here = 0;
        bool end;
        int terminal;
    };
    vector<Node> d{{}};
    void insert(string const& s, int i) {
        int v = 0;
        for (char C : s) {
            int c = C == 'L';
            if (!d[v].to[c]) {
                d[v].to[c] = int(size(d));
                d.emplace_back();
            }
            v = d[v].to[c];
        }
        d[v].end = true;
        d[v].ends_here = 1;
    }

    void push_links() {
        d[0].link = -1;
        queue<int> q;
        q.push(0);
        while (!q.empty()) {
            int v = q.front(); q.pop();
            d[v].terminal = d[v].link == -1 ? 0 : d[d[v].link].end ? d[v].link : d[d[v].link].terminal;
            d[v].ends_here += d[d[v].terminal].ends_here;
            for (int c = 0; c < 2; ++c) {
                int u = d[v].to[c];
                if (!u) continue;
                d[u].link = d[v].link == -1 ? 0 : d[d[v].link].to[c];
                q.push(u);
            }
            if (v) {
                for (int c = 0; c < 2; ++c) {
                    if (!d[v].to[c]) {
                        d[v].to[c] = d[d[v].link].to[c];
                    }
                }
            }
        }
    }

};


/**
 * Return the sum of A and B.
 * 
 * A: a non-negative integer
 * B: another non-negative integer
 */
int solve(int N, int K, int X, int Y, int W1, int W2, int L1, int L2, vector<string>& S) {
    // Transform chances to Fp
    mi W = mi(W1) / mi(W2);
    mi L = mi(L1) / mi(L2);

    // Build graph
    AhoCorasick AC;
    for (int i = 0; i < K; ++i) {
        AC.insert(S[i],i);
    }
    AC.push_links();
    int n = size(AC.d);

    // Build transition matrix
    vector<vector<mi>> A(2 * n, vector<mi>(2 * n, 0));
    for (int i = 0; i < n; ++i) {
        int j_win = AC.d[i].to[0];
        bool swap_win = AC.d[j_win].ends_here & 1;
        if (swap_win) {
            A[i][j_win + n] = W;
            A[i + n][j_win] = L;
        } else {
            A[i][j_win] = W;
            A[i + n][j_win + n] = L;
        }
        int j_lose = AC.d[i].to[1];
        bool swap_lose = AC.d[j_lose].ends_here & 1;
        if (swap_lose) {
            A[i][j_lose + n] = mi(0) - W;
            A[i + n][j_lose] = mi(0) - L;
        } else {
            A[i][j_lose] = mi(0) - W;
            A[i + n][j_lose + n] = mi(0) - L;
        }
    }

    vector<vector<mi>> d0(1, vector<mi>(2 * n, 0));
    d0[0][0] = 1;
    vector<vector<mi>> mu(2 * n, vector<mi>(1));
    for (int i = 0; i < n; ++i) {
        mu[i][0] = mi(X) * W - mi(Y) * (mi(0) - W);
        mu[i+n][0] = mi(X) * L - mi(Y) * (mi(0) - L);
    }

    auto ans = d0 * geometricSum(A, n - 1) * mu;
    return ans[0][0].v;

}

int main() {
    int T;
    cin >> T;
    for (int i = 0; i < T; i++) {
        int N, K, X, Y, W1, W2, L1, L2;
        cin >> N >> K;
        cin >> X >> Y >> W1 >> W2 >> L1 >> L2;
        vector<string> S(K);
        for (int j = 0; j < K; ++j) {
            cin >> S[j];
        }
        cout << solve(N, K, X, Y, W1, W2, L1, L2, S) << '\n';
    }
}
