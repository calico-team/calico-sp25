import java.io.*;

class Solution {
    /**
     * Return the total money Big Ben pays
     *
     * L: list of characters representing the people Big Ben talks to
     */
    static int solve(String[] L) {
        // YOUR CODE HERE
        return -1;
    }
    
    static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    static PrintWriter out = new PrintWriter(System.out);

    public static void main(String[] args) throws IOException {
        int T = Integer.parseInt(in.readLine());
        for (int i = 0; i < T; i++) {
            String[] L = in.readLine().split(" ");
            out.println(solve(L));
        }
        out.flush();
    }
}
