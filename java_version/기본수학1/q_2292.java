package java_version.기본수학1;

import java.util.Scanner;

public class q_2292 {
    public static void main(String[] args) {
 
		Scanner in = new Scanner(System.in);
 
		int N = in.nextInt();
		int count = 1; // 겹 수(최소 루트)
		int range = 2;	// 범위 (최솟값 기준) 
 
		while (range <= N) {	
            // 범위가 N보다 커지기 직전까지 반복 
            range = range + (6 * count);
            count++;
        }
        System.out.print(count);
	}
}
