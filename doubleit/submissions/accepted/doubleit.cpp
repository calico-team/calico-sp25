#include <iostream>
#include <vector>
#include <string>

using namespace std;

/**
 * Return the total money Big Ben pays
 *
 * N: length of the string P
 * P: String representing the people Big Ben talks to
 */
int solve(int N, string P) {
    int total = 0;
    int money = 1;
    for (int i = 0; i < P.size(); i++) {
        if (P[i] == 'T') {
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
        int N;
        string P;
        cin >> N;
        cin >> P;
        cout << solve(N, P) << '\n';
    }
}
