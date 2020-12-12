import java.util.*;
import java.io.*;
public class Main {
		public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String input = br.readLine();
		int ans = 0;
		Stack<String> stack = new Stack<>();
		String start = "([";
		String end = ")]";
		int tmp = 0;
		boolean flag = true;
		loop:for(char c : input.toCharArray()) {
			if(start.contains(c+"")) {
				stack.add(c+"");
			} else if(end.contains(c+"")) {
				if(stack.isEmpty()) {
					flag = false;
					break loop;
				}else if(end.indexOf(c)==start.indexOf(stack.peek())) {
					stack.pop();
					if(c==')') stack.add("2");
					else stack.add("3");
				} else {
					while(!stack.isEmpty() && end.indexOf(c)!=start.indexOf(stack.peek())) {
						if(end.contains(stack.peek()) || start.contains(stack.peek())) {
							flag = false;
							break loop;
						} else {
							tmp +=Integer.parseInt(stack.pop());
						}
					}
					if(stack.isEmpty()) {
						flag = false;
						break loop;
					}
					String peek = stack.pop();
					if(peek.equals("(")) stack.push(tmp*2+"");
					else if(peek.equals("[")) stack.push(tmp*3+"");
					tmp = 0;
				}
			}
		}
		if(flag) {
			while(!stack.isEmpty()) {
				try{
					ans += Integer.parseInt(stack.pop());
				}catch(Exception c) {
					System.out.print("0");
					return;
				}
			}
		}
		System.out.print(ans);
	}
}
