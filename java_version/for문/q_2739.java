package java_version.for문;

import java.util.Scanner;

//구구단 출력
public class q_2739 {
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        int x = sc.nextInt();
        for (int i = 1; i < 10; i++) {
            System.out.println(x + " * " + i + " = " + (x * i));
        }
	}
}
