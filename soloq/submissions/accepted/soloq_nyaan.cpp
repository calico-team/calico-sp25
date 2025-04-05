#pragma GCC optimize("O3,unroll-loops")
#pragma GCC target("avx2")
#include <bits/stdc++.h>
#include <immintrin.h>
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
 * Description: Vectorized modular integer and fast matrix multiplication
 * Source: Nyaan (https://judge.yosupo.jp/submission/48008)
 */

template <uint32_t mod>
struct LazyMontgomeryModInt {
  using mint = LazyMontgomeryModInt;
  using i32 = int32_t;
  using u32 = uint32_t;
  using u64 = uint64_t;

  static constexpr u32 get_r() {
    u32 ret = mod;
    for (i32 i = 0; i < 4; ++i) ret *= 2 - mod * ret;
    return ret;
  }

  static constexpr u32 r = get_r();
  static constexpr u32 n2 = -u64(mod) % mod;
  static_assert(r * mod == 1, "invalid, r * mod != 1");
  static_assert(mod < (1 << 30), "invalid, mod >= 2 ^ 30");
  static_assert((mod & 1) == 1, "invalid, mod % 2 == 0");

  u32 a;

  constexpr LazyMontgomeryModInt() : a(0) {}
  constexpr LazyMontgomeryModInt(const int64_t &b)
      : a(reduce(u64(b % mod + mod) * n2)){};

  static constexpr u32 reduce(const u64 &b) {
    return (b + u64(u32(b) * u32(-r)) * mod) >> 32;
  }

  constexpr mint &operator+=(const mint &b) {
    if (i32(a += b.a - 2 * mod) < 0) a += 2 * mod;
    return *this;
  }

  constexpr mint &operator-=(const mint &b) {
    if (i32(a -= b.a) < 0) a += 2 * mod;
    return *this;
  }

  constexpr mint &operator*=(const mint &b) {
    a = reduce(u64(a) * b.a);
    return *this;
  }

  constexpr mint &operator/=(const mint &b) {
    *this *= b.inverse();
    return *this;
  }

  constexpr mint operator+(const mint &b) const { return mint(*this) += b; }
  constexpr mint operator-(const mint &b) const { return mint(*this) -= b; }
  constexpr mint operator*(const mint &b) const { return mint(*this) *= b; }
  constexpr mint operator/(const mint &b) const { return mint(*this) /= b; }
  constexpr bool operator==(const mint &b) const {
    return (a >= mod ? a - mod : a) == (b.a >= mod ? b.a - mod : b.a);
  }
  constexpr bool operator!=(const mint &b) const {
    return (a >= mod ? a - mod : a) != (b.a >= mod ? b.a - mod : b.a);
  }
  constexpr mint operator-() const { return mint() - mint(*this); }

  constexpr mint pow(u64 n) const {
    mint ret(1), mul(*this);
    while (n > 0) {
      if (n & 1) ret *= mul;
      mul *= mul;
      n >>= 1;
    }
    return ret;
  }
  
  constexpr mint inverse() const { return pow(mod - 2); }

  friend ostream &operator<<(ostream &os, const mint &b) {
    return os << b.get();
  }

  friend istream &operator>>(istream &is, mint &b) {
    int64_t t;
    is >> t;
    b = LazyMontgomeryModInt<mod>(t);
    return (is);
  }
  
  constexpr u32 get() const {
    u32 ret = reduce(a);
    return ret >= mod ? ret - mod : ret;
  }

  static constexpr u32 get_mod() { return mod; }
};
//

#pragma GCC optimize("O3,unroll-loops")
#pragma GCC target("avx2")

using m256 = __m256i;
struct alignas(32) mmint {
  m256 x;
  static m256 R, mR, M0, M1, M2, N2;

  mmint() : x() {}
  inline mmint(const m256& _x) : x(_x) {}
  inline mmint(int a) : x(_mm256_set1_epi32(a)) {}
  inline mmint(int a0, int a1, int a2, int a3, int a4, int a5, int a6, int a7)
      : x(_mm256_set_epi32(a7, a6, a5, a4, a3, a2, a1, a0)) {}
  inline operator m256&() { return x; }
  inline operator const m256&() const { return x; }
  inline int& operator[](int i) { return *(reinterpret_cast<int*>(&x) + i); }
  inline const int& operator[](int i) const {
    return *(reinterpret_cast<const int*>(&x) + i);
  }

  friend ostream& operator<<(ostream& os, const mmint& m) {
    unsigned r = R[0], mod = M1[0];
    auto reduce1 = [&](const uint64_t& b) {
      unsigned res = (b + uint64_t(unsigned(b) * unsigned(-r)) * mod) >> 32;
      return res >= mod ? res - mod : res;
    };
    for (int i = 0; i < 8; i++) {
      os << reduce1(m[i]) << (i == 7 ? "" : " ");
    }
    return os;
  }

  template <typename mint>
  static void set_mod() {
    R = _mm256_set1_epi32(mint::r);
    M0 = _mm256_setzero_si256();
    M1 = _mm256_set1_epi32(mint::get_mod());
    M2 = _mm256_set1_epi32(mint::get_mod() * 2);
    N2 = _mm256_set1_epi32(mint::n2);
    mR = _mm256_sub_epi32(M0, R);
  }

  static inline mmint reduce(const mmint& prod02, const mmint& prod13) {
    m256 unpalo = _mm256_unpacklo_epi32(prod02, prod13);
    m256 unpahi = _mm256_unpackhi_epi32(prod02, prod13);
    m256 prodlo = _mm256_unpacklo_epi64(unpalo, unpahi);
    m256 prodhi = _mm256_unpackhi_epi64(unpalo, unpahi);
    m256 hiplm1 = _mm256_add_epi32(prodhi, M1);
    m256 lomulr = _mm256_mullo_epi32(prodlo, R);
    m256 a13 = _mm256_shuffle_epi32(lomulr, 0xF5);
    m256 prod02_ = _mm256_mul_epu32(lomulr, M1);
    m256 prod13_ = _mm256_mul_epu32(a13, M1);
    m256 unpalo_ = _mm256_unpacklo_epi32(prod02_, prod13_);
    m256 unpahi_ = _mm256_unpackhi_epi32(prod02_, prod13_);
    m256 prod = _mm256_unpackhi_epi64(unpalo_, unpahi_);
    return _mm256_sub_epi32(hiplm1, prod);
  }

  static inline mmint itom(const mmint& A) { return A * N2; }

  static inline mmint mtoi(const mmint& A) {
    m256 lomulr = _mm256_mullo_epi32(A, mR);
    m256 a13 = _mm256_shuffle_epi32(lomulr, 0xF5);
    m256 prod02_ = _mm256_mul_epu32(lomulr, M1);
    m256 prod13_ = _mm256_mul_epu32(a13, M1);
    m256 unpalo_ = _mm256_unpacklo_epi32(prod02_, prod13_);
    m256 unpahi_ = _mm256_unpackhi_epi32(prod02_, prod13_);
    m256 prod = _mm256_unpackhi_epi64(unpalo_, unpahi_);
    m256 cmpA = _mm256_cmpgt_epi32(A, M0);
    m256 addA = _mm256_and_si256(cmpA, mmint(1));
    return _mm256_add_epi32(prod, addA);
  }

  friend inline mmint operator+(const mmint& A, const mmint& B) {
    m256 apb = _mm256_add_epi32(A, B);
    m256 ret = _mm256_sub_epi32(apb, M2);
    m256 cmp = _mm256_cmpgt_epi32(M0, ret);
    m256 add = _mm256_and_si256(cmp, M2);
    return _mm256_add_epi32(add, ret);
  }

  friend inline mmint operator-(const mmint& A, const mmint& B) {
    m256 ret = _mm256_sub_epi32(A, B);
    m256 cmp = _mm256_cmpgt_epi32(M0, ret);
    m256 add = _mm256_and_si256(cmp, M2);
    return _mm256_add_epi32(add, ret);
  }

  friend inline mmint operator*(const mmint& A, const mmint& B) {
    m256 a13 = _mm256_shuffle_epi32(A, 0xF5);
    m256 b13 = _mm256_shuffle_epi32(B, 0xF5);
    m256 prod02 = _mm256_mul_epu32(A, B);
    m256 prod13 = _mm256_mul_epu32(a13, b13);
    return reduce(prod02, prod13);
  }

  inline mmint& operator+=(const mmint& A) { return (*this) = (*this) + A; }
  inline mmint& operator-=(const mmint& A) { return (*this) = (*this) - A; }
  inline mmint& operator*=(const mmint& A) { return (*this) = (*this) * A; }

  bool operator==(const mmint& A) {
    m256 sub = _mm256_sub_epi32(x, A.x);
    return _mm256_testz_si256(sub, sub) == 1;
  }
  bool operator!=(const mmint& A) { return !((*this) == A); }
};
__attribute__((aligned(32))) __m256i mmint::R, mmint::mR;
__attribute__((aligned(32))) __m256i mmint::M0, mmint::M1, mmint::M2, mmint::N2;

/**
 * @brief vectorize modint
 */


constexpr int B = 1 << 6;

// B*Bの正方行列を高速に乗算するライブラリ。
// B*B行列a,bを タテB行 ヨコB/8行の行列と見なす.
// s : 正順に配置。すなわちa_{i,k}をs[i * (B / 8) + k]に配置する。
// t : 逆順に配置。すなわちb_{k,j}をt[j * B + k]に配置する。
// u : 正順に配置。すなわちc_{i,j}をu[i * (B / 8) + j]に配置する。
namespace block_mat_prod_impl {

constexpr int B8 = B / 8;

void mul_simd(mmint* __restrict__ s, mmint* __restrict__ t,
              mmint* __restrict__ u) {
  // normalize
  for (int i = 0; i < B * B8; i++) {
    const m256 cmpS = _mm256_cmpgt_epi32(s[i], mmint::M1);
    const m256 cmpT = _mm256_cmpgt_epi32(t[i], mmint::M1);
    const m256 difS = _mm256_and_si256(cmpS, mmint::M1);
    const m256 difT = _mm256_and_si256(cmpT, mmint::M1);
    s[i] = _mm256_sub_epi32(s[i], difS);
    t[i] = _mm256_sub_epi32(t[i], difT);
  }

  // mul
  mmint th1, th2, zero = _mm256_setzero_si256();
  th1[1] = th1[3] = th1[5] = th1[7] = mmint::M1[0];
  th2[1] = th2[3] = th2[5] = th2[7] = mmint::M2[0];

#define INIT_X(x, y)                          \
  m256 prod02##x##y = _mm256_setzero_si256(); \
  m256 prod13##x##y = _mm256_setzero_si256()

#define INIT_Y(j, k, l, y)            \
  m256 T##y = t[(j + y) * B + k + l]; \
  const m256 T13##y = _mm256_shuffle_epi32(T##y, 0xF5);

#define PROD(x, y)                                              \
  m256 S##x##y = _mm256_set1_epi32(s[(i + x) * B8 + k / 8][l]); \
  const m256 ST02##x##y = _mm256_mul_epu32(S##x##y, T##y);      \
  const m256 ST13##x##y = _mm256_mul_epu32(S##x##y, T13##y);    \
  prod02##x##y = _mm256_add_epi64(prod02##x##y, ST02##x##y);    \
  prod13##x##y = _mm256_add_epi64(prod13##x##y, ST13##x##y)

#define COMP(x, y)                                            \
  m256 cmp02##x##y = _mm256_cmpgt_epi64(zero, prod02##x##y);  \
  m256 cmp13##x##y = _mm256_cmpgt_epi64(zero, prod13##x##y);  \
  m256 dif02##x##y = _mm256_and_si256(cmp02##x##y, th2);      \
  m256 dif13##x##y = _mm256_and_si256(cmp13##x##y, th2);      \
  prod02##x##y = _mm256_sub_epi64(prod02##x##y, dif02##x##y); \
  prod13##x##y = _mm256_sub_epi64(prod13##x##y, dif13##x##y)

#define REDUCE(x, y)                                      \
  for (int _ = 0; _ < 2; _++) {                           \
    m256 cmp02 = _mm256_cmpgt_epi64(prod02##x##y, th1);   \
    m256 cmp13 = _mm256_cmpgt_epi64(prod13##x##y, th1);   \
    m256 dif02 = _mm256_and_si256(cmp02, th1);            \
    m256 dif13 = _mm256_and_si256(cmp13, th1);            \
    prod02##x##y = _mm256_sub_epi64(prod02##x##y, dif02); \
    prod13##x##y = _mm256_sub_epi64(prod13##x##y, dif13); \
  }                                                       \
  u[(i + x) * B8 + j + y] = mmint::reduce(prod02##x##y, prod13##x##y)

  for (int i = 0; i < B; i += 8) {
    for (int j = 0; j < B8; j += 1) {
      INIT_X(0, 0);
      INIT_X(1, 0);
      INIT_X(2, 0);
      INIT_X(3, 0);
      INIT_X(4, 0);
      INIT_X(5, 0);
      INIT_X(6, 0);
      INIT_X(7, 0);
      for (int k = 0; k < B; k += 8) {
        for (int l = 0; l < 8; l++) {
          INIT_Y(j, k, l, 0);
          PROD(0, 0);
          PROD(1, 0);
          PROD(2, 0);
          PROD(3, 0);
          PROD(4, 0);
          PROD(5, 0);
          PROD(6, 0);
          PROD(7, 0);
        }
        COMP(0, 0);
        COMP(1, 0);
        COMP(2, 0);
        COMP(3, 0);
        COMP(4, 0);
        COMP(5, 0);
        COMP(6, 0);
        COMP(7, 0);
      }
      REDUCE(0, 0);
      REDUCE(1, 0);
      REDUCE(2, 0);
      REDUCE(3, 0);
      REDUCE(4, 0);
      REDUCE(5, 0);
      REDUCE(6, 0);
      REDUCE(7, 0);
    }
  }
}

#undef INIT
#undef PROD
#undef COMP
#undef REDUCE

}  // namespace block_mat_prod_impl
using block_mat_prod_impl::mul_simd;

void strassen(int N, mmint* __restrict__ s, mmint* __restrict__ t,
              mmint* __restrict__ u) {
  memset((void*)u, 0, N * N * sizeof(int));

  if (N == B) {
    mul_simd(s, t, u);
    return;
  }

  mmint* ps = s + N * N / 8;
  mmint* pt = t + N * N / 8;
  mmint* pu = u + N * N / 8;
  int nx = N * N / 32;
  int o11 = nx * 0, o12 = nx * 1, o21 = nx * 2, o22 = nx * 3;

  // P1
  for (int i = 0; i < nx; i++) ps[i] = s[o11 + i] + s[o22 + i];
  for (int i = 0; i < nx; i++) pt[i] = t[o11 + i] + t[o22 + i];
  strassen(N / 2, ps, pt, pu);
  for (int i = 0; i < nx; i++) u[o11 + i] = pu[i], u[o22 + i] = pu[i];

  // P2
  for (int i = 0; i < nx; i++) ps[i] = s[o21 + i] + s[o22 + i];
  for (int i = 0; i < nx; i++) pt[i] = t[o11 + i];
  strassen(N / 2, ps, pt, pu);
  for (int i = 0; i < nx; i++) u[o21 + i] = pu[i], u[o22 + i] -= pu[i];

  // P3
  for (int i = 0; i < nx; i++) ps[i] = s[o11 + i];
  for (int i = 0; i < nx; i++) pt[i] = t[o12 + i] - t[o22 + i];
  strassen(N / 2, ps, pt, pu);
  for (int i = 0; i < nx; i++) u[o12 + i] = pu[i], u[o22 + i] += pu[i];

  // P4
  for (int i = 0; i < nx; i++) ps[i] = s[o22 + i];
  for (int i = 0; i < nx; i++) pt[i] = t[o21 + i] - t[o11 + i];
  strassen(N / 2, ps, pt, pu);
  for (int i = 0; i < nx; i++) u[o11 + i] += pu[i], u[o21 + i] += pu[i];

  // P5
  for (int i = 0; i < nx; i++) ps[i] = s[o11 + i] + s[o12 + i];
  for (int i = 0; i < nx; i++) pt[i] = t[o22 + i];
  strassen(N / 2, ps, pt, pu);
  for (int i = 0; i < nx; i++) u[o11 + i] -= pu[i], u[o12 + i] += pu[i];

  // P6
  for (int i = 0; i < nx; i++) ps[i] = s[o21 + i] - s[o11 + i];
  for (int i = 0; i < nx; i++) pt[i] = t[o11 + i] + t[o12 + i];
  strassen(N / 2, ps, pt, pu);
  for (int i = 0; i < nx; i++) u[o22 + i] += pu[i];

  // P7
  for (int i = 0; i < nx; i++) ps[i] = s[o12 + i] - s[o22 + i];
  for (int i = 0; i < nx; i++) pt[i] = t[o21 + i] + t[o22 + i];
  strassen(N / 2, ps, pt, pu);
  for (int i = 0; i < nx; i++) u[o11 + i] += pu[i];
}

constexpr int S = 512;
constexpr int S8 = S / 8;

void place_s(int N, int a, int b, mmint* __restrict__ dst,
             mmint* __restrict__ src) {
  if (N == B) {
    int B8 = B / 8;
    for (int i = 0; i < B; i++) {
      memcpy(dst + i * B8, src + (a + i) * S8 + b / 8, B8 * sizeof(mmint));
    }
    return;
  }
  int nx = N * N / 32, M = N / 2;
  place_s(M, a + 0, b + 0, dst + nx * 0, src);
  place_s(M, a + 0, b + M, dst + nx * 1, src);
  place_s(M, a + M, b + 0, dst + nx * 2, src);
  place_s(M, a + M, b + M, dst + nx * 3, src);
}

void place_t(int N, int a, int b, mmint* __restrict__ dst,
             mmint* __restrict__ src) {
  if (N == B) {
    int B8 = B / 8;
    // t : 逆順に配置。すなわちb_{k,j}をt[j * B + k]に配置する。
    for (int k = 0; k < B; k++) {
      for (int j = 0; j < B8; j++) {
        dst[j * B + k] = src[(a + k) * S8 + j + b / 8];
      }
    }
    return;
  }
  int nx = N * N / 32, M = N / 2;
  place_t(M, a + 0, b + 0, dst + nx * 0, src);
  place_t(M, a + 0, b + M, dst + nx * 1, src);
  place_t(M, a + M, b + 0, dst + nx * 2, src);
  place_t(M, a + M, b + M, dst + nx * 3, src);
}

void place_rev(int N, int a, int b, mmint* __restrict__ dst,
               mmint* __restrict__ src) {
  if (N == B) {
    int w = B / 8;
    for (int i = 0; i < B; i++) {
      memcpy(src + (a + i) * S8 + b / 8, dst + i * w, w * sizeof(mmint));
    }
    return;
  }
  int nx = N * N / 32, M = N / 2;
  place_rev(M, a + 0, b + 0, dst + nx * 0, src);
  place_rev(M, a + 0, b + M, dst + nx * 1, src);
  place_rev(M, a + M, b + 0, dst + nx * 2, src);
  place_rev(M, a + M, b + M, dst + nx * 3, src);
}

mmint s[S * S8 * 3 / 2], t[S * S8 * 3 / 2], u[S * S8 * 3 / 2];

void prod(unsigned int* __restrict__ a, unsigned int* __restrict__ b,
          unsigned int* __restrict__ c) {
  place_s(S, 0, 0, s, reinterpret_cast<mmint*>(a));
  place_t(S, 0, 0, t, reinterpret_cast<mmint*>(b));
  for (int i = 0; i < S * S8; i++) s[i] = mmint::itom(s[i]);
  for (int i = 0; i < S * S8; i++) t[i] = mmint::itom(t[i]);
  strassen(S, s, t, u);
  for (int i = 0; i < S * S8; i++) u[i] = mmint::mtoi(u[i]);
  place_rev(S, 0, 0, u, reinterpret_cast<mmint*>(c));
}

void test() {
  unsigned int* a = reinterpret_cast<unsigned int*>(t);
  unsigned int* b = reinterpret_cast<unsigned int*>(u);
  unsigned int* c = reinterpret_cast<unsigned int*>(s);
  for (int i = 0; i < S; i++) {
    for (int j = 0; j < S; j++) {
      b[i * S + j] = a[i * S + j] = i + j;
    }
  }

  for (int loop = 0; loop < 100; loop++) prod(a, b, c);
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

// Define operators using mint since it will be easier to read
 
using mint = LazyMontgomeryModInt<MOD>;
using vmi = V<mint>;
using Mat = V<vmi>;

Mat operator+(Mat const& A, Mat const& B) {
    Mat C = A;
    F0R(i, sz(A)) F0R(j, sz(A[0])) C[i][j] += B[i][j];
    return C;
}

Mat operator*(Mat const& A, Mat const& B) {
    unsigned int* a = reinterpret_cast<unsigned int*>(t);
    unsigned int* b = reinterpret_cast<unsigned int*>(u);
    unsigned int* c = reinterpret_cast<unsigned int*>(s);
    F0R(i, sz(A)) F0R(j, sz(A[0])) a[i * S + j] = A[i][j].get();
    F0R(i, sz(B)) F0R(j, sz(B[0])) b[i * S + j] = B[i][j].get();
    prod(a, b, c);
    Mat C(sz(A), vmi(sz(B[0])));
    F0R(i, sz(A)) F0R(j, sz(B[0])) C[i][j] = c[i * S + j];
    return C;
}

Mat id(int n) {
    Mat eye(n, vmi(n));
    F0R(i, n) eye[i][i] = 1;
    return eye;
}

Mat pow(Mat A, ll x) {
    Mat res = id(sz(A));
    while (x) {
        if (x & 1) res = res * A;
        A = A * A;
        x >>= 1; 
    }
    return res;
}

// Computes \sum_{i = 0}^{n}{A^i}
Mat geometricSum(Mat const& A, ll n) {
    if (n == 0) return id(sz(A));
    if (n & 1) {
        return (id(sz(A)) + pow(A, n / 2 + 1)) * geometricSum(A, n / 2);
    }
    else {
        return pow(A, n) + geometricSum(A, n - 1);
    }
}

int main() {
    cin.tie(0)->sync_with_stdio(0);
    mmint::set_mod<mint>();

    int tc; cin >> tc;
    rep(tc) {
        // read data
        ll n; int k;
        cin >> n >> k;
        mint x, y, w1, w2, l1, l2;
        cin >> x >> y >> w1 >> w2 >> l1 >> l2;
        vector<str> streaks(k);
        each(si, streaks) cin >> si;

        // calculate probabilities mod 1e9 + 7
        mint w = w1 / w2, l = l1 / l2, one = 1;

        // generate graph using aho-corasick
        ACfixed<2> ac(streaks);
        int nStates = sz(ac.d);
        vector<vector<mint>> A(2 * nStates, vector<mint>(2 * nStates));
        F0R(i, nStates) {
            int u = ac.d[i].to[0], v = ac.d[i].to[1];
            bool swap_u = sz(ac.d[u].endsHere) & 1;
            if (swap_u) {
                A[i][u + nStates] = w;
                A[i + nStates][u] = l;
            } else {
                A[i][u] = w;
                A[i + nStates][u + nStates] = l;
            }
            bool swap_v = sz(ac.d[v].endsHere) & 1;
            if (swap_v) {
                A[i][v + nStates] = one - w;
                A[i + nStates][v] = one - l;
            } else {
                A[i][v] = one - w;
                A[i + nStates][v + nStates] = one - l;
            }
        }
        // Compute mu
        vector<mint> mu(2 * nStates);
        F0R(i, nStates) {
            mu[i] = x * w - y * (one - w);
            mu[i + nStates] = x * l - y * (one - l);
        }
        Mat B = geometricSum(A, n - 1);
        mint ans = 0;
        F0R(i, 2 * nStates) ans += mu[i] * B[0][i];
        cout << ans.get() << '\n';
    }
    return 0;
}