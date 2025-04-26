#include <bits/stdc++.h>
using namespace std;
 
using ll = long long;
using db = long double; // or double, if TL is tight
using str = string; // yay python! //

// pairs
using pi = pair<int,int>;
using pl = pair<ll,ll>;
using pd = pair<db,db>;
#define mp make_pair
#define f first
#define s second

#define tcT template<class T
#define tcTU tcT, class U
// ^ lol this makes everything look weird but I'll try it
tcT> using V = vector<T>; 
tcT, size_t SZ> using AR = array<T,SZ>; 
using vi = V<int>;
using vb = V<bool>;
using vl = V<ll>;
using vd = V<db>;
using vs = V<str>;
using vpi = V<pi>;
using vpl = V<pl>;
using vpd = V<pd>;

// vectors
// oops size(x), rbegin(x), rend(x) need C++17
#define sz(x) int((x).size())
#define bg(x) begin(x)
#define all(x) bg(x), end(x)
#define rall(x) x.rbegin(), x.rend() 
#define sor(x) sort(all(x)) 
#define rsz resize
#define ins insert 
#define pb push_back
#define eb emplace_back
#define ft front()
#define bk back()

#define lb lower_bound
#define ub upper_bound
tcT> int lwb(V<T>& a, const T& b) { return int(lb(all(a),b)-bg(a)); }
tcT> int upb(V<T>& a, const T& b) { return int(ub(all(a),b)-bg(a)); }

// loops
#define FOR(i,a,b) for (int i = (a); i < (b); ++i)
#define F0R(i,a) FOR(i,0,a)
#define ROF(i,a,b) for (int i = (b)-1; i >= (a); --i)
#define R0F(i,a) ROF(i,0,a)
#define rep(a) F0R(_,a)
#define each(a,x) for (auto& a: x)

const int MOD = (int)1e9+7; // 998244353;
const int INF = (int)1e9;
const int MX = (int)2e5+5;
const ll BIG = 1e18; // not too close to LLONG_MAX
const db PI = acos((db)-1);
const int dx[4]{1,0,-1,0}, dy[4]{0,1,0,-1}; // for every grid problem!!
mt19937 rng((uint32_t)chrono::steady_clock::now().time_since_epoch().count()); 
template<class T> using pqg = priority_queue<T,vector<T>,greater<T>>;

// bitwise ops
// also see https://gcc.gnu.org/onlinedocs/gcc/Other-Builtins.html
constexpr int pct(int x) { return __builtin_popcount(x); } // # of bits set
constexpr int bits(int x) { // assert(x >= 0); // make C++11 compatible until USACO updates ...
	return x == 0 ? 0 : 31-__builtin_clz(x); } // floor(log2(x)) 
constexpr int p2(int x) { return 1<<x; }
constexpr int msk2(int x) { return p2(x)-1; }

ll cdiv(ll a, ll b) { return a/b+((a^b)>0&&a%b); } // divide a by b rounded up
ll fdiv(ll a, ll b) { return a/b-((a^b)<0&&a%b); } // divide a by b rounded down

tcT> bool ckmin(T& a, const T& b) {
	return b < a ? a = b, 1 : 0; } // set a = min(a,b)
tcT> bool ckmax(T& a, const T& b) {
	return a < b ? a = b, 1 : 0; } // set a = max(a,b)

tcTU> T fstTrue(T lo, T hi, U f) {
	++hi; assert(lo <= hi); // assuming f is increasing
	while (lo < hi) { // find first index such that f is true 
		T mid = lo+(hi-lo)/2;
		f(mid) ? hi = mid : lo = mid+1; 
	} 
	return lo;
}
tcTU> T lstTrue(T lo, T hi, U f) {
	--lo; assert(lo <= hi); // assuming f is decreasing
	while (lo < hi) { // find first index such that f is true 
		T mid = lo+(hi-lo+1)/2;
		f(mid) ? lo = mid : hi = mid-1;
	} 
	return lo;
}
tcT> void remDup(vector<T>& v) { // sort and remove duplicates
	sort(all(v)); v.erase(unique(all(v)),end(v)); }
tcTU> void erase(T& t, const U& u) { // don't erase
	auto it = t.find(u); assert(it != end(t));
	t.erase(it); } // element that doesn't exist from (multi)set


tcTU> inline ostream& operator << (ostream& o, pair<T, U> const& p);
tcT> inline ostream& operator << (ostream& o, V<T> const& v);

tcTU> inline ostream& operator << (ostream& o, pair<T, U> const& p) {
	return o << '(' << p.f << ", " << p.s << ')';
}

