import java.util.*;
import java.io.*;

public class Main {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));		
		int N = Integer.parseInt(br.readLine());
		int[] dp = new int[N+1];
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		for(int i=0; i<N; i++) {
			dp[i+1] = Integer.parseInt(st.nextToken());
		}
		
		for (int i=2;i<=N;i++) {
			for (int j=0;j<=i/2;j++) {
				dp[i] = Math.max(dp[i], dp[i-j]+dp[j]);
			}
		}
		
		System.out.print(dp[N]);
	}
}