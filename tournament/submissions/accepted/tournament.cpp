#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <limits>

using namespace std;

string helper(const vector<string>& C, const vector<int>& P) {
    if (C.size() == 1) {
        return C[0];
    }
    vector<string> winners;
    vector<int> winnerPowers;
    for (int i = 0; i < C.size(); i += 2) {
        if (P[i] > P[i + 1]) {
            winners.push_back(C[i]);
        } else if (P[i] == P[i + 1]){
            winners.push_back(C[i] + C[i + 1]);
        } else {
            winners.push_back(C[i + 1]);
        }
        winnerPowers.push_back(P[i] + P[i + 1]);
    }
    return helper(winners, winnerPowers);
}

string solve(int N, const vector<string>& C, const vector<int>& P) {
    /**
     * Return a single string of the champion's name
     *
     * N: The length of C and P
     * C: List of strings of the competitors
     * P: List of integers of competitor's power
     */
    return helper(C, P);
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
        getline(cin, line);
        stringstream ss1(line);
        for (int j = 0; j < N; ++j) {
            ss1 >> C[j];
        }
        getline(cin, line);
        stringstream ss2(line);
        for (int j = 0; j < N; ++j) {
            ss2 >> P[j];
        }
        cout << solve(N, C, P) << endl;
    }
}