tcT> inline ostream& operator << (ostream& o, V<T> const& v) {
	F0R(i, sz(v) - 1) o << v[i] << ' ';
	if (sz(v)) o << v.back();
	return o;
}


/**
 * Description: Use in place of \texttt{complex<T>}.
 * Source: http://codeforces.com/blog/entry/22175, KACTL
 * Verification: various
 */

 using T = db; // or ll
 const T EPS = 1e-7; // adjust as needed
 using P = pair<T,T>; using vP = V<P>; using Line = pair<P,P>;
 int sgn(T a) { return (a>EPS)-(a<-EPS); }
 T sq(T a) { return a*a; }
 
 bool close(const P& a, const P& b) { 
     return sgn(a.f-b.f) == 0 && sgn(a.s-b.s) == 0; } 
 T abs2(const P& p) { return sq(p.f)+sq(p.s); }
 T abs(const P& p) { return sqrt(abs2(p)); }
 T arg(const P& p) { return atan2(p.s,p.f); }
 P conj(const P& p) { return P(p.f,-p.s); }
 P perp(const P& p) { return P(-p.s,p.f); }
 P dir(T ang) { return P(cos(ang),sin(ang)); }
 
 P operator-(const P& l) { return P(-l.f,-l.s); }
 P operator+(const P& l, const P& r) { 
     return P(l.f+r.f,l.s+r.s); }
 P operator-(const P& l, const P& r) { 
     return P(l.f-r.f,l.s-r.s); }
 P operator*(const P& l, const T& r) { 
     return P(l.f*r,l.s*r); }
 P operator*(const T& l, const P& r) { return r*l; }
 P operator/(const P& l, const T& r) { 
     return P(l.f/r,l.s/r); }
 P operator*(const P& l, const P& r) { 
     return P(l.f*r.f-l.s*r.s,l.s*r.f+l.f*r.s); }
 P operator/(const P& l, const P& r) { 
     return l*conj(r)/abs2(r); }
 P& operator+=(P& l, const P& r) { return l = l+r; }
 P& operator-=(P& l, const P& r) { return l = l-r; }
 P& operator*=(P& l, const T& r) { return l = l*r; }
 P& operator/=(P& l, const T& r) { return l = l/r; }
 P& operator*=(P& l, const P& r) { return l = l*r; }
 P& operator/=(P& l, const P& r) { return l = l/r; }
 
 P unit(const P& p) { return p/abs(p); }
 T dot(const P& a, const P& b) { return a.f*b.f+a.s*b.s; }
 T dot(const P& p, const P& a, const P& b) { return dot(a-p,b-p); }
 T cross(const P& a, const P& b) { return a.f*b.s-a.s*b.f; }
 T cross(const P& p, const P& a, const P& b) {
     return cross(a-p,b-p); }
 P reflect(const P& p, const Line& l) {
     P a = l.f, d = l.s-l.f;
     return a+conj((p-a)/d)*d; }
 P foot(const P& p, const Line& l) {
     return (p+reflect(p,l))/(T)2; }
 bool onSeg(const P& p, const Line& l) {
     return sgn(cross(l.f,l.s,p)) == 0 && sgn(dot(p,l.f,l.s)) <= 0; }


// {unique intersection point} if it exists
// {b.f,b.s} if input lines are the same
// empty if lines do not intersect
vP lineIsect(const Line& a, const Line& b) {
	T a0 = cross(a.f,a.s,b.f), a1 = cross(a.f,a.s,b.s); 
	if (a0 == a1) return a0 == 0 ? vP{b.f,b.s} : vP{};
	return {(b.s*a0-b.f*a1)/(a0-a1)};
}

// point in interior of both segments a and b, if it exists
vP strictIsect(const Line& a, const Line& b) {
	T a0 = cross(a.f,a.s,b.f), a1 = cross(a.f,a.s,b.s); 
	T b0 = cross(b.f,b.s,a.f), b1 = cross(b.f,b.s,a.s); 
	if (sgn(a0)*sgn(a1) < 0 && sgn(b0)*sgn(b1) < 0)
		return {(b.s*a0-b.f*a1)/(a0-a1)};
	return {};
}

// intersection of segments, a and b may be degenerate
vP segIsect(const Line& a, const Line& b) { 
	vP v = strictIsect(a,b); if (sz(v)) return v;
	set<P> s;
	#define i(x,y) if (onSeg(x,y)) s.ins(x)
	i(a.f,b); i(a.s,b); i(b.f,a); i(b.s,a);
	return {all(s)};
}


