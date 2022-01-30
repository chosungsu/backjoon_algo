package java_version.기본수학1;

import java.util.Scanner;

public class q_1712 {
    public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
 
 
		int A = in.nextInt();	// 불변 비용
		int B = in.nextInt();	// 가변 비용
		int C = in.nextInt(); 	// 상품 가격
        
		if (C <= B) {
			System.out.println("-1");
		} 
		else {
			System.out.println((A/(C-B))+1);
		}
	}
}
