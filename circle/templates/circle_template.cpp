#include <iostream>
#include <vector>

using namespace std;

/**
 * Return the area of the rectangle described by the given points.
 * 
 * N: the number of given points
 * X: a list containing the x-coordinate of each point
 * Y: a list containing the y-coordinate of each point
 */
double solve(int N, const vector<double>& X, const vector<double>& Y) {    
    // YOUR CODE HERE
    return 0.0;
}

int main() {
    int T;
    cin >> T;
    for (int i = 0; i < T; i++) {
        int N;
        cin >> N;
        vector<double> X(N), Y(N);
        for (int j = 0; j < N; j++) {
            cin >> X[j] >> Y[j];
        }
        cout << solve(N, X, Y) << "\n";
    }
}