/**
 * Description: top-bottom convex hull
 * Time: O(N\log N)
 * Source: Wikibooks, KACTL
 * Verification:
	* https://open.kattis.com/problems/convexhull
 */


 pair<vi,vi> ulHull(const vP& v) {
     vi p(sz(v)), u, l; iota(all(p), 0);
     sort(all(p), [&v](int a, int b) { return v[a] < v[b]; });
     each(i,p) {
         #define ADDP(C, cmp) while (sz(C) > 1 && cross(\
             v[C[sz(C)-2]],v[C.bk],v[i]) cmp 0) C.pop_back(); C.pb(i);
         ADDP(u, >=); ADDP(l, <=);
     }
     return {u,l};
 }
 vi hullInd(const vP& v) { // returns indices in CCW order
     vi u,l; tie(u,l) = ulHull(v); if (sz(l) <= 1) return l;
     if (v[l[0]] == v[l[1]]) return {0};
     l.insert(end(l),1+rall(u)-1); return l;
 }
 vP hull(const vP& v) {
     vi w = hullInd(v); vP res; each(t,w) res.pb(v[t]);
     return res; }







/**
 * Description: Basic 3D geometry. 
 * Source: Own
 * Verification: (haven't done much 3D geo yet)
	* AMPPZ 2011 Cross Spider
	* https://atcoder.jp/contests/JAG2013Spring/tasks/icpc2013spring_h
	* https://codeforces.com/gym/102040 - I
	* https://codeforces.com/gym/102452/problem/F
 */



using P3 = AR<T,3>; using Tri = AR<P3,3>; using vP3 = V<P3>;
T abs2(const P3& x) { 
	T sum = 0; F0R(i,3) sum += sq(x[i]);
	return sum; }
T abs(const P3& x) { return sqrt(abs2(x)); }

P3& operator+=(P3& l, const P3& r) { F0R(i,3) l[i] += r[i]; 
	return l; }
P3& operator-=(P3& l, const P3& r) { F0R(i,3) l[i] -= r[i]; 
	return l; }
P3& operator*=(P3& l, const T& r) { F0R(i,3) l[i] *= r; 
	return l; }
P3& operator/=(P3& l, const T& r) { F0R(i,3) l[i] /= r; 
	return l; }
P3 operator-(P3 l) { l *= -1; return l; }
P3 operator+(P3 l, const P3& r) { return l += r; }
P3 operator-(P3 l, const P3& r) { return l -= r; }
P3 operator*(P3 l, const T& r) { return l *= r; }
P3 operator*(const T& r, const P3& l) { return l*r; }
P3 operator/(P3 l, const T& r) { return l /= r; }

P3 unit(const P3& x) { return x/abs(x); }
T dot(const P3& a, const P3& b) { 
	T sum = 0; F0R(i,3) sum += a[i]*b[i]; 
	return sum; }
P3 cross(const P3& a, const P3& b) {
	return {a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],
			a[0]*b[1]-a[1]*b[0]}; }
P3 cross(const P3& a, const P3& b, const P3& c) {
	return cross(b-a,c-a); }
P3 perp(const P3& a, const P3& b, const P3& c) {
	return unit(cross(a,b,c)); }

bool isMult(const P3& a, const P3& b) { // for long longs
	P3 c = cross(a,b); F0R(i,sz(c)) if (c[i] != 0) return 0; 
	return 1; }
bool collinear(const P3& a, const P3& b, const P3& c) { 
	return isMult(b-a,c-a); }

T DC(const P3&a,const P3&b,const P3&c,const P3&p) { 
	return dot(cross(a,b,c),p-a); }
bool coplanar(const P3&a,const P3&b,const P3&c,const P3&p) { 
	return DC(a,b,c,p) == 0; }
bool op(const P3& a, const P3& b) { 
	int ind = 0; // going in opposite directions?
	FOR(i,1,3) if (std::abs(a[i]*b[i])>std::abs(a[ind]*b[ind])) 
		ind = i;
	return a[ind]*b[ind] < 0;
}
// coplanar points, b0 and b1 on opposite sides of a0-a1?
bool opSide(const P3&a,const P3&b,const P3&c,const P3&d) { 
	return op(cross(a,b,c),cross(a,b,d)); }
// coplanar points, is a in Triangle b
bool inTri(const P3& a, const Tri& b) { 
	F0R(i,3)if(opSide(b[i],b[(i+1)%3],b[(i+2)%3],a))return 0;
	return 1; }

// point-seg dist
T psDist(const P3&p,const P3&a,const P3&b) { 
	if (dot(a-p,a-b) <= 0) return abs(a-p);
	if (dot(b-p,b-a) <= 0) return abs(b-p);
	return abs(cross(p,a,b))/abs(a-b);
}
// projection onto line
P3 foot(const P3& p, const P3& a, const P3& b) { 
	P3 d = unit(b-a); return a+dot(p-a,d)*d; }
