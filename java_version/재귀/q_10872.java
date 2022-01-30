package java_version.재귀;

import java.util.Scanner;

public class q_10872 {
    public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		int N = in.nextInt();
		in.close();
		int cnt = factorial(N);
		System.out.println(cnt);
	}
	
	public static int factorial(int N) {
		if(N <= 1) return 1;	// 재귀 종료조건
		return N * factorial(N - 1);		
	}
}
