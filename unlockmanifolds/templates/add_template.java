import java.io.*;

class Solution {
    /**
     * Return the sum of A and B.
     * 
     * A: a non-negative integer
     * B: another non-negative integer
     */
    static int solve(int N, int M, int[][] G) {
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
            int[][] G = new int[N][]
            for (int j = 0; j < N; j++) {
                temp = in.readLine().split(" ");
                for (k = 0; k < temp.length(); k++) {
                    G[j][k] = Integer.parseInt(temp[k]);
                }
            }
            out.println(G)
            out.println(solve(N, M, G));
        }
        out.flush();
    }
}


