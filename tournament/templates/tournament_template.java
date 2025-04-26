import java.io.*;

class Solution {
    /**
     * Return a single string of the champion's name
     *
     * N: The length of C and P
     * C: List of strings of the competitors
     * P: List of integers of competitor's power
     */
    static String solve(int N, String[] C, int[] P) {
        // YOUR CODE HERE
        return "";
    }
    
    static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    static PrintWriter out = new PrintWriter(System.out);

    public static void main(String[] args) throws IOException {
        int T = Integer.parseInt(in.readLine());
        for (int i = 0; i < T; i++) {
            int N = Integer.parseInt(in.readLine());
            String[] C = in.readLine().split(" ");
            String[] temp = in.readLine().split(" ");
            int[] P = new int[N];
            for (int j = 0; j < N; j++) {
                P[j] = Integer.parseInt(temp[j]);
            }
            out.println(solve(N, C, P));
        }
        out.flush();
    }
}
