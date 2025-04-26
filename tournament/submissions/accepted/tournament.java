import java.io.*;
import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;

class Solution {
    static String solve(int N, String[] C, Integer[] P) {
        return helper(Arrays.asList(C), Arrays.asList(P));
    }

    private static String helper(List<String> C, List<Integer> P) {
        if (C.size() == 1) {
            return C.get(0);
        }
        List<String> Winners = new ArrayList<>();
        List<Integer> WinnerPowers = new ArrayList<>();
        for (int i = 0; i < C.size(); i += 2) {
            if (P.get(i) > P.get(i + 1)) {
                Winners.add(C.get(i));
            } else if (P.get(i) == P.get(i + 1)) {
                Winners.add(C.get(i) + C.get(i + 1));
            } else {
                Winners.add(C.get(i + 1));
            }
            WinnerPowers.add(P.get(i) + P.get(i + 1));
        }
        return helper(Winners, WinnerPowers);
    }
    
    static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    static PrintWriter out = new PrintWriter(System.out);

    public static void main(String[] args) throws IOException {
        int T = Integer.parseInt(in.readLine());
        for (int i = 0; i < T; i++) {
            int N = Integer.parseInt(in.readLine());
            String[] C = in.readLine().split(" ");
            String[] temp = in.readLine().split(" ");
            Integer[] P = new Integer[N];
            for (int j = 0; j < N; j++) {
                P[j] = Integer.parseInt(temp[j]);
            }
            out.println(solve(N, C, P));
        }
        out.flush();
    }
}
