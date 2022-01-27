package java_version;

import java.io.IOException;
import java.util.*;

//숫자개수
//곱셈 후 0~9 사이 숫자 개수 세기
public class q_2577 {
    public static void main(String args[]) throws IOException{
        Scanner in = new Scanner(System.in);
 
		int value = (in.nextInt() * in.nextInt() * in.nextInt());
		String str = Integer.toString(value);
		
		for (int i = 0; i < 10; i++) {
			int count = 0;
			for (int j = 0; j < str.length(); j++) {
				if ((str.charAt(j) - '0') == i) {
					count++;
				}
			}
			System.out.println(count);
		}
	}
}
