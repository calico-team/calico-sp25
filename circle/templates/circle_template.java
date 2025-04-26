import java.io.*;

public class Main {
    /**
     * Return the area of the rectangle described by the given points.
     * 
     * N: the number of given points
     * X: a list containing the x-coordinate of each point
     * Y: a list containing the y-coordinate of each point
     */
    static double solve(int N, double[] X, double[] Y) {
        // YOUR CODE HERE
        return 0.0;
    }
    
    static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    static PrintWriter out = new PrintWriter(System.out);

    public static void main(String[] args) throws IOException {
        int T = Integer.parseInt(in.readLine());
        for (int i = 0; i < T; i++) {
            int N = Integer.parseInt(in.readLine());
            double[] X = new double[N], Y = new double[N];
            for (int j = 0; j < N; j++) {
                String[] XY = in.readLine().split(" ");
                X[j] = Double.parseDouble(XY[0]);
                Y[j] = Double.parseDouble(XY[1]);
            }
            out.println(solve(N, X, Y));
        }
        out.flush();
    }
}
