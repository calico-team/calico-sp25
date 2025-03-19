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
    //YOUR CODE HERE
    return -1;
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
