/*
public static int[] solution(int[] heights) {
    int[] answer = new int[heights.length];
	        for(int i=heights.length-1; i>0; i--) {
	            for(int j=i-1; j>=0; j--) {
	                if(heights[i]<heights[j]) {
	                    answer[i] = j;
	                    break;
	                }
	            }
	        }
    return answer;
}
*/
import java.io.*;
import java.util.*;
public class  {
	static class Node{
        long h;
        int n;
        public Node(long h, int n){
            this.h = h;
            this.n = n;
        }
    }
	public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int N = Integer.parseInt(br.readLine());
        Stack<Node> stack = new Stack<Node>();
        StringTokenizer st = new StringTokenizer(br.readLine());
        for(int i = 0; i < N; i++){
            long a = Long.parseLong(st.nextToken());
            while(!stack.isEmpty()){
                if(stack.peek().h >= a){
                    sb.append(stack.peek().n).append(" ");
                    break;
                }
                stack.pop();
            }
            if(stack.isEmpty()) sb.append("0").append(" ");
            stack.push(new Node(a, i));
        }
        System.out.print(sb);
    }
}
