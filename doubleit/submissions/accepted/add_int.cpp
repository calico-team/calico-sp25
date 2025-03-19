#include <iostream>
#include <vector>
#include <string>

using namespace std;

/**
 * Return the total money Big Ben pays
 *
 * L: vector of strings representing the people Big Ben talks to
 */
int solve(const vector<char>& L) {
    int total = 0;
    int money = 1;
    for (int i = 0; i < L.size(); i++) {
        if (L[i] == 'T') {
            total += money;
            money = 1;
        }
        else {
            money *= 2;
        }
    }
    return total;
}

int main() {
    int T;
    cin >> T;
    for (int i = 0; i < T; i++) {
        vector<char> L;
        string S;
        cin >> S;
        for (char c : S) {
            if (c != ' ') {
                L.push_back(c);
            }
        }
        cout << solve(L) << '\n';
    }
}
