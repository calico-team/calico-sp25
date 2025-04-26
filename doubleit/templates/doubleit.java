import java.io.*;

class Solution {
    /**
     * Return the total money Big Ben pays
     *
     * N: length of the string P
     * P: string of characters representing the people Big Ben talks to
     */
    static int solve(int N, String P) {
        // YOUR CODE HERE
        return -1;
    }
    
    static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    static PrintWriter out = new PrintWriter(System.out);

    public static void main(String[] args) throws IOException {
        int T = Integer.parseInt(in.readLine());
        for (int i = 0; i < T; i++) {
            int N = Integer.parseInt(in.readLine());
            String P = in.readLine();
            out.println(solve(N, P));
        }
        out.flush();
    }
}
