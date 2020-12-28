import java.util.*;
import java.io.*;
public class Main {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int K = Integer.parseInt(st.nextToken());
		int N = Integer.parseInt(st.nextToken());

		int[] arr = new int[K];
		for(int k=0; k<K; k++) {
			arr[k] = Integer.parseInt(br.readLine());
		}
		Arrays.sort(arr);
		
		long start = 1;
		long end = arr[K-1];
		
		while(start<=end) {
			long mid = (start + end) / 2;
			long tmp = 0;
			for(int i=0; i<K; i++) {
				tmp += arr[i] / mid;
			}
			if(tmp>=N) start = mid + 1;
			else end = mid -1;
		}
		System.out.print(end);
	}
}