// rotate p about axis
P3 rotAxis(const P3& p, const P3& a, const P3& b, T theta) {
	P3 dz = unit(b-a), f = foot(p,a,b); 
	P3 dx = p-f, dy = cross(dz,dx);
	return f+cos(theta)*dx+sin(theta)*dy;
}
// projection onto plane
P3 foot(const P3& a, const Tri& b) {
	P3 c = perp(b[0],b[1],b[2]);
	return a-c*(dot(a,c)-dot(b[0],c)); }
// line-plane intersection
P3 lpIntersect(const P3&a0,const P3&a1,const Tri&b) { 
	P3 c = unit(cross(b[2]-b[0],b[1]-b[0]));
	T x = dot(a0,c)-dot(b[0],c), y = dot(a1,c)-dot(b[0],c);
	return (y*a0-x*a1)/(y-x);
}

ostream& operator << (ostream& o, P3 const& p) {
    return o << p[0] << ' ' << p[1] << ' ' << p[2];
}



// Cylinder Problem

db volume(vP3& v) {
    db minHeight = v[0][2], maxHeight = v[0][2];
    each(p, v) {
        ckmin(minHeight, p[2]);
        ckmax(maxHeight, p[2]);
    }
    if (sgn(minHeight) * sgn(maxHeight) == -1) {
        return -1;
    }
    // Now we have one face of the box in the XY plane
    each(p, v) {
        p[2] -= minHeight;
    }
    maxHeight -= minHeight;  
    // the box is in the subspace {Z>0} now
    vP upperFace, sides, w;
    each(p, v) {
        if (sgn(p[2] - maxHeight) == 0 || sgn(p[2]) == 0) upperFace.pb({p[0],p[1]});
        else sides.pb({p[0], p[1]});
        w.pb({p[0], p[1]});
    }
    // First construct the Convex Hull of w
    auto h = hull(w); // please be ccw
    // If sol is unique then one of the sides has to appear in the CH of all the points
    // Tons of rotating shittiers
    int i = 0, j = 0, k = 1, l = 0, n = sz(h);
    for (int x = 0; x < n; ++x) {
        #define d(y) (abs2(h[y] - h[0]) * cos(arg(h[y]-h[0]) - arg(h[1]-h[0])))
        if (d(x) > d(j)) j = x;
    }
    for (int x = 0; x < n; ++x) {
        #define d(y) (abs2(h[y] - h[1]) * cos(arg(h[0] - h[1]) - arg(h[y] - h[1])))
        if (d(x) > d(l)) l = x;
    }
    for (i; i < n; ++i) {
        P A = h[i], B = h[(i+1)%n];
        for (j;;j = (j + 1) % n) {
            #define d(y) (abs2(h[y] - A) * cos(arg(h[y] - A) - arg(B - A)))
            if (d(j) > d((j + 1) % n)) break;
        }
        for(l;;l = (l + 1) % n) {
            #define d(y) (abs2(h[y] - B) * cos(arg(A - B) - arg(h[y] - B)))
            if (d(l) > d((l + 1) % n)) break;
        }

        for (k;;k = (k + 1) % n) {
            if (cross(B - A, h[(k+1)%n] - h[k]) <= 0) break;
        }

        P p = lineIsect({A,B},{h[j], h[j]+perp(B-A)})[0];
        P q = lineIsect({h[k], h[k]+B-A}, {p, p+perp(B-A)})[0];
        P r = lineIsect({h[k], h[k]+B-A}, {h[l], h[l]+perp(B-A)})[0];
        P s = lineIsect({A, B}, {h[l], h[l]+perp(B-A)})[0];

        // pqrs is the candidate for being the rectangle

        bool possible = true;
        each(u, sides) {
            if (!onSeg(u, {p,q}) && !onSeg(u, {q,r}) && !onSeg(u, {r,s}) && !onSeg(u, {s,p})) {
                possible = false;
                break;
            }
        }
        if (possible) {
            return abs(p-q) * abs(q-r) * maxHeight;
        }
    }
    return -1;
}

P3 transform(P3 const& e1, P3 const& e2, P3 const& e3, P3 const& x) {
    P3 ans = {0,0,0};
    for (int i = 0; i < 3; ++i) ans[0] += e1[i] * x[i];
    for (int i = 0; i < 3; ++i) ans[1] += e2[i] * x[i];
    for (int i = 0; i < 3; ++i) ans[2] += e3[i] * x[i];
    return ans;
}

