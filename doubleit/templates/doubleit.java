import java.io.*;

class Solution {
    /**
     * Return the total money Big Ben pays
     *
     * P: string of characters representing the people Big Ben talks to
     */
    static int solve(int L, String[] P) {
        // YOUR CODE HERE
        return -1;
    }
    
    static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    static PrintWriter out = new PrintWriter(System.out);

    public static void main(String[] args) throws IOException {
        int T = Integer.parseInt(in.readLine());
        for (int i = 0; i < T; i++) {
            int L = Integer.parseInt(in.readLine());
            String[] P = in.readLine().split(" ");
            out.println(solve(L, P));
        }
        out.flush();
    }
}
