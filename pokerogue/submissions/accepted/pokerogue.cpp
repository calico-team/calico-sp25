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
 * Description: 1D range increment and sum query.
 * Source: USACO Counting Haybales
 	* https://codeforces.com/blog/entry/82400
 * Verification: USACO Counting Haybales
 */

 struct LazySeg { 
	struct F { // lazy update
		db inc = 0;
		F() {}
		F(db x) { inc = x; }
		F& operator*=(const F& a) { inc += a.inc; return *this; }
	}; V<F> lazy;
	struct T { // data you need to store for each interval
		db mx = numeric_limits<db>::min();
        T() {}
		T(db x) { mx = x; }
		friend T operator+(const T& a, const T& b) {
            T res;
            res.mx = max(a.mx, b.mx);
            return res;
		}
		T& operator*=(const F& a) {
            mx += a.inc;
            return *this;
        }
	}; V<T> seg;
	int SZ = 1;
	void init(const V<T>& _seg) {
		while (SZ < sz(_seg)) SZ *= 2;
		seg.rsz(2*SZ); lazy.rsz(2*SZ);
		F0R(i,SZ) seg[SZ+i] = _seg[i];
		ROF(i,1,SZ) pull(i);
	}
	void push(int ind) { /// modify values for current node
		seg[ind] *= lazy[ind];
		if (ind < SZ) F0R(i,2) lazy[2*ind+i] *= lazy[ind];
		lazy[ind] = F();
	} // recalc values for current node
	void pull(int ind) { seg[ind] = seg[2*ind]+seg[2*ind+1]; }
	void upd(int lo, int hi, F inc, int ind, int L, int R) {
		push(ind); if (hi < L || R < lo) return;
		if (lo <= L && R <= hi) { 
			lazy[ind] = inc; push(ind); return; }
		int M = (L+R)/2; upd(lo,hi,inc,2*ind,L,M); 
		upd(lo,hi,inc,2*ind+1,M+1,R); pull(ind);
	}
	void upd(int lo, int hi, db inc) { upd(lo,hi,{inc},1,0,SZ-1); }
	T query(int lo, int hi, int ind, int L, int R) {
		push(ind); if (lo > R || L > hi) return T();
		if (lo <= L && R <= hi) return seg[ind];
		int M = (L+R)/2; 
		return query(lo,hi,2*ind,L,M)+query(lo,hi,2*ind+1,M+1,R);
	}
	T query(int lo, int hi) { return query(lo,hi,1,0,SZ-1); }
};

using vd = vector<db>;

// Returns true if the answer can be >= x
bool possible(int n, int k, vd const& a, vd const& b, vd const& c, vd const& d, db x) {
    int s = 2 * n + 5;
    vector<LazySeg::T> v(s + 1);
    for (int i = n + 1; i < sz(v); ++i)
        v[i].mx = 0;
    LazySeg st;
    st.init(v);
    vd dp(n + 1);
    for (int i = n - 1; i >= 0; --i) {
        dp[i] = a[i] - x * b[i] + max(dp[i + 1], st.query(i + k + 1, s).mx);
        st.upd(i, i, dp[i]);
        st.upd(i + 1, s, a[i] + c[i] - x * d[i]);
    }
    return dp[0] >= 0;
}

double solve(int N, int K, vector<int> A, vector<int> B, vector<int> C, vector<int> D) {
    vd a(N), b(N), c(N), d(N);
    for (int i = 0; i < N; ++i) {
        a[i] = A[i];
        b[i] = B[i];
        c[i] = C[i];
        d[i] = D[i];
    }
    db l = 0, r = 1e9;
    while (r - l > 1e-6) {
        db m = (r + l) / db(2);
        if (possible(N, K, a, b, c, d, m)) l = m;
        else r = m;
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
        cout << fixed << setprecision(5) << solve(N, K, A, B, C, D) << '\n';
    }
}