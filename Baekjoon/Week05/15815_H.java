import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String s = br.readLine();
		Stack<Integer> stack = new Stack<>();
		for(char c : s.toCharArray()) {
			int a=0, b=0;
            if(c=='+') {
				stack.add(stack.pop()+stack.pop());
			} else if (c=='-') {
				a = stack.pop();
				b = stack.pop();
				stack.add(b-a);
			} else if(c=='*') {
				stack.add(stack.pop()*stack.pop());
			} else if(c=='/') {
				a = stack.pop();
				b = stack.pop();
				stack.add(b/a);
			}
			else stack.add(c-'0');
		}
		System.out.print(stack.peek());
	}
}
