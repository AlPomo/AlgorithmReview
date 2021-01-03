import java.util.*;
import java.io.*;

public class Main {
	static int[] S;
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		S = new int[30];
		
		S[0] = 3;
		for(int k=1; k<S.length; k++) {
			S[k] = 2*S[k-1] + (k+3);
		}
		
		System.out.println(solve(N));
		
	}
	static char solve(int N) {
		if(N==1) return 'm';
		else if(N==2||N==3) return 'o';
		int k=0;
		
		//(1)현재 N이 속한 S(k)의 k값을 구한다.		
		while(S[k]<N) k++;
	
		//N이 가운데에 속해있으면 구할 수 있음
		if(S[k-1]+1==N) return 'm';
		if(S[k-1]+(k+3)>=N) return 'o';
			
		//그게 아니면 solve 재귀
		return solve(N-S[k-1]-(k+3));
	}
}
