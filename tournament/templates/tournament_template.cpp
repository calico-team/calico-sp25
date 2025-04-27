#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <limits>

using namespace std;

string solve(int N, const vector<string>& C, const vector<int>& P) {
    /**
     * Return a single string of the champion's name
     *
     * N: The length of C and P
     * C: List of strings of the competitors
     * P: List of integers of competitor's power
     */
    return "";
}

int main() {
    int T;
    cin >> T;

    for (int i = 0; i < T; ++i) {
        int N;
        cin >> N;
        vector<string> C(N);
        vector<int> P(N);
        string line;
        for (int j = 0; j < N; ++j) {
            cin >> C[j];
        }
        for (int j = 0; j < N; ++j) {
            cin >> P[j];
        }
        cout << solve(N, C, P) << endl;
    }
}
