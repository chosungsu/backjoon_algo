package java_version.정렬;

import java.util.Arrays;
import java.util.Scanner;

public class q_1427 {
    public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String N = sc.nextLine();
		
		char[] str = N.toCharArray();
		Arrays.sort(str);
		
		//내림차순
		for(int i = str.length-1; i >=0; i--) {
			System.out.print(str[i]);
		}
 
	}
}
