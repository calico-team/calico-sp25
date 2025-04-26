import java.io.*;
import java.util.Map;
import java.util.HashMap;

class Solution {
    /**
     * Return the minimum number of actions
     *
     * N: a non-negative integer representing the number of rows
     * M: another non-negative integer representing the number of columns
     * G: N x M array representing a grid
     */
    static int solve(int N, int M, int[][] G) {
        Map<Integer, Integer> row = new HashMap<>();
        Map<Integer, Integer> col = new HashMap<>();
        int actions = 0;
        int cursor_row = 0;
        int cursor_col = 0;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                row.put(G[i][j], i);
                col.put(G[i][j], j);
            }
        }
        for (int k = 1; k < (N * M) + 1; k++) {
            actions += Math.min((row.get(k) - cursor_row) % N, (cursor_row - row.get(k)) % N);
            actions += Math.min((col.get(k) - cursor_col) % M, (cursor_col - col.get(k)) % M);
            cursor_row = row.get(k);
            cursor_col = col.get(k);
        }
        return actions;
    }

    static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    static PrintWriter out = new PrintWriter(System.out);

    public static void main(String[] args) throws IOException {
        int T = Integer.parseInt(in.readLine());
        for (int i = 0; i < T; i++) {
            String[] temp = in.readLine().split(" ");
            int N = Integer.parseInt(temp[0]), M = Integer.parseInt(temp[1]);
            int[][] G = new int[N][M];
            for (int j = 0; j < N; j++) {
                temp = in.readLine().split(" ");
                for (int k = 0; k < M; k++) {
                    G[j][k] = Integer.parseInt(temp[k]);
                }
            }
            out.println(solve(N, M, G));
        }
        out.flush();
    }
}


