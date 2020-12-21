import java.util.*;
import java.io.*;
public class Main {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T  = Integer.parseInt(br.readLine());
		StringTokenizer st = null;
		for(int t=0; t<T; t++) {
			StringBuilder sb = new StringBuilder();
			int N = Integer.parseInt(br.readLine());			
			st = new StringTokenizer(br.readLine());
			Map<Integer, Integer> map = new HashMap<>();
			for(int i=0; i<N; i++) map.put(Integer.parseInt(st.nextToken()), 1);
			int M = Integer.parseInt(br.readLine());
			st = new StringTokenizer(br.readLine());
			for(int i=0; i<M; i++) {
				if(map.containsKey(Integer.parseInt(st.nextToken()))) sb.append("1").append("\n");
				else sb.append("0").append("\n");
			}
			System.out.print(sb);
		}
	}
}
