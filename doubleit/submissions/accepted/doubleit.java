import java.io.*;

class Solution {
    static int solve(int L, String P) {
        int total = 0;
        int money = 1;
        for (int i = 0; i < P.length(); i++) {
            if (P.charAt(i) == 'D') {
                money *= 2;
            } else {
                total += money;
                money = 1;
            }
        }
        return total;
    }
    
    static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    static PrintWriter out = new PrintWriter(System.out);

    public static void main(String[] args) throws IOException {
        int T = Integer.parseInt(in.readLine());
        for (int i = 0; i < T; i++) {
            int L = Integer.parseInt(in.readLine());
            String P = in.readLine();
            out.println(solve(L, P));
        }
        out.flush();
    }
}