import java.io.*;

class Solution {
    /**
     * Return the minimum number of actions
     * 
     * N: a non-negative integer representing the number of rows
     * M: another non-negative integer representing the number of columns
     * S: A string representing a sequence of drift inputs
     * G: N x M array representing a grid
     */
    static int solve(int N, int M, String S, int[][] G) {
        // YOUR CODE HERE
        return -1;
    }
    
    static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    static PrintWriter out = new PrintWriter(System.out);
    
    public static void main(String[] args) throws IOException {
        int T = Integer.parseInt(in.readLine());
        for (int i = 0; i < T; i++) {
            String[] temp = in.readLine().split(" ");
            int N = Integer.parseInt(temp[0]), M = Integer.parseInt(temp[1]);
            String S = in.readLine();
            int[][] G = new int[N][M];
            for (int j = 0; j < N; j++) {
                temp = in.readLine().split(" ");
                for (int k = 0; k < M; k++) {
                    G[j][k] = Integer.parseInt(temp[k]);
                }
            }
            out.println(solve(N, M, S, G));
        }
        out.flush();
    }
}