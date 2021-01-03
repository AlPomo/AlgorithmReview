import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = null;
        StringBuilder sb = new StringBuilder();
        while (true) {
        	st = new StringTokenizer(br.readLine());
            int N = Integer.parseInt(st.nextToken());
            int M = (int) ((Double.parseDouble(st.nextToken()) * 100) + 0.5);
            int[] dp = new int[M + 1];
            int[] c = new int[N];
            int[] p = new int[N];

            if (N == 0 && M == 0) {
                break;
            }

            for (int i = 0; i < N; i++) {
            	st = new StringTokenizer(br.readLine());
                c[i] = Integer.parseInt(st.nextToken());
                p[i] = (int) ((Double.parseDouble(st.nextToken()) * 100) + 0.5);
            }

            for (int i = 0; i < N; i++) {
                for (int j = p[i]; j <= M; j++) {
                    dp[j] = Math.max(dp[j], dp[j - p[i]] + c[i]);
                }
            }
            sb.append(dp[M]).append("\n");
        }
        System.out.print(sb);
    }

}