db solve(int N, vd X, vd Y, vd Z) {
    vP3 v(N);
    F0R(i, N) v[i] = {X[i], Y[i], Z[i]};
    rep(1000) {
        // Sample 3 points
        int i = rng() % N;
        int j = rng() % N;
        int k = rng() % N;

        // Check they are different
        if (i == j or j == k or k == i) continue;
        
        P3 A = v[i], B = v[j], C = v[k];
        // Check that they are not collinear
        if (collinear(A, B, C)) continue;
        
        // Let's rotate all the points so that they are in the {z = 0} plane
        P3 u = B - A, e1 = unit(u), e3 = unit(cross(u, C - A)), e2 =  cross(e3, e1);

        vP3 w(N);
        F0R(x, N) w[x] = transform(e1, e2, e3, v[x] - A);

        db ans = volume(w);
        if (ans != -1) {
            // cout << "plane points = " << endl;
            // cout << v[i] << endl;
            // cout << v[j] << endl;
            // cout << v[k] << endl;
            return ans;
        }
    }
    return -1;

}

int main() {
    // int tc; cin >> tc;
    // while (tc--) {
    //     int N; cin >> N;
    //     vd X(N), Y(N), Z(N);
    //     // each(x, X) cin >> x;
    //     // each(y, Y) cin >> y;
    //     // each(z, Z) cin >> z;
    //     F0R(i,N) cin >> X[i] >> Y[i] >> Z[i];
    //     cout << fixed << setprecision(6) << solve(N, X, Y, Z) << '\n';
    // }

    // Create random test cases

    int NC = 2;
    ofstream in("00_main.in");
    ofstream ans("00_main.ans");
    in << NC << '\n';
    F0R(_,NC) {
        int height = 1 + rng() % 50, width = 1 + rng() % 50, depth = 1 + rng() % 50;
        int numPoints = 15;
        int alpha = rng() % 100, beta = rng() % 100, gamma = rng() % 100;
        int A = height * width, B = width * depth, C = depth * height;
        vP3 points;
        for (int i = 0; i < numPoints; ++i) {
            int choice = rng() % (A + B + C), x = rng() % 2;
            if (choice < A) {
                P3 p = { db(rng() % (height * 100 + 1)) / 100, db(rng() % (width * 100 + 1)) / 100, depth * x };
                points.pb(p);
            }
            else if (choice < A + B) {
                P3 p = { height * x, db(rng() % (width * 100 + 1)) / 100, db(rng() % (depth * 100 + 1)) / 100 };
                points.pb(p);
            }
            else {
                P3 p = { db(rng() % (height * 100 + 1)) / 100, width * x, db(rng() % (depth * 100 + 1)) / 100 };
                points.pb(p);
            }
        }
        
        // Let's add rotations
        if (_) each(p, points) {
            p = transform({1,0,0}, {0, cos(alpha), -sin(alpha)}, {0, sin(alpha), cos(alpha)}, p);
            p = transform({cos(beta), 0, sin(beta)}, {0,1,0}, {-sin(beta), 0, cos(beta)}, p);
            p = transform({cos(gamma), -sin(gamma), 0}, {sin(gamma), cos(gamma), 0}, {0,0,1}, p);
        }

        db minx = points[0][0], maxx = points[0][0], miny = points[0][1], maxy = points[0][1], minz = points[0][2], maxz = points[0][2];
        each(p, points) {
            minx = min(minx, p[0]);
            maxx = max(maxx, p[0]);
            miny = min(miny, p[1]);
            maxy = max(maxy, p[1]);
            minz = min(minz, p[2]);
            maxz = max(maxz, p[2]);
        }
        db cx = (minx + maxx) * 0.5, cy = (miny + maxy) * 0.5, cz = (minz + maxz) * 0.5;

        each(p, points) {
            p[0] -= cx;
            p[1] -= cy;
            p[2] -= cz;
        }

        int N = sz(points);
        vd X(N), Y(N), Z(N);
        F0R(i, N) {
            X[i] = points[i][0];
            Y[i] = points[i][1];
            Z[i] = points[i][2];
        }

        db volume = solve(N, X, Y, Z);
        db expected = height * width * depth;
        // cout << fixed << setprecision(6) << abs(volume - expected) << '\n';

        if (abs(volume - expected) < 1e-5) {
            
            in << N << '\n';
            in << fixed << setprecision(6) << X << '\n';
            in << fixed << setprecision(6) << Y << '\n';
            in << fixed << setprecision(6) << Z << '\n';
            ans << fixed << setprecision(6) << expected << '\n';
            
        }
        else {
            --_;
        }
    }
    in.close();
    ans.close();
    return 0;
}