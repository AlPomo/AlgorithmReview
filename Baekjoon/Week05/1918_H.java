import java.util.*;
import java.io.*;
/*
 * (1) a+b => ab+
 * (2) 우선순위 : 괄호 > 연산자 우선순위(*, /)규칙 > 왼쪽부터
 */
public class Main {
	public static int priority(char c) {
		if(c=='*' || c=='/') return 2;
		else if(c=='(') return 0;
		return 1;
	}
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		StringBuilder sb = new StringBuilder();
		Stack<Character> stack = new Stack<>();
		
		for(char c : br.readLine().toCharArray()) {
			if(c>='A' && c<='Z') {
				sb.append(c);
			} else if(c=='(') {
				stack.add(c);
			} else if(c==')') {
				while(!stack.isEmpty()) {
					char p = stack.pop();
					if(p=='(') break;
					sb.append(p);
				}
			} else { //연산자
				while(!stack.isEmpty() && priority(stack.peek()) >= priority(c)) {
					sb.append(stack.pop());
				}
				stack.add(c);
			}
		}
		while(!stack.isEmpty()) {
			sb.append(stack.pop());
		}
		System.out.print(sb);
	}
}
